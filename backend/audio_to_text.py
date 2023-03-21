import subprocess
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

whisper_cpp_path = os.getenv('WHISPER_CPP')


class WhisperAudio:
    def __init__(self, wav_audio_dir, transcript_dir, model_type='base'):
        self.wav_audio_dir = wav_audio_dir
        self.transcript_dir = transcript_dir
        self.model_type = model_type

    def audio_to_text(self, audio_mp3_path, lang='auto'):
        audio_wav_path = os.path.join(self.wav_audio_dir, f"{Path(audio_mp3_path).stem}.wav")
        transcript_f_path = os.path.join(self.transcript_dir, f"{Path(audio_mp3_path).stem}")
        subprocess.run(["ffmpeg", "-i", f"{audio_mp3_path}", "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", f"{audio_wav_path}", "-y"])

        subprocess.run(
            ["./main", "-m", f"./models/ggml-{self.model_type}.bin", "-f", f"{os.path.abspath(audio_wav_path)}", "-of", f"{os.path.abspath(transcript_f_path)}", "-otxt", "-l", f"{lang}"],
            cwd=whisper_cpp_path)
        # print(f"{transcript_f_path}.txt")
        with open(os.path.abspath(f"{transcript_f_path}.txt"), "r") as f:
            content = f.read()
        return content


if __name__ == '__main__':
    Path("audios/transcript").mkdir(exist_ok=True, parents=True)
    wh_model = WhisperAudio("audios/wav", "backend/audios/transcript")
    text = wh_model.audio_to_text("audios/d8fff429-8810-58aa-b28d-67c95212f2d9.mp3")
    print(text)
