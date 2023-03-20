from yt_dlp import YoutubeDL
import uuid
import os


class YoutubeDownload:
    def __init__(self, audio_dir):
        self.audio_dir = audio_dir

    def get_videos_from_link(self, youtube_link):
        hash_name = uuid.uuid5(uuid.NAMESPACE_URL, youtube_link)
        ydl_opts = {
            'format': 'bestaudio/best',
            'paths': {"home": f"{self.audio_dir}"},
            'outtmpl': {"default": f"{hash_name}"},
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            output = ydl.download([youtube_link])
        return str(os.path.join(self.audio_dir, f"{hash_name}.mp3"))
