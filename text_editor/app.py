from flask import Flask, render_template
from models import get_documents  

app = Flask(__name__)

@app.route('/')
def index():
    documents = get_documents()
    return render_template('index.html', documents=documents)

if __name__ == '__main__':
    app.run(debug=True)
