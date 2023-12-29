import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError

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

        print(f"Audio downloaded, and renamed successfully: {cleaned_title}")

    except RegexMatchError:
        print("Error: Invalid URL format. Please enter a valid YouTube video URL.")
    except VideoUnavailable:
        print("Error: The video is unavailable or restricted. Please choose another video.")
    except PytubeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

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

def main():
    while True:
        print_menu()
        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == '1':
            url = input("Enter the YouTube video URL: ")
            output_path = 'C:/Songs/'  # Adjust the output path as needed
            download_and_rename_audio(url, output_path)
            input("Press Enter to continue...")

        elif user_choice == '2':
            file_path = input("Enter the file path containing YouTube video URLs: ")
            output_path = 'C:/Songs/'  # Adjust the output path as needed

            try:
                with open(file_path, 'r') as file:
                    urls = file.readlines()
                    for url in urls:
                        url = url.strip()  # Remove any leading/trailing whitespace or newline characters
                        if url:  # Check if the URL is not empty
                            download_and_rename_audio(url, output_path)
                            input("Press Enter to continue...")
                        else:
                            print("File is empty!!")
            except Exception as e:
                print(f"Error reading URLs from file: {e}")
                input("Press Enter to continue...")

        elif user_choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
