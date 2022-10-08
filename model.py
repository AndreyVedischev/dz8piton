
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phones = relationship("Phone", back_populates="user")
    info = relationship("Info", back_populates="user")

    def __str__(self):
        return self.name
    
    @classmethod
    def add(cls, name): 
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user


    @classmethod
    def del_user(cls):
        i = session.query(cls).one()
        session.delete(i)
        session.commit()


    @classmethod
    def all(cls): 
        return session.query(cls).all()


class Info(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    info = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="info")

    def __str__(self):
        return self.info

    @classmethod
    def add(cls, info, user): 
        info = cls(info=info,user=user )
        session.add(info)
        session.commit()
        return info

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

    @classmethod
    def add(cls, phone, user):
        phone = cls(phone=phone, user=user)
        session.add(phone)
        session.commit()
        return phone


Base.metadata.create_all(engine)