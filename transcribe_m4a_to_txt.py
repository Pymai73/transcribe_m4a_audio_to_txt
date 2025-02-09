import tkinter as tk
from tkinter import filedialog
import whisper
import os

def select_file():
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.m4a")])
    return file_path

def transcribe_audio(file_path):
    model = whisper.load_model("small")  # Carica il modello Whisper
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(text, file_path):
    txt_file = os.path.splitext(file_path)[0] + ".txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Trascrizione salvata in: {txt_file}")

def main():
    file_path = select_file()
    if file_path:
        print("Trascrizione in corso...")
        transcription = transcribe_audio(file_path)
        save_transcription(transcription, file_path)
    else:
        print("Nessun file selezionato.")

if __name__ == "__main__":
    main()
