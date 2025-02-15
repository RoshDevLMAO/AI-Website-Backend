import os
from flask import Flask, request, jsonify
from models.image_gen import generate_image
from models.text_gen import generate_text
from models.text_to_speech import text_to_speech

app = Flask(__name__)

@app.route("/generate-image", methods=["POST"])
def image_gen():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400
        
        prompt = data["prompt"]
        image_url = generate_image(prompt)
        return jsonify({"image_url": image_url})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate-text", methods=["POST"])
def text_gen():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Prompt is required"}), 400

        prompt = data["prompt"]
        text = generate_text(prompt)
        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/text-to-speech", methods=["POST"])
def tts():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Text is required"}), 400

        text = data["text"]
        audio_url = text_to_speech(text)
        return jsonify({"audio_url": audio_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 5000 if PORT is not set
    print(f"Server running on port {port}...")
    app.run(host="0.0.0.0", port=port)
