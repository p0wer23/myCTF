#!/usr/bin/env python3
from flask import Flask, request, render_template, render_template_string
import pytesseract
import uuid
import os
app = Flask(__name__)

blacklist_letters = '0123456789%|=+-#'
blacklist_words = ['join', 'class', 'globals', 'builtins', 'request', 'self', 'config', 'init']



def sanitize(content):
    for letter in blacklist_letters:
        if letter in content:
            return render_template_string('Blacklisted Letter Detected!!!')
    for word in blacklist_words:
        if word in content:
            return render_template_string('Blacklisted Word Detected!!!')
    return content


@app.route('/')
@app.route('/read', methods=['GET'])
def hello_world():
    #return 'Hello, World!'
    return render_template('read_file.html')

@app.route('/read', methods=['POST'])
def read():
    f = request.files['file']
    file_name = 'Image''File_' + str(uuid.uuid4())
    f.save(file_name)
    try:
        content=pytesseract.image_to_string(file_name)
    except:
        os.remove(file_name)
        return render_template_string('Unable to read')
    os.remove(file_name)
    sanitize(content)
    try:
        return render_template_string(f'{content}')
    except Exception as e:
        return render_template_string(f'{e}')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)