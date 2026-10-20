sen = int(input("سن خود را وارد کنید: "))
rooz = input("روز هفته را وارد کنید: ")


gheymat = 0


if sen < 5:
    print("ورود رایگان !")
    
elif sen >= 5 and sen <= 12:
    gheymat = 50000
    
elif sen > 60:
    gheymat = 60000
    
else:
    gheymat = 100000


if rooz == "سه‌شنبه" and gheymat > 0:
    gheymat = gheymat - (gheymat * 0.2)  

if gheymat > 0:
    print("قیمت بلیط :", int(gheymat), "تومان")
