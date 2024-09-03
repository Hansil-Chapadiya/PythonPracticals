from PIL import Image

def black_and_white(input_image_path,output_image_path):
    color_image = Image.open(input_image_path)
    bw = color_image.convert('L')
    bw.save(output_image_path)

if __name__ == '__main__':
    black_and_white('C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\DESKTOP PICTURE\\10.jpg',
    'C:\\Users\\Admin\\OneDrive\\Pictures\\Saved Pictures\\DESKTOP PICTURE\\20.jpg')