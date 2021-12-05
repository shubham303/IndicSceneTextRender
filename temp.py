lines = open("/usr/datasets/synthetic_text_dataset/Hindi/test1.tsv").readlines()
lines2 = open("/usr/datasets/synthetic_text_dataset/Hindi/test2.tsv").readlines()
f = open("/usr/datasets/synthetic_text_dataset/Hindi/test.tsv", "w")
for line in lines:
	f.write(line)

for line in lines2:
	f.write(line)

f.close()


"""lines = open("/media/shubham/One Touch/Indic_OCR/datasets/ocr_dataset/synthetic/recognition/devanagari/hindi2/train.tsv")
lines = [ line.split("\t")[0]+"\t"+line.split("\t")[1]  if  len(line.split("\t")) ==3 else line  for line in lines ]
lines = "\n".join(map(str, lines))
lines = lines.replace("\n\n", "\n")
with open("/media/shubham/One Touch/Indic_OCR/datasets/ocr_dataset/synthetic/recognition/devanagari/hindi2/train1.tsv"
          "", "w") as f:
	f.write(lines)
"""
"""lines = open("/media/shubham/One Touch/Indic_OCR/datasets/ocr_dataset/synthetic/recognition/devanagari/hindi2"
             "/devanagari/test.tsv").readlines()
out=[]
for line in lines:
	line = line.split(", ")
	line = line[0]+"\t"+line[1]
	line.replace("\n", "")
	line = "17"+ line[1:]
	out.append(line)

f =open("/media/shubham/One Touch/Indic_OCR/datasets/ocr_dataset/synthetic/recognition/devanagari/hindi2"
             "/devanagari/test1.tsv", "w")
f.write("\n".join(map(str, out)))

f.close()
"""