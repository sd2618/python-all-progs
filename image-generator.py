# from PIL import Image

# data = bytes.fromhex('f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc')
# width = len(data)//3
# # height =
# img = Image.frombuffer("RGB", (width, 1), data, "raw", "RGB", 0, 1)
# # img = Image.frombuffer("RGB", (width, 1), data, "raw", "RGB", 0, 1)
# img.show()


# from PIL import Image
# import os

# data = bytes.fromhex('f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc')
# width = len(data) // 3
# img = Image.frombuffer("RGB", (width, 1), data, "raw", "RGB", 0, 1)

# # Specify the path to save the image
# save_path = os.path("")
# img.save(save_path)

# print("Image saved successfully at:", save_path)


from PIL import Image
import os

# data = bytes.fromhex('f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc')
data = bytes.fromhex('f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc f4efe0 ecebe7 abb3ec edf2f6 f2f4f3 edf2f6 e8eae7 d4d7d8 fcfcfc c1c6ca f3f3f3 2c2722 c1c6ca 72b4b2 d4d7d8 9b9d9c bdc1c9 c4e3df ecebe7 683a27 f5b458 f4efe0 e2d8cc e2d8cc')
# width = len(data) // 3
# h=1
# if width>50:
#     q=width//50
#     if width%50!=0:
#         r=1
#     h=q+r
# img = Image.frombuffer("RGB", (width, 1), data, "raw", "RGB", 50, 1)

# # Get the current working directory
# current_dir = os.getcwd()

# # Specify the path to save the image in the current directory
# save_path = os.path.join(current_dir, "output_image.png")
# img.save(save_path)

# print("Image saved successfully at:", save_path)



# from PIL import Image
# import os

# data = bytes.fromhex('00FF80 800080 00FF80 FF00FF FF0000 800080 FF8000 FF8000 FF0080 800080 800000 8000FF FF8000 800080 FF0080 00FF80 00FF80 9b9d9c 9b9d9c 00FF80 800080 00FF80 FF00FF FF0000 800080 FF8000 FF8000 FF0080 800080 800000 8000FF FF8000 800080 FF0080 00FF80 00FF80 9b9d9c 9b9d9c 00FF80 800080 00FF80 FF00FF FF0000 800080 FF8000 FF8000 FF0080 800080 800000 8000FF FF8000 800080 FF0080 00FF80 00FF80 9b9d9c 9b9d9c 00FF80 800080 00FF80 FF00FF FF0000 800080 FF8000 FF8000 FF0080 800080 800000 8000FF FF8000 800080 FF0080 00FF80 00FF80 9b9d9c 9b9d9c')

width = 70
height = len(data) // (3 * width)
if len(data) % (3 * width) != 0:
    height += 1

expected_data_size = 3 * width * height
data += bytes([0] * (expected_data_size - len(data)))   #Pad the data if necessary

img = Image.frombuffer("RGB", (width, height), data, "raw", "RGB", 0, 1)

# Get the current working directory
current_dir = os.getcwd()

# Specify the path to save the image in the current directory
save_path = os.path.join(current_dir, "output_image.png")
img.save(save_path)

print("Image saved successfully at:", save_path)
