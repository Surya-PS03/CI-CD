from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def getHealth():
    return {"message":"Server is fine and running"}

@app.get("/hello")
async def hello():
    return {"message":"hello world!"}

@app.get("/get_name")
async def getName():
    return {"message":"My name is Surya"}