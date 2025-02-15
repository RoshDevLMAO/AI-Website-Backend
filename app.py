import os
from flask import Flask, request, jsonify
from models.image_gen import generate_image
from models.text_gen import generate_text
from models.text_to_speech import text_to_speech

app = Flask(__name__)

@app.route("/generate-image", methods=["POST"])
def image_gen():
    data = request.json
    prompt = data.get("prompt")
    image_url = generate_image(prompt)
    return jsonify({"image_url": image_url})

@app.route("/generate-text", methods=["POST"])
def text_gen():
    data = request.json
    prompt = data.get("prompt")
    text = generate_text(prompt)
    return jsonify({"text": text})

@app.route("/text-to-speech", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text")
    audio_url = text_to_speech(text)
    return jsonify({"audio_url": audio_url})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get PORT from environment variables
    app.run(host="0.0.0.0", port=port)
