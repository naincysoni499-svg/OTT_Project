import subprocess

video_file = "Uploads/sample.mp4"
thumbnail_file = "thumbnail.jpg"

print("Step 1: Starting thumbnail generation...")

try:
    subprocess.run([
        "ffmpeg",
        "-i", video_file,
        "-ss", "00:00:05",
        "-frames:v", "1",
        thumbnail_file
    ], check=True)

    print("Step 2: FFmpeg executed successfully")
    print("Step 3: Thumbnail created at:", thumbnail_file)

except subprocess.CalledProcessError:
    print("Error: Thumbnail generation failed")