from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    t_id = Column(Integer)
    lists = relationship('List')


class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'), index=True)
    date = Column(Date)
    status = Column(String(40), default='created')
    words = relationship('Word')
    notify_times = relationship('NotifyTime')


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(256))
    list_id = Column(Integer, ForeignKey('lists.id', ondelete='cascade'), index=True)


class NotifyTime(Base):
    __tablename__ = 'notify_times'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Time)
    status = Column(String(40))
    list_id = Column(Integer, ForeignKey('lists.id', ondelete='cascade'), index=True)
