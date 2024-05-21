
![Logo](https://example.example/example.png)


# Transcriptor

Transcript Youtube videos and your own video/audio files.


## Installation

Install modules with python pip

```bash
cd Transcriptor/
pip install -r requirements.txt
```
    
## Usage/Examples

```bash
python3 main.py
```
You can change this line for another models of whisper.

```python
whisper_model = whisper.load_model("medium")
```

| Size     | Parameters | English-only                                         | Multilingual                                        |
|----------|------------|------------------------------------------------------|-----------------------------------------------------|
| tiny     | 39 M       | [✓](https://huggingface.co/openai/whisper-tiny.en)   | [✓](https://huggingface.co/openai/whisper-tiny)     |
| base     | 74 M       | [✓](https://huggingface.co/openai/whisper-base.en)   | [✓](https://huggingface.co/openai/whisper-base)     |
| small    | 244 M      | [✓](https://huggingface.co/openai/whisper-small.en)  | [✓](https://huggingface.co/openai/whisper-small)    |
| medium   | 769 M      | [✓](https://huggingface.co/openai/whisper-medium.en) | [✓](https://huggingface.co/openai/whisper-medium)   |
| large    | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large)    |
| large-v2 | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large-v2) |
| large-v3 | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large-v3) |

## Disclaimer

This project is an experimental work. Users are responsible for any errors, damages, or system malfunctions that may occur. The creator of this project will not be held liable for any issues that arise from its use.
## Credits

This project uses the following open-source libraries:

- [Whisper](https://github.com/openai/whisper): An open-source library for automatic speech recognition, developed by OpenAI.
- [Pytube](https://github.com/pytube/pytube): A lightweight, dependency-free Python library for downloading YouTube videos.
- [Gradio](https://github.com/gradio-app/gradio): A library for quickly building and deploying machine learning models as web applications.
