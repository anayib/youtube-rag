import os
import tempfile
import whisper
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=VSmobknYl0E"



if not os.path.exists("transcription.txt"):
    try:
        # Create a temporary directory for the download
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(tmpdir, '%(id)s.%(ext)s'),  # Save directly to tmpdir
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'keepvideo': True,  # Keep the original video file (optional)
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(YOUTUBE_VIDEO, download=True)
                file = ydl.prepare_filename(info)  # This will now point to the tmpdir

            # The extracted file will be in mp3 format
            mp3_file = os.path.splitext(file)[0] + '.mp3'

            # Check if the mp3 file exists before transcribing
            if os.path.exists(mp3_file):
                whisper_model = whisper.load_model("base")
                transcription = whisper_model.transcribe(mp3_file, fp16=False)["text"].strip()

                with open("transcription.txt", "w") as output_file:
                    output_file.write(transcription)
            else:
                print(f"Downloaded mp3 file does not exist: {mp3_file}")

    except DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")