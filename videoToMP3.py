#----------------------------------------------------------------------------------------------------------
#import necessary packages 
#----------------------------------------------------------------------------------------------------------
import yt_dlp as youtube_dl

#----------------------------------------------------------------------------------------------------------
# Create a function to download songs
#----------------------------------------------------------------------------------------------------------

def download_songs(url):
    # Create a YoutubeDL object with options
    ydl_opts = {
                'format': 'bestaudio/best',  # This selects the best audio-only format available
                'outtmpl': 'C:/Songs/%(title)s.%(ext)s',  # Save each song with its title and .ext extension
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    

#----------------------------------------------------------------------------------------------------------
# Call the function
#----------------------------------------------------------------------------------------------------------

try:
    url = "https://www.youtube.com/watch?v=87JIOAX3njM"
    download_songs(url)
    print("Song downloaded successfully! ")

except Exception as e:
    print(e)


