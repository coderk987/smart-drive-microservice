from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
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