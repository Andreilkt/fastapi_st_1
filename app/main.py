from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Тест": "Первый роут"}

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"тест": "Второй роут"}
