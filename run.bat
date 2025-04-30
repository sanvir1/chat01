@echo off
REM Активация виртуального окружения
call venv\Scripts\activate

REM Запуск приложения в новом окне
start python chatbot.py

REM Открытие браузера
start http://localhost:5000

