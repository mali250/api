

# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS  # Import the CORS module
# import os

# from google.api_core.exceptions import InvalidArgument
# from google.cloud import dialogflow_v2 as dialogflow
# from google.api_core.exceptions import InvalidArgument

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes


# app = Flask(__name__)





# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

# DIALOGFLOW_PROJECT_ID = 'travelbot-409509'
# DIALOGFLOW_LANGUAGE_CODE = 'en'
# SESSION_ID = 'me'


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/dialogflow', methods=['POST'])
# def dialogflow_request():
#     # Change 'message' to 'userMessage'
#     user_message = request.json['userMessage']
#     session_client = dialogflow.SessionsClient()
#     session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#     text_input = dialogflow.types.TextInput(text=user_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
#     query_input = dialogflow.types.QueryInput(text=text_input)

#     try:
#         response = session_client.detect_intent(session=session, query_input=query_input)
#     except InvalidArgument:
#         raise

#     return jsonify({
#         'fulfillment_text': response.query_result.fulfillment_text
        
#     })


# if __name__ == '__main__':
#     app.run(debug=True,port=5001)


from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

from google.api_core.exceptions import InvalidArgument
from google.cloud import dialogflow_v2 as dialogflow

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'travelbot-409509'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dialogflow', methods=['POST'])
def dialogflow_request():
    user_message = request.json['userMessage']
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=user_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        fulfillment_text = response.query_result.fulfillment_text
        print(f"Fulfillment Text: {fulfillment_text}")  # Print the fulfillment text
    except InvalidArgument:
        raise

    return jsonify({
        'fulfillment_text': fulfillment_text
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
