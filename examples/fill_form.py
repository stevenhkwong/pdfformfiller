from pdfformfiller import PdfFormFiller
filler = PdfFormFiller("./bluecard_application_hp.pdf")
#filler = PdfFormFiller("./sampleform.pdf")
#filler.add_text("TEST TEXT", 1, (x1, y1), (x2, y2))
#filler.add_text("XXXXXXXXXX", 1, (36, 318), (48, 330))

# Mr checkbox: ((35, 335), (47, 347)
filler.add_text(chr(10003), 1, (140, 79), (149, 92))

# family name:
filler.add_text("O'Dell", 1, (110, 130), (286, 144))


filler.write("./bluecard_application_hp_FILLED.pdf")

