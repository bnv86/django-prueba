from PIL import Image, ImageFilter


try:
    img = Image.open("images/k1.jpg")
    #print(img.mode) #RGB o RGBA
    #print(img.getpixel((100, 200))) #x,y

    #CONVERTIR
    #img = img.convert("L")

    #ROTAR
    #img = img.rotate(40, expand=True) #grados
    #img = img.transpose(Image.ROTATE_180)

    #GUARDAR (no crea carpetas nuevas)
    #img.save("images/k1-copia.jpg")

    #SIZE, RESIZE
    #print(img.size)
    #print(img.width)
    #print(img.height)
    #img = img.resize((200, 250)) #ancho y alto
    #img = img.resize((img.width/2, img.height/2)) #ancho y alto
    
    #CROP
    #box = (300, 100, 500, 400) # x (desde),y (desde), x (hasta),y (hasta)
    #img = img.crop(box)
    
    #FILTER
    #img = img.filter(ImageFilter.EMBOSS)

    #PASTE
    #im = Image.open("images/k2.jpg")
    #copy = im.resize((300,200))
    #im.paste(copy, (200,300))
    #im.show()
    #im.save("images/nueva/paste.jpg")

    #img.show()
    #print(img.size)
except IOError:
    print("Error: No es posible abrir la imagen")

"""
filters:
BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SHARPEN
SMOOTH
SMOOTH_MORE
"""
