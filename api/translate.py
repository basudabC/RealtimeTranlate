from flask import Flask, request, jsonify, send_from_directory, render_template
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask with explicit template folder
app = Flask(__name__, 
            static_folder='../static', 
            static_url_path='/static', 
            template_folder='../templates')

@app.route('/')
def index():
    """Serve the homepage"""
    logger.debug("Serving index.html")
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Failed to render index.html: {str(e)}")
        return jsonify({'error': f'Failed to load homepage: {str(e)}'}), 500

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
        logger.debug(f"Translating '{transcript}' from {input_lang[:2]} to {output_lang[:2]}")
        translator = GoogleTranslator(source=input_lang[:2], target=output_lang[:2])
        translated = translator.translate(transcript)
        logger.debug(f"Translated text: {translated}")

        audio_dir = '/tmp/audio'
        os.makedirs(audio_dir, exist_ok=True)
        audio_file = f"translated_{int(time.time())}.mp3"
        audio_path = os.path.join(audio_dir, audio_file)

        logger.debug(f"Saving audio to: {audio_path}")
        tts = gTTS(text=translated, lang=output_lang[:2], slow=False)
        tts.save(audio_path)
        logger.debug(f"Audio file created: {audio_path}")

        audio_url = f"/audio/{audio_file}"
        return jsonify({'translated': translated, 'audio_url': audio_url})
    except Exception as e:
        logger.error(f"Error in translate route: {str(e)}")
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    """Serve audio files from /tmp/audio"""
    audio_dir = '/tmp/audio'
    try:
        logger.debug(f"Serving audio file: {os.path.join(audio_dir, filename)}")
        return send_from_directory(audio_dir, filename)
    except Exception as e:
        logger.error(f"Error serving audio: {str(e)}")
        return jsonify({'error': f'Audio file not found: {str(e)}'}), 404
