from fastapi import FastAPI, UploadFile, File, HTTPException
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"


@app.post("/onboard/")
async def onboard(files: list[UploadFile] = File(...)):
    try:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        for file in files:
            file_name = os.path.join(UPLOAD_FOLDER, file.filename)
            with open(file_name, "wb") as buffer:
                buffer.write(await file.read())

        return {"message": "Files uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

