"""
使用pillow操作圖像

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""
from PIL import Image, ImageFilter

img = Image.open('./res/guido.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./res/guido.png')

img2 = Image.open('./res/guido.png')

#裁切
img3 = img2.crop((335, 435, 430, 615))
img3.save('./res/guido3.png')

for x in range(4):
    for y in range(5):
        #黏貼
        img2.paste(img3, (95 * y , 180 * x))
#縮放
img2.resize((img.size[0] // 2, img.size[1] // 2))
#旋轉
img2.rotate(90)
img2.save('./res/guido2.png')

img4 = img2
#生成縮略圖
img4.thumbnail((128, 128))
img4.save('./res/guido4.png')

#翻轉
img5 = img.transpose(Image.FLIP_LEFT_RIGHT)
img5.save('./res/guido5.png')

#濾鏡
img6 = img.filter(ImageFilter.CONTOUR)
img6.save('./res/guido6.png')

#操作像素
for x in range(80, 310):
        for y in range(20, 360):
                img.putpixel((x, y), (128, 128, 128))
img.show()