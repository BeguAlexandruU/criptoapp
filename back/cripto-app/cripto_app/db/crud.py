from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import Union

class CrudBase:
    def __init__(self, model):
        self.model = model
    
    async def create(self, db: Session, obj_data):
        try:
            db_obj = self.model(**obj_data.dict())
            db.add(db_obj)
            await db.commit()
            return db_obj
        except IntegrityError as e:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e.orig))
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def read(self, db: AsyncSession, id: int):
        try:
            stmt = select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            db_obj = result.scalar().first()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    async def read_all(self, db: AsyncSession):
        try:
            stmt = select(self.model)
            result = await db.execute(stmt)
            db_obj = result.scalars().all()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
        