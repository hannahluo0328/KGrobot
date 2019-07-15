with open("relation.txt",'r',encoding='utf8') as f:
    for line in f.readlines():
        rela_array=line.strip("\n").split(",")
        print(rela_array)