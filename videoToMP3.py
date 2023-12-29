import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4", abr="128kbps").first()
        downloaded_file = audio_stream.download(output_path)
        return downloaded_file, yt.title
    except (RegexMatchError, VideoUnavailable, PytubeError) as e:
        raise e
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")

correct_and_rename = lambda downloaded_file, title: (
    os.rename(downloaded_file, os.path.join(output_path, f'{clean_title(title)}.mp3'))
)

def handle_error(error):
    if isinstance(error, RegexMatchError):
        print("Error: Invalid URL format. Please enter a valid YouTube video URL.")
    elif isinstance(error, VideoUnavailable):
        print("Error: The video is unavailable or restricted. Please choose another video.")
    elif isinstance(error, PytubeError):
        print(f"Error: {error}")
    else:
        print(f"Unexpected error: {error}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print("+" + "-"*38 + "+")
    print("|              CUI MENU               |")
    print("+" + "-"*38 + "+")
    print("| Options:                            |")
    print("| 1. Fetch audio from a URL           |")
    print("| 2. Read URLs from a file            |")
    print("| 3. Exit                             |")
    print("+" + "-"*38 + "+")

def fetch_audio(url, output_path):
    try:
        downloaded_file, title = download_audio(url, output_path)
        correct_and_rename(downloaded_file, title)
        print(f"Audio downloaded and renamed successfully: {title}")
    except Exception as e:
        handle_error(e)

def read_from_file(file_path, output_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:
                    fetch_audio(url, output_path)
                    input("Press Enter to continue...")
                else:
                    print("File is empty!!")
    except Exception as e:
        handle_error(e)

def main():
    while True:
        print_menu()
        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == '1':
            url = input("Enter the YouTube video URL: ")
            output_path = 'C:/Songs/'  # Adjust the output path as needed
            fetch_audio(url, output_path)
            input("Press Enter to continue...")

        elif user_choice == '2':
            file_path = input("Enter the file path containing YouTube video URLs: ")
            output_path = 'C:/Songs/'  # Adjust the output path as needed
            read_from_file(file_path, output_path)
            input("Press Enter to continue...")

        elif user_choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
