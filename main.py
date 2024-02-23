from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/<word>")
def meaning(word):
    df = pd.read_csv("dictionary.csv")
    meaning = df.loc[df['word']==word]['definition'].squeeze()
    return {"Meaning": meaning,
            "word": word}


if __name__ == "__main__":
    app.run(port=5001, debug=True)
