@echo off
chcp 65001 > nul
title FRUIT FARM 서버 및 클라우드플레어 터널 자동 실행기

echo ========================================================
echo   FRUIT FARM 푸꾸옥 직영 플래그십 서버 자동 실행 중...
echo ========================================================

cd /d "E:\fruitfarm"

:: 1. Flask 서버 실행
start "FruitFarm_Flask" /b python app.py

:: 2. 잠시 대기 (서버 기동)
timeout /t 3 /nobreak > nul

:: 3. Cloudflare Tunnel 실행
start "FruitFarm_Tunnel" /b cloudflared tunnel --url http://127.0.0.1:5000

echo [완료] 서버(포트 5000) 및 외부 접속 터널이 백그라운드에서 가동되었습니다.
