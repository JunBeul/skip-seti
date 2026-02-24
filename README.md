# skip-seti

SETI 사이트 학습 진행을 보조하는 Selenium 기반 매크로 프로젝트입니다.

## 환경

- Windows (키 입력 감지 `keyboard` 사용)
- Python 3.10 이상 권장
- Google Chrome 설치
- 인터넷 연결 (첫 실행 시 ChromeDriver 다운로드)

## 설치

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 실행 방법

```powershell
python skipSeti.py
```

실행 시 참고 사항:

- 첫 실행에서 `webdriver-manager`가 ChromeDriver를 자동으로 내려받습니다.
- 크롬 프로필 경로로 `C:\selenium\AutomationProfile`를 사용합니다.
- 같은 프로필을 쓰는 Chrome 창이 이미 열려 있으면 충돌할 수 있습니다.
- 매크로 루프 중 `Space`를 3초 정도 길게 누르면 루프를 중단하고 다시 준비 상태로 돌아갑니다.

## 빌드 방법 (exe)

PyInstaller가 없다면 먼저 설치합니다.

```powershell
pip install pyinstaller
```

### 방법 1: 배치 파일 사용

```powershell
.\porting.bat
```

### 방법 2: spec 파일 사용

```powershell
pyinstaller skipSeti.spec
```

빌드 결과물:

- `dist\\skipSeti.exe`

## Git 관리 메모 (간단)

- 소스/설정 파일만 커밋 (`skipSeti.py`, `skipSeti.spec`, `porting.bat`, `assets/*`)
- 빌드 산출물은 커밋하지 않음 (`build/`, `dist/`)
- 레거시 참고 파일은 목적이 보이게 이름 유지 (`legacy_*`)