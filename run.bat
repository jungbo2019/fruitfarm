@echo off
chcp 65001 > nul
cd /d "E:\fruitfarm"

echo ========================================================
echo   FRUIT FARM 푸꾸옥 2호점 웹사이트 & 관리자 포털 (E 드라이브)
echo ========================================================
echo.
echo [1] 고객 쇼핑몰: http://127.0.0.1:5000
echo [2] 관리자 포털: http://127.0.0.1:5000/admin
echo     - 아이디: admin
echo     - 비밀번호: password123!
echo.
echo 웹 브라우저를 열고 E:\fruitfarm 에서 서버를 가동합니다...
echo (서버를 종료하려면 이 창에서 Ctrl + C 를 누르세요)
echo ========================================================

start http://127.0.0.1:5000
python app.py

pause
