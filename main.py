## author:   11unx0 (https://github.com/11unx0)
## project: https://github.com/11unx0/Transcriptor

import argparse
import whisper
from pytube import YouTube
import gradio as gr

# parameters
parser = argparse.ArgumentParser(description='Transcript Youtube videos and your own video/audio files. Uses Whisper. Developer: https://github.com/11unx0')
parser.add_argument('--device', type=str, choices=['cpu', 'cuda'], default='cpu', help='Device to run Whisper model on. Choices are "cpu" or "cuda". Default is "cpu".')
parser.add_argument('--model', type=str, choices=['tiny', 'base', 'small', 'medium', 'large', 'large-v2', 'large-v3'], default='medium', help='Choose a model for Whisper. Default is "medium". More details for models: https://github.com/11unx0/Transcriptor')
args = parser.parse_args()

# Whisper model load.
#whisper_model = whisper.load_model("base")
whisper_model = whisper.load_model(args.model, args.device) # tiny - base - small - medium - large - large-v2 - large-v3

#|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
#|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
#|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
#|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
#| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
#| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
#| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
#  large-v2   1550 M 	           x 	               yes
#  large-v3   1550 M 	           x 	               yes

def transcribe(input_data, file_data=None):
    if input_data.startswith("https://www.youtube.com/") or input_data.startswith("http://www.youtube.com/") or input_data.startswith("www.youtube.com/") or input_data.startswith("youtube.com/"):
        try:
            yt = YouTube(input_data)
            video = yt.streams.filter(only_audio=True).first()
            audio_file_path = video.download(output_path=".")
            result = whisper_model.transcribe(audio_file_path)
            return result['text'].strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"
    elif file_data is not None:
        try:
            result = whisper_model.transcribe(file_data.name)
            return result['text'].strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return "Please enter a YouTube URL or upload an audio file."

input_text_url = gr.Textbox(label='YouTube URL', placeholder='Enter YouTube video URL or upload audio file')
input_file = gr.File(label="Upload Audio File")

iface = gr.Interface(
    fn=transcribe,
    inputs=[input_text_url, input_file],  # Both input types
    outputs="text",
    title="11unx0's Transcriptor.",
    description="Enter a YouTube video URL or upload an audio file to transcribe it.\n Uses Whisper models by OpenAI.",
)

iface.launch()
