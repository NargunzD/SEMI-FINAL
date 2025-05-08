from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return (
        'Dionar M. Timbal<br>'
        'Section 1st A<br>'
        'System integration<br>'
        'Semi Finals'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env variable or default to 5000
    app.run(host='0.0.0.0', port=port)
