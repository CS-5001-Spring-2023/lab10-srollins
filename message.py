class Message:

	message_id_generator = 1

	'''
	This class represents the information about a single 
	message.
	'''
	def __init__(self, message):
		self.message = message
		self.message_id = Message.message_id_generator
		Message.message_id_generator += 1