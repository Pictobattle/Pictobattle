from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "<head><title>bro</title></head><h1>Looking for Picto Battle</h1>Uhmmm... how do I say this... <br> <strong>WE AREN'T DONE DEVELOPING YET!</strong>"
<head>Picto Battle will be on the app store later<br>untill then<strong>bye bye
if __name__ == "__main__":
	app.secret_key = 'Ymsf,sfatwBU!Iwruh,bus'
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=4000
		)
