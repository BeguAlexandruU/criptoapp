from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, MetaData
from .base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

metadata = MetaData()

#user section
class User(Base):
    __tablename__ = 'user'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    firstname   = Column(String(30))
    lastname    = Column(String(30))
    email       = Column(String(30))
    ref_code    = Column(String(255))
    id_red      = Column(Integer)
    password    = Column(String(255))
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1

class Admin(Base):
    __tablename__ = 'admin'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    firstname   = Column(String(30))
    lastname    = Column(String(30))
    username    = Column(String(30))
    sold        = Column(Integer)
    password    = Column(String(255))
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1

#notification posts
class Notification(Base):
    __tablename__ = 'notification'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user     = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_post     = Column(Integer, ForeignKey('post.id', ondelete= 'CASCADE'), nullable=False) 
    status      = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1 

class Post(Base):
    __tablename__ = 'post'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    title       = Column(String(30))
    description = Column(String(255))
    type        = Column(Integer)
    status      = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1


#wallet sercion
class Wallet(Base):
    __tablename__ = 'wallet'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user     = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_product  = Column(Integer, ForeignKey('product.id', ondelete= 'CASCADE'), nullable=False) 
    status      = Column(Integer)
    start_date  = Column(DateTime, default=datetime.now)
    end_date    = Column(DateTime, default=datetime.now)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1 

class Product(Base):
    __tablename__ = 'product'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    title       = Column(String(64))
    description = Column(String(255))
    status      = Column(Integer)
    duration    = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1


#referal section
class Referal(Base):
    __tablename__ = 'referal'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_parent   = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_child    = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    id_level    = Column(Integer, ForeignKey('level.id', ondelete= 'CASCADE'), nullable=False)  
    
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1

class Level(Base):
    __tablename__ = 'level'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    nr_level    = Column(Integer)
    debit       = Column(Integer)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.token = self.id+1

#dard (in dev section)
class Card(Base):
    __tablename__ = 'card'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user     = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    sold        = Column(Integer)
    nr_ref      = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class DemoOrder(Base):
    __tablename__ = 'demo_order'
    metadata = metadata

    id = Column(Integer, primary_key=True, index=True)
    id_user     = Column(Integer, ForeignKey('user.id', ondelete= 'CASCADE'), nullable=False) 
    price       = Column(Integer)
    type        = Column(Integer)
    status      = Column(Integer)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


#test tables
'''
class User(Base):
    __tablename__ = 'users'
    metadata = metadata
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    token = Column(String(255))
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.token = self.id+1

class Child(Base):
    __tablename__ = 'child'
    metadata = metadata
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id', ondelete= 'CASCADE'), nullable=False)  
    username = Column(String(255))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

'''
