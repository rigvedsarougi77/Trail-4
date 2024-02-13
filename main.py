from fastapi import FastAPI, File, UploadFile
from ur_audio_sub import subGen_path, read_txt

app = FastAPI()

def generate_subtitle(mp3_file_path):
    # Generate subtitle
    subGen_path(mp3_file_path)

    # Read subtitle content
    subtitle_file_path = mp3_file_path.replace('.mp3', '.txt')
    subtitle_content = read_txt(subtitle_file_path)

    return subtitle_content

@app.post("/generate_subtitle/")
async def generate_subtitle_endpoint(mp3_file: UploadFile = File(...)):
    with open(mp3_file.filename, "wb") as buffer:
        buffer.write(mp3_file.file.read())

    subtitle_content = generate_subtitle(mp3_file.filename)
    return {"subtitle_content": subtitle_content}
