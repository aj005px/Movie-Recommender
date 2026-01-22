## 🍿 Movie Recommender System

A simple **content-based movie recommendation system** built using **Cosine Similarity** and **TF-IDF Vectorization**.
The app suggests movies similar to a user’s preference and displays **similarity scores**, posters, and movie details using a **Streamlit UI**.

---

## 🚀 Features

* Recommends movies based on textual similarity
* Uses **Cosine Similarity** for recommendation logic
* Displays:

  * Movie posters
  * Movie information
  * Likability (similarity percentage)
* Interactive **Streamlit** interface
* Option to:

  * Select from random movie suggestions
  * Search for a movie manually

---

## 🧠 How It Works

1. Movie metadata is combined into a single text feature (`Combined_Info`)
2. Text is vectorized using **TF-IDF**
3. **Cosine similarity** is calculated between movies
4. Top similar movies are ranked and displayed

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn (TF-IDF & Cosine Similarity)

---

## 📁 Dataset

* Data is loaded from `updated_file.csv`
* Required columns:

  * `Series_Title`
  * `Combined_Info`
  * `Poster_Link`

---

## 🖥️ User Interface

* Displays **3 random movies** as clickable options
* Allows users to **search for a movie manually**
* Shows **Top 5 similar movies** with:

  * Poster
  * Movie details
  * Similarity score (Likability %)

---

## ▶️ Run the App

```bash
pip install streamlit pandas scikit-learn
streamlit run app.py
```

> Make sure `updated_file.csv` is in the same directory.

---

## 📸 Preview

<img width="1879" height="945" alt="image" src="https://github.com/user-attachments/assets/6dea331d-65a7-4055-870e-ae74f1b375c9" />

<img width="1879" height="511" alt="image" src="https://github.com/user-attachments/assets/0437e105-4623-40ab-ad3d-0353c07b2e0e" />


