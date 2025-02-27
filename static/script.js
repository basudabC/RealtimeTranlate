console.log("Script.js loaded");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
console.log("SpeechRecognition initialized:", recognition);

const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');

if (!startBtn) {
    console.error("Start button not found");
} else {
    console.log("Start button found:", startBtn);
}

recognition.continuous = true;
recognition.interimResults = false;

startBtn.addEventListener('click', () => {
    console.log("Start button clicked");
    const inputLang = document.getElementById('input-lang').value;
    const outputLang = document.getElementById('output-lang').value;
    recognition.lang = inputLang;
    try {
        recognition.start();
        console.log("Speech recognition started");
        document.getElementById('status').textContent = 'Listening...';
        startBtn.classList.add('hidden');
        stopBtn.classList.remove('hidden');
    } catch (error) {
        console.error("Error starting recognition:", error);
        document.getElementById('status').textContent = `Error: ${error.message}`;
    }
});

stopBtn.addEventListener('click', () => {
    console.log("Stop button clicked");
    recognition.stop();
    document.getElementById('status').textContent = 'Stopped listening';
    stopBtn.classList.add('hidden');
    startBtn.classList.remove('hidden');
});

recognition.onresult = (event) => {
    console.log("Speech recognition result received");
    const transcript = event.results[event.results.length - 1][0].transcript;
    document.getElementById('transcript').textContent = transcript;
    const inputLang = document.getElementById('input-lang').value;
    const outputLang = document.getElementById('output-lang').value;
    document.getElementById('status').textContent = 'Processing...';

    fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ transcript, input_lang: inputLang, output_lang: outputLang })
    })
    .then(response => {
        console.log("Fetch response received:", response);
        return response.json();
    })
    .then(data => {
        if (data.error) {
            console.error("Translation error:", data.error);
            document.getElementById('status').textContent = `Error: ${data.error}`;
        } else {
            console.log("Translation successful:", data);
            document.getElementById('translated').textContent = data.translated;
            document.getElementById('speak-btn').classList.remove('hidden');
            const audioPlayer = document.getElementById('audio-player');
            audioPlayer.src = data.audio_url;
            audioPlayer.classList.remove('hidden');
            audioPlayer.play();
            document.getElementById('status').textContent = 'Translation complete';
        }
    })
    .catch(error => {
        console.error("Fetch error:", error);
        document.getElementById('status').textContent = `Fetch error: ${error}`;
    });
};

recognition.onerror = (event) => {
    console.error("Speech recognition error:", event.error);
    document.getElementById('status').textContent = `Error: ${event.error}`;
    stopBtn.classList.add('hidden');
    startBtn.classList.remove('hidden');
};

recognition.onstart = () => {
    console.log("Speech recognition actively listening");
};

recognition.onend = () => {
    console.log("Speech recognition ended");
};
