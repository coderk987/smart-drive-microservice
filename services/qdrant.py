from qdrant_client import QdrantClient
from config import QDRANT_API_KEY, QDRANT_API_URL

qdrant_client = QdrantClient(
    url=QDRANT_API_URL, 
    api_key=QDRANT_API_KEY,
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