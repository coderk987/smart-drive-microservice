import random

EMBEDDING_DIM = 512

def train():
    # fake embedding
    return [random.uniform(-1, 1) for _ in range(EMBEDDING_DIM)]

#print(train())

def predict():
    # fake prediction
    return random.choice([True, False])
