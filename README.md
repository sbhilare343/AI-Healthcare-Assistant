# Healthcare Assistant Chatbot

## Overview
The **Healthcare Assistant Chatbot** is a web-based application that provides users with healthcare-related assistance by responding to queries about symptoms, medications, and appointments. Built using advanced natural language processing techniques, it combines pre-trained machine learning models with custom logic to deliver an engaging and user-friendly experience.

---

## Features
- Intelligent healthcare query responses using pre-trained NLP models.
- Provides general advice on symptoms, medications, and appointments.
- Simple and interactive user interface powered by Streamlit.
- Preprocessing of user input to enhance response accuracy.

---

## Objective
To build a smart chatbot that enhances healthcare query handling using state-of-the-art NLP and machine learning models.

---

## Outcome
- Streamlined user engagement with tailored responses to healthcare queries.
- Demonstrates the integration of machine learning models for real-world applications.

---

## Tools and Technologies
- **Programming Language:** Python
- **Libraries:**
  - Hugging Face Transformers (DistilBERT)
  - NLTK (Natural Language Toolkit)
  - Streamlit
- **Model:** distilbert-base-uncased-distilled-squad

---

## How to Run
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

4. Open the application in your browser (usually at `http://localhost:8501`).

---

## File Structure
- **app.py:** Main application script.
- **requirements.txt:** Contains the list of Python dependencies.

---

## Sample Inputs
| Input Query                | Response                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| "Hello" or "Hi"           | "Hello! How can I assist you today?"                                   |
| "What are flu symptoms?"  | "Symptoms of the flu include fever, cough, and fatigue."                |
| "What medications to take?"| "Please consult to Doctors for medication advice."                     |
| "Book an appointment."    | "Please consult to Doctors for appointment scheduling."                |

---

## Future Enhancements
- Expand response logic with additional healthcare scenarios.
- Integrate API for real-time medical information.
- Include multi-language support for broader accessibility.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or fixes.

---

## Acknowledgments
- Hugging Face for their pre-trained models.
- Streamlit for providing an excellent framework for web-based applications.

---

Feel free to share your feedback and suggestions to improve this project. Happy coding!

