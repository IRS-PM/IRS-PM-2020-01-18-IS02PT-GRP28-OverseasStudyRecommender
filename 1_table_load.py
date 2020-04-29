from sqlalchemy import create_engine
engine = create_engine('mysql://root:Test123!@localhost/oscres_db')

import pandas as pd
data_frame = pd.read_csv('Miscellaneous/university.csv')
# con expect type sqlalchemy.engine.Engine or sqlite3.Connection
data_frame.to_sql(con=engine, name='Recommender_university_course', if_exists='replace')