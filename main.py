from fastapi import FastAPI
from login import login_router 
from signup import signup_router

app = FastAPI()

app.include_router(login_router, tags=["Login Router"])
app.include_router(signup_router, tags=["Signup Page"])

@app.get('/')
def route():
    return "My friendly RAG App"
