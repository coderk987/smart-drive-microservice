from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from config import QDRANT_API_KEY, QDRANT_API_URL

qdrant_client = QdrantClient(
    url=QDRANT_API_URL, 
    api_key=QDRANT_API_KEY,
)

print(qdrant_client.get_collections())
#qdrant_client.create_payload_index(
    #collection_name="embeds",
    #field_name="event",
    #field_schema = "keyword" 
#)

def upsert_embedding(public_id, embedding, event):
    qdrant_client.upsert(
        collection_name="embeds",
        points=[
            {
                "id": public_id,
                "vector": embedding,
                "payload": {
                    "source": "image",
                    "event": event
                }
            }
        ]
    )

def fetch_embedding(event):
    points, nextoffset = qdrant_client.scroll(
        collection_name="embeds",
        scroll_filter=Filter(
            must=[
                FieldCondition(key="event", match=MatchValue(value=event)),
            ]
        ),
        limit=10,
        with_payload=True,
        with_vectors=True
    )

    return points