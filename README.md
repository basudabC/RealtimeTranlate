# Real-Time Healthcare Translation Web App

This is a web application that enables real-time multilingual translation for healthcare communication. It converts spoken input into text, translates it into a user-selected language, and provides audio playback of the translated text. Built with Python (Flask) and JavaScript, it leverages the Web Speech API for speech recognition and is deployed on Vercel for accessibility.

## Features
- **Speech-to-Text**: Converts spoken input to text using the browser's Web Speech API.
- **Real-Time Translation**: Translates text into a user-defined language using `deep_translator` (Google Translate backend).
- **Text-to-Speech**: Generates and plays audio of the translated text with `gTTS`.
- **Multilingual Support**: Supports numerous languages, including English, Spanish, French, Hindi, Bengali, Arabic, Tamil, Telugu, Malayalam, Kannada, Marathi, Gujarati, Punjabi, Russian, Chinese, Japanese, Korean, Thai, and Vietnamese.
- **Mobile-Friendly**: Responsive design with Tailwind CSS for seamless use on mobile and desktop devices.
- **Deployed on Vercel**: Accessible online with a serverless architecture.

## Demo
Visit the live app: [https://realtime-healthcare-translation.vercel.app](https://realtime-healthcare-translation.vercel.app)  
*(Note: Best experienced in Chrome due to Web Speech API support.)*

## Prerequisites
- **Python 3.8+**: For local development and server-side logic.
- **Node.js**: Required for Vercel CLI installation.
- **Git**: For version control and deployment.

## Project Structure

realtime-healthcare-translation/
├── api/
│   └── translate.py       # Flask backend for translation and TTS
├── static/
│   ├── style.css         # Custom CSS styles
│   ├── script.js         # Client-side JS for speech recognition
│   └── audio/            # Temporary folder (not tracked)
├── templates/
│   └── index.html        # Frontend UI
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment configuration
└── README.md             # This file


## Setup Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/realtime-healthcare-translation.git
   cd realtime-healthcare-translation
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   python api/translate.py
   ```
   - Open `http://localhost:5000` in your browser (Chrome recommended).

## Deployment on Vercel

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```
   - Follow prompts to set up the project.
   - Ensure `vercel.json` is configured to serve static files and route requests to `api/translate.py`.

4. **Access the App**:
   - Vercel provides a URL (e.g., `https://realtime-healthcare-translation.vercel.app/`[https://realtime-healthcare-translation.vercel.app/]).

## Usage
1. Open the app in a browser (Chrome preferred).
2. Select an **input language** (language you’ll speak) and an **output language** (desired translation).
3. Click **"Start Listening"** and speak clearly.
4. The app will:
   - Display the transcribed text.
   - Show the translated text.
   - Play the translated audio automatically.
5. Click **"Stop Listening"** to end recording.

## Troubleshooting
- **Button Not Working**: Check browser console (F12) for errors. Ensure microphone permissions are granted.
- **Static Files 404**: Verify `static/style.css` and `static/script.js` load (200 status in Network tab).
- **Translation Fails**: Ensure internet connectivity; logs may indicate network issues with `deep_translator` or `gTTS`.

## Technologies Used
- **Backend**: Flask, `deep_translator`, `gTTS`
- **Frontend**: HTML, Tailwind CSS, JavaScript (Web Speech API)
- **Deployment**: Vercel (serverless)

## Notes
- **Browser Support**: Works best in Chrome due to robust Web Speech API support.
- **Vercel Constraints**: Audio files are stored in `/tmp` due to read-only file system; no persistent storage.

## Contributing
Feel free to fork this repository, submit issues, or send pull requests to enhance functionality (e.g., adding more languages, improving UI).

## License
This project is open-source under the [MIT License](LICENSE).

## Acknowledgments
Built as an interview submission project with assistance from Grok (xAI) for rapid development and debugging.
```

---

### Instructions to Add to GitHub

1. **Create `README.md`**:
   - In your project root (`realtime-healthcare-translation/`), create a file named `README.md`.
   - Copy the content above into it.

2. **Commit and Push**:
   ```bash
   git add README.md
   git commit -m "Added README for GitHub"
   git push origin main
   ```

3. **Update Repository**:
   - If not already on GitHub:
     ```bash
     git remote add origin https://github.com/yourusername/realtime-healthcare-translation.git
     git branch -M main
     git push -u origin main
     ```
   - Replace `yourusername` with your GitHub username.

4. **Verify**:
   - Visit your GitHub repo (e.g., `https://github.com/yourusername/realtime-healthcare-translation`) and ensure the README renders correctly.

---

### Customization
- **Username**: Replace `yourusername` with your actual GitHub username.
- **Live URL**: Update the demo link if your Vercel URL differs.
- **License**: Add a `LICENSE` file if you want to formalize the MIT License (optional).
