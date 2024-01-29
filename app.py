import streamlit as st
from joblib import load

# Main title and subheader
st.header("News Classification")
st.subheader("Enter Sentence")

# Function to show input fields
def show_page():
    comment_text = st.text_input("Enter the sentence:")
    return comment_text

sentence = show_page()

# Button to trigger prediction
if st.button("Predict"):
    if sentence is not None and len(sentence.strip()) > 0:
        try:
            # Load the model
            classifier = load('tccc.pkl')

            # Make a prediction (including TF-IDF transformation)
            prediction = classifier.predict([sentence])

            # Define result categories
            result_categories = {
                0: "Terrorism / Protest / Political Unrest / Riot",
                1: "Positive/Uplifting",
                2: "Natural Disasters",
                3: "Others"
            }

            # Display the prediction result
            st.success(f"The prediction is: {result_categories.get(prediction[0], 'Terrorism / Protest / Political Unrest / Riot')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a sentence before predicting.")
