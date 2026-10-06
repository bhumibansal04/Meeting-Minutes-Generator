import whisper
from meeting_ai import analyze_meeting

whisper_model = whisper.load_model("base")

# ---------------- AUDIO ----------------
def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path, fp16=False)
    return result["text"]

# ---------------- AI PROCESS ----------------
def generate_minutes(text):
    return analyze_meeting(text)