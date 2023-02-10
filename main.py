from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def home() -> str:
    return render_template('index.html')


@app.route('/me/', endpoint="aboutMe")
def aboutMe() -> str:
    return render_template('aboutMe.html')


@app.route('/Mom/', endpoint="Mom")
def aboutMe() -> str:
    return render_template('mom.html')


@app.route('/dad/', endpoint="Dad")
def aboutMe() -> str:
    return render_template('dad.html')


if __name__ == "__main__":
    app.run(debug=True)
