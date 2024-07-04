import re

reg = re.compile("www.google.de|com")
print(reg.match("www.google.com")) # match sucht am anfang, com steht am ende
 #reg.search("www.google.com") --> kommt com raus weil, prüft auf de und com und de ist ohne ergebnis, einfügen von klammern um de und com sucht entweder de oder com

reg = re.compile("www\.google\.(de|com)")
print(reg.match("www.google.de"))
print(reg.match("wwwwgoogle.de"))
#einmal www.google.de und einmal None

string = "Niko Stein"

reg = re.compile("Nikolai Stein")  #None, weil nicht identisch
print(reg.match(string))

reg = re.compile("Niko Stein")
print(reg.match(string))

reg = re.compile("Niko|Nikolai Stein")
print(reg.match(string))

reg = re.compile("(Niko | Nikolai) Stein")
print(reg.match(string)) #wird nichts finden, weil zu viele Leerzeichen

reg = re.compile("(Niko|Nikolai) Stein")
print(reg.match(string))

string = "\."

reg = re.compile(".")
print(reg.match(string)) #wird backslash finden
print(reg.findall(string)) #gibt liste zurück, einaml mit backslash einmal mit punkt


reg = re.compile("\.")
print(reg.match(string)) #kommt nichts raus
print(reg.search(string)) #kommt punkt raus

reg = re.compile("\\\\")
print(reg.match(string))

reg = re.compile("\\\\.")
print(reg.match(string))

reg = re.compile("\\\\\.")
print(reg.match(string))

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("is")
match = re.findall(reg, text) #findet alle is in der liste 
print(match)

reg = re.compile("\d")     
match = re.findall(reg, text) #findet alle ziffern d for digit D für alles außer Zahlen
print(match) 


reg = re.compile("\$\d.\d\d")
reg = re.search(reg, text)  #reg.match(string) acuh möglich, sucht pattern \$\d.\d\d in string text
print(match)