from PIL import Image
import os
import cv2

# def embed_image(background_image, foreground_image, x, y):
#     # Open the background and foreground images
#     background = Image.open(background_image)
#     foreground = Image.open(foreground_image)

#     # Resize the foreground image to fit within the background image
#     foreground = foreground.resize((background.width, background.height))

#     # Create a new image with transparent background
#     composite = Image.new("RGBA", background.size)

#     # Paste the background and foreground images onto the composite image
#     composite.paste(background, (0, 0))
#     composite.paste(foreground, (x, y), mask=foreground)

#     # Save the resulting image
#     composite.save("output_image_changed.png")

#     print("Image successfully embedded!")

def place_image_over(background_image, foreground_image, x, y):
    # Read the background and foreground images
    background = cv2.imread(background_image)
    foreground = cv2.imread(foreground_image)

    # Ensure the foreground image fits within the background image
    foreground_height, foreground_width = foreground.shape[:2]
    if x + foreground_width > background.shape[1] or y + foreground_height > background.shape[0]:
        raise ValueError("Foreground image exceeds the dimensions of the background image.")

    # Place the foreground image over the background image at the specified pixel
    background[y:y+foreground_height, x:x+foreground_width] = foreground

    # Save the resulting image
    cv2.imwrite("output_image.png", background)

    print("Image successfully edited!")












p={"a" :  "e8eae7","b" :  "dd947a","c" :  "eff0f2","d" :  "be9682","e" :  "f2f4f3","f" :  "e9e9e9","g" :  "f3f3f3","h" :  "ecebe7","i" :  "e9e9e7","j" :  "e4d2c4","k" :  "e4e3e1","l" :  "c9492b","m" :  "c9492b","n" :  "72b4b2","o" :  "f5b458","p" :  "6a8ab2","q" :  "bd667e","r" :  "37555b","s" :  "dee7e4","t" :  "e4db98","u" :  "e0dfdd","v" :  "dcdbd9","w" :  "f8f3e8","x" :  "aea096","y" :  "aea096","z" :  "4c5c2d","A" :  "f4efe0","B" :  "f5d7e0","C" :  "e0e0e0","D" :  "abb3ec","E" :  "c4e3df","F" :  "d4d7d8","G" :  "e280a2","H" :  "62dada","I" :  "ff888b","J" :  "fbf3e4","K" :  "bdc1c9","L" :  "93bae1","N" :  "a3e5e2","O" :  "f9d8a5","P" :  "fafafa","Q" :  "fcfcfc","R" :  "cdd1d4","S" :  "49413f","T" :  "a17e6f","U" :  "9b9d9c","V" :  "c3c2bd","W" :  "f5f6f8","X" :  "683a27","Y" :  "485e3e","Z" :  "485e3e","0" :  "c1c6ca","1" :  "cdcdcd","2" :  "edf2f6","3" :  "d0d0ce","4" :  "cdb3b6","5" :  "2c2722","6" :  "669a7a","7" :  "d3d9df","8" :  "e6e7ec","9" :  "d3c1b3","+" :  "ebe1d6","/" :  "e7e8ea","=" :  "e2d8cc" ,"*": "008000"}

k=input("set of characters")
s=""
for i in k:
    for j in p:
        if i==j:
            s=s+p[i]+" "

print(s)
print("\n\n")
print(s.split())

data = bytes.fromhex(s)

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

# background_image = input("Enter the path to the background image: ")

# x = int(input("Enter the x-coordinate for the foreground image: "))
# y = int(input("Enter the y-coordinate for the foreground image: "))

# # Call the function to embed the image
# embed_image(background_image, "output_image.png", x, y)

# background_image = input("Enter the path to the background image: ")

# x = int(input("Enter the x-coordinate for the foreground image: "))
# y = int(input("Enter the y-coordinate for the foreground image: "))

# # Call the function to embed the image
# embed_image(background_image, "output_image.png", x, y)

# Prompt the user for inputs
background_image = input("Enter the path to the background image: ")
foreground_image = input("Enter the path to the foreground image: ")
x = int(input("Enter the x-coordinate for the foreground image: "))
y = int(input("Enter the y-coordinate for the foreground image: "))

# Call the function to place the image over the background
place_image_over(background_image, foreground_image, x, y)









