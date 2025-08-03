from flask import Flask, request, render_template, jsonify
from resume_parser import parse_resume
from analyzer import analyze_resume
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        parsed_data = parse_resume(filepath)
        analysis = analyze_resume(parsed_data)

        return render_template('results.html', results=analysis)

if __name__ == '__main__':
    app.run(debug=True)
