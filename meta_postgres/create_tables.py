# Imports

from sqlalchemy import create_engine
import time

# Waiting for database !!! Причина не ясна
time.sleep(10)
# Creating meta tables
engine = create_engine("postgresql://test_user:1234@meta_postgres:5432/meta_db")

engine.execute("""create schema meta""")

engine.execute("""
    create table meta.logging (
    	table_name varchar(255),
    	operation_type varchar(50),
    	log_message text,
    	log_state varchar(50),
    	log_dttm timestamp
    )
    """)

# Other tables 
