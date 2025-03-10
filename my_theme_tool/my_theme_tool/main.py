import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_most_similar_theme(master_file: str, themes_dir: str):
    with open(master_file, 'r', encoding='utf-8') as f:
        master_css = f.read()

    candidate_paths = []
    candidate_texts = []
    
    for theme in os.listdir(themes_dir):
        theme_css_path = os.path.join(themes_dir, theme, "theme.css")
        if os.path.isfile(theme_css_path):
            candidate_paths.append(theme_css_path)
            with open(theme_css_path, 'r', encoding='utf-8') as f:
                candidate_texts.append(f.read())

    documents = [master_css] + candidate_texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    master_vector = tfidf_matrix[0]
    candidate_vectors = tfidf_matrix[1:]
    similarities = cosine_similarity(master_vector, candidate_vectors).flatten()

    best_idx = similarities.argmax()
    best_match_path = candidate_paths[best_idx]
    best_similarity = similarities[best_idx]
    return best_match_path, best_similarity

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Find the theme.css file most similar to the master theme.')
    parser.add_argument('master_theme', help='Path to the master theme.css file')
    parser.add_argument('themes_dir', help='Directory containing theme folders with theme.css files')
    args = parser.parse_args()

    match, similarity = find_most_similar_theme(args.master_theme, args.themes_dir)
    print(f"The theme.css file most similar to the master theme is: {match}")
    print(f"Similarity ratio: {similarity:.2f}")

if __name__ == '__main__':
    main()
