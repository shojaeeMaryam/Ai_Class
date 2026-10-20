words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "and": "و",
    "is": "است",
    "good": "خوب",
    "book": "کتاب",
    "we": "ما"
}
sentence = "I love python and AI"
shomaresh_tarjome_shode = 0
shomaresh_tarjome_nashode = 0
javab_farsi = ""
for word in sentence.split():
  
    kalame_kuchik = word.lower()

    if kalame_kuchik in words:
        javab_farsi = javab_farsi + words[kalame_kuchik] + " "   

        shomaresh_tarjome_shode = shomaresh_tarjome_shode + 1  

        javab_farsi = javab_farsi + "[" + kalame_kuchik + "] "
        shomaresh_tarjome_nashode = shomaresh_tarjome_nashode + 1 

print("جمله ترجمه شده:")
print(javab_farsi)


print("-----------------")
print("تعداد کلمات ترجمه شده:", shomaresh_tarjome_shode)
print("تعداد کلمات ترجمه نشده:", shomaresh_tarjome_nashode)
