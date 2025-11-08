- Активация виртуального окружения и загрузка зависимостей

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- Для локальной отладки:
```uvicorn app.main:app --reload```