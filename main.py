from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from Scripts.email_sender import send_email_with_photo
from Scripts.stegonography import encode_image, decode_image
import Scripts.crypto

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send-file")
async def create_upload_file(file: UploadFile, message: str = Form(...),password: str = Form(...), receiver: str = Form(...)):
    try:
        [im, messageLength] = encode_image(file.file, message, password)
        send_email_with_photo(im, file.filename, receiver)
        return {
            "password1": password,
            "code": messageLength
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encode-file")
async def create_upload_file(file: UploadFile, password: str = Form(...), code: int = Form(...)):
    try:
        encoded_message = await decode_image(file, code, password)
        return {
            "message": encoded_message
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))