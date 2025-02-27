from flask import Flask, request, jsonify, send_from_directory
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
import logging

# Configure logging
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
        translator = GoogleTranslator(source=input_lang[:2], target=output_lang[:2])
        translated = translator.translate(transcript)
        logger.debug(f"Translated text: {translated}")

        # Use /tmp for audio files
        audio_dir = '/tmp/audio'
        os.makedirs(audio_dir, exist_ok=True)
        audio_file = f"translated_{int(time.time())}.mp3"
        audio_path = os.path.join(audio_dir, audio_file)

        # Generate audio
        logger.debug(f"Saving audio to: {audio_path}")
        tts = gTTS(text=translated, lang=output_lang[:2], slow=False)
        tts.save(audio_path)
        logger.debug(f"Audio file created: {audio_path}")

        audio_url = f"/audio/{audio_file}"
        return jsonify({'translated': translated, 'audio_url': audio_url})
    except Exception as e:
        logger.error(f"Error during translation or TTS: {str(e)}")
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    """Serve audio files from /tmp/audio"""
    audio_dir = '/tmp/audio'
    try:
        return send_from_directory(audio_dir, filename)
    except Exception as e:
        logger.error(f"Error serving audio: {str(e)}")
        return jsonify({'error': 'Audio file not found'}), 404

# No custom handler needed; Flask's app is WSGI-compatible
