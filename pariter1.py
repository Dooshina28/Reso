#!/usr/bin/env python3

def parite(d):
	countn = 0
	resultat = []
	for i in d:
		countn = 0
		for j in i:
			if '1' in j:
				countn = countn + 1
		if countn%2==0:
			resultat.append("0"+i)
		else:
			resultat.append("1"+i)
	return resultat

a=["101010","1101"]

print(parite(a))
