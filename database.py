
from sqlalchemy import create_engine, text
import os

db_connection_string=os.environ['DB_CONNECTION_STRING']

engine=create_engine(db_connection_string,connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = []
    column_name = result.keys()
    for rowi in result.all():
      rows.append(dict(zip(column_name, rowi)))
    if len(rows) == 0:
      return None
    else:
      return (rows[0])

    
  


  
  
  
  






