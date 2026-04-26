# Instagram Border Tool

A Python script that adds a white border to photos and outputs them in a **4:5 vertical aspect ratio**, perfect for Instagram portrait posts.

## Features

- Adds a customizable white border around any photo
- Forces output to **4:5 aspect ratio** regardless of input dimensions
- Works with landscape, portrait, and square photos
- Supports batch processing of entire folders
- Preserves image quality (95% JPEG quality)
- Supports `.jpg`, `.jpeg`, and `.png` files

## Requirements

- Python 3.x
- Pillow

Install the dependency with:

```bash
pip install Pillow
```

## Usage

### Single image

```python
add_border_4x5(
    image_path="my_photo.JPG",
    output_path="my_photo_bordered.JPG",
    border_size=50
)
```

### Batch processing

```python
batch_border_4x5(
    input_folder="photos",
    output_folder="photos_canvas",
    border_size=50
)
```

Place all your photos in the `input_folder` and the script will process each one and save the results in `output_folder` (created automatically if it doesn't exist).

## How it works

The algorithm follows these steps:

1. Opens the input image
2. Adds the minimum white border (`border_size` pixels) on all sides
3. Calculates whether the image is too wide or too tall to fit a 4:5 ratio
4. Expands the white canvas on the necessary side to reach exactly 4:5
5. Centers the original photo on the canvas
6. Saves the result

This means the photo itself is never cropped or stretched — only the white border size adjusts to hit the target ratio.


## Tips

- A `border_size` of `100` works well for standard posts
- Use `200–500` for a thicker, more prominent border
- Instagram's recommended resolution for 4:5 posts is **1080 × 1350 px** — if your photos are at least 1080px wide, the output will look sharp
- Run the batch version on a copy of your photos folder the first time to be safe

## License

MIT — free to use and modify.