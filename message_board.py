# Make sure to install flask!
# I did this with the following command:
# python3 -m pip install flask 

# Run with the following command:
# flask --app message_board run

from flask import Flask
from flask import render_template
from flask import request
from message import Message

message_list = []

app = Flask(__name__)

@app.route('/messages/', methods=['GET'])
def messages():
	# retrieve the query parameter with name 'message'
	# message will be a list
	message = request.args.getlist('message')
	
	# if the parameter was present
	if len(message) > 0:
		# create a new Message object
		# the value is the item at position 0 of the message list
		new_message = Message(message[0])
		# add the new message
		message_list.append(new_message)
	# the template is found in the templates directory
	return render_template('message_board.html', items=message_list)
