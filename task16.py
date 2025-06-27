asosiy_narx = 100000


yosh = int(input("Yoshingizni kiriting: "))


if yosh < 8:
    chegirma = 0.5  
elif yosh < 18:
    chegirma = 0.2 
else:
    chegirma = 0.0 

chegirma_miqdori = asosiy_narx * chegirma
yakuniy_narx = asosiy_narx - chegirma_miqdori
foiz = int(chegirma * 100)
print(f"Yakuniy narx: {int(yakuniy_narx)} so'm ({foiz}% chegirma qo'llanildi)")
