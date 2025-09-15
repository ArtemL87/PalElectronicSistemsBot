from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from dotenv import load_dotenv


load_dotenv()

engine = create_async_engine(url='sqlite+aiosqlite:///database.db',
                             echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


#class Score(Base):
#    __tablename__ = 'scores'


#class Phone(Base):
#    __tablename__ = 'phones'


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
