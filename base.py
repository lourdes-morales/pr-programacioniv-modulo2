from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:UIP2023Root_@localhost/diccionariotest')
Session = sessionmaker(bind=engine)

Base = declarative_base()