class Game:
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power
    def fight(self,enemy_hp,enemy_power):
        final_hp=self.hp-enemy_power
        enemy_final_hp=enemy_hp-self.power
        if final_hp>enemy_final_hp:
            print("我赢了")
        elif final_hp<enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")
class Houyi(Game):
    def __init__(self):
        super().__init__(1000,200)
        self.defense = 100
    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.defense+self.hp - enemy_power
            print("我的最终血量{}".format(self.hp))
            enemy_hp = enemy_hp - self.power
            if enemy_hp<=0:
                print("我赢了")
                break
            elif self.hp <=0:
                print("敌人赢了")
                break
hp=1000
power=300
houyi=Houyi()
houyi.houyi_fight(hp,power)
