text = open("/home/shubham/Documents/MTP/recognition_data_generation/data/newsgroup_HI.txt").read()
text = text.replace(" ", "\n")
f = open("/home/shubham/Documents/MTP/recognition_data_generation/data/newsgroup_HI.txt", "w")
f.write(text)