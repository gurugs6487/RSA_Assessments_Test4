from app import flask_app
from waitress import serve

if __name__ == '__main__':
    serve(flask_app, host='0.0.0.0', port=5000)
    #flask_app.run(debug=True, host='0.0.0.0', port=5000)