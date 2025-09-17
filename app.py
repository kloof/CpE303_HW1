from flask import Flask, render_template, request, session, redirect
from datetime import datetime



app = Flask(__name__)
app.secret_key = 'i_swear_this_isnt_ai_:)'



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/insert_name', methods=['GET', 'POST'])
def insert_name():
    if request.method == 'POST' and request.form['name']:
        name = request.form['name']
        timestamp = datetime.now().strftime('%H:%M:%S')
        entry = {'name': name, 'timestamp': timestamp}

        guestbook = session.get('guestbook', [])
        guestbook.insert(0, entry)
        session['guestbook'] = guestbook

        print(session['guestbook'])
        print(entry)

        return redirect('guestbook')

    
    return render_template('sign.html')

@app.route('/sign')   
def sign():
    return render_template('sign.html')

@app.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    session['guestbook'] = []
    return redirect('guestbook')


if __name__ == '__main__':
    
    app.run(debug=True)
