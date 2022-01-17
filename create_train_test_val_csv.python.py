import os.path

import fire


def write_to_file(data, file,fontlist):
	
	for i ,line in enumerate(data):
		if i%1000==0:
			print("{} completed".format(i))
		del line[2]
		font = line[2]
		if not isfontValid(fontlist, font):
			continue
		line = ", ".join(map(str, line))
		file.write(line)
		file.write("\n")

def isfontValid(fontList, font):
	#font is not valid if it is not in fontlist.
	font = font.split(" ")[0]
	
	for f in fontList:
		if font.lower() in f.lower():
			return True
	return False

def create_train_test_val_csv(filename, lang, output_path="./"):
	fontlist = open("fontlists/{}.txt".format(lang), "r").readlines()
	
	lines = open(filename).readlines()
	lines = [line.split(", ") for line in lines]
	lines = [line[0:4] for line in lines]
	import random
	
	random.shuffle(lines)
	length = len(lines)
	train_length = int(16 / 25 * length)
	test_length = int(1/5 * length)
	
	train = lines[0:train_length]
	test = lines[train_length: train_length+test_length]
	val = lines[train_length + test_length:]
	
	train_out = open(os.path.join(output_path, "train.tsv"), "w")
	test_out = open(os.path.join(output_path, "test.tsv"), "w")
	val_out = open(os.path.join(output_path, "val.tsv"), "w")
	
	write_to_file(train, train_out, fontlist)
	write_to_file(test, test_out, fontlist)
	write_to_file(val, val_out, fontlist)

if __name__ == '__main__':
	fire.Fire(create_train_test_val_csv)
