import argparse
import glob
import os
from PIL import Image

def add_suffix_os_path(filename, suffix):
    """
    Add suffix using os.path module
    
    Args:
        filename (str): Original filename
        suffix (str): Suffix to add
    
    Returns:
        str: New filename with suffix
    """
    # Split filename and extension
    name, ext = os.path.splitext(filename)
    
    # Add suffix and rejoin
    new_filename = f"{name}{suffix}{ext}"
    return new_filename

def resize_image_by_width(input_path, output_path, new_width):
    """
    Resize PNG image by width while maintaining aspect ratio
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save resized image
        new_width (int): New width in pixels
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            
            # Calculate new height maintaining aspect ratio
            aspect_ratio = original_height / original_width
            new_height = int(new_width * aspect_ratio)
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save the resized image
            resized_img.save(output_path)
            
            print(f"Image resized from {original_width}x{original_height} to {new_width}x{new_height}")
            print(f"Saved to: {output_path}")
            
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found")
    except Exception as e:
        print(f"Error resizing image: {e}")


def createthumbs(args):
    extension = args.filesextension
    if not extension.startswith('.'):
        extension = '.' + extension

    # Create search pattern
    pattern = os.path.join(args.path, f'*{extension}')
    
    # Get all matching files
    files = glob.glob(pattern)

    for file in files:
        print(file)
        newfile = add_suffix_os_path(file, f"_{args.suffix}")
        resize_image_by_width(file, newfile, args.width)
        print(newfile)

        #os.rename(file,f"{directory}/{filename}")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='The scripts create thimbnails files')
    
    # Add arguments
    parser.add_argument('path', help='Path to the directory where the files are. (required)')
    parser.add_argument('--filesextension', '-x', default="png", help='File extention of the files (optional)')
    parser.add_argument('--suffix', '-s', default='thumb', help='Add a prefix in the files (optional)')
    parser.add_argument('--width', '-w', default=150, help='Width of the thumbnail (optional)')
    
    # Parse arguments
    args = parser.parse_args()

    createthumbs(args)



if __name__ == '__main__':
    main()