from PIL import Image
from math import sqrt
import json

img = Image.open("pendejo.png")

pix = img.load()

originx = 1284
originy = 1948

color_mappings = {
    '#BE0039': 1,
    '#FF4500': 2,
    '#FFA800': 3,
    '#FFD635': 4,
    '#00A368': 6,
    '#00CC78': 7,
    '#7EED56': 8,
    '#00756F': 9,
    '#009EAA': 10,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#493AC1': 15,
    '#6A5CFF': 16,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#FF3881': 22,
    '#FF99AA': 23,
    '#6D482F': 24,
    '#9C6926': 25,
    '#000000': 27,
    '#898D90': 29,
    '#D4D7D9': 30,
    '#FFFFFF': 31
}

def clamp(x): 
  return max(0, min(int(x), 255))

def rgb_to_hex(rgb):
    return ("#{0:02x}{1:02x}{2:02x}".format(clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2]))).upper()

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in color_mappings:
        cr, cg, cb = hex_to_rgb(color)
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

arr = []

for y in range(32):
    for x in range(32):
        arr.append([x+originx,y+originy,color_mappings[closest_color(pix[x,y][:3])]])

with open('data.json', 'w') as f:
    json.dump(arr, f)