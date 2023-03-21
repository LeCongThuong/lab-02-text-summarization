from summarization import OpenAISummarazation
from download_audio import YoutubeDownload
from audio_to_text import WhisperAudio
from pathlib import Path


class VideoSummarization:
    def __init__(self, mp3_dir, wav_dir, transcript_dir):
        self.ytb_dl = YoutubeDownload(mp3_dir)
        self.ad_to_txt = WhisperAudio(wav_dir, transcript_dir)
        self.sum_text = OpenAISummarazation()

    def video_summarization(self, url):
        audio_path = self.ytb_dl.get_videos_from_link(url)
        text_list = self.ad_to_txt.audio_to_text(audio_path)
        text_str = "".join(text_list)
        result_str = self.sum_text.summarize(text_str)
        return result_str


if __name__ == '__main__':
    mp3_dir = "audios/mp3"
    wav_dir = "audios/wav"
    transcript_dir = "audios/transcript"
    Path(mp3_dir).mkdir(exist_ok=True, parents=True)
    Path(wav_dir).mkdir(exist_ok=True, parents=True)
    Path(transcript_dir).mkdir(exist_ok=True, parents=True)
    test_link = "https://www.youtube.com/watch?v=CQ2LY_SbqwM"
    video_sum = VideoSummarization(mp3_dir, wav_dir, transcript_dir)
    sum_text = video_sum.video_summarization(test_link)
    print(sum_text)
