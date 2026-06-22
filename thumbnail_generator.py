import subprocess

video_file = "Uploads/sample.mp4"
thumbnail_file = "thumbnail.jpg"
print(video_file)
subprocess.run([
    "ffmpeg",
    "-i", video_file,
    "-ss", "00:00:05",
    "-vframes", "1",
    thumbnail_file
])

print("Thumbnail generated!")