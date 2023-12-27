#----------------------------------------------------------------------------------------------------------
#import necessary packages
#----------------------------------------------------------------------------------------------------------
import os
from pytube import YouTube

#----------------------------------------------------------------------------------------------------------
# Create a function to download songs
#----------------------------------------------------------------------------------------------------------

def clean_title(title):
    cleaned_title = ''.join(e for e in title if e.isalnum() or e.isspace())
    return cleaned_title.strip()
    
def download_and_rename_audio(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the audio stream with specified parameters
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4", abr="128kbps").first()

        # Download the audio
        downloaded_file = audio_stream.download(output_path)

        # Get the cleaned title
        cleaned_title = clean_title(yt.title)

        # Construct the new path with the cleaned title and original extension
        new_file_path = os.path.join(output_path, f'{cleaned_title}.mp3')

        # Rename the file with the cleaned title
        os.rename(downloaded_file, new_file_path)

        print(f"Audio downloaded, renamed, and information saved successfully: {cleaned_title}")

    except Exception as e:
        print(f"Error: {e}")
#----------------------------------------------------------------------------------------------------------
# Call the function
#----------------------------------------------------------------------------------------------------------

try:
    file_path = 'Songs_List.txt'
    output_path = 'C:/Songs/'
    with open(os.path.join(output_path, file_path), 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()  # Remove any leading/trailing whitespace or newline characters
            if url:  # Check if the URL is not empty
                download_and_rename_audio(url, output_path)
            else:
                print("File is empty!!")

except Exception as e:
    print(f"Error reading URLs from file: {e}")


