"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Analyze the emotion of text submitted through the API."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return (
        "For the given statement, the system response is "
        "'anger': " + str(response["anger"]) +
        ", 'disgust': " + str(response["disgust"]) +
        ", 'fear': " + str(response["fear"]) +
        ", 'joy': " + str(response["joy"]) +
        " and 'sadness': " + str(response["sadness"]) +
        ". The dominant emotion is " +
        response["dominant_emotion"] + "."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
