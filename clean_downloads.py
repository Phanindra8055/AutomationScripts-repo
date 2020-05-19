import os
import shutil

os.chdir("/path/to/your/downloads/folder")


img_formats = [
    ".jpg",
    ".jpeg",
    ".jpe",
    ".jif",
    ".jfif",
    ".jfi",
    ".png",
    ".gif",
    ".webp",
    ".tiff",
    ".tif",
    ".psd",
    ".raw",
    ".arw",
    ".cr2",
    ".nrw",
    ".k25",
    ".bmp",
    ".dib",
    ".heif",
    ".heic",
    ".ind",
    ".indd",
    ".indt",
    ".jp2",
    ".j2k",
    ".jpf",
    ".jpx",
    ".jpm",
    ".mj2",
    ".svg",
    ".svgz",
    ".ai",
    ".eps",
    ".ico",
]

video_formats = [
    ".webm",
    ".mpg",
    ".mp2",
    ".mpeg",
    ".mpe",
    ".mpv",
    ".mp4",
    ".m4p",
    ".m4v",
    ".avi",
    ".wmv",
    ".mov",
    ".qt",
    ".flv",
    ".swf",
]

doc_formats = [
    ".doc",
    ".docx",
    ".html",
    ".htm",
    ".odt",
    ".pdf",
    ".xls",
    ".xlsx",
    ".ods",
    ".ppt",
    ".pptx",
    ".txt",
    ".odp",
    ".rtf",
]

audio_formats = [
    ".mp3",
    ".m4a",
    ".aac",
    ".oga",
    ".ogg",
    ".pcm",
    ".wav",
    ".aiff",
    ".flac",
    ".ogg",
]


def is_image(file_name):
    """Returns True if the file is an image, else False"""
    file_ext = os.path.splitext(file_name)[1]

    if file_ext in img_formats:
        return True
    return False


def is_doc(file_name):
    """Returns True if the file is a document, else False"""
    file_ext = os.path.splitext(file_name)[1]

    if file_ext in doc_formats:
        return True
    return False


def is_video(file_name):
    """Returns True if the file is a video file, else False"""
    file_ext = os.path.splitext(file_name)[1]

    if file_ext in video_formats:
        return True
    return False


def is_audio(file_name):
    """Returns True if the file is an Audio file, else False"""
    file_ext = os.path.splitext(file_name)[1]

    if file_ext in audio_formats:
        return True
    return False


for f in os.listdir():
    if is_image(f):
        shutil.move(f"{f}", f"/path/to/your/images/folder/{f}")
    elif is_video(f):
        shutil.move(f"./{f}", f"/path/to/your/videos/folder/{f}")
    elif is_doc(f):
        shutil.move(f"./{f}", f"/path/to/your/documents/folder/{f}")
    elif is_audio(f):
        shutil.move(f"./{f}", f"/path/to/your/audios/folder/{f}")
