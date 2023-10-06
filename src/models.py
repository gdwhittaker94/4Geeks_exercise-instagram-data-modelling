import os
import sys
from enum import Enum as EnumType
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Media_Type(EnumType):
    photo = "photo"
    video = "video"


# LVL 1
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    # Relationships 
    user_posts = relationship('Users_Posts', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    followers = relationship('Follower', backref='user', lazy=True)
    messages = relationship('Message', backref='user', lazy=True)


# LVL 2
class User_Posts(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, primary_key=True)
    user_posting_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment', backref='user_posts', lazy=True)
    media = relationship('Media', backref='user_posts', lazy=True)


# LVL 3
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('user_posts.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Media_Type), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('user_posts.id'))


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_following_id = Column(Integer, ForeignKey('user.id'))
    user_followed_id = Column(Integer, ForeignKey('user.id'))


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    message_text = Column(String(250))
    user_message_author_id = Column(Integer, ForeignKey('user.id'))
    user_message_receiver_id = Column(Integer, ForeignKey('user.id'))








## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# Note:
# varchar = String(n) in Python 
# a "class" = a table 


# ENUM EXPLANATION
# In this code:

# We import the Enum class from Python's enum module and rename it as EnumType to avoid a name conflict with SQLAlchemy's Enum.

# We define an Enum class called MediaType that specifies the possible values for the type column in the Media table 
# (i.e., "photo" and "video").

# In the Media class definition, we use Column(Enum(MediaType), nullable=False) to define the type column as an Enum type that 
# references the MediaType enumeration.