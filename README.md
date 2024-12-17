# stock-analyst-crewai

# Requirements

- Python3.11

# Commands

```bash

# venv 실행이 안될 시 Powershell 관리자 권한 주기
Set-ExecutionPolicy RemoteSigned

# 프로젝트 신규 clone 시 가상환경 생성 해주기
python -m venv .venv

# 가상환경 접속
. .venv/Scripts/activate.ps1

# 패키지 설치 명령어
pip install -r requirements.txt

# 프로젝트 실행
python main.py TSLA
pythonw main.py

# 가상환경 연결해제
deactivate

# 신규 패키지 설치 명령어
pip install LIBRARY_NAME

# 신규 설치된 패키지 Export 최신화
pip freeze > requirements.txt

# pip 업그레이드
python -m pip install --upgrade pip

```
