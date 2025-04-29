from PIL import Image
import piexif

original_image = "orijinal_resim.jpeg"
secret_message = "Bu mesaj EXIF içine gömüldü."

img = Image.open(original_image)

exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
exif_dict["0th"][piexif.ImageIFD.ImageDescription] = secret_message.encode("utf-8")

exif_bytes = piexif.dump(exif_dict)

img.save("exifli_resim.jpeg", exif=exif_bytes)

print("Mesaj EXIF metadata'ya başarıyla gömüldü")
