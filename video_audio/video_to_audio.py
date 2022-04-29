import moviepy.editor

edd = moviepy.editor.VideoFileClip()
video = edd("video.mp4")
audio_data = video.audio
audio_data.write_audiofile("audio_do_video.mp3")