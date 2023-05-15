from PIL import Image
from . import crypto
from io import BytesIO

def message_to_binary(message):
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    return binary_message

def encode_image(image_path: Image, message, key):
    image = Image.open(image_path)
    message = str(crypto.encrypt(message, key))
    encrypt_length = len(message)
    binary_message = message_to_binary(message)
    if len(binary_message) > (image.size[0] * image.size[1] * 3):
        raise ValueError("Message is too long to encode in this image")
    pixel_list = list(image.getdata())
    binary_list = []
    for pixel in pixel_list:
        binary_pixel = []
        for color in pixel:
            binary_pixel.append(bin(color)[2:].zfill(8))
        binary_list.append(binary_pixel)
    binary_index = 0
    for i in range(len(binary_list)):
        for j in range(len(binary_list[i])):
            if binary_index < len(binary_message):
                binary_list[i][j] = binary_list[i][j][0:7] + binary_message[binary_index]
                binary_index += 1
            else:
                break
        if binary_index >= len(binary_message):
            break
    new_pixel_list = []
    for binary_pixel in binary_list:
        new_pixel = ()
        for color in binary_pixel:
            new_pixel += (int(color, 2),)
        new_pixel_list.append(new_pixel)
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_pixel_list)
    

    return [new_image, encrypt_length]

async def decode_image(file, message_length, key):

    contents = await file.read()  
    image = Image.open(BytesIO(contents)) 

    pixel_list = list(image.getdata())
    binary_list = []
    for pixel in pixel_list:
        binary_pixel = []
        for color in pixel:
            binary_pixel.append(bin(color)[2:].zfill(8))
        binary_list.append(binary_pixel)
    binary_message = ""
    for i in range(len(binary_list)):
        for j in range(len(binary_list[i])):
            binary_message += binary_list[i][j][-1]
    message = ""
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))
        if message.endswith('\0'):
            break
    message = message[0:message_length]

    message = message[2:-1].encode()

    message = crypto.decrypt(message, key)
    return message
