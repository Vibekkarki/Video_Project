# Image to Video Generator

## Objective

This Python script generates a short video from an image using FFmpeg and Pillow. It overlays text onto the image, applies a grayscale transformation, and then converts it into a short video clip with background music.

## Features

- Loads an image using Pillow.
- Overlays custom text on the image.
- Applies a grayscale transformation.
- Generates a short video (at least 5 seconds) from the transformed image.
- Overlays background music onto the video.
- Allows user configuration for text and background music.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- Pillow
- FFmpeg

## Installation


1. Install dependencies:

```
pip install pillow
```

2. Install FFmpeg:
   - Windows: Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.
   - Linux/macOS:
   ```
   sudo apt install ffmpeg  # Debian-based
   brew install ffmpeg      # macOS
   ```

## Usage

1. Place an image (`input_image.jpg`) and a music file (`background_music.mp3`) in the project folder.
2. Run the script:

```
python generate_video.py
```

3. The processed image (`processed_image.jpg`) and generated video (`output_video.mp4`) will be saved in the same directory.

## Configuration

You can modify the following parameters inside "generate_video.py"

```python
input_image = "input_image.jpg"  # Path to input image
output_image = "processed_image.jpg"  # Output processed image
output_video = "output_video.mp4"  # Output video file
background_music = "background_music.mp3"  # Background music file
overlay_text = "Hello, World!!!"  # Text to overlay on image
video_duration = 5  # Duration of video in seconds
```

## Notes

- Ensure FFmpeg is installed and accessible from the command line.
- If `arial.ttf` is not found, the script will use a default font.
- You can replace `input_image.jpg` and `background_music.mp3` with your own files.





