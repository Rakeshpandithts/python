line = "hi im in jaaga"

splitted_line = line.split(" ")
parts = []

print(splitted_line)

for i in range(0, len(splitted_line)):
    capitalWords =  splitted_line[i].capitalize()
    parts.append(capitalWords)

print(" ".join(parts))



    

