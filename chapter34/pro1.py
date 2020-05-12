class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ap = ability_power

    def tibbers(self):
        damage = self.ap * 0.65 + 400
        print('티버 : 피해량 {0}'.format(damage))

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()