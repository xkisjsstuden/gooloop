import os
from PIL import Image

def convert_to_webp(image_path):
    try:
        with Image.open(image_path) as img:
            filename, _ = os.path.splitext(image_path)
            new_path = f"{filename}.webp"
            img.save(new_path, 'WEBP', quality=90)  # 使用较高的质量设置
        print(f"转换成功: {new_path}")
    except Exception as e:
        print(f"转换失败 {image_path}: {str(e)}")

def batch_convert_to_webp(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(directory, filename)
            convert_to_webp(file_path)

if __name__ == "__main__":
    image_directory = r"C:\Users\26084\Desktop\gooloop\static\img" 
    batch_convert_to_webp(image_directory)
    print("WebP 转换完成。")