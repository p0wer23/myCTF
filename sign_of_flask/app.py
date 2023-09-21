#!/usr/bin/env python3
from flask import Flask, request, render_template_string, session, make_response
app = Flask(__name__)
app.secret_key = b'MilanRocks'

@app.route('/')
def challenge():
    if request.headers['User-Agent'].strip()!='Kludge Browser':
        return render_template_string('Only users with "Kludge Browser" are allowed')
    elif 'role' not in session or session['role']!='Head':
        resp = make_response( render_template_string('Welcome Participant!!!\nOnle \'Head\' gets the flag.\nBTW, have you heard of flask unsign?') )
        session['role'] = 'participant'
        session['secret'] = 'MilanRocks'
        return resp
    return render_template_string('MilanCTF{d3m0_f14g}')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)