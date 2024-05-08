import sys
from PIL import Image #pip install Pillow

def resize_image(image_path, scale_percent):
    # Open an image file
    with Image.open(image_path) as img:
        # Calculate the new size
        width, height = img.size
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Save the resized image
        resized_img.save(f"{image_path.split('.')[0]}_{int(scale_percent)}.{image_path.split('.')[-1]}")

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scale.py <image_path> <scale_percent>")
        sys.exit(1)
    
    arg1, arg2 = sys.argv[1], sys.argv[2]
    
    if is_number(arg1) and not is_number(arg2):
        # Assume arg1 is scale_percent and arg2 is image_path
        scale_percent = int(arg1)
        image_path = arg2
    elif not is_number(arg1) and is_number(arg2):
        # Assume arg1 is image_path and arg2 is scale_percent
        image_path = arg1
        scale_percent = int(arg2)
    else:
        print("Invalid arguments. Please provide an image path and a scale percentage.")
        sys.exit(1)
    
    resize_image(image_path, scale_percent)
