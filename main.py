import os,sys,subprocess
import ffmpeg
import time
import eel
import multiprocessing
from PIL import Image

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def convert_video(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file).run()
        return True
    except ffmpeg.Error as e:
        return False

def convert_image(input_file, output_file):
    try:
        img = Image.open(input_file)
        img.save(output_file)
        return True
    except Exception as e:
        return False

def main():
    eel.start('index.html')

if __name__ == '__main__':
    eel.init('web')
    if check_ffmpeg():
        main()
    else:
        eel.start('ffmpeg.html')

        