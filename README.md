![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit)
![Powered by Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20Pro-blueviolet?logo=google)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

# 📄 ATS Resume Analyzer using Gemini + Streamlit

An **AI-powered ATS resume analyzer** that lets users upload their resume and job descriptions to receive:
- ✅ Match percentage
- 📋 Missing keywords
- 💪 Strengths
- 🔧 Areas of improvement

- ## 🚀 Features

- 📝 Upload your resume (PDF or DOCX)
- 💼 Paste the job description of your target role
- 🧠 Extracts keywords and skills using NLP
- 📊 Calculates a match percentage
- ✅ Provides suggestions to improve alignment
- ⚡ Real-time analysis via a user-friendly interface

- ## 🧠 How It Works

1. **Resume Parsing**: Reads your uploaded resume and extracts key sections like skills, experience, and education.
2. **Job Description Analysis**: Extracts keywords and required skills from the provided job description.
3. **Keyword Matching**: Compares both texts to calculate a match score.
4. **Score Breakdown**: Shows your resume’s alignment with job requirements and areas needing improvement.


Built using Google Gemini's **Generative AI** + **Streamlit**.

---

## 📸 Demo GIF

![Demo](https://github.com/arju-chaturvedi/ATS-Resume-Analyzer/blob/main/Screenshot%202025-04-25%20at%201.00.08%20PM.png)

https://github.com/arju-chaturvedi/ATS-Resume-Analyzer/blob/main/Screenshot%202025-05-02%20at%2011.41.38%20PM.png

https://github.com/arju-chaturvedi/ATS-Resume-Analyzer/blob/main/Screenshot%202025-05-02%20at%2011.41.50%20PM.png

https://github.com/arju-chaturvedi/ATS-Resume-Analyzer/blob/main/Screenshot%202025-05-02%20at%2011.42.21%20PM.png


---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-API-blue?style=for-the-badge)
![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/arju-chaturvedi/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
ATS-Resume-Analyzer/
├── app.py
├── resume_parser.py
├── requirements.txt
├── .env.example
├── assets/
└── README.md
```

---

## 📚 References

- [spaCy](https://spacy.io/)
- [NLTK](https://www.nltk.org/)
- [Streamlit](https://streamlit.io/)

---

## 🙌 Acknowledgements

- Inspired by the need for career support tools that bridge the gap between job seekers and AI-based recruitment systems.
- Built and guided with support from OpenAI’s ChatGPT and educational platforms.

