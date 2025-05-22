# ♻️ Recycler – Can It Be Recycled?

A lightweight Streamlit web app that allows users to upload an image and receive a prediction on whether the object is **recyclable** or **non-recyclable**.

> ⚠️ *Note: This is an experimental project. The model is in its early stages and may not be fully accurate yet.*

---

## 🔗 Live Demo

- 🌐 **Web App**: [Streamlit App](https://recycler-lydianzr.streamlit.app/)
- ⚙️ **API Endpoint**: [Recycler API](https://recycler-api.onrender.com)

---

## 🧠 What It Does

1. Upload an image of an item (e.g. bottle, food, paper, etc.)
2. App sends the image to a hosted machine learning API
3. The API returns a simple response:  
   - ✅ `Recyclable`  
   - ❌ `Not Recyclable`
4. The app shows the result to the user.

---

## 🛠 Tech Stack

| Layer        | Technology                     |
|--------------|-------------------------------|
| Frontend     | [Streamlit](https://streamlit.io) |
| Backend API  | Hosted on [Render](https://render.com) |

---

## ⚙️ How to Run It Locally

### Clone the Repository

```bash
git clone https://github.com/your-username/Recycler.git
cd Recycler
streamlit run recycler_image_app.py
