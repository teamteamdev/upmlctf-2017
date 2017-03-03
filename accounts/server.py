from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username'].lower()
    password = request.form['password']
    if username == 'petro' and password == 'Ukra1nEur0pe':
      return render_template('flag.html')
    elif username == 'petro' or username == 'muhtar':
      error = 'Invalid password'
    else:
      error = 'Invalid username'
  return render_template('login.html', error=error)

@app.route('/restore/', methods=['POST', 'GET'])
def restore():
  error = None
  if request.method == 'POST':
    username = request.form['username'].lower()
    if username == 'petro':
      return render_template('restore2.html', error=None)
    elif username == 'muhtar':
      error = 'This user deactivated password restoring'
    else:
      error = 'Invalid username'
  return render_template('restore1.html', error=error)

@app.route('/restore/email/', methods=['POST', 'GET'])
def restore2():
  error = None
  if request.method == 'POST':
    email = request.form['email'].lower()
    if email == 'pogav@hq.dog':
      return render_template('restore3.html', error=None)
    else:
      error = 'Incorrect e-mail'
  return render_template('restore2.html', error=error)

@app.route('/restore/question/', methods=['POST', 'GET'])
def restore3():
  error = None
  if request.method == 'POST':
    answer = request.form['answer'].lower()
    if answer == 'russia':
      return render_template('restore4.html')
    else:
      error = 'Wrong answer'
  return render_template('restore3.html', error=error)

