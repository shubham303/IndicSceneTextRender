import os


for filename in os.listdir("fontlists"):
	if filename=="zz":
		continue
		
	with open(os.path.join("fontlists", filename), 'r') as f:
		lines = f.readlines()
		f = open("fontlists/zz/{}".format(filename),"w+")
		fonts=""
		for line in lines:
			x="/home/shubham/.fonts/{}/".format(filename.replace(".txt",""))
			w = line.replace(x,"")
			i=w.find(".ttf")
			w=w[0:i]
			w = w.replace("-", " ")
			fonts+=w
			fonts+="\n"
			
		f.write(fonts)
