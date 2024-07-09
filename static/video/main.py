from moviepy.editor import VideoFileClip

def compress_video(input_file, output_file, target_size_mb):
    # 目标大小转换为字节
    target_size = target_size_mb * 1024 * 1024
    # 加载视频
    clip = VideoFileClip(input_file)
    # 获取视频的初始大小
    initial_size = clip.size[0] * clip.size[1] * clip.fps * clip.duration / 8
    # 计算压缩比
    compression_ratio = target_size / initial_size
    # 设置新的视频比特率
    new_bitrate = clip.fps * clip.size[0] * clip.size[1] * compression_ratio / 1024
    # 输出压缩视频
    clip.write_videofile(output_file, bitrate=f"{new_bitrate}k")

input_file = r"C:\Users\26084\Desktop\gooloop\static\video\WeChat_20240708174346_compressed.mp4"
output_file = "WeChat_20240708174346_compressed.mp4"
target_size_mb = 5  # 目标大小为20MB

compress_video(input_file, output_file, target_size_mb)
