from PIL import Image
import numpy as np
import openpyxl
import uuid


def transform_image_to_xlsx(image_path: str, default_cols: int = 50, is_scale=False) -> None:
    """
    Transforms an image into an xlsx file where each cell corresponds to a pixel of the image.
    Each cell is filled with a color corresponding to the RGB value of the corresponding pixel.

    Args:
        image_path (str): The path to the image file.
        default_cols (int, optional): The number of columns to use if `is_scale` is True. Defaults to 50.
        is_scale (bool, optional): Whether to scale the image to fit `default_cols` columns. Defaults to False.

    Returns:
        None: Saves the xlsx file with a unique filename.
    """
    # Open image
    with Image.open(image_path) as image:
        if is_scale:
            # Scale image if requested
            width, height = image.size
            image_scale = default_cols / width
            scaled_size = (int(width * image_scale), int(height * image_scale))
            image = image.resize(scaled_size, resample=Image.Resampling.LANCZOS)

        # Convert image to RGB array
        rgb_array = np.array(image.convert("RGB"))
        width, height, _ = rgb_array.shape

        # Create xlsx workbook and worksheet
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Create list of fill colors for each pixel
        fill_colors = [f"{r:02X}{g:02X}{b:02X}" for r, g, b in rgb_array.reshape(-1, 3)]

        # Fill worksheet cells with appropriate color
        for x in range(0, width):
            for y in range(0, height):
                fill_color = fill_colors[x * height + y]
                cell = worksheet.cell(row=x + 1, column=y + 1)
                cell.fill = openpyxl.styles.PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")

        # Save workbook with unique filename
        filename = f"{uuid.uuid4().hex[:12]}.xlsx"
        workbook.save(filename)
