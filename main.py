import whisper
from pytube import YouTube
import gradio as gr

# Whisper model load.
#whisper_model = whisper.load_model("base")
whisper_model = whisper.load_model("medium") # tiny - base - small - medium - large - large-v2 - large-v3

# Size 	Parameters 	English-only 	Multilingual
# tiny 	    39 M 	    yes 	        yes
# base 	    74 M 	    yes 	        yes
# small	    244 M 	    yes 	        yes
# medium 	769 M 	    yes 	        yes
# large	    1550 M 	    x 	            yes
# large-v2 	1550 M 	    x 	            yes
# large-v3 	1550 M 	    x 	            yes

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

input_text_url = gr.inputs.Textbox(label='YouTube URL', placeholder='Enter YouTube video URL or upload audio file')
input_file = gr.inputs.File(label="Upload Audio File")

iface = gr.Interface(
    fn=transcribe,
    inputs=[input_text_url, input_file],  # Both input types
    outputs="text",
    title="Transcription Tool",
    description="Enter a YouTube video URL or upload an audio file to transcribe it.",
)

iface.launch()
