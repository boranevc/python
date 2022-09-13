import random

liste = []

while True:
    x = input("İsim girin veya çıkmak için 'q' ya basın.")
    if(x=="q"):
        break
    
    liste.append(x)
    
kazanan = random.choice(liste)
print(kazanan," Seçildi")

