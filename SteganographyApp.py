from PIL import Image

def numberToBinary(num):
    """Convert a base-10 number (0–255) to an 8-bit binary string."""
    return format(num, '08b')

def binaryToNumber(bin_str):
    """Convert an 8-bit binary string to a base-10 integer."""
    return int(bin_str, 2)

def encode(img, msg):
    """Encodes a message into the least significant bits of an image."""
    pixels = img.load() 
    width, height = img.size
    msgLength = len(msg)
    total_pixels = width * height

    if msgLength * 3 + 1 > total_pixels:
        raise ValueError("Message too long for this image!")

    red, green, blue = pixels[0, 0]
    pixels[0, 0] = (msgLength, green, blue)

    letterSpot = 0
    pixel = 1  

    for i in range(1, msgLength * 3 + 1):
        x = i % width
        y = i // width

        red, green, blue = pixels[x, y]
        redBinary = numberToBinary(red)
        greenBinary = numberToBinary(green)
        blueBinary = numberToBinary(blue)

        if pixel % 3 == 1:
            letterBinary = numberToBinary(ord(msg[letterSpot]))
            greenBinary = greenBinary[:7] + letterBinary[0]
            blueBinary = blueBinary[:7] + letterBinary[1]
        elif pixel % 3 == 2:
            redBinary = redBinary[:7] + letterBinary[2]
            greenBinary = greenBinary[:7] + letterBinary[3]
            blueBinary = blueBinary[:7] + letterBinary[4]
        else:
            redBinary = redBinary[:7] + letterBinary[5]
            greenBinary = greenBinary[:7] + letterBinary[6]
            blueBinary = blueBinary[:7] + letterBinary[7]
            letterSp
