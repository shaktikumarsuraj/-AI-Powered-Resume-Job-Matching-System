from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model= SentenceTransformer("all-MiniLM-L6-v2")

def calculate_semantic_similarity(resume,job_description):
    resume_embedding= model.encode([resume])
    job_embedding=model.encode([job_description])

    similarity= cosine_similarity(
        resume_embedding,
        job_embedding
    )

    return similarity[0][0]

