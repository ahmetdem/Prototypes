
input = "kaanz"
text = "kana"

# Harf sayısını içerecek variable
data = {
    "input": {},
    "text": {},
}

# İkiye ayrılıyor: metin verisi ve input verisi


# Metin karakterlerini looptan geçir
    # Harf sayısını say
for letter in input:
    
    if letter in data['input']:
        data["input"][letter] += 1
    else:
        data["input"][letter] = 1
        
        
for letter in text:
    
    if letter in data['text']:
        data["text"][letter] += 1
    else:
        data["text"][letter] = 1
   
isTrue = True

for key in data["text"].keys():
    # Datanın içindeki text dict'inin her elementini itere et
        # Elementin keyinin inputtaki aynı keyle eşleşen değerleri aynı mı
    
    if data["input"][key] != data["text"][key]: 
        isTrue = False
    

   
print( isTrue)


# {input: {k: 1} }

# Metin için yukarıdakini yap


