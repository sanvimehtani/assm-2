line = "Python is a case sensitive language"
#question a)
a = len(line)
print ("a)", a)
#question b)
b = line [::-1]
print ("b)", b)
#question c)
start = line.find("a")
end = line.find("language")
c = slice (start,end)
c = line[c]
print ("c)", c)
#question d)
d = line.replace("a case sensitive ", "object oriented")
print ("d)", d)
#question e)
e = line.index ("a")
print ("e)", e)
#question f)
f = line.replace(" ","")
print ("f)", f)
