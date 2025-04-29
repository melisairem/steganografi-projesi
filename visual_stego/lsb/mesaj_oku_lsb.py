from stegano import lsb

revealed_message = lsb.reveal("mesajli_resim.png")

print("Resmin içindeki gizli mesaj :")
print(revealed_message)
