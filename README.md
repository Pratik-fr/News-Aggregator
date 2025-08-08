# News-Aggregator

Welcome to the News Aggregator project! This application allows users to view top news headlines from various countries and categories, and perform keyword-based searches. The app is built using Streamlit and leverages the News API to fetch real-time news articles.

## Features

- View top headlines from multiple countries.
- Filter news by categories like Business, Entertainment, Health, Science, Sports, and Technology.
- Search for specific news articles using keywords.
- Responsive layout with a user-friendly interface.

## Technologies Used

- [Streamlit](https://www.streamlit.io/): A framework to build interactive web apps.
- [News API](https://newsapi.org/): A simple HTTP REST API for searching and retrieving live articles from all over the web.

## Installation

1. Clone the repository:

   bash
   git clone https://github.com/yourusername/news-aggregator.git
   cd news-aggregator
   

2. Create a virtual environment and activate it:

   bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   

3. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

## Running the Application

1. Set up your News API key in the NEWS_API_KEY variable in app.py.

2. Run the Streamlit app:

   bash
   streamlit run app.py
   

3. Open your browser and navigate to http://localhost:8501 to view the app.

## Usage

- Select the country and news category from the sidebar.
- Enter a keyword in the search bar to search for specific news articles.
- Click on the news article titles or images to read the full articles.


## Contributing

Contributions are welcome! Please create a pull request or submit an issue to contribute to the project.

## License

This project is licensed under the MIT License.
