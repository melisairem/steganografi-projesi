from PIL import Image
import piexif

img = Image.open("exifli_resim.jpeg")

exif_data = piexif.load(img.info["exif"])

message = exif_data["0th"][piexif.ImageIFD.ImageDescription].decode("utf-8")
print("EXIF'ten okunan mesaj:", message)
