import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile("$This")
match = reg2.search(text)
print(match)

reg2 = re.compile("^This")
match = reg2.search(text)
print(match)

reg2 = re.compile("This^")
match = reg2.search(text)
print(match)

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart\.$")
match = reg2.search(text)
print(match)

reg2 = re.compile("........$")
match = reg2.search(text)
print(match)    # gibt genau das gleiche wie oben raus, 8 platzhalter und doller zeichen machen letztes worte ende am satz