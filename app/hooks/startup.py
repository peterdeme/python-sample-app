from app.config import config
from app.services.database import db


async def on_startup() -> None:
    await db.set_bind(config.get("connectionstring"))
