import random

EMBEDDING_DIM = 512

def train():
    # fake embedding
    return [random.uniform(-1, 1) for _ in range(EMBEDDING_DIM)]

#print(train())

def predict(embeds, user_img):
    #fake filter
    return [embed for embed in embeds if random.random() < 0.25]
