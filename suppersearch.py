from googlesearch import search
from newspaper import Article
from newspaper.article import ArticleException 
import streamlit as st
import nltk

nltk.download('punkt')
st.title("Supper Clubs")
def article_content(url):
    article = Article(url)
    
    try:
        article.download()
        article.parse()
        article.nlp()
        st.write(article.summary)
    except ArticleException as e:
        print("Error while processing article:", e)

def search_and_extract(query):
    search_results = search(query)
    for i, result in enumerate(search_results, start=1):
        if result in visited_links:
            continue
        visited_links.add(result)
        st.subheader(result)
        article_content(result)

if __name__ == "__main__":
    visited_links = {"https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dsupper%252Bclubs%26num%3D12%26hl%3Den%26start%3D0&hl=en&q=EhD9o-ciCsMAEAA62BfAqA_qGOGN0asGIjAS6h9SudvjHRUiWw0qro5Fhr65pAcbD1BlEZm6o918p6it79mSu8atzQl1yvz2nVoyBWpjbmRyWgFD"}
    search_queries = ['supper clubs', 'supper clubs hosted by charities' 'organizing supper clubs']
    for search_query in search_queries:
        st.header(search_query.upper(), divider = "rainbow")
        search_and_extract(search_query)
