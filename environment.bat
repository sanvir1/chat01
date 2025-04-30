@echo off
REM Создание виртуального окружения (если еще не создано)
if not exist venv (
    python -m venv venv
)

REM Активация виртуального окружения
call venv\Scripts\activate

REM Установка необходимых библиотек
pip install -r requirements.txt

REM Создание папки для модели, если она не существует
if not exist model (
    mkdir model
)

REM Загрузка модели в папку model
cd model
git lfs install
git clone https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-extracted
cd ..

pause
