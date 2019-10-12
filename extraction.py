import re
file1 = open("AMiner-Paper.txt","r",encoding="utf8")
filetext=file1.read()
file1.close()
matches = re.findall("#index\s*\d+\n#\*\s+.*", filetext)
matches1 = re.findall("#index\s*\d+", filetext)
matches2 = re.findall("#\*\s+.*", filetext)
match1=[]
for i in range(len(matches1)):
    match1.append(re.sub("#index\s",'',matches1[i]))
match2=[]
for i in range(len(matches2)):
    match2.append(re.sub("#\*\s",'',matches2[i]))
f= open("extracted3.csv","a+",encoding="utf8")
for i in range(len(match1)):
    f.write(match1[i]+","+match2[i]+"\n")
f.close()
