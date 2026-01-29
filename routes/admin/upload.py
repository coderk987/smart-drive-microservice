from fastapi import FastAPI, APIRouter, UploadFile, File, Form, Header
import config
import uuid
from services.cloudinary import upload_cloud
from services.model import train, predict
from services import qdrant

router = APIRouter(prefix="/admin")
API_KEY = config.API_KEY

@router.post('/upload')
def upload_image(
    image: UploadFile=File(...),
    event: str = Form(...),
    x_api_key: str = Header(None)):

    if True:
        image_id = str(uuid.uuid4())
        image_embed = train()
        
        cloud_result = upload_cloud(image, image_id, event)
        print(cloud_result)

        return {
            "filename": image.filename,
            "content_type": image.content_type,
            "event": event,
            "image_link": cloud_result["url"],
            "image_id": image_id
        }
    else:
        return "Unauthorized Access"