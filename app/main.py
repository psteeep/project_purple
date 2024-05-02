import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def health():
    return {
        "status_code": 200,
        "details": "ok",
        "result": "working"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
