import pymysql
from sqlalchemy import *
db = create_engine('sqlite:////Users/zhengyichen/Documents/Python/tutorial.db')
db.echo = False
metadata = MetaData(db)

Users = Table('tutorial', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('email', String(120)),
    extend_existing=True)

Users.create()

## Level 1 Hand-Written SQL
# db=create_engine("pymysql:///:memory:", echo=True)
# db.execute("create table users(userid char(10), username char(50))")
# resultProxy=db.execute("insert into users (userid,username) values('user1','tony')")
# resultProxy=db.execute("select * from users")x

## Level 2 SQL Expressions in Python
i = Users.insert
type(db)
i({'name': 'ghost'},{'name': 'tutorial'}).execute()
s = Users.select()
rs = s.execute()

C = Users.c

Users.select(C.name == 'john')
S = Users.select
S(C.name == 'john')

## Level 3 ORM
# create class accouding to the table
from sqlalchemy.orm import *
class User(object):
    pass

# create mapping
mapper(User, Users)

# create session
session = sessionmaker(bind=db)()
query = session.query(User)

# create a new row as an instance of the class
fred = User()
fred.name = 'Fred'
fred.email = 'fred@gmail.com'

# insert fred into the table
session.add(fred)
session.flush()

# select Fred in the table
u = query.filter_by(name='Fred').first().name

# Data Mapping
Age = Table('age', metadata,
    Column('age_id', Integer, primary_key=True),
    Column('user_name', String(40)),
    Column('age', String(120)),
    extend_existing=True)

Age.create() # Here's a problem that 'the database is locked'

class Ages(object):
    pass
# We create the Email mapper first...
agemapper = mapper(Age, Ages)
# ... so that we can use it in the User mapper
usermapper = mapper(User, Users, properties={
    'Age': relation(agemapper)})  # Here's where the magic happens

# Also can use class instand of mapper
mapper(Age, Ages)
mapper(User, users, properties={
    'Age': relation(Ages)})

mary = session.query(User).get_by(name='Mary')
print (mary.emails)
