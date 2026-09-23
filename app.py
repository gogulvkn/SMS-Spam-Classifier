from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the saved vectorizer and model pipeline
data = joblib.load('sms_spam.pkl')

# Handle cases where only the model was dumped vs dict containing both
if isinstance(data, dict):
    vectorizer = data.get('vectorizer')
    model = data.get('model')
else:
    model = data
    vectorizer = None

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    user_message = ""
    
    if request.method == 'POST':
        user_message = request.form.get('message', '')
        if user_message.strip():
            if vectorizer is not None:
                transformed_input = vectorizer.transform([user_message])
                pred = model.predict(transformed_input)[0]
            else:
                pred = model.predict([user_message])[0]
                
            prediction_text = "Spam" if pred == 1 else "Ham (Not Spam)"

    return render_template('index.html', prediction=prediction_text, message=user_message)

if __name__ == '__main__':
    app.run(debug=True)