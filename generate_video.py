import os
from PIL import Image, ImageDraw, ImageFont
import subprocess

def process_image(image_path, output_image_path, text):
    # Load the image
    image = Image.open(image_path)

    # Convert to grayscale
    image = image.convert("L")

    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)

    # Load a font (adjust path as needed)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Add text to the image
    text_position = (50, 50)  # (x, y) coordinates
    draw.text(text_position, text, font=font, fill="black")

    # Save the processed image
    image.save(output_image_path)

def generate_video(image_path, output_video_path, music_path, duration=5):
    """
    Generate a video from an image using FFmpeg and overlay background music.
    """
    # FFmpeg command to create a video from the image
    ffmpeg_command = [
        "ffmpeg",
        "-loop", "1",  # Loop the image
        "-i", image_path,  # Input image
        "-i", music_path,  # Background music
        "-c:v", "libx264",  # Video codec
        "-t", str(duration),  # Duration of the video
        "-c:a", "aac",  # Audio codec
        "-strict", "experimental",
        "-shortest",  # Ensure the video ends when the audio ends
        "-vf", "scale=1280:720",  # Resize to 1280x720 (optional)
        output_video_path  # Output video file
    ]

    # Run the FFmpeg command
    subprocess.run(ffmpeg_command, check=True)

def main():
    # Configuration
    input_image = "input_image.jpg"  # Path to the input image
    output_image = "processed_image.jpg"  # Path to save the processed image
    output_video = "output_video.mp4"  # Path to save the output video
    background_music = "background_music.mp3"  # Path to the background music file
    overlay_text = "Hello, World!!!"  # Text to overlay on the image
    video_duration = 5  # Duration of the video in seconds

    # Process the image
    process_image(input_image, output_image, overlay_text)

    # Generate the video
    generate_video(output_image, output_video, background_music, video_duration)

    print(f"Video generated successfully: {output_video}")

if __name__ == "__main__":
    main()