from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()

template = Jinja2Templates(directory="./")

class JD(BaseModel):
    QA: str
    
    
@app.put("/JobDescription/{Job_Description}")
def create_item(Job_Description: str, jd: JD):
    return {"Job_Description": Job_Description,"Q&A": jd.QA}


