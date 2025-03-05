# print("insira uma frase: ")

frase = "pablo vavrik"
count = 0

for i in frase:
   if i.lower() in {'a', 'e', 'i', 'o', 'u'}:
        count +=1
    
        
print("A frase contem",count,"vogais!")
    
