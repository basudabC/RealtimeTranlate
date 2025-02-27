from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='../static', static_url_path='/static')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    logger.debug(f"Received data: {data}")
    transcript = data.get('transcript')
    input_lang = data.get('input_lang', 'en-US')
    output_lang = data.get('output_lang', 'es-ES')

    if not transcript:
        logger.error("No transcript provided")
        return jsonify({'error': 'No transcript provided'}), 400

    try:
        # Translate
        logger.debug(f"Translating '{transcript}' from {input_lang[:2]} to {output_lang[:2]}")
        translated = GoogleTranslator(source=input_lang[:2], target=output_lang[:2]).translate(transcript)
        
        # Generate audio
        audio_dir = '../static/audio'
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)
        audio_file = f"audio/translated_{int(time.time())}.mp3"
        audio_path = os.path.join('../static', audio_file)
        tts = gTTS(text=translated, lang=output_lang[:2], slow=False)
        tts.save(audio_path)
        logger.debug(f"Audio saved at: {audio_path}")

        # Return translated text and audio URL
        audio_url = f"/static/{audio_file}"
        return jsonify({'translated': translated, 'audio_url': audio_url})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Vercel requires a function handler for serverless
def handler(request):
    return app(request.environ, request.start_response)