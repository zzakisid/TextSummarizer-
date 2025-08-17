from flask import Flask, render_template, request
from summarizer import summarize_large_text
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summary = summarize_large_text(text)
    return render_template('result.html', summary=summary)

def open_browser():
    """Open browser automatically when app starts"""
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(0, open_browser).start()
    app.run(debug=True)

#use 3.13(venv) as python interpreter