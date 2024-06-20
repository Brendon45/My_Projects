#!/usr/bin/env python3

# Import the pytube library for YouTube video manipulation
import pytube
import os

def download_youtube_video():
    """
    Download a YouTube video with the highest resolution available.
    
    Prompts the user to input the video URL and downloads the video to the specified directory.
    """
    # Prompt the user to input the video URL
    video_url = input("Enter the YouTube video URL: ")
    
    try:
        # Create a YouTube object with the provided video URL
        yt = pytube.YouTube(video_url)
        
        # Get the stream with the highest resolution
        stream = yt.streams.get_highest_resolution()
        
        # Specify the download location (current working directory)
        download_location = os.getcwd()
        
        # Inform the user that the video is being downloaded
        print("Video is being downloaded...")
        
        # Download the video using the selected stream
        stream.download(download_location)
        
        # Inform the user that the download is complete
        print(f"Video downloaded successfully! Saved to: {download_location}")
    except pytube.exceptions.RegexMatchError:
        print("Invalid URL. Please enter a valid YouTube video URL.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
