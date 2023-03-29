from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from gpt import Assistant

assistant = Assistant()
app = Flask(__name__)
CORS(app, origins=["http://localhost:8000","http://localhost:5173"], supports_credentials=True)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Accepts a JSON payload containing a user's message and returns a response from the GPT model.

    Raises:
        ValueError: If the input data is empty or doesn't contain a 'message' key.

    Returns:
        A JSON response containing the generated response from the GPT model.
    """
    try:
        data = request.get_json()
        message = data['message']
        if not message:
            raise ValueError("Invalid input data. Expected a 'message' key with a non-empty value.")
        # response = assistant.chat(message)
        response = "DEBUG MODE"
        return jsonify({'response': response})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500

@app.route('/api/completion', methods=['POST'])
def completion():
    """
    Accepts a JSON payload containing a user's message and returns a response from the GPT model.
    However, prompt messages are not saved on the server.

    Raises:
        ValueError: If the input data is empty or doesn't contain a 'message' key.

    Returns:
        A JSON response containing the generated response from the GPT model.
    """
    try:
        data = request.get_json()
        messages = data['messages']
        if not messages:
            raise ValueError("Invalid input data. Expected a 'message' key with a non-empty value.")
        response = Assistant.completion(messages)
        return jsonify({'response': response})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500



@app.route('/')
def home():
    """
    Returns a JSON message.
    """
    return jsonify({'message': 'Hello, World!'})

@app.errorhandler(404)
def not_found_error(error):
    """
    Handles a 404 error by returning a JSON response.
    """
    return jsonify({'error': 'The requested resource was not found.'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles a 500 error by returning a JSON response.
    """
    return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    app.run()