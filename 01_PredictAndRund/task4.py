import re

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("([A-Z][a-z]+) ([A-Z]*)( )?([A-Z][a-z]+)")  #1. gruppe. irgendwas aus charakteset großschreibung, dann min. 1 kleiner buchstabe, 2. gruppe billige Anzahl   
m = reg.match("Hanna J Gruber")           #an Großbuchstaben dann 3. gruppe Leerzeichen optional 0 oder einmal, 4. gruppe wieder wie erste
print(m)
print(m.group(0))   #ganzer string
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
#--> es gibt 4 gruppen , alles was in () gesetzt ist

m = reg.match("Hanna Gruber")
print(m)
print(m.group(4))

m = reg.match("Hanna Jana Gruber")
print(m)
print(m.group(4)) #-> würde nur Hanna Jana finden, reg müsste angepasst werden, druckt nur jana

m = reg.match("Albert KD Klein")
print(m)
print(m.group(2))

m = reg.match("Christoph M Flath")
print(m)
print(m.group(2))

m = reg.search("Hanna J Gruber, PhD")
print(m)
print(m.group(2))

m = reg.search("xw. Alfred Nobel")
print(m)
print(m.group(2))