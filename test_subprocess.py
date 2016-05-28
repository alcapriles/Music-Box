import subprocess

def abrir_partitura():
    lilypond = r"C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe"
    subprocess.run([lilypond, "--png", "teste.ly"])