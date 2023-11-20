# Лабораторна №3 Flask

У цій лабораторній роботі я створила віртуальне середовище venv, також згенерувала файл requirements.txt в якому прописано все, що потрібно завантажити для запуску моїх програм app_fastapi.py та app_flask.py


## Технології
- Flask
- FastAPI
- Uvicorn

## Встановлення

Інструкції щодо встановлення залежностей та запуску проекту:

Для встановлення Flask, FastAPI та Uvicorn:

```bash
pip install -r requirements.txt
```

Для запуску app_fastapi.py:
```bash
uvicorn main:app --reload
```
Після запуску серверу для зручнішого тестування ендпоінту перейдіть за адресою:
http://127.0.0.1:8000/docs

=================================

Для запуску app_flask.py:
```bash
python app_flask.py
```
Після запуску серверу, перейдіть за наступною адресою:
http://127.0.0.1:8000/api/v1/hello-world-16


## Приклад запиту
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/hello-world-16' \
  -H 'accept: application/json'
  
## Очікувана відповідь
{
  "message": "Hello World 16"
}
