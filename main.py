from flask import Flask
from google.cloud import dialogflow

import logging

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello, World!'


# [START dialogflow_detect_intent_text]
def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    logging.warning("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(request={"session": session, "query_input": query_input})

        logging.warning("Query text: {}".format(response.query_result.query_text))
        logging.warning("Detected intent: {} (confidence: {})\n".format(response.query_result.intent.display_name, response.query_result.intent_detection_confidence))
        logging.warning("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)