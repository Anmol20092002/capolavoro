from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')
@app.route('/about')
def serve_about():
    return send_from_directory('', 'about.html')
@app.route('/contact')
def serve_contact():
    return send_from_directory('', 'contact.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
