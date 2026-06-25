from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from typing import Optional





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
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'

    )

    cur=conn.cursor()
    cur.execute(
        'insert into student values (%s,%s,%s,%s,%s,%s)',
        (student.id,student.name,student.age,student.phone_no,student.passwordd,student.address)
    )
    data=cur.fetchall()
    cur.close()
    conn.close()
    return {'student':data}



@app.get('/students/')
def get_students():
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'

    )

    cur=conn.cursor()
    cur.execute(
        'select *from student'
    )
    data=cur.fetchall()
    cur.close()
    conn.close()
    return{'result':data}


@app.put('/students/update/{id}')
def update_students(id:int,student:Student):
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'
    )
    cur=conn.cursor()
    cur.execute(
        'update student set id=%s,name=%s,age=%s,phone_no=%s,passwordd=%s,address=%s where id=%s',
        (student.id,student.name,student.age,student.phone_no,student.passwordd,student.address,id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {'message':'successfully updated student details'}


@app.delete('/student/delete/{id}')
def delete_student(id:int):
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'
    )
    cur=conn.cursor()
    cur.execute(
        'delete from student where id=%s',(id,)
    )

    conn.commit()
    cur.close()
    conn.close()
    return {'message':'student details deleted successfully'}




@app.patch('/student/patch/{id}')
def student_patch(id:int,name:str):
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'
    )
    cur=conn.cursor()
    cur.execute(
        'update student set name=%s where id=%s',(name,id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {'message':'student details patched successfully..'}


# if user sends name in body then uodated name ,
#if user send age in body updated age
#if users send both updated both in a single endpoint
# if users did not give anything it will work fine..

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None

@app.patch('/students/patch_NAME_OR_AGE/{id}')
def students_patch(id:int,student:UpdateStudent): # if updatestudent class having id has a class variable no need to write (id:int) if doesn't contain id then we need to write(id:int)
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'  
            )
    cur=conn.cursor()
    if student.name is not None:
        cur.execute(
            'update student set name=%s where id=%s',
            (student.name,id)

        )
    if student.age is not None:
        cur.execute(
            'update student set age=%s where id=%s',
            (student.age,id)
        )
    conn.commit()
    cur.close()
    conn.close()
    return {'message':'student details patched successfullyy'}




#if user send name and phone_no both condition satisfied then update age 
class patch_age(BaseModel):
    name:str
    phone_no:int
    age:int

@app.patch('/students/patch_AGE_by_Name_and_phone_no/')
def student_patch(student:patch_age):
    conn=psycopg2.connect(
        host='localhost',
        database='TestAPI',
        user='postgres',
        password='lion'

    )
    cur=conn.cursor()
    cur.execute(
        'update student set age=%s where name=%s and phone_no=%s',(student.age,student.name,student.phone_no)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {'message':'student details patched successfullyy'}


# demo modified push into git



