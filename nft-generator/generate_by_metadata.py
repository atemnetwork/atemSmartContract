from PIL import Image
import random
import json
import os
import time
from multiprocessing.dummy import Pool as ThreadPool

background_files = {
    "Planet Elon": "B_01",
    "Neverland": "B_09",
    "Web3 Mars": "B_02",
    "Crypto Moon": "B_03",
    "DeFi Asteroids": "B_04",
    "DAO Polaris": "B_05",
    "NFT Pandora": "B_06",
    "GameFi Neptune": "B_07",
    "Blockchain Jupiter": "B_08",
}
accessories_eyewear_files = {
    "No Eyewear": "AE_00",
    "Green Sci-fi Eyewear": "AE_01_1",
    "Grey Sci-fi Eyewear": "AE_01_2",
    "Silver LED Eyewear": "AE_02_2",
    "Purple Scholar Eyewear": "AE_03_2",
    "Blue LED Eyewear": "AE_02_1",
    "Yellow LED Eyewear": "AE_02_3",
}
hair_front_files = {
    "Bald" :"HF_00",
    "Green Fringe Hair": "HF_01_4",
    "Purple Fringe Hair": "HF_01_1",
    "Blue Wavy Hair": "HF_04_1",
    "Blue Circle Hair": "HF_07_4",
    "Purple A Zone Helmet": "HF_08_3",
    "Silver Fringe Hair": "HF_01_5",
    "Silver Curl Hair": "HF_02_1",
    "Brown Afro Hair with Loop Hair Accessories": "HF_06_3",
    "Blue Curl Hair with Butterfly Hair Accessories": "HF_03_2",
    "Brown Afro Hair": "HF_05_2",
    "Brown Patterned A Zone Helmet": "HF_08_2",
    "Blue Curl Hair": "HF_02_2",
    "Silver Circle Hair": "HF_07_1",
    "Black Afro Hair": "HF_05_1",
    "Green Curl Hair": "HF_02_3",
    "Blond Wavy Hair": "HF_04_2",
    "Silver A Zone Helmet": "HF_08_1",
    "Pink Fringe Hair": "HF_01_2",
    "Colourful Circle Hair": "HF_07_2",
}
accessories_earring_files = {
    "No Earring": "AR_00",
    "Colourful ATEM Earring": "AR_01_1",
    "Gold Stud Earring": "AR_02_1",
    "Blue ATEM Earring": "AR_01_2",
    "Red Stud Earring": "AR_02_2",
}
accessories_cuff_files = {
    "No Cuff": "AC_00",
    "Colourful Chain Ear Cuff": "AC_01_1",
    "Blue Star Nose Cuff": "AC_02_2",
    "Silver Star Nose Cuff": "AC_02_1",
    "Gold Chain Ear Cuff": "AC_01_3",
    "Silver Chain Ear Cuff": "AC_01_2",
}
accessories_necklace_files = {
    "No Necklace": "AN_00",
    "Blue Pearl Necklace": "AN_02_1",
    "White Pearl Necklace": "AN_02_3",
    "Gold ATEM Watch Necklace": "AN_01_1",
    "Green ATEM Watch Necklace": "AN_01_2",
    "Silver ATEM Watch Necklace": "AN_01_3",
    "Red ATEM Watch Necklace": "AN_01_4",
}
eyebrow_files = {
    "No Eyebrow": "EB_00",
    "Light Spider Eyelash": "EB_02_2",
    "Dark Ninja Eyebrow": "EB_04_2",
    "Dark Spider Eyelash": "EB_02_1",
    "Lightning Drop": "EB_06",
    "Light Ninja Eyebrow": "EB_04_1",
    "Purple Fire Eyelash": "EB_05_1",
    "Rock Eyebrow": "EB_01",
    "Gold Dragon Eyebrow": "EB_03_2",
    "Silver Dragon Eyebrow": "EB_03_1",
}
eye_left_files = {
    "Loving Eyes": "EL_09",
    "Volcano Eyes": "EL_04",
    "Ocean Eyes": "EL_03",
    "Voyager  Eyes": "EL_10",
    "Microgravity Eyes": "EL_12",
    "Desert Eyes": "EL_01",
    "Aurora Eyes": "EL_05",
    "Sun Eyes": "EL_06",
    "Star Eyes": "EL_08",
    "Mars Eyes": "EL_02",
    "Kaleidoscope Eyes": "EL_07",
    "Inky Eyes": "EL_11",
}
eye_right_files = {
    "Loving Eyes": "ER_09",
    "Volcano Eyes": "ER_04",
    "Ocean Eyes": "ER_03",
    "Voyager  Eyes": "ER_10",
    "Microgravity Eyes": "ER_12",
    "Desert Eyes": "ER_01",
    "Aurora Eyes": "ER_05",
    "Sun Eyes": "ER_06",
    "Star Eyes": "ER_08",
    "Mars Eyes": "ER_02",
    "Kaleidoscope Eyes": "ER_07",
    "Inky Eyes": "ER_11",
}
eye_cloth_files = {
    "Orange Fur Dress": "C_02_3",
    "Red ATEM T-shirt": "C_05_2",
    "Black Fur Dress": "C_02_1",
    "Grey Fur Hoodie": "C_03_1",
    "Purple Gem Suit": "C_06_3",
    "Black Rock Leather Jacket": "C_01_1",
    "Red ATEM Sport Top": "C_04_2",
    "Purple ATEM T-shirt": "C_05_1",
    "White Rock Leather Jacket": "C_01_2",
    "Purple Fur Dress": "C_02_2",
    "Burgundy Fur Hoodie": "C_03_2",
    "Gold Gem Suit": "C_06_1",
    "Green Gem Suit": "C_06_2",
    "Green Fur Hoodie": "C_03_3",
    "Orange ATEM T-shirt": "C_05_3",
}
eye_skin_files = {
    "Neverland Unicorn Skin": "S_14",
    "Neverland Elf Skin": "S_13",
    "Elon Dark Skin": "S_01",
    "Elon Beige Skin": "S_02",
    "Elon Bright Skin": "S_03",
    "Mars Traveler Skin": "S_04",
    "Mars Capital Skin": "S_05",
    "Moon Vision Skin": "S_06",
    "Moon Crater Skin": "S_07",
    "Asteroids Skin": "S_08",
    "Polaris Skin": "S_09",
    "Pandora Skin": "S_10",
    "Neptune Passenger Skin": "S_11",
    "AKA Blockchain Jupiter Skin": "S_12",
}
hair_back_files = {
    "Bald": "HB_00",
    "Green Fringe Hair": "HB_01_4",
    "Purple Fringe Hair": "HB_01_1",
    "Blue Wavy Hair": "HB_04_1",
    "Blue Circle Hair": "HB_07_4",
    "Purple A Zone Helmet": "HB_08_3",
    "Silver Fringe Hair": "HB_01_5",
    "Silver Curl Hair": "HB_02_1",
    "Brown Afro Hair with Loop Hair Accessories": "HB_06_3",
    "Blue Curl Hair with Butterfly Hair Accessories": "HB_03_2",
    "Brown Afro Hair": "HB_05_2",
    "Brown Patterned A Zone Helmet": "HB_08_2",
    "Blue Curl Hair": "HB_02_2",
    "Silver Circle Hair": "HB_07_1",
    "Black Afro Hair": "HB_05_1",
    "Green Curl Hair": "HB_02_3",
    "Blond Wavy Hair": "HB_04_2",
    "Silver A Zone Helmet": "HB_08_1",
    "Pink Fringe Hair": "HB_01_2",
    "Colourful Circle Hair": "HB_07_2",
}
def read_file(path):
    if path == "-":
        return sys.stdin.read()
    # The newline argument preserves the original line break (see issue #2)
    with open(path, "r", newline="") as myfile:
        return myfile.read()


