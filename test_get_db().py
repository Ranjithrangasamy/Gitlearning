from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from typing import Optional
from database import get_db




app=FastAPI()

class Student(BaseModel):
    id:int
    name:str
    phone_no:int
    age : int
    address:str
    passwordd:str

@app.post('/students/')
def insert_student(student:Student):
    # conn=psycopg2.connect(
    #     host='localhost',
    #     database='TestAPI',
    #     user='postgres',
    #     password='lion'

    # )
    conn=get_db()
    cur=conn.cursor()
    cur.execute(
        'insert into student values (%s,%s,%s,%s,%s,%s)',
        (student.id,student.name,student.age,student.phone_no,student.passwordd,student.address)
    )
    data=cur.fetchall()
    cur.close()
    conn.close()
    return {'student':data}

