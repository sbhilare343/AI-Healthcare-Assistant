from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import streamlit as st

# 1.Downloading necessary nltk data.
nltk.download('punkt')
nltk.download('stopwords')

# 2.Loading pre-trained hugging face model.
bot_pipeline = pipeline(task='question-answering', model='distilbert-base-uncased-distilled-squad')

# 3.Pre-process user input
def pre_process_input(user_input):
    # Tokenize the input text into words
    tokens = word_tokenize(user_input)
    # Remove stopwords from the tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    # Join the filtered tokens back into a string
    filtered_input = ' '.join(filtered_tokens)
    return filtered_input

# 4.Define Healthcare-specific response logic
def health_care_response(user_input):
    # 4.1.Pre-process the user input
    user_input = pre_process_input(user_input).lower()
    
    # 4.2.Logic
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "symptoms" in user_input:
        return "It seems like you're experiencing some symptoms. Please consult to Doctors."
    elif "medication" in user_input:
        return "Please consult to Doctors for medication advice."
    elif "appointment" in user_input:
        return "Please consult to Doctors for appointment scheduling."
    else:
        # 4.3.Using the pre-trained model to generate a response
        context = """I am here to assist with healthcare-related queries. I can provide information about symptoms, medications, 
    and appointments. Please consult a healthcare professional for critical concerns. For example:
    1. Symptoms of the flu include fever, cough, and fatigue.
    2. Common medications include paracetamol for fever and ibuprofen for pain relief.
    3. Appointments can be booked through online healthcare portals or hospital reception.
    """
        response = bot_pipeline(question=user_input, context=context)
        return response
    
# 5.StreamLit web app interface
def main():
    st.title("Healthcare Assistant ChaBot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("You: ", user_input)
            response = health_care_response(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")
            
# main method
if __name__ == "__main__":
    main()