from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#
DATABASE_URL = "mysql+pymysql://root:<password>@127.0.0.1:3306/project"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#sqlalchemy에서 engine을 만들어 데이터베이스 연결
engine = create_engine(DATABASE_URL)
# session이란 데이터베이스와 클라이언트 사이에서 통신을 시작하는 것부터 종료까지
SessionFactory = sessionmaker(autocommit = False, autoflush= False, bind = engine)

# decorater session으로 db를 열고 닫기까지를 선언
def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()