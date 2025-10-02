import os
from PIL import Image

# --- Configuration ---
# The folder where your original images are located
INPUT_FOLDER = "images_to_resize"
# The folder where the resized images will be saved
OUTPUT_FOLDER = "resized_images"
# The desired maximum width for the resized images (in pixels)
# The height will be calculated automatically to maintain the aspect ratio.
TARGET_WIDTH = 800
# The quality for the output JPEG files (0-100)
JPEG_QUALITY = 90
# A list of file extensions the script should look for
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
# ---------------------

def resize_and_convert_image(input_path, output_path, target_width, quality):
    """
    Opens an image, calculates the new height to maintain aspect ratio,
    resizes the image, and saves it as a JPEG.
    """
    try:
        # Open the image file
        img = Image.open(input_path)

        # Calculate the new height to maintain the aspect ratio
        original_width, original_height = img.size
        if original_width > target_width:
            # Only resize if the image is actually larger than the target width
            ratio = target_width / original_width
            new_height = int(original_height * ratio)
            
            # Resize the image using the calculated dimensions
            img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the image in JPEG format with specified quality
        # Use .lower() to ensure the extension is always lowercase
        img.save(output_path, "jpeg", quality=quality)
        print(f"  SUCCESS: Resized and saved {os.path.basename(input_path)}")

    except FileNotFoundError:
        print(f"  ERROR: File not found at {input_path}")
    except Exception as e:
        print(f"  ERROR: Failed to process {os.path.basename(input_path)}. Reason: {e}")


def batch_resize_images():
    """
    Main function to orchestrate the batch processing.
    """
    print("--- Starting Batch Image Resizer ---")

    # 1. Use os to ensure the output folder exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created output folder: '{OUTPUT_FOLDER}'")
    
    # Check if input folder exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"\nERROR: Input folder '{INPUT_FOLDER}' not found.")
        print("Please create this folder and place your images inside it.")
        return

    # Counter for processed images
    processed_count = 0

    # 2. Use os.listdir to read the image folder
    for filename in os.listdir(INPUT_FOLDER):
        # Construct the full path for the input file
        input_path = os.path.join(INPUT_FOLDER, filename)
        
        # Check if the path is a file and has a supported extension
        file_extension = os.path.splitext(filename)[1].lower()

        if os.path.isfile(input_path) and file_extension in SUPPORTED_EXTENSIONS:
            processed_count += 1
            
            # Create a new filename for the output (e.g., 'original_name.jpg')
            # The extension is always '.jpg' because we are converting to JPEG
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(OUTPUT_FOLDER, new_filename)
            
            # Process the image
            resize_and_convert_image(
                input_path, 
                output_path, 
                TARGET_WIDTH, 
                JPEG_QUALITY
            )
    
    print(f"\n--- Batch Resizing Complete ---")
    print(f"Total images processed: {processed_count}")
    print(f"Output saved to: '{OUTPUT_FOLDER}'")


if __name__ == "__main__":
    batch_resize_images()