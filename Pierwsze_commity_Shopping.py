shopping = {
"piekarnia": ["chleb","bułki","pączek"],
"warzywniak": ["marchew","seler","rukola"]
}

print("Lista zakupów")

for shop in shopping:
    shopping[shop] = [product.capitalize() for product in shopping[shop]]   
    
    print(f"Idę do {shop.capitalize()} i kupuję tam {shopping[shop]}")
