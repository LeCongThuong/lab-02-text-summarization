import gradio as gr
from utils import summarize_text

demo = gr.Interface(
    summarize_text,
    inputs=[
        gr.Textbox(label="Youtube link", placeholder="Enter Youtube link here..."),
        gr.Dropdown(["auto", "en"], label="Language", value="auto"),
    ],
    outputs=[
        gr.Textbox(label="Audio2Text", placeholder="Content of the Youtube video", lines=5),
        gr.Textbox(label="Summarization", placeholder="Main content of the Youtube video", lines=5)
    ],
    examples=[["https://www.youtube.com/watch?v=Uew5BbvmLks", "en"], ["https://www.youtube.com/watch?v=p79GmLNLMrY", "en"], ["https://www.youtube.com/watch?v=cZv-m3Bvnn4", "auto"]],
    allow_flagging="never"
    )

if __name__ == '__main__':
    demo.launch()
