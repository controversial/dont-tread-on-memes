import io

import dont_tread_on_memes

import flask

app = flask.Flask(__name__)


@app.route("/", defaults={"caption": "tread on"})
@app.route("/<caption>/")
def main(caption):
    # Color argument
    color = flask.request.args.get("color") or "black"
    # Allow disabling of formatting
    should_format = flask.request.args.get("format")
    if should_format == "false":
        flag = dont_tread_on_memes.tread_on(caption, color)
    else: 
        flag = dont_tread_on_memes.dont_me(caption, color)

    data = io.BytesIO()
    flag.save(data, "PNG")
    data.seek(0)
    return flask.send_file(data, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
