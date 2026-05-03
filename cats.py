from cat import Cat
import random
class Musya(Cat):
    def __init__(self):
        super().__init__(5,5,"Musya")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        self.hp += 3
        print("Муся: Да, это муся")
    def __repr__(self):
        return "Musya"
class Lelik(Cat):
    def __init__(self):
        super().__init__(4,6,"Lelik")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        self.damage += 2
        print("Лёлик: Нет, это не Муся ")
    def __repr__(self):
        return "Lelik"
class Kimrik(Cat):
    def __init__(self):
        super().__init__(6,4,"Kimrik")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        self.hp += 2
        print("Получаай!")
    def __repr__(self):
        return "Kimric"
class Minuet(Cat):
    def __init__(self):
        super().__init__(4,4,"Minuet")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        if random.random():
            if len(runned_team_1)!=0:
                kitty=random.choice(runned_team_1)
                my_team.append(kitty)
                print("Minuet призвал товарища",kitty)
        print("Хм!")
    def __repr__(self):
        return "Minuet"
class Lelik_Lelikovich(Cat):
    def __init__(self):
        super().__init__(2,3,"Lelik_Lelikovich")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        for kisa in range(len(enemy_team)):
            enemy_team[kisa].hp-=2
        print("Я стану как папа!")
    def __repr__(self):
        return "Lelik_Lelikovich"
class Busya(Cat):
    def __init__(self):
        super().__init__(2,8,"Busya")
    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        self.hp += 1
        print(" Нет, это Буся!!!")
    def __repr__(self):
        return "Busya"
class Loaf(Cat):
    def __init__(self):
        super().__init__(2,8,"Loaf")

    def feature(self, my_team, enemy_team,runned_team_1,runned_team_2):
        self.hp += 1
        print("Запомните, я кот-батон!")
    def __repr__(self):
        return "loaf"
class Misa(Cat):
    def __init__(self):
        super().__init__(6,4,"Misa")
    def feature(self,my_team,enemy_team,runned_team_1,runned_team_2):
        if 0.8<random.random():
            if Lelik_Lelikovich not in enemy_team:
                my_team.append(Lelik_Lelikovich())
                print("Миса кастует призыв")
        print("Где мой сынишка?")
    def __repr__(self):
        return "Misa"