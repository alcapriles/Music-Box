# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:42:32 2016

@author: Victor
"""

import subprocess

lilypond = r"C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe"

subprocess.run([lilypond, "--png", "teste.ly"])