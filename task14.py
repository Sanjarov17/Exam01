filename = "report.pdf"

if filename.endswith(".pdf"):
    print("Fayl turi: pdf")
elif filename.endswith(".docx"):
    print("Fayl turi: docx")
elif filename.endswith(".txt"):
    print("Fayl turi: txt")
else:
    print("Noma'lum fayl turi")
