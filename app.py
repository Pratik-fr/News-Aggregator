import streamlit as st
import requests

# API Setup
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = 'c201c7b3b6934547b2acf7bb1b3259f5'  # Use your own key

# Function to fetch news
def fetch_news(country, category=None, q=None):
    params = {
        'country': country,
        'apiKey': NEWS_API_KEY,
    }
    if category and category != 'All':
        params['category'] = category
    if q:
        params['q'] = q

    response = requests.get(NEWS_API_ENDPOINT, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'articles': []}

# Streamlit Page Config
st.set_page_config(page_title='News Aggregator', layout='wide')

# Light Theme Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #f4f6f8;
    }}
    .article-title {{
        color: #0077b6;
        font-size: 16px;
        font-weight: bold;
    }}
    .news-item {{
        margin-bottom: 20px;
    }}
    .stImage > img {{
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title('🗞️ News Aggregator')

# Sidebar
with st.sidebar:
    st.subheader("Select Options")
    selected_country = st.selectbox('Select a country', ['US', 'IN','GB', 'CA', 'AU', 'FR', 'DE', 'JP', 'CN', 'RU', 'BR', 'MX', 'IT', 'ES', 'KR'])
    selected_category = st.selectbox('Select a category (optional)', ['All','Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'])

# Search Bar
col1, col2 = st.columns([4, 1])
search_query = col1.text_input(placeholder="Enter a keyword and press Enter to search", label=" ", value="")

# Fetch News
news_data = fetch_news(selected_country, category=selected_category if selected_category != 'All' else None, q=search_query)

# Fallback logic: if no articles and country is not US, switch to US
if not news_data.get("articles") and selected_country != "US":
    st.warning("⚠️ News not available for this country in the free tier. Showing US news instead.")
    news_data = fetch_news("US", category=selected_category if selected_category != 'All' else None, q=search_query)

# Display Articles
articles = news_data.get('articles', [])

col1, col2, col3 = st.columns(3)
if articles:
    for i, article in enumerate(articles):
        with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
            st.markdown('<div class="news-item">', unsafe_allow_html=True)
            if article.get('urlToImage'):
                st.image(article['urlToImage'], use_container_width=True)
            st.markdown(
                f'<a href="{article["url"]}" target="_blank" class="article-title">{article["title"]}</a>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error("No articles found for the selected filters.")
