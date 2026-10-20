scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

ghabooliha = []
jame_nomarat = 0
shagerd_aval = ""
bishtarin_nomre = 0


for name in scores:
    nomre = scores[name]
    jame_nomarat += nomre
    
    if nomre > bishtarin_nomre:
        bishtarin_nomre = nomre
        shagerd_aval = name

    if nomre >= 17:
        vaziat = "عالی"
    elif nomre >= 14:
        vaziat = "خوب"
    elif nomre >= 10:
        vaziat = "قبول"
    else:
        vaziat = "مردود"
        
    
    print(f"{name}: {nomre} ← {vaziat}")
    
    
    if nomre >= 10:
        ghabooliha.append(name)


print(f"قبول‌شده‌ها: {ghabooliha}")


miangin = jame_nomarat / len(scores)
print(f"میانگین کلاس: {miangin}")

print(f"نفر اول: {shagerd_aval}")
