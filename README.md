# QlassifyAI-FBISE-Physics-Question-Classifier-


## Overview

**QlassifyAI** is a Machine Learning-powered question classification system designed specifically for **FBISE SSC-II (Class 10) Physics**.

Simply enter a Physics question, and the model predicts the chapter from which the question most likely originated. This helps students, teachers, and educational platforms quickly identify relevant topics and organize study material more efficiently.

## Features

✅ Predicts the chapter of a Physics question instantly

✅ Trained on **1000+ FBISE SSC-II Physics questions**

✅ Covers all chapters in the FBISE Class 10 Physics syllabus

✅ Fast and lightweight machine learning model

✅ Simple and user-friendly interface

✅ Useful for exam preparation, question bank organization, and educational applications

---

## How It Works

1. The user enters a Physics question.
2. The text is preprocessed and converted into numerical features.
3. A trained Machine Learning model analyzes the question.
4. The model predicts the most likely chapter associated with that question.

### Example

**Input:**

> What is total internal reflection? State two applications of optical fibers.

**Output:**

> OPTICS

---

## Dataset

QlassifyAI was trained on a custom-built dataset containing **over 1000 Physics questions** collected, categorized, and labeled according to the FBISE SSC-II Physics curriculum.

The dataset includes:

* Long Questions
* Short Questions
* Conceptual Questions
* Numerical-Based Questions
* Past Paper Questions
* Model and Practice Questions

Each question is mapped to its corresponding chapter, enabling supervised machine learning classification.

---

## Current Scope

### Supported Curriculum

* FBISE SSC-II (Class 10) Physics

### Supported Chapters

* HEAT CAPACITY AND MODES OF HEAT TRANSFER
* THERMAL EXPANSION AND CHANGE OF STATE
* WAVES
* SOUND
* OPTICS
* ELECTROSTATICS
* CURRENT ELECTRICITY
* ELECTRIC CIRCUITS
* ELECTRONICS
* ELECTROMAGNETISM
* ELECTROMAGNETIC WAVES
* NUCLEAR PHYSICS


---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Machine Learning
* Natural Language Processing (NLP)

---

## Future Improvements

🚀 Support for additional FBISE subjects

🚀 Support for SSC-I (Class 9)

🚀 AI-powered explanation of why a question belongs to a specific chapter

🚀 Automatic classification of entire past papers

🚀 OCR integration for scanned question papers

🚀 Deep Learning and Transformer-based models for higher accuracy

---

## Educational Impact

Students often struggle to identify which chapter a question belongs to, especially when revising from past papers. QlassifyAI streamlines the revision process by automatically classifying questions, helping learners focus on the relevant concepts and chapters.

This project demonstrates how Machine Learning and Natural Language Processing can be applied to solve real-world educational challenges within the FBISE curriculum.

---

## Installation

```bash
git clone https://github.com/manahiljavaid13-design/QlassifyAI.git
cd QlassifyAI

pip install -r requirements.txt

streamlit run app.py
```

---

## Project Status

🟢 Active Development

Current version focuses on **FBISE SSC-II Physics chapter classification** and serves as the foundation for a larger AI-powered educational toolkit.

---

## Author

**Manahil Javaid**

Built as an educational AI project exploring the intersection of **Machine Learning, Natural Language Processing, and Education Technology (EdTech)**. 🚀📚
