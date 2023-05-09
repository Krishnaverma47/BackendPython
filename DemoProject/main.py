from fastapi import FastAPI,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr


app = FastAPI()

origins = [
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.post("/uploadfile")
def Home(file:UploadFile):
    if not file:
        return {'detail':'Please Upload File.'}
    if file:
        r = sr.Recognizer()
        jackhammer = sr.AudioFile(file)
        with jackhammer as source:           
            audio = r.record(source)                        
        r.recognize_google(audio)
        