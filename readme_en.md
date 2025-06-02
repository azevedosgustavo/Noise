
Binaural Audio Generator with Pink Noise (Python)
=================================================

This project generates a stereo audio file with a 40 Hz binaural beat (440 Hz in the left ear and 480 Hz in the right ear),
mixed with pink noise in the background, with a total duration of 10 minutes.

Great for concentration, focus, and brainwave entrainment applications.

Requirements
------------

- Python 3.10 or higher
- Pip
- FFmpeg installed and configured
- Python packages: pydub, numpy, scipy

Installation
------------

1. Install Python dependencies:

    pip install pydub numpy scipy

2. Download and configure FFmpeg:

   - Download FFmpeg from this link:
     https://objects.githubusercontent.com/github-production-release-asset-2e65be/292087234/049b6494-41db-4b3c-b705-d0917d549bcc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250602%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250602T190658Z&X-Amz-Expires=300&X-Amz-Signature=68a663be42f93dd5db9615a99b180834ac35f0486947d6facf4f783b0e6ee054&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dffmpeg-master-latest-win64-gpl-shared.zip

   - Extract the ZIP file to a folder like: C:\ffmpeg\

   - Make sure this file exists: C:\ffmpeg\bin\ffmpeg.exe

   - Add the path to your system's environment variables:
     1. Control Panel → System → Advanced System Settings
     2. Environment Variables → find "Path" → Edit
     3. Click "New" and add: C:\ffmpeg\bin
     4. Restart your terminal (CMD, PowerShell, or VSCode)

   - Test with: ffmpeg -version

Usage
-----

- Save the Python script in the same folder as this README
- Run it with:

    python binaural_40hz_pink_noise.py

- The output file will be saved at: C:\tmp\binaural_40hz_10min_pink_noise.wav

Common Issues
-------------

- Error: "Couldn't find ffmpeg or avconv"
  Solution: add this line at the top of your script:

    from pydub import AudioSegment
    AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"

License
-------

Free to use for personal, academic, and therapeutic purposes.
