shopping2 = {
"nabial": ["ser","mleko"],
"kiosk": ["gazeta","bilety"]
}
Ilosc = 0

linia = "Lista zakupów2\n"

for shop in shopping2:
    shopping2[shop] = [product.capitalize() for product in shopping2[shop]]   
    
    linia += f"Idę do {shop.capitalize()} i kupuję tam {shopping2[shop]}\n"
    Ilosc += (len(shopping2[shop]))

linia += (f"W sumie kupuję {Ilosc} produktów")

print(linia)