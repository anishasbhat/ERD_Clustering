from PIL import Image
import pytesseract
import json
import re
import cv2
from pytesseract import Output
from PIL import Image
import urllib

'''
    title : rel
    coordinates is [833.1358464360237, x
                    319.4648642539978, y
                    367.20498675107956, width
                    246.4319360256195] height
    takes in coordinates as input, returns an item
'''
coords_8 = [[2, 1, 723, 840], [1400, 715, 2118, 1564], [2646, 1, 3359, 479], [1, 1156, 725, 1531], [1873, 1, 2282, 167], 
[2193, 240, 2568, 488], [834, 322, 1214, 560], [675, 883, 1002, 1122], [725, 126, 859, 238], [1275, 785, 1398, 890], 
[2121, 765, 2255, 874], [2505, 4, 2641, 97], [718, 619, 846, 719], [723, 1288, 834, 1385]]

coords_23 = [[2520, 321, 3124, 1886], [1279, 438, 1889, 803], [1306, 1117, 1901, 1478], [4, 317, 601, 1523], [791, 332, 1064, 619],
[2031, 334, 2308, 623], [2039, 653, 2322, 923], [804, 680, 1087, 942], [781, 1200, 1108, 1523], [2041, 1178, 2358, 1496],
[795, 1678, 1085, 1807], [2062, 1640, 2343, 1761]]

#sample_str = "One-way trips PK trip_id class. price origin destination   max_bags departure_date-time arrival_date-time duration"
def create_arr(input_str): 
    #item = input_str.split('\n')
    #[line for line in mystr.split('\n') if line.strip() != '']
    item = input_str.split('\n')
    #item = [word.rstrip() for word in input_str.split('\n')]
    item = [line for line in input_str.split('\n') if line.strip() != '']
    print(item)
    return

def test_xml(coords):
    for i, coordinates in enumerate(coords):
        x = int(coordinates[0])
        y = int(coordinates[1])
        w = int(coordinates[2]) - int(coordinates[0])
        h = int(coordinates[3]) - int(coordinates[1])

        ###############CROP IMAGE###############
        im = Image.open(r"023.png")
        im1 = im.crop((x, y, int(coordinates[2]), int(coordinates[3])))
        url = "test" + str(i) + ".png"
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
        if(output_str != ""):
            print(output_str)
            #print("output string is: " +  output_str)
            
            arr = create_arr(output_str)
            #print("array list thing is: " + arr)
        #arr = create_arr(output_str)
        #print("array list thing is: " + arr)
        
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # create_arr(sample_str)
        print("-----------DONE READING, STARTING NEXT----------")
    return
    
def pass_image(id, entity, coordinates):
    x = int(coordinates[0])
    y = int(coordinates[1])
    w = int(coordinates[2]) - int(coordinates[0])
    h = int(coordinates[3]) - int(coordinates[1])

    ###############CROP IMAGE###############
    im = Image.open(r"023.png")
    im1 = im.crop((x, y, int(coordinates[2]), int(coordinates[3])))
    url = "test" + str(i) + ".png"
    im1 = im1.save(url)
    ###############CROP IMAGE###############

    img = cv2.imread(id)
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ##############RESIZING SHENANIGANS###############
    scale_percent = 57 # percent of original size 56-57 bless
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    ##############RESIZING SHENANIGANS###############
    
    output_str = pytesseract.image_to_string(img)
    arr = create_arr(output_str)
    

    
    
    print("-----------DONE READING, STARTING NEXT----------")
    # d = pytesseract.image_to_data(img, output_type=Output.DICT)
    # n_boxes = len(d['text'])
    # for i in range(n_boxes):
    #     if int(d['conf'][i]) > 60:
    #         #(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    #         print(coordinates)
    #         print(x, y, w, h)
    #         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # print(pytesseract.image_to_string(img))
        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # print(pytesseract.image_to_string(img))
        #break

    #cv2.imshow('img', img)
    #cv2.waitKey(0)
    #return:
    # TYPE OF REL, TABLE NAME, VALUE
    return arr

def read_json(path):
    #open json object, data is dict with information
    f = open('output.json')
    data = json.load(f)
    res = []
    #data: "{image-url: [rel,[x, y, width, height]]}"
    for pair in data:
        image_url, relations = list(pair.items())[0]

        #get image url
        id = image_url.rsplit('/', 1)[-1]
        #parse relation, coordinates, pass image
        for relation in relations:
            entity = relation[0]
            coordinates = relation[1]
            #print(coordinates)
            res.append(pass_image(id, entity, coordinates))

    f.close()
    return res

def main():
    #res = pass_image("", "", [833.1358464360237, 319.4648642539978, 367.20498675107956, 246.4319360256195])
    #results = read_json("replace")
    test_xml(coords_23)

if __name__ == "__main__":
    main()