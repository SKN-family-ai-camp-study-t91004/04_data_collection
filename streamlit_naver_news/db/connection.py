""" DB 연결 모듈

DB 접속 코드를 한 곳에 모아두면 저장/조회 로직에서 같은 연결 방식을 재사용할 수 있다.
"""

import mysql.connector

from config.settings import DatabaseSettings

def get_connection(db_settings: DatabaseSettings):
    # MySQL 연결 객체 생성

    return mysql.connector.connect(
        host=db_settings.host,
        port=db_settings.port,
        user=db_settings.user,
        password=db_settings.password,
        database=db_settings.database
    )