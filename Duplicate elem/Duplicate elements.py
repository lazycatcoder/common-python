#search for duplicate elements
import re

def duplicate(txt, elem, len_elem):
	if len_elem > 0:
		dict_find = {}
		for el in elem:
			if el not in txt:
				print(f"{el} - not found")
			else:
				for word in txt:
					if word == el:
						dict_find.setdefault(word, 0)
						dict_find[word] += 1
		# print(dict_find)
		dict_list_sorted = dict(sorted(dict_find.items(), key=lambda elem: elem[1], reverse=True))
		dict_list = dict_list_sorted.keys()
		for words in dict_list:
			print ("found word: %s - %s (times duplicated)" % (words, dict_find[words]))
	else:
		dict_find = {}
		for word in txt:
			dict_find.setdefault(word, 0)
			dict_find[word] += 1
		# print(dict_find)
		if all(value == 1 for value in dict_find.values()) == True:
			print ("duplicate words not found") 
		else:
			dict_list_sorted = dict(sorted(dict_find.items(), key = lambda elem: elem[1], reverse = True))
			dict_list = dict_list_sorted.keys()
			for words in dict_list:
				if dict_find[words] <= 1:
					pass
				else:
					print ("found word: %s - %s (times duplicated)" % (words, dict_find[words]))
	
def main():
	text = str(input("enter the text: "))
	txt = re.sub('[%s]' % ',.:;!?-', ' ', text.lower()).split()
	find_elem = str(input("enter the word which you want to find or leave this field blank (to search for all duplicate items): "))
	elem = re.sub('[%s]' % ',.:;!?-', ' ', find_elem.lower()).split()
	len_elem = int(len(elem))

	duplicate (txt, elem, len_elem)

if __name__ == '__main__':
	main()