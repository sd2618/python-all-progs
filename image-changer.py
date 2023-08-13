import cv2

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


# Prompt the user for inputs
background_image = input("Enter the path to the background image: ")
foreground_image = input("Enter the path to the foreground image: ")
x = int(input("Enter the x-coordinate for the foreground image: "))
y = int(input("Enter the y-coordinate for the foreground image: "))

# Call the function to place the image over the background
place_image_over(background_image, foreground_image, x, y)
