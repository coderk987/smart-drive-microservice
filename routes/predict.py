from fastapi import APIRouter, UploadFile, File, Form, Header
from services.cloudinary import fetch_cloud
from services.qdrant import fetch_embedding
from services.model import predict

router = APIRouter()

@router.post("/predict")
def get_images(image: UploadFile=File(...), event: str = Form(...)):

    cloudRes = fetch_cloud(event)
    qdrantRes = fetch_embedding(event)
    predictRes = predict(qdrantRes)

    print(predictRes)

    filter_img = []
    for prediction in predictRes:
        cur_id = event+'/'+prediction.id
        for cloud_image in cloudRes:
            if cloud_image["id"]==cur_id:
                filter_img.append(cloud_image)

    return [filter_img]

