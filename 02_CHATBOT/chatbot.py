import json
import nltk
import os
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Force NLTK to use local directory for resources
custom_nltk_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(custom_nltk_dir, exist_ok=True)
nltk.data.path.append(custom_nltk_dir)

# Auto download required resources (to custom path)
nltk.download('punkt', download_dir=custom_nltk_dir)
nltk.download('stopwords', download_dir=custom_nltk_dir)

# Load FAQs
with open("faq_data.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

questions = [item['question'] for item in faq_data]
answers = [item['answer'] for item in faq_data]

def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    return " ".join([word for word in tokens if word.isalnum() and word not in stop_words])

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

def get_answer(user_query):
    user_query_processed = preprocess(user_query)
    user_query_vector = vectorizer.transform([user_query_processed])
    similarities = cosine_similarity(user_query_vector, question_vectors)
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]
    
    if best_score < 0.2:
        return "Sorry, I couldn't find a relevant answer. Please try rephrasing your question."
    
    return answers[best_match_index]

if __name__ == "__main__":
    print("🤖 Chatbot: Ask me about Social Media Addiction!\n(Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        print("Bot:", get_answer(user_input))
