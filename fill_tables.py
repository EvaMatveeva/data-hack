from sqlalchemy import create_engine
import pandas as pd
from faker import Faker

engine = create_engine("postgresql://test_user:1234@postgres:5432/sourse_db")

engine.execute("""
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
CREATE TABLE IF NOT EXISTS public.address (
    id int,
    address varchar
    )
    """)

engine.execute("""
    INSERT INTO public.address
    VALUES (1, 'Moscow')
""")
