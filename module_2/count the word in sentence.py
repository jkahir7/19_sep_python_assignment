
str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for i in txt:
	if i in c:
		c[i] += 1
	else:
		c[i] = 1
print(c)