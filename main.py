from fastapi import FastAPI
from routes.admin.upload import router as upload_router
from routes import router as predict_router

app = FastAPI()
print("server running ")

@app.get('/')
def root():
    return {"body": "Welcome to CCS Smart Drive"}

app.include_router(upload_router)
app.include_router(predict_router)