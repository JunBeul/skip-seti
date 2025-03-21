from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys
import keyboard

# 버전관리
VERSION = "1.2.4"

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
        driver.get('https://www.seti.go.kr/system/login/login.do')
        
        while True:
            print_welcome_message()
            input('준비가 완료되면 엔터를 입력하세요...'.strip())
            # 창 전환
            switch_to_classroom_window(driver)
            # 매크로 시작
            loop_macro(driver)
        
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")
        
    finally:
        if driver:
            driver.quit()
        print("프로그램이 종료됩니다.")
        os._exit(0)  # Forcefully exit the program

def resource_path(relpath):
    try:
        abspath = sys._MEIPASS
    except Exception:
        abspath = os.path.abspath(".")
    return os.path.join(abspath, relpath)

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

def switch_to_classroom_window(driver):
    """강의실 창 전환"""
    for window in driver.window_handles:
        driver.switch_to.window(window)
        if '강의실' in driver.title:
            return
    raise Exception('강의실 창을 찾을 수 없습니다.')

def video_play_script(driver):
    """재생 자바스크립트 실행"""
    script = """document.querySelector(".vjs-big-play-button")?.click()"""
    driver.execute_script(script)

def execute_script(driver):
    """스킵 자바스크립트 실행"""
    script = """
    if (document.querySelector("#quizPage").src) {
        showPlayer();
        document.querySelector("#next-btn")?.click();
    }
    document.getElementsByTagName('video')[0].addEventListener('ended', function() {
        document.querySelector("#next-btn")?.click();
    });
    """
    driver.execute_script(script)

def loop_macro(driver):
    """매크로 시작"""
    video_play_script(driver)
    execute_script(driver)
    
    print('매크로를 다시시작 하시려면 스페이스바를 3초 동안 길게 눌러주세요.')

    n = 0
    skipVideo = 0
    previous_video_src = driver.execute_script("return document.getElementsByTagName('video')[0].src")
    while True:
        if keyboard.is_pressed('space'):
            start_time = time.time()
            sys.stdout.write('\r\033[K')
            while keyboard.is_pressed('space'):
                elapsed_time = time.time() - start_time
                sys.stdout.write(f'\r{3-elapsed_time:.1f}초 후 재시작.')
                sys.stdout.flush()
                time.sleep(0.1)
                if elapsed_time >= 3:
                    return
        
        current_video_src = driver.execute_script("return document.getElementsByTagName('video')[0].src")
        if current_video_src != previous_video_src:
            sys.stdout.write('\r\033[K')
            sys.stdout.write(f'\r다음 차시로 넘어가는 중 입니다.')
            sys.stdout.flush()
            time.sleep(3)
            execute_script(driver)
            previous_video_src = current_video_src
            skipVideo += 1
        
        sys.stdout.write(f'\r완료한 강의: {skipVideo} / 매크로 작동중{"." * (n % 4)}   ')
        sys.stdout.flush()

        n = (n + 1) % 100
        time.sleep(1)

if __name__ == '__main__':
    main()