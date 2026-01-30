import grpc
from concurrent import futures
from proto import service_pb2_grpc
from proto import service_pb2

from services.cloudinary import upload_cloud
from services.model import train
from services.qdrant import upsert_embedding
import uuid

class ImageService(service_pb2_grpc.ImageServiceServicer):

    def UploadImage(self, request, context):
        image_id = str(uuid.uuid4())
        image_embed = train()
        upsert_embedding(image_id, image_embed, request.event)
        cloud_result = upload_cloud(request.image, image_id, request.event)
        #print(cloud_result)

        return service_pb2.UploadImageResponse(image_event=request.event, image_url=cloud_result["secure_url"], image_id=image_id)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    service_pb2_grpc.add_ImageServiceServicer_to_server(
        ImageService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()