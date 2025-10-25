# Kid-Safe Text-Mood Detector (Curriculum Developer Intern Project)

This project is a simple web application that classifies the sentiment (mood) of a short text input and displays a kid-friendly emoji result (😊, 😔, 🤔). It is built using Python, the Streamlit framework for the user interface, and the TextBlob library for core sentiment analysis.

## 1. Setup and Run Instructions

To run this application locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Fidha-Fazal/Fidha-Fazal-mood2emoji.git](https://github.com/Fidha-Fazal/Fidha-Fazal-mood2emoji.git)
    cd Fidha-Fazal-mood2emoji
    ```

2.  **Install Dependencies:** Ensure Python 3.9+ is installed, then install the required libraries (listed in `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 2. What the Project Does and How Kids Learn From It

**Function:** The app takes a sentence, calculates a sentiment **Polarity Score** (from -1 to +1), and uses simple rules (logic clarity) to map that score to an emoji. It also includes a **kid-safe filter** (safety) to handle inappropriate inputs.

**Learning Concepts (Ages 12-16):** This introduces students to fundamental AI concepts:
* **Text Classification Basics:** Understanding how computers "read" human language.
* **Rule-Based Logic:** Learning that computers follow explicit rules (e.g., IF score > 0.3 THEN Happy).
* **Data Representation:** Seeing how human emotion is quantified into a numerical score (polarity).

## 3. How I Would Teach It in 60 Minutes

The lesson would follow a **Demo, Explain, Challenge** format:
* **10 Min - Hook:** Introduce the concept of AI "reading feelings."
* **25 Min - Demo & Explain:** Demonstrate the app, and use the **'Teacher Mode'** to reveal the numerical polarity score and explain the simple IF/THEN rules.
* **20 Min - Challenge:** Challenge students to "trick" the app with **sarcasm** (e.g., "I just *love* having 10 hours of homework!") to highlight the **limitations** of simple rule-based AI.
* **5 Min - Wrap-up:** Review the three classification rules and the purpose of the safety filter.

## 4. Known Limitations

* **Sarcasm and Irony:** The model often fails to detect sarcasm because it relies on word sentiment, not context.
* **Cultural Context/Slang:** It struggles with language outside of formal English or modern slang.
* **Double Negatives:** Complex sentences like "I'm not unhappy" can confuse the polarity scoring.