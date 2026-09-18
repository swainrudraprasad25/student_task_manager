from fastapi import FastAPI
from mysql.connector import connect
from pydantic import BaseModel

app = FastAPI()
class TaskRequest(BaseModel):
    #id:int
    title:str
    status:str
connection=connect(
    user="root",
    password="swain@12345",
    host="localhost",
    database="fastapi"
)
pen=connection.cursor()

# decorator in python-a decorator
# is a function that takes ur func as input and
# adds extra features around the func with modify the original function
# @ is used to give func to decorator
# uvicorn is used
# @app.get("/home")
# def home():
#     return "this get request home page"

#pydantic-we define blueprint 
# of our request,pass that class to typehinting
#this is amodule used to define schemas
# @app.post("/sweethome")
# def sweethome():
#     return "this post request home page"
@app.get("/")
def home():
    return "This is home page"
#middelewares-are modules we attach to 
# our application that runs for every req and response
#to know which module is installed,syntax-pip list
@app.post("/create")
def create_task(request:TaskRequest):
    title=request.title
    status=request.status
    pen.execute("insert into task(title,status) values(%s,%s)",
                (title,status))
    connection.commit()
    return "task added successfully"
@app.get("/show")
def show_tasks():
    pen.execute("select * from task")
    task=pen.fetchall()
    return task
@app.put("/update")
def update_tasks():
    pen.execute("update task set status=%s where id=%s",('uncompleted',2))
    pen.execute("update task set id=%s where title=%s",(4,"task4"))
    connection.commit()
    return "task updated"
@app.delete("/delete")
def delete_task():
    pen.execute("delete from task where id between %s and %s",(4,6))
    connection.commit()
    return "task deleted"
connection.close()