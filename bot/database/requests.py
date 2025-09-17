import aiosqlite


async def get_users() -> list[tuple]:
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("SELECT * FROM scores")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows


async def get_phone() -> list[tuple]:
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("SELECT * FROM phones")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows
