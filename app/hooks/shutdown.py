from app.services.database import db


async def on_shutdown() -> None:
    await db.pop_bind().close()
