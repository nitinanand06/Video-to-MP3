# YouTube to MP3 Downloader

## Overview

This Python script uses the `yt_dlp` library to download audio from a YouTube video in MP3 format. The script defines a function `download_songs` that takes a YouTube video URL as input and downloads the corresponding audio to the specified output directory.

## Prerequisites

- Python 3.x
- `yt_dlp` library (install using `pip install yt_dlp`)

## Usage

1. Clone the repository or download the `youtube_to_mp3.py` file.
2. Install the required library: `pip install yt_dlp`
3. Open the `youtube_to_mp3.py` file and modify the `url` variable with your desired YouTube video URL.
4. Run the script using `python youtube_to_mp3.py`.

## Code Structure

- `youtube_to_mp3.py`: Contains the main script for downloading MP3 from a YouTube video.
- `C:/Songs/`: The default output directory where the downloaded songs will be saved.

## Functionality

The script defines a function `download_songs(url)` that downloads the audio from the specified YouTube video URL. The downloaded MP3 file is saved in the 'C:/Songs/' directory with the title of the video.

## Example

```python
try:
    url = "https://www.youtube.com/watch?v=87JIOAX3njM"
    download_songs(url)
    print("Song downloaded successfully!")
except Exception as e:
    print(e)
