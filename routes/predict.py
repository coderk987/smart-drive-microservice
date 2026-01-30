from fastapi import FastAPI, APIRouter, UploadFile, File, Form, Header
from services.cloudinary import fetch_cloud
from services.qdrant import fetch_embedding
from services.model import predict

router = APIRouter()

@router.post("/predict")
def get_images(event: str = Form(...)):
    cloudRes = fetch_cloud(event)
    qdrantRes = fetch_embedding(event)

    predict(qdrantRes)

    return [cloudRes, qdrantRes]

