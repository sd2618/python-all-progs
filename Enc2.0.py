from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from PIL import Image
import os
import secrets
import cv2
def generate_random_color():
    # Generate random red, green, and blue components
    red = secrets.choice(range(256))
    green = secrets.choice(range(256))
    blue = secrets.choice(range(256))
    
    # Convert to hex strings and format the color code
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    return color_code

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

# Example usage
key = input("Enter 16-byte Key: ").encode('utf-8')
plaintext = input("Enter Real Message: ")
faketext=input("Enter Fake Message:")

encrypted_text = encrypt(key, plaintext)
distract_text = encrypt(key, faketext)
p = {'A': '#FFFFFF','B': '#FEFEFE','C': '#FDFDFD','D': '#FCFCFC','E': '#FBFBFB','F': '#FAFAFA','G': '#F9F9F9','H': '#F8F8F8','I': '#F7F7F7','J': '#F6F6F6','K': '#F5F5F5','L': '#F4F4F4','M': '#F3F3F3','N': '#F2F2F2','O':'#F1F1F1','P': '#F0F0F0','Q': '#EFEFEF','R': '#EEEEEE','S': '#EDEDED','T': '#ECECEC','U': '#EBEBEB',
'V': '#EAEAEA','W': '#E9E9E9','X': '#E8E8E8','Y': '#E7E7E7','Z': '#E6E6E6','a': '#E5E5E5','b': '#E4E4E4',
'c': '#E3E3E3','d': '#E2E2E2','e': '#E1E1E1','f': '#E0E0E0','g': '#DFDFDF','h': '#DEDEDE','i': '#DDDDDD',
'j': '#DCDCDC','k': '#DBDBDB','l': '#DADADA','m': '#D9D9D9','n': '#D8D8D8','o': '#D7D7D7','p': '#D6D6D6',
'q': '#D5D5D5','r': '#D4D4D4','s': '#D3D3D3','t': '#D2D2D2','u': '#D1D1D1','v': '#D0D0D0','w': '#CFCFCF',
'x': '#CECECE','y': '#CDCDCD','z': '#CCCCCC','0': '#7A7A7A','1': '#CBCBCB','2': '#C8C8C8','3': '#C5C5C5',
'4': '#C2C2C2','5': '#BFBFBF','6': '#BCBCBC','7': '#B9B9B9','8': '#B6B6B6','9': '#B3B3B3','+': '#B0B0B0',
'/': '#ADADAD','=': '#AAAAAA'
}


s=""
e=""
ig=[]
im=[]
for i in encrypted_text:
    for j in p:
        if i==j:
            s=s+p[i]+" "
            ig.append(p[i])
for i in distract_text:
    for j in p:
        if i==j:
            e=e+p[i]+" "
            im.append(p[i])
ds=s.replace('#',"")
dm=e.replace('#','')
print(ig)
print(im)
rk=[]
fk=[]

pass_key=(input("Enter Real Key:"))
fake_key=(input("Enter Fake Key:"))
pk=int(pass_key[0:1])+int(pass_key[1:2])-int(pass_key[2:3])-int(pass_key[3:4])
if pk%2!=0:
    pk=pk+1
fy=int(fake_key[0:1])+int(fake_key[1:2])-int(fake_key[2:3])-int(fake_key[3:4])
if fy%2!=0:
    fy=fy-1

for i in range(10,len(ig)+11):
    rk.append(i*2+pk)
for j in range(50,len(im)+51):
    fk.append(j*2-7-fy)
av=0
fv=0
lol=[]
for i in range(2500):
    if i not in fk and i not in rk:
        r_c = generate_random_color()
        for clrs in p.values():
            if clrs==r_c:
                r_c=generate_random_color()
        lol.append(r_c)
    if i in fk:
        if fv<len(im):
            lol.append(im[fv])
            fv=fv+1
        
    if i in rk:
        if av<len(ig):
            lol.append(ig[av])
            av=av+1

print("LOL::::::",len(lol))
if pass_key==fake_key:
    print("Invalid KEys")
    exit
lel=''
for i in lol:
    lel+=' '+i.replace('#','')
data = bytes.fromhex(lel)
width = 50
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
background_image = r'C:\Users\Devansh\OneDrive\Desktop\imgs\8.jpg'
foreground_image=r'C:\Users\Devansh\OneDrive\Desktop\PYTHON\output_image.png'
x = int(input("Enter the x-coordinate for the foreground image: "))
y = int(input("Enter the y-coordinate for the foreground image: "))

# Call the function to place the image over the background
place_image_over(background_image, foreground_image, x, y)