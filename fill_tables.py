from sqlalchemy import create_engine
import pandas as pd
from faker import Faker

engine = create_engine("postgresql://test_user:1234@localhost:5432/sourse_db")

engine.execute("""
DROP TABLE companies;
CREATE TABLE IF NOT EXISTS companies (
    id int,
    name varchar(255),
    created_at date
    )
    """)

engine.execute("""
    INSERT INTO companies
    VALUES (1, 'Roga&Kopyta', '2022-08-05')
""")

engine.execute("""
DROP TABLE address;
CREATE TABLE IF NOT EXISTS address (
    id int,
    address varchar
    )
    """)

engine.execute("""
    INSERT INTO address
    VALUES (1, 'Moscow')
""")
