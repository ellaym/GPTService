# app/routes.py
from flask import Blueprint, request, jsonify
from app.gpt_service import query_gpt
import logging

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@main.route('/query', methods=['POST'])
def handle_message():
    """API endpoint to handle GPT queries."""
    data = request.get_json()
    gpt_query = data.get('query')

    if not gpt_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        logging.info(f'Processing query: {gpt_query}')
        # Pass the client explicitly (will be provided from main.py)
        output = query_gpt(main.client, gpt_query)
        return jsonify({"output": output}), 200
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return jsonify({"error": "Failed to communicate with OpenAI", "message": str(e)}), 500
