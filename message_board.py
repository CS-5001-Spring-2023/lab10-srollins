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

# Show a single message
@app.route('/message/', methods=['GET'])
def message():
	message_id = request.args.getlist('message_id')
	if len(message_id) > 0:
		for i in message_list:
			if i.message_id == int(message_id[0]):
				result = i
				break
		return render_template('message.html', item=result)

	# return default messages page if no message_id
	return render_template('message_board.html')

# Show a list of messages
# Post a new message
@app.route('/messages/', methods=['GET'])
def messages():
	message = request.args.getlist('message')
	# name

	if len(message) > 0:
		new_message = Message(message[0])
		message_list.append(new_message)


	return render_template('message_board.html', items=message_list)


@app.route('/dict/', methods=['GET'])
def dict():
	test = {
		'a': [1, 2, 3],
		'b': [4, 5, 6]
	}
	return render_template('test.html', items=test)




