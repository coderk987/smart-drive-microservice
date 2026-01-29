from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import config

router = APIRouter(prefix="/admin")

@router.get('/upload')
def upload_image():
    return "upload request"