# lib/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lib/db/app.db')
Session = sessionmaker(bind=engine)
session = Session()

