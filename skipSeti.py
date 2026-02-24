from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys
import keyboard

# 버전관리
VERSION = "1.3.0"

LOGIN_URL = 'https://www.seti.go.kr/system/login/login.do'
SPACE_HOLD_EXIT_SECONDS = 3
VIDEO_CHANGE_WAIT_SECONDS = 3
LOOP_SLEEP_SECONDS = 1
SPACE_POLL_INTERVAL = 0.1
ELEMENT_WAIT_SECONDS = 10
WAIT_POLL_INTERVAL = 0.3

GET_VIDEO_SRC_JS = """
const video = document.querySelector('video');
return video ? (video.currentSrc || video.src || null) : null;
"""

CLICK_BIG_PLAY_JS = """document.querySelector(".vjs-big-play-button")?.click();"""

PREPARE_PAGE_JS = """
const quizPage = document.querySelector('#quizPage');
if (quizPage?.src) {
  if (typeof showPlayer === 'function') {
    showPlayer();
  }
  document.querySelector('#next-btn')?.click();
}

const video = document.querySelector('video');
if (video && !video.dataset.skipSetiEndedBound) {
  video.dataset.skipSetiEndedBound = '1';
  video.addEventListener('ended', function() {
    document.querySelector('#next-btn')?.click();
  });
}
"""

def print_welcome_message():
  """주의 사항 및 준비 절차 안내"""
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"교육연수 스킵 v{VERSION}")
  print('-----------------------------------------------------------------')
  print("<<주의 사항>>")
  print("1. 여러 브라우저 등을 사용하여 중복 로그인 금지")
  print("2. 과도한 사용 금지 (매크로 돌리고 퇴근 금지)")
  print("3. 강의를 종료하시려면 해당 프로그램을 종료")
  print('-----------------------------------------------------------------')
  print('<<준비 절차>>')
  print('1. 페이지 로그인')
  print('2. 수강할 강의실 입장')
  print('3. 매크로를 시작할 강의(동영상) 선택\n')

def wait_for_learning_page(driver, timeout=ELEMENT_WAIT_SECONDS):
  """강의실에 사용가능한 제어, 비디오 요소가 있을 때 까지 대기"""
  try:
    WebDriverWait(driver, timeout, poll_frequency=WAIT_POLL_INTERVAL).until(
      lambda d: (
        d.find_elements(By.TAG_NAME, 'video')
        or d.find_elements(By.ID, 'quizPage')
        or d.find_elements(By.ID, 'next-btn')
      )
    )
    return True
  except TimeoutException:
    return False

def switch_to_classroom_window(driver):
  """강의실 창 전환"""
  for window in driver.window_handles:
    driver.switch_to.window(window)
    if '강의실' in driver.title:
      wait_for_learning_page(driver)
      return
  raise Exception('강의실 창을 찾을 수 없습니다.')

def get_video_src(driver):
  """영상 src 받아오기"""
  try:
    return driver.execute_script(GET_VIDEO_SRC_JS)
  except Exception:
    return None

def loop_macro(driver):
  """매크로 시작"""
  wait_for_learning_page(driver)
  driver.execute_script(CLICK_BIG_PLAY_JS)    # 재생 자바스크립트
  driver.execute_script(PREPARE_PAGE_JS)      # 스킵 자바스크립트
  
  print('매크로를 다시시작 하시려면 스페이스바를 3초 동안 길게 눌러주세요.')

  n = 0
  skipVideo = 0
  previous_video_src = get_video_src(driver)
  while True:
    if keyboard.is_pressed('space'):
      start_time = time.monotonic()
      sys.stdout.write('\r\033[K')
      while keyboard.is_pressed('space'):
        elapsed_time = time.monotonic() - start_time
        sys.stdout.write(f'\r{3-elapsed_time:.1f}초 후 재시작.')
        sys.stdout.flush()
        time.sleep(SPACE_POLL_INTERVAL)
        if elapsed_time >= SPACE_HOLD_EXIT_SECONDS:
          return
    
    current_video_src = get_video_src(driver)
    if current_video_src and current_video_src != previous_video_src:
      sys.stdout.write('\r\033[K')
      sys.stdout.write(f'\r다음 차시로 넘어가는 중 입니다.')
      sys.stdout.flush()
      wait_for_learning_page(driver, timeout=VIDEO_CHANGE_WAIT_SECONDS)
      driver.execute_script(PREPARE_PAGE_JS)
      previous_video_src = current_video_src
      skipVideo += 1
    
    sys.stdout.write(f'\r완료한 강의: {skipVideo} / 매크로 작동중{"." * (n % 4)}   ')
    sys.stdout.flush()

    n = (n + 1) % 100
    time.sleep(LOOP_SLEEP_SECONDS)

def main():
  driver = None
  try:
    # 크롬 드라이버 옵션 설정 및 실행
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--user-data-dir=C:\\selenium\\AutomationProfile')
    options.add_argument('--remote-debugging-port=9222')
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    os.environ['WDM_SSL_VERIFY'] = '0'
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # 시작 준비
    driver.get(LOGIN_URL)
    
    while True:
      print_welcome_message()
      input('준비가 완료되면 엔터를 입력하세요...')
      # 창 전환
      switch_to_classroom_window(driver)
      # 매크로 시작
      loop_macro(driver)
    
  except Exception as e:
    print(f"프로그램 실행 중 오류 발생: {e}")
    
  finally:
    if driver:
      try:
        driver.quit()
      except Exception:
        pass
    print("프로그램이 종료됩니다.")
    os._exit(0)  # 프로그램 강제 종료

if __name__ == '__main__':
  main()
