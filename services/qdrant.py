from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://4fedf2d2-42dd-486c-80e3-fe05b78e59e6.us-east4-0.gcp.cloud.qdrant.io", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.nCoI4CGT8r4TSx9yWSy1KQtH3h-Dp_GPOYaEtFAKypk",
)

print(qdrant_client.get_collections())

def upsert_embedding(public_id, embedding):
    qdrant_client.upsert(
        collection_name="embeds",
        points=[
            {
                "id": public_id,
                "vector": embedding,
                "payload": {
                    "source": "image"
                }
            }
        ]
    )