ls = []

with open("requirements.txt", "r", encoding="UTF-16") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break
        a = line.split("=", 1)[0]
        ls.append(a.strip())
print(ls)