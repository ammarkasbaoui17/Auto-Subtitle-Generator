from utils.audio_extractor import extract_audio
from utils.subtitle_generator import transcribe_audio, create_srt
from utils.video_subtitle_merger import add_subtitles_to_video
from utils.whisper_model import get_whisper_model
import os

def main():
    # File paths
    video_file_path = input("Enter the path of the video file: ")
    audio_file_path = "audio.mp3"
    subtitle_file_path = "subtitles.srt"
    output_video_path = "C:/Users/ammar/Desktop/studies/ASR_Project/output/video.mp4"

    # Load Whisper model
    model = get_whisper_model()

    # Extract audio from video
    audio_file_path = extract_audio(video_file_path, audio_output_path=audio_file_path)

    if audio_file_path:
        # Transcribe audio to generate subtitles
        result = model.transcribe(audio_file_path)
        create_srt(result["segments"], output_srt_path=subtitle_file_path)

        # Add subtitles to the video
        add_subtitles_to_video(video_file_path, subtitle_file_path, output_video_path)

        # Delete temporary files
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
        if os.path.exists(subtitle_file_path):
            os.remove(subtitle_file_path)

if __name__ == "__main__":
    main()
