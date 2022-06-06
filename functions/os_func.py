import os
import subprocess, sys

def open_notepad():
    subprocess.call(['open', '/System/Applications/Notes.app'])


def open_spotify():
    subprocess.call(['open', '/Applications/Spotify.app'])


def open_terminal():
    subprocess.call(['open', '/System/Applications/Terminal.app'])


def open_camera():
    subprocess.call(['open', '/System/Applications/Photo Booth.app'])


def open_calculator():
    subprocess.call(['open', '/System/Applications/Calculator.app'])