def save_file(path, content):
    file = open(path, "w")
    file.write(content)
    file.close()

def generate_image(item):
    time1 =time.time()
    im1 = Image.open(f'./trait-layers/12_Background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/11_Hair Back/{hair_back_files[item["hair_back"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/10_Skin/{eye_skin_files[item["skin"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/09_Clothes/{eye_cloth_files[item["cloth"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/08_Eye Right/{eye_right_files[item["eye_right"]]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/07_Eye Left/{eye_left_files[item["eye_left"]]}.png').convert('RGBA')
    im7 = Image.open(f'./trait-layers/06_Eyebrow/{eyebrow_files[item["eyebrow"]]}.png').convert('RGBA')
    im8 = Image.open(f'./trait-layers/05_Accessories Necklace/{accessories_necklace_files[item["accessories_necklace"]]}.png').convert('RGBA')
    im9 = Image.open(f'./trait-layers/04_Accessories Cuff/{accessories_cuff_files[item["accessories_cuff"]]}.png').convert('RGBA')
    im10 = Image.open(f'./trait-layers/03_Accessories Earring/{accessories_earring_files[item["accessories_earring"]]}.png').convert('RGBA')
    im11 = Image.open(f'./trait-layers/02_Hair Front/{hair_front_files[item["hair_front"]]}.png').convert('RGBA')
    im12 = Image.open(f'./trait-layers/01_Accessories Eyewear/{accessories_eyewear_files[item["accessories_eyewear"]]}.png').convert('RGBA')

    time2 = time.time()

    #print('time cost1', time2 - time1, 's')
    #Create each composite
    im2 = im2.resize(im1.size)
    com1 = Image.alpha_composite(im1, im2)

    im3 = im3.resize(com1.size)
    com2 = Image.alpha_composite(com1, im3)
    im4 = im4.resize(com2.size)
    com3 = Image.alpha_composite(com2, im4)
    im5 = im5.resize(com3.size)
    com4 = Image.alpha_composite(com3, im5)
    im6 = im6.resize(com4.size)
    com5 = Image.alpha_composite(com4, im6)
    im7 = im7.resize(com5.size)
    com6 = Image.alpha_composite(com5, im7)
    im8 = im8.resize(com6.size)
    com7 = Image.alpha_composite(com6, im8)
    im9 = im9.resize(com7.size)
    com8 = Image.alpha_composite(com7, im9)
    im10 = im10.resize(com8.size)
    com9 = Image.alpha_composite(com8, im10)
    im11 = im11.resize(com9.size)
    com10 = Image.alpha_composite(com9, im11)
    im12 = im12.resize(com10.size)
    com11 = Image.alpha_composite(com10, im12)

    time3 = time.time()
    #print('time cost2', time3 - time2, 's')

    #Convert to RGB
    rgb_im = com11.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    save_path = "./new_images/"
    if item["cloth"] == "Green Fur Hoodie":
        file_name = "Green_Fur_Hoodie_" + file_name
    rgb_im.save(save_path + file_name)
    print("Saved ./new_images/%s" % file_name)

    

    time4 = time.time()
    #print('time cost3', time4 - time3, 's')

def generate_between(start, end):
    l = []
    for x in range(start, end):
        l.append(x)

    def process(x):
        print('file: ' + str(x))
        input_file = "current_meta/"+str(x)
        except_file = "except/"+str(x)
        try:
            if os.path.isfile('current_meta/'+str(x)) & (not os.path.isfile('new_images/'+str(x)+".png")):
                original = read_file(input_file)
                metadata = json.loads(original)
                attributes = metadata["attributes"]
                item = {}
                item["tokenId"] = metadata["tokenId"]
                for i in attributes:
                    item[i["trait_type"]] = i["value"]
                generate_image(item)
        except:
            save_file(except_file, original)
    
    pool = ThreadPool(10)
    pool.map(process, l)
    pool.close()
    pool.join()

def main(args=None):
    _path = "./new_images/"
    isExist = os.path.exists(_path)
    if not isExist:
        os.makedirs(_path)
        print("new_images directory is created!")
    _path = "./except/"
    isExist = os.path.exists(_path)
    if not isExist:
        os.makedirs(_path)
        print("except directory is created!")
    timeStart = time.time()
    generate_between(0, 5000)
    timeEnd = time.time()
    print('Total time spend: ' + str(timeEnd - timeStart))

if __name__ == "__main__":
    main()