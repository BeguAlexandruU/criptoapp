from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import Union
from sqlalchemy.exc import NoInspectionAvailable

class CrudBase:
    """  """
    def __init__(self, model):
        self.model = model
    
    async def verify_exist_column(self, db: AsyncSession, column: str) -> bool:
        try:
            model_columns = [c_attr.key for c_attr in inspect(self.model).mapper.column_attrs]
        except NoInspectionAvailable:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Model inspection failed")

        if column not in model_columns:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Column '{column}' not found in the model")
        
        return True
    
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
            db_obj = result.first()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def read_by_column(self, db: AsyncSession, column: str, value: Union[str, int]):
        
        try:
            if not await self.verify_exist_column(db, column):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Column '{column}' not found in the model")
            
            stmt = select(self.model).where(getattr(self.model, column) == value)
            result = await db.execute(stmt)
            db_obj = result.first()
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
    
    async def count(self, db: AsyncSession):
        try:
            stmt = select(self.model)
            result = await db.execute(stmt)
            db_obj = result.scalars().all()
            return len(db_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def count_by_column(self, db: AsyncSession, column: str, value: Union[str, int]):
        try:
            if not await self.verify_exist_column(db, column):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Column '{column}' not found in the model")
            
            stmt = select(self.model).where(getattr(self.model, column) == value)
            result = await db.execute(stmt)
            db_obj = result.scalars().all()
            return len(db_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def update(self, db: AsyncSession, id: int, obj_data: BaseModel):
        try:
            stmt = select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            db_obj = result.scalar().first()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            for key, value in obj_data.model_dump().items():
                setattr(db_obj, key, value)
            await db.commit()
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def update_by_column(self, db: AsyncSession, id: int, column: str, value: Union[str, int]):
        try:
            if not await self.verify_exist_column(db, column):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Column '{column}' not found in the model")
            
            stmt = select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            db_obj = result.scalar().first()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            
            setattr(db_obj, column, value)
            await db.commit()
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    
    async def delete(self, db: AsyncSession, id: int):
        try:
            stmt = select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            db_obj = result.scalar().first()
            if db_obj is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
            db.delete(db_obj)
            await db.commit()
            return db_obj
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
        
        