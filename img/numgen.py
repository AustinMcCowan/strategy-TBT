# Used just to generate text for img_codex.txt

for i in range(500):
    interval_string = str(i)
    value = ""
    if i < 10:
        value = "00" + interval_string + " ="
    elif i < 100:
        value = "0" + interval_string + " ="
    else:
        value = interval_string + " ="
    print(value)
    
    