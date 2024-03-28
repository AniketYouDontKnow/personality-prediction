import random
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
import streamlit as st
import pickle
from streamlit.runtime.state import get_session_state


def clean_data(post):
    all_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    ps = PorterStemmer()
    post = re.sub(r"https?:\/\/(www)?.?([A-Za-z_0-9-]+)([\S])*", "", post) # Remove links
    post = re.sub("\|\|\|", "", post) # Remove |||
    post = re.sub("[0-9]", "", post) # Remove numbers
    post = re.sub("[^a-z]", " ", post) # Remove punctuation
    post = post.split()
    post = [word for word in post if word not in all_stopwords] # Stopwords removal
    post = " ". join([ps.stem(word) for word in post]) # Stemming
    return post

def final_type(pred):

    random.shuffle((pred))

    mbti_types = [
        ["E", "I"],
        ["N", "S"],
        ["F", "T"],
        ["J", "P"]
    ]
    ans = []
    for i, p in enumerate(pred):
        ans.append(mbti_types[i][p[0]])
    return "".join(ans)

def main():
    session_state = get_session_state()
    common_list = session_state.common_list
    response = ''
    for i in common_list:
        response = response + i

    with open('cv.pkl', 'rb') as pickle_file:
        cv = pickle.load(pickle_file)

    with open('xgb_introv.pkl', 'rb') as pickle_file:
        introv_model = pickle.load(pickle_file)

    with open('xgb_perc.pkl', 'rb') as pickle_file:
        perc_model = pickle.load(pickle_file)

    with open('xgb_sens.pkl', 'rb') as pickle_file:
        sens_model = pickle.load(pickle_file)

    with open('xgb_think.pkl', 'rb') as pickle_file:
        think_model = pickle.load(pickle_file)

    response = response.lower()
    response = clean_data(response)
    response = cv.transform([response])

    prediction_q = [
        introv_model.predict(response),
        sens_model.predict(response),
        think_model.predict(response),
        perc_model.predict(response)
    ]

    st.write("\nPredicted Personality type is:", final_type(prediction_q))
    st.image("final.jpeg")



if __name__ == "__main__":
    main()