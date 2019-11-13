'''
To Pool data from set data structure.
'''
import redis
from flask import Flask,redirect,render_template,url_for
# To start the application.
app=Flask(__name__)

# Main method to show application.
@app.route('/')
def main():
	return render_template('main.html')

# to pool data from redis data structure.
@app.route('/pool')
def pool():
	m=[]
	r=redis.Redis(host='localhost',port=6379,password='chiku123',db=0)
	setdata=r.smembers('mydata')
	for x in setdata:
		m.append(x.decode('utf-8'))
	return render_template('main1.html',setdata=m)
#check if name == main.
if __name__=='__main__':
	app.run(debug=True)