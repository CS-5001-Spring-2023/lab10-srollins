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

@app.route('/foo/', methods=['GET'])
def bar():
	return f'<html>Hello, World!</html>'

@app.route('/messages/', methods=['GET'])
def messages():
	message = request.args.getlist('message')
	message_id = request.args.getlist('message_id')

	if len(message) > 0:
		new_message = Message(message[0])
		message_list.append(new_message)
		return render_template('message_board.html', items=message_list)
		
	elif len(message_id) > 0:
		for i in message_list:
			if i.message_id == int(message_id[0]):
				result = i
				break
		return render_template('message.html', item=result)

	return render_template('message_board.html', items=message_list)






