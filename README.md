<H2> The app only is served for the demo in class.

To deploy the app need to do some steps:
* Need insert OpenAI key and whisper.cpp path into the .env file 
* pip install -r requirements.txt: to install the necessary packages.
* setup backend:
  * cd backend
  * uvicorn main:app --reload
* setup frontend
  * cd frontend
  * python3 gradio_app.py

If do these above steps correctly, after the setup fontend step, a public URL will appear.

Warning: Because the codebase is developed in "lightning" time, so there are many potential bugs. 


