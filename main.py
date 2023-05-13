from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from Scripts.stegonography import encode_image, decode_image
import Scripts.crypto

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile, message: str = Form(...),password: str = Form(...), newFileName: str = Form(...)):
    try:
        [im, messageLength] = encode_image(file.file, message, password, newFileName)
        print("here")
        resMessage = decode_image(newFileName + ".png", messageLength, password)
        return {"Done": resMessage}
        # some code that may raise an error
    except Exception as e:
        print(e)
        print("TEST")
        raise HTTPException(status_code=500, detail=str(e))
    