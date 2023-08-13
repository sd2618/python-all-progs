p={"a" :  "#e8eae7","b" :  "#dd947a","c" :  "#eff0f2","d" :  "#be9682","e" :  "#f2f4f3","f" :  "#e9e9e9","g" :  "#f3f3f3","h" :  "#ecebe7","i" :  "#e9e9e7","j" :  "#e4d2c4","k" :  "#e4e3e1","l" :  "#c9492b","m" :  "#c9492b","n" :  "#72b4b2","o" :  "#f5b458","p" :  "#6a8ab2","q" :  "#bd667e","r" :  "#37555b","s" :  "#dee7e4","t" :  "#e4db98","u" :  "#e0dfdd","v" :  "#dcdbd9","w" :  "#f8f3e8","x" :  "#aea096","y" :  "#aea096","z" :  "#4c5c2d","A" :  "#f4efe0","B" :  "#f5d7e0","C" :  "#e0e0e0","D" :  "#abb3ec","E" :  "#c4e3df","F" :  "#d4d7d8","G" :  "#e280a2","H" :  "#62dada","I" :  "#ff888b","J" :  "#fbf3e4","K" :  "#bdc1c9","L" :  "#93bae1","N" :  "#a3e5e2","O" :  "#f9d8a5","P" :  "#fafafa","Q" :  "#fcfcfc","R" :  "#cdd1d4","S" :  "#49413f","T" :  "#a17e6f","U" :  "#9b9d9c","V" :  "#c3c2bd","W" :  "#f5f6f8","X" :  "#683a27","Y" :  "#485e3e","Z" :  "#485e3e","0" :  "#c1c6ca","1" :  "#cdcdcd","2" :  "#edf2f6","3" :  "#d0d0ce","4" :  "#cdb3b6","5" :  "#2c2722","6" :  "#669a7a","7" :  "#d3d9df","8" :  "#e6e7ec","9" :  "#d3c1b3","+" :  "#ebe1d6","/" :  "#e7e8ea","=":"#e2d8cc"}
k=input("set of characters")
s=""
for i in k:
    for j in p:
        if i==j:
            s=s+p[i]+" "

print(s)
print("\n\n")
print(s.split())
