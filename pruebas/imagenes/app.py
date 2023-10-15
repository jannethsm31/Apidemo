from PIL import Image
im = Image.open("ojo.jpg")

print(im.format, im.size, im.mode)

box = (0, 0, 1000, 800)
region = im.crop(box)
region.save("recorte.jpg")

r, g, b = region.split()
region = Image.merge("RGB", (r, r, r))
region.save("cambio.jpg")

out = region.rotate(10)
out.save("giro.jpg")