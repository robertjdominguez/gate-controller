from flask import Flask, jsonify, request
from utilities.text_parser import check_query
from utilities.gate_handlers import handle_open_gate, handle_close_gate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Route for health check. Returns a simple message to indicate the server is running.
@app.route('/healthcheck', methods=['GET'])
def check_health():
    return jsonify(message="I'm alive!")


# Route for handling POST requests from Google Assistant. 
# It parses the incoming JSON data, extracts the user's query, and returns a response.
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # get the user's query
    user_command = data['queryResult']['queryText']

    # check the query for the command verb
    command_verb = check_query(user_command.lower())

    # return a response based on the command verb
    if command_verb == 'Opening':
        handle_open_gate()
        return jsonify(fulfillmentText='Opening the gate')
    elif command_verb == 'Closing':
        handle_close_gate()
        return jsonify(fulfillmentText='Closing the gate')
    else:
        return jsonify(fulfillmentText='IDFK')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)