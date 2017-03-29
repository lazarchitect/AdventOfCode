for each in open("4.txt").readlines():
	
	ID = ""
	
	checksum = each[each.index("[")+1:each.index("]")]
	
	for i in range(len(each)):
		if each[i].isdigit():
			start = i
			end = each.index("[")
			ID = each[start:end]
			break
	
	name = each[0:each.index(ID)].replace("-", "")
	
	letterFreqs = {}
	for i in name:
		if i in letterFreqs:
			letterFreqs[i]+=1
		else:
			letterFreqs[i] =0
			
	print(letterFreqs)
	exit()		