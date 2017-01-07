import io

import dont_tread_on_memes

import flask

app = flask.Flask(__name__)


@app.route("/", defaults={"caption": "tread on"})
@app.route("/<caption>/")
def main(caption):
    flag = dont_tread_on_memes.dont_me(caption)
    data = io.BytesIO()
    flag.save(data, "PNG")
    data.seek(0)
    return flask.send_file(data, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
