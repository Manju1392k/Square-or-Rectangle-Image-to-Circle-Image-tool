from PIL import Image, ImageOps, ImageDraw

def Square_Rectangle_Image_to_Cricle(Image_input_path, Image_output_image_savingPath, border_ratio=0.2):

    Img = Image.open(Image_input_path)

    # Croping the image into a square aspect ratio for better results.
    width, height = Img.size
    max_dim = max(width, height)
    left = (width - max_dim)/2
    top = (height - max_dim)/2
    right = (width + max_dim)/2
    bottom = (height + max_dim)/2
    Img = Img.crop((left, top, right, bottom))

    # Seting the new_size to the size of the cropped image
    new_size = Img.size

    Img = Img.resize(new_size)

    mask = Image.new('L', Img.size, 0)

    draw = ImageDraw.Draw(mask)

    # Calculating the border size of the image in pixels.
    Border_size = int(border_ratio * min(Img.size))

    # Drawing a smaller ellipse in the mask. And adjusting border size.
    draw.ellipse((Border_size, Border_size, Img.size[0] - Border_size, Img.size[1] - Border_size), fill=255)

    # Centering the image to set the content of image in center. 
    # Adjust center of the image based on the size of the image
    centering = (new_size[0] / 2, new_size[1] / 2)
    result = ImageOps.fit(Img, mask.size, centering=centering)
    result.putalpha(mask)

    result.save(Image_output_image_savingPath)

# Giving Image path.
Image_input_path = 'RectangleCarImage.png'

# Giving path to saving the output image file. And also giving Image name with format.
Image_output_image_savingPath = 'Output_RectangleCarImage.png'

Square_Rectangle_Image_to_Cricle(Image_input_path, Image_output_image_savingPath)
print("Your Image successfully converted into Circle size Image.")
