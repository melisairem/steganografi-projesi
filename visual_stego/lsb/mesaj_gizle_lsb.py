from stegano import lsb

original_image = "orijinal_resim.png"

secret_message = "Bu bir gizli mesaj denemesidir."

secret_image = lsb.hide(original_image, secret_message)
secret_image.save("mesajli_resim.png")

print("Mesaj başarıyla resme gömüldü!")
