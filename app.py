# app.py
from flask import Flask, render_template, request, jsonify
from ml import get_pictures

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/get_images', methods=['POST'])
def get_images():
    try:
        text = request.json.get('text')
        print('Received text:', text)

        images = get_pictures(text)
        print('Images:', images)

        response = jsonify(images)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
