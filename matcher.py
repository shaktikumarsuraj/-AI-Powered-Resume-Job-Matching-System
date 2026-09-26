from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances

def calculate_similarity(resume, job_description):
    documents=[resume,job_description]
    vectorizer= TfidfVectorizer()
    tfidf_matrix= vectorizer.fit_transform(documents)

    similarity= cosine_similarity(tfidf_matrix[0],tfidf_matrix[1])
    return similarity[0][0]
