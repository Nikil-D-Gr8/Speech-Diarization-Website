# Speech Diarizer

This Speech Diarizer is a Streamlit application designed to transcribe audio files into text using the AssemblyAI transcription service. With this app, users can easily upload audio files in MP3 format, initiate the transcription process, and view the transcribed text on the screen. Additionally, users have the option to download the transcribed text as a text file for further reference.

## Setup

### Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### AssemblyAI API Key Setup

Before using the app, you need to obtain an API key from AssemblyAI. Follow these steps:

1. Sign up for an account on [AssemblyAI](https://www.assemblyai.com/).
2. Once logged in, navigate to the API section of your dashboard.
3. Copy your API key.
4. Create a file named `api_credentials.py` in the project directory.
5. Inside `api_credentials.py`, define a variable named `api_KEY_aai` and assign your API key to it:

```python
# api_credentials.py

api_KEY_aai = "YOUR_API_KEY"
```

Replace `"YOUR_API_KEY"` with your actual API key.

## Usage

1. Run the Streamlit app by executing the following command:

```bash
streamlit run main.py
```

2. The app will open in your default web browser.
3. Upload an audio file by clicking the "Upload audio file" button.
4. Click the "Transcribe" button to start the transcription process.
5. Once the transcription is complete, the transcribed text will be displayed on the screen.
6. Optionally, click the "Download transcribed text" button to download the transcribed text as a text file.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [AssemblyAI](https://www.assemblyai.com/)

## Contributor

- [NIKIL PAUL] - [https://github.com/Nikil-D-Gr8)]

## License

This project is licensed under the [MIT License](LICENSE).


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Nikil-D-Gr8/DentalTranscribe/tree/main/HEAD)
