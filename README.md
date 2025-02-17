
![Logo](https://github.com/11unx0/Transcriptor/blob/main/img/demo.png)


# Transcriptor

Transcript Youtube videos and your own video/audio files. Uses Whisper.

Developer: https://github.com/11unx0

## Installation

Install modules with python pip

```bash
git clone https://github.com/11unx0/Transcriptor
cd Transcriptor/
pip install -r requirements.txt
```
    
## Usage/Examples

You can change device with --device and also for model change use --model.

Default device is cpu and default model is medium.

```bash
python3 main.py --device < cpu | cuda > --model < model >
```

Example run with cpu & large-v3 model.

```bash
python3 main.py --device cpu --model large-v3
```

```bash
python3 main.py --help

usage: main.py [-h] [--device {cpu,cuda}] [--model {tiny,base,small,medium,large,large-v2,large-v3}]

Transcript Youtube videos and your own video/audio files. Uses Whisper. Developer: https://github.com/11unx0

options:
  -h, --help            show this help message and exit
  --device {cpu,cuda}   Device to run Whisper model on. Choices are "cpu" or "cuda". Default is "cpu".
  --model {tiny,base,small,medium,large,large-v2,large-v3}
                        Choose a model for Whisper. Default is "medium". More details for models: 
                        https://github.com/11unx0/Transcriptor
```

## Whisper models.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       [tiny](https://huggingface.co/openai/whisper-small)      |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       [base](https://huggingface.co/openai/whisper-base)      |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      [small](https://huggingface.co/openai/whisper-small)      |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      [medium](https://huggingface.co/openai/whisper-medium)     |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      [large](https://huggingface.co/openai/whisper-large)      |    ~10 GB     |       1x       |
| large-v2 | 1550 M   | N/A                  | [large-v2](https://huggingface.co/openai/whisper-large-v2) |
| large-v3 | 1550 M   | N/A                  | [large-v3](https://huggingface.co/openai/whisper-large-v3) |

## Disclaimer

This project is an experimental work. Users are responsible for any errors, damages, or system malfunctions that may occur. The creator of this project will not be held liable for any issues that arise from its use.
## Credits

This project uses the following open-source libraries:

- [Whisper](https://github.com/openai/whisper): An open-source library for automatic speech recognition, developed by OpenAI.
- [Pytube](https://github.com/pytube/pytube): A lightweight, dependency-free Python library for downloading YouTube videos.
- [Gradio](https://github.com/gradio-app/gradio): A library for quickly building and deploying machine learning models as web applications.
