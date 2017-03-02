import pymysql
from sqlalchemy import *
from sqlalchemy.orm import *

db = create_engine('sqlite:////Users/zhengyichen/Documents/Python/javlib.db')
db.echo = False
metadata = MetaData(db)

data = Table('Javlib', metadata,
    Column('video_id', String),
    Column('video_title', String),
    Column('video_img', String),
    Column('video_length', String),
    Column('video_review', String),
    Column('video_genres', String),
    extend_existing=False)

data.create()

class Data(object):
    pass

class Sql:

    @classmethod
    def concat(cls, video_title, video_img, video_id, video_length, video_review, video_genres, video_cast):
        mapper(Data, data)
        session = sessionmaker(bind=db)()
        query = session.query(Data)

        page = Data()

        page.video_title = video_title
        page.video_img = video_img
        page.video_id = video_id
        page.video_length = video_length
        page.video_review = video_review
        page.video_genres = video_genres
        page.video_cast = video_cast

        session.add(page)
        session.flush()
