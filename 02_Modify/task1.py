import re

# reg = re.compile("www.google.(de|com)")

reg = re.compile("(https?://)?www\.[a-zA-Z\-\.]+\.(com|de)[a-zA-Z\-\./]*")


m = reg.match("www.google.com")
print(m)

m = reg.match("http://www.google.com")
print(m)

m = reg.match("https://www.google.com")
print(m)

m = reg.match("https://www..com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)

