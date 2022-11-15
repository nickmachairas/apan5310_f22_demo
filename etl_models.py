from sqlalchemy.orm import Session

from db import engine
from db.models import Posts, Users

session = Session(engine)

user1 = Users(
    name="John Doe",
    email="john@example.com",
    password="123"
)
session.add(user1)
session.commit()

post1 = Posts(
    title="My first post",
    body="This is my first post",
    user=user1
)
session.add(post1)
session.commit()


print(session.query(Users).all())
print(session.query(Posts).all())
