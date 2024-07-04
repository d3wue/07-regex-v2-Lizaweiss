import re

text = "This book on tennis cost $3.99 at Walmart."

reg1 = re.compile("ten")
match = reg1.match(text)
print(match)                # nichts passiert

reg2 = re.compile("this")
match = reg2.match(text)
print(match)                #This not this , muss extra gesagt werden       

reg3 = re.compile("This")
match = reg3.match(text)
print(match)


match = reg1.search(text)
print(match)

match = reg1.findall(text)
print(match)