from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ORM:

    def __init__(self, dbName):
        engine = create_engine("mysql+mysqlconnector://root:admin@localhost/%s" % dbName,
                               encoding='utf8')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def __del__(self):
        self.session.close()

    def filter(self, tb_class, *args):
        return self.session.query(tb_class).filter(*args)


