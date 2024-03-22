from sqlalchemy import create_engine
import os

# Construct the database URL
db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
    os.getenv('HBNB_MYSQL_USER'),
    os.getenv('HBNB_MYSQL_PWD'),
    os.getenv('HBNB_MYSQL_HOST'),
    os.getenv('HBNB_MYSQL_DB')
)

# Print the database URL
print("Database URL:", db_url)

# Test the database connection
try:
    engine = create_engine(db_url, pool_pre_ping=True)
    engine.connect()
    print("Database connection successful!")
except Exception as e:
    print("Database connection error:", e)

