import uvicorn
from fastapi import FastAPI

from .hooks import on_shutdown, on_startup
from .router import app_router

app = FastAPI()

app.include_router(app_router)
app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
