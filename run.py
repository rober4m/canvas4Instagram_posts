from PIL import Image
import os

def add_border_to_folder(input_folder, output_folder, border_size):
    os.makedirs(output_folder, exist_ok=True)
    
    extensions = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")
    
    for filename in os.listdir(input_folder):
        if filename.endswith(extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            img = Image.open(input_path)

            # Add minimum border around the original image
            inner_width = img.width + (border_size * 2)
            inner_height = img.height + (border_size * 2)

            # Force output to 4:5 vertical aspect ratio
            target_ratio = 4 / 5  # width / height

            current_ratio = inner_width / inner_height

            if current_ratio > target_ratio:
                # Image is too wide → expand height to fit 4:5
                canvas_width = inner_width
                canvas_height = int(canvas_width / target_ratio)
            else:
                # Image is too tall (or already correct) → expand width to fit 4:5
                canvas_height = inner_height
                canvas_width = int(canvas_height * target_ratio)

            # Create white canvas at exact 4:5 ratio
            new_img = Image.new("RGB", (canvas_width, canvas_height), "white")

            # Center the original image on the canvas
            x_offset = (canvas_width - img.width) // 2
            y_offset = (canvas_height - img.height) // 2

            new_img.paste(img, (x_offset, y_offset))
            new_img.save(output_path, quality=95)
            print(f"Processed: {filename} → {canvas_width}x{canvas_height} ({canvas_width/canvas_height:.2f} ratio)")

# --- Usage ---
add_border_to_folder(
    input_folder="photos/",        # folder with your original photos
    output_folder="photos_canvas/",  # where to save results
    border_size=300
)