from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_text
from utils.analyzer import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    result = analyze_resume(text)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)