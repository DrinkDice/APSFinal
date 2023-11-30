import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_base import ModelBase
from models.filmes import Filme
import uuid  # Import the uuid module

# Replace 'your_database_url' with the actual connection string for your database
database_url = 'sqlite:///C:/Users/Bruno/Desktop/APS/banco/sqla_sync/db/filmes.sqlite'
engine = create_engine(database_url)
ModelBase.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Replace 'path/to/your/csv_file.csv' with the actual path to your CSV file
csv_file_path = r'C:\Users\Bruno\Desktop\APS\kaggle\Movies.csv'

# Assuming your CSV file has a header row
try:
    # Specify the delimiter as ';'
    df = pd.read_csv(csv_file_path, delimiter=';')
except FileNotFoundError:
    print(f"Error: CSV file not found at {csv_file_path}")
    session.close()
    exit()

# Import uuid here

# Iterate over DataFrame rows and insert data into the database
data_to_insert = []
for index, row in df.iterrows():
    try:
        rating = float(row['rating'])
        released_year = pd.to_datetime(row['released_year'])
    except ValueError as e:
        print(f"Skipping row {index + 2}: {e}")
        continue

    movie_instance = Filme(
        id=str(uuid.uuid4()),  # Convert UUID to string
        movie=row['movie'],
        released_year=released_year,
        rating=rating,
        director=row['director']
    )

    data_to_insert.append(movie_instance)

# Use bulk_save_objects for better performance
session.bulk_save_objects(data_to_insert)

session.commit()
session.close()
