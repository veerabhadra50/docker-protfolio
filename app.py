from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    # host=0.0.0.0 so Docker can expose it
    app.run(debug=True, host='0.0.0.0', port=5000)
