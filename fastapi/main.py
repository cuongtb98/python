from fastapi import FastAPI
from config.database import connect 
import re
from untils import *
from models.course import course

app = FastAPI()
collection = connect()

# __ get course __
# get all
@app.get("/course") 
async def get_courses():
    return get_course(collection)

# get by id
@app.get("/course/{course_id}")
async def get_course_id(course_id: int):
    myquery = { "id": course_id}
    course = collection.find_one(myquery)
    if course:
        course['_id'] = str(course['_id'])
        return course
    else:
        return{
            "message": f"course ID {course_id} not found. please check again!"
        }

# __ post course __
@app.post("/course")
async def add_course(course: course):
    data = course.dict()
    create_id_auto_increment(collection,data)
    collection.insert_one(data)
    get_items(data['_id'], data)
    return data

# __ post delete __
@app.delete("/course/{course_id}")
async def delete_course(course_id: int):
    myquery = {"id": course_id}
    collection.delete_one(myquery)
    return {
        "message": "course has been deleted succesfully"
    }

# __ update course __
@app.patch("/course/{course_id}")
async def update_course(course_id: int, title: str):
    myquery = {"id": course_id}
    tilte_old = collection.find_one(myquery)['title']
    newvalues = { "$set": { "title": title } }
    collection.update_one(myquery, newvalues)
    return {
        "message": "course has been updated succesfully",
        "tilte-old": tilte_old,
        "title-new": title
    }
