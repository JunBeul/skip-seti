from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    print("교육연수 스킵 v0.0.1")
    print('!!!프로그램이 실행되면 오작동을 방지하기 위해 아무 동작도 하지 않아야 합니다.!!!')
    print('\n-----------------------------------------------------------------')
    print("\n<<준비 절차: 첫 사용자>>")
    print('1. 크롬을 실행한 뒤 f12입력')
    print('2. 개발자 도구 창이 뜨면 우측 상단의 톱니바퀴 클릭')
    print('3. 환경설정 창의 ctrl + 1~9 단축키 사용 설정 체크 후 설정 닫기(창 닫기 전에 설정을 먼저 닫아야 합니다.)')
    print('4. 크롬을 통해 교육연수 홈페이지 접속')
    print('5. 스킵을 희망하는 교육 연수를 킨 뒤 동영상 재생 후 준비완료(y) 입력.')

    while True:
        temp = input('\n준비완료 (y): ')
        if temp == 'y':
            break
        else:
            print('오입력 하셨습니다. 다시 입력 바랍니다.')

    print('\n실행 준비중...')

    # 크롬 드라이버 옵션 설정
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    # 크롬 드라이버 실행
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.seti.go.kr/system/login/login.do')  # 교육연수 웹사이트 URL 입력

    # 개발자 도구 열기 (F12)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome://devtools/')
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(2)

    # 자바스크립트 코드 실행
    script = """
    document.getElementsByTagName('video')[0].addEventListener('ended', function() {
        document.querySelector("#next-btn")?.click();
        if (document.querySelector(".ui-draggable-handle").style.z-index > 0) {
            document.querySelector(".ui-draggable-handle")?.click();
            document.querySelector("#next-btn")?.click();
        }
    });
    """
    driver.execute_script(script)
    
    print('프로그램 작동중')

if __name__ == "__main__":
    main()