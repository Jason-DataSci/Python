from sqlalchemy import *
from sqlalchemy.orm import *

db = create_engine('sqlite:////Users/zhengyichen/Documents/Python/web_spider.db')
db.echo = False
metadata = MetaData(db)

data = Table('web_spider', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('link', String),
    Column('reads',String),
    extend_existing=True)

# data.create()

class Data(object): #ID, title, link, reads
    pass

mapper(Data, data)

session = sessionmaker(bind=db)()
query = session.query(Data)

ID = 1
dict = {}
dict[1] = Data()
dict[1].id = 1
dict[1].title = 'hello'
dict[1].link = 'www.baidu.com'
dict[1].reads = 888


session.add(dict[ID])
session.flush()

query.filter_by(id=1).first.id
