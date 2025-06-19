from flask import Flask, render_template

app = Flask(__name__)

# Render index.html
@app.route('/')
def index_page():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
