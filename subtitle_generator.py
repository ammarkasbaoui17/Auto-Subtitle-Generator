import whisper
import torch

def transcribe_audio(audio_file_path, model_size="medium"):
    model = whisper.load_model(model_size, device="cuda" if torch.cuda.is_available() else "cpu")
    result = model.transcribe(audio_file_path)
    return result

def create_srt(transcription_segments, output_srt_path="subtitles.srt"):
    with open(output_srt_path, "w") as srt_file:
        for i, segment in enumerate(transcription_segments):
            start_time = format_time(segment["start"])
            end_time = format_time(segment["end"])
            text = segment["text"].strip()

            # Write SRT entry
            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
