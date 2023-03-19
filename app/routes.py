from flask import jsonify, render_template, request
from app import flask_app


@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/check', methods=['POST'])
def validate():
    try:
        number = request.json['number']
        if number > 100:
            result = 'High'
        elif number < 100:
            result = 'Low'
        else:
            result = "Equal"
        response_data = {
            'integer': number,
            'result': result
        }
        return jsonify(response_data)
    except Exception as e:
        error_message = str(e)
        response_data = {
            'error': error_message
        }
        return jsonify(response_data)