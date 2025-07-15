import os
import sample_texts
import numpy as np
from dotenv import load_dotenv
from scipy.stats import pearsonr
from langchain_openai import OpenAIEmbeddings
from scipy.spatial.distance import euclidean,cityblock,chebyshev

load_dotenv()

#initialize embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-large")

#distance/similarity metrics between vectors. All functions take two numpy arrays and return a float
def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    return euclidean(a, b)

def manhattan_distance(a: np.ndarray, b: np.ndarray) -> float:
    return cityblock(a, b)

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b)

def chebyshev_distance(a: np.ndarray, b: np.ndarray) -> float:
    return chebyshev(a, b)

def pearson_correlation(a: np.ndarray, b: np.ndarray) -> float:
    corr, _ = pearsonr(a, b)
    return corr

# normalize vector to unit length
def normalize_vector(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)

#generate and normilize embeddins for text samples
texts = [sample_texts.text_agent,sample_texts.text_agent_planning,sample_texts.text_skyline]
embeddings = [normalize_vector(embedding.embed_query(text)) for text in texts]

#compare each pair of embeddings using various metrics
pairs = [(0,1),(0,2),(1,2)]

if __name__ == "__main__":
    for i,j in pairs:
        a,b = embeddings[i], embeddings[j]
        print(f'Compare text {i+1} and {j+1}')
        print('Euclidean: ',euclidean_distance(a,b))
        print('Manhattan: ',manhattan_distance(a,b))
        print('Chebyshev: ',chebyshev(a,b))
        print('Cosine similarity: ',cosine_similarity(a,b))
        print('Pearson correlation: ',pearson_correlation(a,b))
        print()