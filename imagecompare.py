from itertools import izip
import Image

BASEWIDTH = 200


def resize(image):
    wpercent = (BASEWIDTH / float((image.size[0])))
    hsize = int((float(image.size[1]) * float(wpercent)))
    return image.resize((BASEWIDTH, hsize), Image.ANTIALIAS)


def compare(image1, image2):
    image1 = resize(image1)
    image2 = resize(image2)
    pairs = izip(image1.getdata(), image2.getdata())
    if len(image1.getbands()) == 1:
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs
                      for c1, c2 in zip(p1, p2))
    ncomponents = image1.size[0] * image1.size[1] * 3
    print "Difference: ", (dif / 255.0 * 100) / ncomponents
