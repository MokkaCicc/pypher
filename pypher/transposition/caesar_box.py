# TODO: rework

class CaesarBox:
	# TODO: Rework implementation (keep punctuation, whitespace...)
	@classmethod
	def encrypt(cls, message, key):
		#Check the inputs
		try:
			if not isinstance(message, str):
				raise ValueError("Message is not a string")
			if not isinstance(key, int):
				raise ValueError("Key is not an integer")
			if len(message) < key:
				raise ArithmeticError("The length of the message is too small compare to the key")

		except (ValueError, ArithmeticError) as e:
			print("An error occured: {}".format(e))

		else:
			message = message.replace(' ', '')
			message = message.upper()

			#Creation of the transposition table
			transpose = list()
			number_lines = len(message) // key + 1
			for i in range(number_lines):
				offset = i * key
				line = list(message[offset:offset+key])
				transpose.append(line)

			#Add charactere if needed
			while len(transpose[-1]) < key:
				transpose[-1].append('·')

			crypted_message = ""
			for x in range(key):
				for y in range(len(transpose)):
					crypted_message += transpose[y][x]

			return crypted_message

	# TODO: decrypt method
	@classmethod
	def decrypt(cls, crypted_message):
		pass