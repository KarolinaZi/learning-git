shopping = {
"piekarnia": ["chleb","bułki","pączek"],
"warzywniak": ["marchew","seler","rukola"]
}

print("Lista zakupów")

for shop in shopping:  
    print(f"Idę do {shop} i kupuję tam {shopping[shop]}")
