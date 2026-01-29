from fastapi import FastAPI, APIRouter, UploadFile, File, Form, Header
from pydantic import BaseModel
import config

router = APIRouter(prefix="/admin")
API_KEY = config.API_KEY

@router.post('/upload')
def upload_image(
    image: UploadFile=File(...),
    event: str = Form(...),
    x_api_key: str = Header(None)):

    if x_api_key==API_KEY:
        return {
            "filename": image.filename,
            "content_type": image.content_type,
            "event": event
        }
    else:
        return "Unauthorized Access"