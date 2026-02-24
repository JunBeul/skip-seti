# skip-seti

SETI 사이트 학습 진행을 보조하는 Selenium 기반 자동화 도구입니다.

---

## 기술 스택

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Selenium" src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
</p>

---

## 환경

- Windows (키 입력 감지 `keyboard` 사용)
- Python 3.10 이상 권장
- Google Chrome 설치
- 인터넷 연결 (첫 실행 시 ChromeDriver 다운로드)

---

## 실행 방법

> 실행 시 참고 사항:
>
> - 첫 실행에서 `webdriver-manager`가 ChromeDriver를 자동으로 내려받습니다.
> - 크롬 프로필 경로로 `C:/selenium/AutomationProfile`를 사용합니다.
> - 같은 프로필을 쓰는 Chrome 창이 이미 열려 있으면 충돌할 수 있습니다.
> - 매크로 루프 중 `Space`를 3초 정도 길게 누르면 루프를 중단하고 다시 준비 상태로 돌아갑니다.

### 패키지 및 환경 설치

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 실행

```powershell
python skipSeti.py
```

---

## 빌드 방법 (exe)

### PyInstaller 설치

```powershell
pip install pyinstaller
```

### spec 파일 빌드

```powershell
pyinstaller skipSeti.spec
```

### 빌드 결과

- `dist/skipSeti.exe`

---
