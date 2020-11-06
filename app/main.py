from fastapi import FastAPI
import uvicorn

from routers import bot, botnet, config

app = FastAPI()

app.include_router(botnet.router, prefix="/botnet")
app.include_router(bot.router, prefix="/bot/{bot_id}")
app.include_router(config.router, prefix="/config")

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 42432
    uvicorn.run(app, host=host, port=port)
