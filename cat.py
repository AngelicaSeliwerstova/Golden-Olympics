class Cat:
    def __init__(self,damage:int,hp:int,name:str):
        self.damage=damage
        self.name=name
        self.hp=hp
    def feature(self,my_team,enemy_team,runned_team_1,runned_team_2):
        pass
    def atack(self,target:"Cat",my_team,enemy_team,runned_team_1,runned_team_2):
        self.feature(my_team,enemy_team,runned_team_1,runned_team_2)
        target.hp-=self.damage
        return f"Кошечка {self.name} наносит урон кошечке {target} {self.damage}"