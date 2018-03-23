from flask import Flask, request, render_template, redirect, url_for
from app import Encryption

object = Encryption()
object.code_allocation2()
app = Flask(__name__)

# server version for the Encrytion Engine

@app.route('/') # defines the homepage
def homePage():
	return render_template('intro.html')

@app.route('/values') # returns back the input file

def inputFile():
	return render_template('input_val.html')

@app.route('/test')
def test():
	return render_template('output.html', uff = 'Love You')

@app.route('/received', methods=['GET'])
def received():
	if request.method == 'GET':
		text = request.args.get('code')
		b = object.open_file(text)

		return render_template('output.html', uff = b)

if __name__ == '__main__':
	app.run('0.0.0.0', 5000, True)
