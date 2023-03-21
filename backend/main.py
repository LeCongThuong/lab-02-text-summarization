from fastapi import FastAPI
from video_summarization import VideoSummarization
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


class YoutubeLinkInfo(BaseModel):
    yt_link: str
    lang: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

video_summarization = VideoSummarization()


@app.get("/")
def hello_world():
    return "Hello World!"


@app.post("/summarize/")
async def summarize_video(yt_video_info: YoutubeLinkInfo):
    """
    Converts an image file to text and returns the result.
    """
    yt_link = yt_video_info.yt_link
    language = yt_video_info.lang
    content_str, summarization_str = video_summarization.video_summarization(yt_link, language)
    # Return the text file as a response
    return {"content": content_str, "summarization": summarization_str}


