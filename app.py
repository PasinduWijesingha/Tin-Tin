from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)



UPLOAD_FOLDER = os.path.join('D:\\Connex')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
