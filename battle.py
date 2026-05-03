def fight(team_1,team_2):
    while team_1 and team_2:
        print(team_1,team_2)
        cat_1=team_1[0]
        cat_2=team_2[0]
        print(cat_1.atack(cat_2))
        print(cat_2.atack(cat_1))
        if cat_1.hp<=0:
            print("котёнок", cat_1.name, "убежал")
            team_1.pop(0)
        if cat_2.hp<=0:
            team_2.pop(0)
            print("котеночек", cat_2.name,"убежал")
def victory(team_1,team_2):
    if len(team_1)==len(team_2)==0:
        print("Победила дружба")
    elif len(team_1)==0:
        print("Победила команда 2")
    elif len(team_2)==0:
        print("Победила команда 1")