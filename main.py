try:
	print("импортируем модули...")
	from flask import Flask, send_from_directory, abort
	from sys import argv
	
	print("парсим все параметры командной строки...")
	
	for i in range(2, len(argv) - 1):
		if argv[i].startswith("--help") == True:
			print("webhome 1.00 - создайте вашу личную веб-страничку")
			print("  --port=[ПОРТ] - использовать другой порт вместо")
			print("                  80. помогает, если у вас нет   ")
			print("                  привилегий для запуска на порту")
			print("                  80                             ")
			print("  --version - показать версию и выйти            ")
			exit("  --help - показать этот вывод и выйти           ")
	
	port = 80
	
	for arg in argv:
		if arg.startswith("--port"):
			print(int(arg.split("=")[1]))
			port = int(arg.split("=")[1])
	
	print(str(port))
	
	print("создаём приложение...")
	app = Flask(__name__)
	
	print("создаём маршруты... ", end="")

	@app.route('/', defaults={'path': ''})
	@app.route('/<path:path>')
	@app.route('/<path:filename>')
	def get_file(filename):
		if 'hide' in filename:
			return send_from_directory('.', '403.html')
		try:
			return send_from_directory('.', filename)
		except FileNotFoundError:
			return send_from_directory('.', '404.html')
		
	@app.errorhandler(404)
	def not_found(error):
		return send_from_directory('.', '404.html')
		
	if __name__ == '__main__':
		try:
			print("запуск приложения...")
			app.run('0.0.0.0', port)
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
