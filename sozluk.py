import time
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
print("Liste: CRINGE, LOL, ROFL, SHEESH, CREEPY, AGGRO")
for i in range(10):
    word = input("Anlamını öğrenmek istediğiniz kelimeyi listeden seçerek, büyük harflerle yazınız.(Dikkat et 10 hakkın var!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
        time.sleep(2)
    else:
        print("Aradığınız kelime sözlükte bulunamadı. Tekrar deneyiniz.")
        time.sleep(2)
