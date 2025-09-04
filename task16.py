yosh = 5
narx = 100_000

if yosh < 7:               
    chegirma = 0.5
elif yosh <= 17:           
    chegirma = 0.2
elif yosh > 60:            
    chegirma = 0.3
else:                     
    chegirma = 0

yakuniy = narx * (1 - chegirma)

print(f"Yakuniy narx: {yakuniy:,.0f} so'm ({int(chegirma*100)}% chegirma qo'llanildi)".replace(",", "."))