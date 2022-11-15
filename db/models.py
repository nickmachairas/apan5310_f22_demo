from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(150), unique=True)
    password = Column(String(50))
    posts = relationship("Posts", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"Users(id={self.id}, name={self.name}, email={self.email})"


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Posts(id={self.id}, title={self.title}, body={self.body}, user_id={self.user_id})"
