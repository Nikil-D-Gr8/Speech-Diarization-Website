import os
import streamlit as st
import assemblyai as aai
import pandas as pd
import base64
from api_credentials import key

def main():
    st.title("Speech Diarizer")

    st.write("Upload your .mp3 file below:")
    uploaded_file = st.file_uploader("Choose an .mp3 file", type="mp3")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write("Now click the button below to generate transcript.")

        if st.button("Generate Transcript"):
            generate_transcript(uploaded_file)

def generate_transcript(uploaded_file):
    # Set API key
    aai.settings.api_key = key

    # Create directories if they don't exist
    if not os.path.exists("audios"):
        os.makedirs("audios")
    if not os.path.exists("transcripts"):
        os.makedirs("transcripts")

    # Save uploaded file
    audio_path = os.path.join("audios", uploaded_file.name)
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Transcription configuration
    config = aai.TranscriptionConfig(speaker_labels=True, speakers_expected=2)

    # Transcribe the uploaded file
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path, config=config)

    # Display transcript in a scrollable dialog box
    with st.expander("Transcript", expanded=False):
        for utterance in transcript.utterances:
            st.write(f"Speaker {utterance.speaker}: {utterance.text}")

    # Offer download option
    st.write("Download transcript as Excel:")
    download_link = get_excel_download_link(transcript, uploaded_file.name)
    st.markdown(download_link, unsafe_allow_html=True)

def get_excel_download_link(transcript, file_name):
    # Convert transcript to DataFrame
    data = {"Speaker": [], "Text": []}
    for utterance in transcript.utterances:
        data["Speaker"].append(utterance.speaker)
        data["Text"].append(utterance.text)
    df = pd.DataFrame(data)

    # Save DataFrame to Excel
    excel_path = os.path.join("transcripts", f"{os.path.splitext(file_name)[0]}.xlsx")
    df.to_excel(excel_path, index=False)

    # Generate download link
    with open(excel_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.splitext(file_name)[0]}.xlsx">Download Excel file</a>'
    return href

if __name__ == "__main__":
    main()
