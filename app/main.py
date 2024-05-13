import uvicorn
from fastapi import FastAPI
from .routers.pred_route import router

app = FastAPI()

app.include_router(router)


@app.get('/')
def health():
    return {
        "status_code": 200,
        "details": "ok",
        "result": "working"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
