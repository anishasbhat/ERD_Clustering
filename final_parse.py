from PIL import Image
import pytesseract
import json
import re
import cv2
from pytesseract import Output
from PIL import Image
import urllib

#xml coordinates for auto testing
coords_8 = [[2, 1, 723, 840], [1400, 715, 2118, 1564], [2646, 1, 3359, 479], [1, 1156, 725, 1531], [1873, 1, 2282, 167], 
[2193, 240, 2568, 488], [834, 322, 1214, 560], [675, 883, 1002, 1122], [725, 126, 859, 238], [1275, 785, 1398, 890], 
[2121, 765, 2255, 874], [2505, 4, 2641, 97], [718, 619, 846, 719], [723, 1288, 834, 1385]]
coords_23 = [[2520, 321, 3124, 1886], [1279, 438, 1889, 803], [1306, 1117, 1901, 1478], [4, 317, 601, 1523], [791, 332, 1064, 619],
[2031, 334, 2308, 623], [2039, 653, 2322, 923], [804, 680, 1087, 942], [781, 1200, 1108, 1523], [2041, 1178, 2358, 1496],
[795, 1678, 1085, 1807], [2062, 1640, 2343, 1761]]

def test(id, entity, coordinates, manual_flag):
    coordinates = [int(i) for i in coordinates]

    #get coords
    x = coordinates[0]
    y = coordinates[1]
    w = coordinates[2] - coordinates[0]
    h = coordinates[3] - coordinates[1]
    r = coordinates[2] #change r,b values for manual vs auto
    b = coordinates[3]

    if manual_flag: #if manual testing, must add x + y to get true right and bottom coords
        r += x
        b += y

    #crop image
    im = Image.open(id, mode='r')
    im1 = im.crop((x, y, r, b))
    url = "test.png"
    im1 = im1.save(url)

    #scale image for better text reading, return pytesseract text
    def scale(url, scale_percent):
        img = cv2.imread(url)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return pytesseract.image_to_string(img)

    output_str = scale(url, 57)
    if len(output_str) <= 0: #recompute scaling, as text was found to be empty
        output_str = scale(url, 30)
    return create_arr(output_str)

def create_arr(input_str): 
    item = input_str.split('\n')
    item = [line for line in input_str.split('\n') if line.strip() != '']
    return item

def manual_parsing():
    f = open('output.json')
    data = json.load(f)
    res = []
    #data: "{image-url: [rel,[x, y, width, height]]}"
    for pair in data:
        image_url, relations = list(pair.items())[0]
        id = image_url.rsplit('/', 1)[-1]

        for entity, coordinates in relations:
            cur_res = test(id, entity, coordinates, True)
            if len(cur_res) > 0:
                res.append(cur_res)
    f.close()
    return res

def auto_parsing():
    results = []
    for coord in coords_23:
        cur_res = test("023.png", "entity,", coord, False)
        if len(cur_res) > 0:
            results.append(cur_res)
    return results

def main():
    #results = manual_parsing() #parsing from json
    results = auto_parsing() #parsing from xml file coordinate arrays
    print(results)

if __name__ == "__main__":
    main()