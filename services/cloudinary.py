import cloudinary
import cloudinary.uploader
from config import (
    CLOUDINARY_CLOUD_NAME,
    CLOUDINARY_API_KEY,
    CLOUDINARY_API_SECRET,
)
import cloudinary.api

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True
)

def upload_cloud(image, image_id, event):
    image.file.seek(0)
    return cloudinary.uploader.upload(image.file, folder=event, public_id=image_id)

def fetch_cloud(event, next_cursor=None):
    images = cloudinary.api.resources(type="upload", prefix=event, max_results=50, next_cursor=next_cursor)
    res = []
    
    for image in images["resources"]:
        res.append({"url": image["secure_url"], "id": image["public_id"]})

    return res