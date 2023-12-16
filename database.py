import asyncpg

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

#Подключение к бд
async def connect_to_db():
    conn = await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

async def get_all_comics() -> int:
    conn = await connect_to_db()
    query = "SELECT COUNT(id) FROM comic"
    count = await conn.fetchval(query)
    await conn.close()
    return count


