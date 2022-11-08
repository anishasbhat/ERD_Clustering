from PIL import Image
import pytesseract
import json
import re
import cv2
from pytesseract import Output
from PIL import Image
import urllib

coords_8 = [[2, 1, 723, 840], [1400, 715, 2118, 1564], [2646, 1, 3359, 479], [1, 1156, 725, 1531], [1873, 1, 2282, 167], 
[2193, 240, 2568, 488], [834, 322, 1214, 560], [675, 883, 1002, 1122], [725, 126, 859, 238], [1275, 785, 1398, 890], 
[2121, 765, 2255, 874], [2505, 4, 2641, 97], [718, 619, 846, 719], [723, 1288, 834, 1385]]

coords_23 = [[2520, 321, 3124, 1886], [1279, 438, 1889, 803], [1306, 1117, 1901, 1478], [4, 317, 601, 1523], [791, 332, 1064, 619],
[2031, 334, 2308, 623], [2039, 653, 2322, 923], [804, 680, 1087, 942], [781, 1200, 1108, 1523], [2041, 1178, 2358, 1496],
[795, 1678, 1085, 1807], [2062, 1640, 2343, 1761]]
def test_xml(id, entity, coordinates):
    x = int(coordinates[0])
    y = int(coordinates[1])
    w = int(coordinates[2]) - int(coordinates[0])
    h = int(coordinates[3]) - int(coordinates[1])

    ###############CROP IMAGE###############
    im = Image.open(id, mode='r')
    #USE FOR ADITYA'S VERSION
    #im1 = im.crop((x, y, x + int(coordinates[2]), y + int(coordinates[3])))
    #USE FOR COORDS
    im1 = im.crop((x, y, int(coordinates[2]), int(coordinates[3])))

    url = "test.png"
    im1 = im1.save(url)
    ###############CROP IMAGE###############


    img = cv2.imread(url) #HAVE TO CHANGE THIS BASED ON image
    #img = cv2.medianblur(img, 30)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ##############RESIZING SHENANIGANS###############
    scale_percent = 57 # percent of original size 56-57 bless
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    ##############RESIZING SHENANIGANS###############
    arr = []
    output_str = pytesseract.image_to_string(img)
    if (output_str == ""):
        img = cv2.imread(url)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        scale_percent = 30 # percent of original size 56-57 bless
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        output_str = pytesseract.image_to_string(img)
        arr = create_arr(output_str)
    if(output_str != ""):
        #print(output_str)
        #print("output string is: " +  output_str)
        
        arr = create_arr(output_str)
        #print("array list thing is: " + arr)
    #arr = create_arr(output_str)
    #print("array list thing is: " + arr)
    
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # create_arr(sample_str)
    #print("-----------DONE READING, STARTING NEXT----------")
    return arr

def create_arr(input_str): 
    item = input_str.split('\n')
    item = [line for line in input_str.split('\n') if line.strip() != '']
    return item

def pass_image(id, entity, coordinates):
    #print(coordinates)
    x = int(coordinates[0])
    y = int(coordinates[1])
    w = int(coordinates[2]) - int(coordinates[0])
    h = int(coordinates[3]) - int(coordinates[1])

    ###############CROP IMAGE###############
    im = Image.open(id, mode='r')
    #print("left: ", x, "top: ", y, "right: ", x + int(coordinates[2]), "bottom: ", y + int(coordinates[3]))
    im1 = im.crop((x, y, x + int(coordinates[2]), y + int(coordinates[3])))
    url = "test.png"
    im1 = im1.save(url)
    ###############CROP IMAGE###############

    img = cv2.imread(url)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ##############RESIZING SHENANIGANS###############
    scale_percent = 57 # percent of original size 56-57 bless
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    ##############RESIZING SHENANIGANS###############
    
    output_str = pytesseract.image_to_string(img)
    if (output_str == ""):
        img = cv2.imread(url)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        scale_percent = 30 # percent of original size 56-57 bless
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        output_str = pytesseract.image_to_string(img)


    print(pytesseract.image_to_string(img))
    #READD LATER
    #arr = create_arr(output_str)
    arr = []
    print("-----------DONE READING, STARTING NEXT----------")
    return arr

def pass_image_old(id, entity, coordinates):
    #print(coordinates)
    x = int(coordinates[0])
    y = int(coordinates[1])
    w = int(coordinates[2]) - int(coordinates[0])
    h = int(coordinates[3]) - int(coordinates[1])

    ###############CROP IMAGE###############
    im = Image.open(id, mode='r')
    #print("left: ", x, "top: ", y, "right: ", x + int(coordinates[2]), "bottom: ", y + int(coordinates[3]))
    im1 = im.crop((x, y, x + int(coordinates[2]), y + int(coordinates[3])))
    url = "test.png"
    im1 = im1.save(url)
    ###############CROP IMAGE###############

    img = cv2.imread(url)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ##############RESIZING SHENANIGANS###############
    scale_percent = 57 # percent of original size 56-57 bless
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    ##############RESIZING SHENANIGANS###############
    
    output_str = pytesseract.image_to_string(img)
    print(pytesseract.image_to_string(img))
    #READD LATER
    #arr = create_arr(output_str)
    arr = []
    print("-----------DONE READING, STARTING NEXT----------")
    return arr

def read_json(path):
    f = open('output.json')
    data = json.load(f)
    res = []
    #data: "{image-url: [rel,[x, y, width, height]]}"
    for pair in data:
        image_url, relations = list(pair.items())[0]
        id = image_url.rsplit('/', 1)[-1]

        for relation in relations:
            entity = relation[0]
            coordinates = relation[1]
            #print(coordinates)
            cur_res = test_xml(id, entity, coordinates)
            if len(cur_res) > 0:
                res.append(cur_res)
    f.close()
    return res

def main():
    #res = pass_image("", "", [833.1358464360237, 319.4648642539978, 367.20498675107956, 246.4319360256195])
    results = []
    #results = read_json("output.json")
    # res = []
    for coord in coords_23:
        cur_res = test_xml("023.png", "entity,", coord)
        if len(cur_res) > 0:
            results.append(cur_res)
    print(results)

if __name__ == "__main__":
    main()