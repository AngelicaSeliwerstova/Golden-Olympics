class Cat:
    def __init__(self,damage:int,hp:int,name:str):
        self.damage=damage
        self.name=name
        self.hp=hp
    def feature(self):
        pass
    def atack(self,target:"Cat"):
        self.feature()
        target.hp-=self.damage
        return f"Кошечка {self.name} наносит урон кошечке {target} {self.damage}"