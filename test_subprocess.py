import subprocess
import os

def abrir_partitura():
    lilypond = r"C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe"
    subprocess.run([lilypond, "--png", "teste.ly"])
    
    while True:
        if os.path.isfile('teste.png'):
            return os.path.abspath('teste.png')