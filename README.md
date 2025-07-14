DEMO link : https://movie-recommender-3-x3ua.onrender.com


# 🎬 Movie Recommendation System (Content-Based)

This project is a **content-based movie recommender system** built using **vectorization techniques** like **TF-IDF** and **cosine similarity**. It suggests movies that are most similar in terms of content, based on an input movie title.

---

## 🎯 Objective

To recommend movies similar to a user’s favorite one, using only the available **movie metadata** like genres, keywords, overview, and cast.

---

## 📊 Dataset

Used a cleaned version of a **movie metadata dataset** containing:
- Title
- Overview
- Genre
- Keywords
- Cast
- Director

---

## 🧠 How It Works

1. **Preprocessing & Feature Engineering**
   - Combined textual features into a single column
   - Removed stopwords and converted text to lowercase

2. **Vectorization**
   - Applied **TF-IDF (Term Frequency-Inverse Document Frequency)** or **CountVectorizer**
   - Measured **cosine similarity** between movies

3. **Recommendation Logic**
   - On selecting a movie, returns the top 5-10 most similar movies

---

## 💡 Technologies Used

- `pandas`, `numpy`
- `scikit-learn` (TF-IDF, cosine_similarity)
- `nltk` (text preprocessing)
- `Flask` or `Streamlit` for deployment (if applicable)

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
python app.py  # or streamlit run app.py
