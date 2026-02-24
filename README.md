# skip-seti

SETI 사이트 학습 진행을 보조하는 Selenium 기반 매크로 프로젝트입니다.

## 프로젝트 구조

```text
skip-seti/
├─ assets/                # 아이콘/이미지 리소스
├─ legacy/                # 이전 버전 참고 코드
├─ scripts/               # 보조 스크립트/실험용 코드
├─ skipSeti.py            # 메인 실행 스크립트
├─ skipSeti.spec          # PyInstaller 빌드 설정
├─ requirements.txt       # Python 의존성 목록
├─ README.md              # 실행/빌드 문서
└─ .gitignore             # Git 제외 규칙
```

참고:

- `build/`, `dist/`는 PyInstaller 빌드 결과 폴더이며 Git에서 제외합니다.
- `.venv/`는 로컬 가상환경 폴더이며 Git에서 제외합니다.

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

### 방법: spec 파일 사용

```powershell
pyinstaller skipSeti.spec
```

빌드 결과물:

- `dist\\skipSeti.exe`
