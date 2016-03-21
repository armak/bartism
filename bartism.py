import sys
import random

def generate_markov(input):
	out = dict()
	for line in input:
		line = line.lower()
		words = line.replace("\n", "").split(" ")
		for i in range(len(words)-2):
			key = words[i]+" "+words[i+1]
			val = words[i+2]
			if key in out.keys():
				out[key].append(val)
			else:
				out[key] = [val]
	return out

def produce_sentence(mc):
	string = list()
	pair = random.choice(list(mc.keys()))
	val  = random.choice(mc[pair])
	string.extend(pair.split(" "))
	while(True):
		string.append(val)
		pair = (string[-2])+" "+(string[-1])
		if pair in mc.keys():
			val = random.choice(mc[pair])
		else:
			break
	sentence = " ".join(string)
	if not (sentence.endswith(".") or sentence.endswith("?") or sentence.endswith("!")):
		sentence += "."
	if sentence.endswith(","):
		sentence[-1] = "."
	return sentence.replace(" ,", ",").replace(" !", "!").replace(" ?", "?")


def main():
	mc = generate_markov(open("database.db", "r"))
	for i in range(0, int(sys.argv[1])):
		print(produce_sentence(mc))

if __name__ == "__main__":
	main()
