from fastapi import FastAPI
import uvicorn

from config import settings
from routers import bot, botnet, config

app = FastAPI()

app.include_router(botnet.router, prefix="/botnet")
app.include_router(bot.router, prefix="/bot/{bot_id}")
app.include_router(config.router, prefix="/config")

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
