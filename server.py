from flask import Flask, request, render_template, redirect, url_for, send_file
from app import Encryption
from decryptor import decryptor

object = Encryption()
object.code_allocation2()
app = Flask(__name__)

object2 = decryptor()
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

@app.route('/received', methods=['GET', 'POST'])
def received():
	if request.method == 'GET':
		text = request.args.get('code')
		b, h = object.open_file(text)

		return render_template('output.html', uff = b, decrypt = h)

@app.route('/decryptor', methods=['GET','POST'])
def decryptorCaller():
	return render_template('decryptAsker.html')

@app.route('/received2', methods=["POST"])
def decryptionProcess():
	if request.method == 'POST':
		key = request.form['key']
		object2.assigning_key(key)
		object2.accessing_en_doc(request.form['en_code'])
		got = object2.new_extracted_file()
		#print(got)
		return render_template('decryptedCode.html', message = got)

if __name__ == '__main__':
	app.run('0.0.0.0', 5000, True)

