try:
	print("импортируем модули...")
	from flask import Flask, send_from_directory
	
	print("создаём приложение...")
	app = Flask(__name__)
	
	print("создаём маршруты... ", end="")
	@app.route('/')
	def index():
		try:
			return send_from_directory('.', 'index.html')
		except FileNotFoundError:
			return send_from_directory('.', '404.html') 
	print("index.html ", end="")
	
	@app.route('/<path:filename>')
	def get_file(filename):
		if 'hide' in filename:
			return send_from_directory('.', '403.html')
		return send_from_directory('.', filename)
	print("остальное" end="\n")
	if __name__ == '__main__':
		try:
			print("запуск приложения...")
			run_simple('0.0.0.0', 80, app, use_reloader=True)
		except PermissionError:
			print("ошибка: нет привилегий для работы на порту 80. попробуйте:")
			print("  * запустить программу от лица root, вставив sudo перед  ")
			print("    командой                                              ")
			print("  * использовать аргумент port. он запустит сервер на     ")
			print("    выбранном вами порту, допустим:                       ")
			print("    python3 main.py --port=3000 запустит сервер на порту  ")
			exit("    3000, т.е. localhost:3000 либо <ваш URL>:3000         ")
	
except KeyboardInterrupt:
	print("ошибка: Ctrl+C нажат. попробуйте:")
	exit("  * запустить программу заново")
except EOFError:
	print("ошибка: вызван EOF (клавиша Ctrl+D). попробуйте:")
	exit("  * запустить программу заново")
