import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Recycle Detector", layout="centered")

# Header
st.title("♻️ Recycle Detector")
st.write("Upload an image to check if the item is recyclable.")

# Styled upload box
with st.container():
    uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

# Button and result area
if uploaded_file:
    if st.button("Check"):
        with st.spinner("Sending image to AI model..."):
            try:
                response = requests.post(
                    "https://recycler-api.onrender.com/predict",
                    files={"file": uploaded_file}
                )

                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get("prediction", "Unknown")

                    # Show uploaded image
                    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)


                    # Show result
                    st.markdown("### 🔍 Result")

                    if prediction.lower() == "recyclable":
                        st.success("✅ The item is recyclable.")
                    elif prediction.lower() == "non-recyclable":
                        st.error("❌ The item is not recyclable.")
                    else:
                        st.warning("⚠️ Unable to determine recyclability.")

                else:
                    st.error(f"❌ API error. Status code: {response.status_code}")

            except Exception as e:
                st.error(f"🚨 Error contacting API: {e}")
else:
    st.info("👆 Please upload an image file to continue.")
