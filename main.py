import random
from cats import (
    Lelik,
    Misa,
    Busya,
    Musya,
    Loaf,
    Lelik_Lelikovich,
    Kimrik,
    Minuet,
)
from battle import fight,victory
team_1=[]
team_2=[]
pull=[
    Lelik(),
      Misa(),
      Busya(),
      Musya(),
      Loaf(),
      Lelik_Lelikovich(),
      Kimrik(),
      Minuet()
]
for kit in pull:
    while len(team_1)!=4:
        random_kit=random.choice(pull)
        team_1.append(random_kit)
        pull.remove(random_kit)
    while len(team_2) != 4:
        random_kit = random.choice(pull)
        team_2.append(random_kit)
        pull.remove(random_kit)

fight(team_1,team_2)
victory(team_1,team_2)










