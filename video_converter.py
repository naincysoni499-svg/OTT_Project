import subprocess

input_video = "Uploads/sample.mp4"

subprocess.run([
    "ffmpeg",
    "-i", input_video,
    "-vf", "scale=-2:720",
    "video_720p.mp4"
])

subprocess.run([
    "ffmpeg",
    "-i", input_video,
    "-vf", "scale=-2:480",
    "video_480p.mp4"
])

print("Video conversion completed!")