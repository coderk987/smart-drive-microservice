import grpc
from proto import service_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = service_pb2_grpc.ImageServiceStub(channel)