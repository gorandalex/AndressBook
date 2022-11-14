from dataclasses import replace
from pathlib import Path
import sys
import os

def sorting(dir=None):
    if dir is None:
        dir = sys.argv[1]
    images_path = dir + "images"
    videos_path = dir + "videos"
    docs_path = dir + "docs"
    musics_path = dir + "musics"
    zips_path = dir + "zips"
    not_recognize_path = dir + "not_recognize"

    if not os.path.exists(images_path):
        os.makedirs(images_path)
    if not os.path.exists(videos_path):
        os.makedirs(videos_path)
    if not os.path.exists(docs_path):
        os.makedirs(docs_path)
    if not os.path.exists(musics_path):
        os.makedirs(musics_path)
    if not os.path.exists(zips_path):
        os.makedirs(zips_path)
    if not os.path.exists(not_recognize_path):
        os.makedirs(not_recognize_path)
    
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if file_path.endswith( '.jpg') or file_path.endswith( '.png') or file_path.endswith( '.png') or file_path.endswith( '.svg') or file_path.endswith( '.jfif') or file_path.endswith( '.gif'):
            new_file = os.path.join(images_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.avi') or file_path.endswith( '.mp4') or file_path.endswith( '.mov') or file_path.endswith( '.mkv'):
            new_file = os.path.join(videos_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.doc') or file_path.endswith( '.docx') or file_path.endswith( '.txt') or file_path.endswith( '.pdf') or file_path.endswith( '.xlxs') or file_path.endswith( '.pptx'):
            new_file = os.path.join(docs_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.mp3') or file_path.endswith( '.ogg') or file_path.endswith( '.wav') or file_path.endswith( '.amr'):
            new_file = os.path.join(musics_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.zip') or file_path.endswith( '.gz') or file_path.endswith( '.tar'):
            new_file = os.path.join(zips_path, file)
            os.replace(file_path, new_file)
        elif os.path.isfile(dir + file):
            new_file = os.path.join(not_recognize_path, file)
            os.replace(file_path, new_file)