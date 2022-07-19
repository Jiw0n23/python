baby = {"말":"망아지",
            "개":"강아지",
            "소":"송아지",
            "닭":"병아리",
            "꿩":"꺼병이",
            "매":"초고리",
}

while (True) :
    mybaby = input(str(list(baby.keys())) + "의 새끼 이름은?")
    if mybaby in baby :
        print("<%s> 의 새끼 이름은 <%s>입니다." % (mybaby, baby.get(mybaby))) 
    elif mybaby == "끝" :
        break
    else :
        print("그런 동물은 없습니다. 확인해 보세요.")