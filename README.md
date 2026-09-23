# 📱 SMS Spam Classifier

A Machine Learning-based web application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and Scikit-learn.

## 🚀 Project Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, phishing links, or other potentially harmful content.

This project uses Machine Learning and Natural Language Processing techniques to automatically classify an SMS message into one of two categories:

* 🟢 **Ham** — Legitimate / normal message
* 🔴 **Spam** — Unwanted or potentially malicious message

The trained Machine Learning model is integrated with a **Flask web application**, allowing users to enter an SMS message and receive a prediction.

## ✨ Features

* 📩 SMS text classification
* 🧹 Text preprocessing
* 🔤 Natural Language Processing
* 🤖 Machine Learning classification
* 📊 Model evaluation
* 🌐 Flask web application
* ⚡ Real-time prediction
* 💾 Trained model saved using Pickle

## 🛠️ Technologies Used

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Programming language                  |
| Pandas           | Data manipulation                     |
| NumPy            | Numerical operations                  |
| Scikit-learn     | Machine Learning                      |
| NLP              | Text preprocessing                    |
| Jupyter Notebook | Model development and experimentation |
| Flask            | Web application                       |
| HTML/CSS         | User interface                        |
| Pickle           | Model serialization                   |

## 📂 Project Structure

```text
SMS-Spam-Classifier/
│
├── dataset/
│   └── SMSSpamCollection
│
├── templates/
│   └── index.html
│
├── SMSSpamCollection.ipynb
├── app.py
├── sms_spam.pkl
└── README.md
```

## 🔄 Machine Learning Workflow

The project follows these major steps:

```text
SMS Dataset
     ↓
Data Cleaning
     ↓
Text Preprocessing
     ↓
Feature Extraction
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Save Trained Model
     ↓
Flask Web Application
     ↓
SMS Prediction
```

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains SMS messages labelled as either:

* `ham`
* `spam`

Each message is used as training data for the classification model.

## 🧹 Text Preprocessing

The SMS text is prepared before it is given to the Machine Learning model.

Typical preprocessing steps include:

* Converting text to lowercase
* Removing unnecessary characters
* Cleaning unwanted spaces
* Tokenizing text
* Removing unnecessary words
* Converting text into numerical features

## 🤖 Machine Learning Model

The project uses **Scikit-learn** for Machine Learning and stores the trained model in:

```text
sms_spam.pkl
```

The saved model can then be loaded by the Flask application to make predictions on new SMS messages.

## 🌐 Flask Web Application

The Flask application provides a simple interface where users can enter an SMS message.

### Example

**Input:**

```text
Congratulations! You have won a free prize. Click the link to claim now!
```

**Output:**

```text
Spam
```

Another example:

**Input:**

```text
Hey, are we meeting at 6 PM today?
```

**Output:**

```text
Ham
```

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/gogulvkn/SMS-Spam-Classifier.git
```

### 2. Navigate to the project

```bash
cd SMS-Spam-Classifier
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install pandas numpy scikit-learn flask jupyter
```

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Enter an SMS message and click the prediction button to classify it.

## 📈 Model Evaluation

The Machine Learning model can be evaluated using standard classification metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help measure how effectively the model distinguishes between spam and legitimate messages.

## 🎯 Project Objective

The main objective of this project is to build an automated SMS classification system that can:

1. Process raw SMS text.
2. Extract useful features from the text.
3. Train a Machine Learning classification model.
4. Predict whether a new message is Spam or Ham.
5. Provide the prediction through a web interface.

## 🔮 Future Improvements

Possible improvements include:

* Add multiple Machine Learning models and compare performance.
* Improve NLP preprocessing.
* Add TF-IDF feature extraction.
* Add prediction confidence/probability.
* Improve the web interface.
* Deploy the application online.
* Add multilingual SMS spam detection.
* Add more real-world SMS examples for testing.

## 📌 Applications

SMS spam classification can be useful for:

* 📱 Mobile messaging applications
* 🏦 Banking communication systems
* 📧 Communication platforms
* 🔐 Phishing detection
* 🛡️ Fraud prevention systems
* 📩 Automated message filtering

## 👨‍💻 Author

**Gogul V K N**

GitHub:
https://github.com/gogulvkn

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is intended for educational and demonstration purposes.
