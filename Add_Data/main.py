'''
To add data to redis database.
'''
import redis
from flask import Flask,request,render_template,redirect,url_for

# To start the application.
app=Flask(__name__)
# Main method to call.
@app.route('/')
def main():
	return render_template('main.html')
# To connect Database.
@app.route('/database/<alphanum>')
def database(alphanum):
	r=redis.Redis(host='localhost',port=6379,password='chiku123',db=0)
	if r.llen('tutorial')!=16:
		r.lpush('tutorial',alphanum)
		print('ok')
		return render_template('main.html')
	else:
		return "<p>Only 16 charachter allowed.</p>"
# Add methods.
@app.route('/add',methods=['POST'])
def add():
	value=request.form['Add']
	return redirect(url_for('database',alphanum=value))

# If name == main start the app. 
if __name__=='__main__':
	app.run(debug=True)