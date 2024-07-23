from weakref import ref
from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey, MetaData
from .base import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

metadata = MetaData()

#user section
class User(SQLAlchemyBaseUserTableUUID, Base):
    metadata = metadata
    
    name = Column(String(60))
    ref_code = Column(String(255), unique=True, default=lambda: str(uuid4()))
    ref_code_parent = Column(String(255), default='')
    id_stripe_customer = Column(String(255), default='')

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    notification = relationship("Notification", back_populates="user")
    wallet = relationship("Wallet", back_populates="user")
    card = relationship("Card", back_populates="user")
    demo_order = relationship("DemoOrder", back_populates="user")
   
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    

class Admin(Base):
    __tablename__ = 'admin'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    username = Column(String(30))
    sold = Column(Integer, default=0)
    password = Column(String(255))
    token = Column(String(255), unique=True, default=str(uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.token = str(uuid4())


#notification posts
class Notification(Base):
    __tablename__ = 'notification'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 

    title = Column(String(30))
    message = Column(String(255))
    status = Column(Integer)
    type = Column(String(30))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="notification")

class Post(Base):
    __tablename__ = 'post'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30))
    description = Column(String(255))
    type = Column(String(30))
    status = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


#wallet sercion
class Wallet(Base):
    __tablename__ = 'wallet'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_product = Column(Integer, ForeignKey('product.id', ondelete= 'CASCADE'), nullable=False) 
    status = Column(Integer)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, default=datetime.now)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="wallet")
    product = relationship("Product", back_populates="wallet")

class Product(Base):
    __tablename__ = 'product'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64))
    description = Column(String(255))
    price = Column(Float)
    status = Column(Integer)
    duration = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    wallet = relationship("Wallet", back_populates="product")


#referal section
class Referal(Base):
    __tablename__ = 'referal'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_parent = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_child = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user_parent = relationship("User", foreign_keys=[id_parent])
    user_child = relationship("User", foreign_keys=[id_child])
    

class Level(Base):
    __tablename__ = 'level'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    nr_level = Column(Integer)
    debit = Column(Integer)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#card (in dev section)
class Card(Base):
    __tablename__ = 'card'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False)  
    sold = Column(Integer)
    nr_ref = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship("User", back_populates="card")

class DemoOrder(Base):
    __tablename__ = 'demo_order'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(String(36), ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    price = Column(Integer)
    order_type = Column(Integer)
    status = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="demo_order")

