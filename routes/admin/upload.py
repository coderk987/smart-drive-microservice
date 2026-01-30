from fastapi import APIRouter, UploadFile, File, Form, Header
import config
import uuid
from client.client import stub
from proto import service_pb2

router = APIRouter(prefix="/admin")
API_KEY = config.API_KEY

@router.post('/upload')
async def upload_image(image: UploadFile=File(...), event: str = Form(...), x_api_key: str = Header(None)):

    if x_api_key==API_KEY:
        image_bytes = await image.read()
        response = stub.UploadImage(
            service_pb2.ImageRequest(
                image=image_bytes,
                event=event
            )
        )

        return {
            "event": response.image_event,
            "id": response.image_id,
            "url": response.image_url
        }
    else:
        return "Unauthorized Access"