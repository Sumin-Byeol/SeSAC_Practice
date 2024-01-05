class Pikachu:
    def __init__(self, name="그냥 피카츄"):
        self.name = name
        self.health =100
        self.level = 1
        self.attack_power = 10

    def __repr__(self):
        return "pika pika!"
    
    def attack(self, target = None):
        if target is None:
            print(f"{self.name}는 공격할 상대가 필요해요 ㅜㅜ")
            return
        
        damage = self.attack_power * self.level
        print(f"{self.name}가 {target.name}을 {damage}의 데미지로 공격했다!")
        target.be_attacked(damage, self)

    def be_attacked(self, damage, attacker):
        self.health -= damage
        print(f"{self.name} 는 {damage}의 데미지만큼 {attacker.name}에게 상처를 입었다!")
        if self.health <= 0:
            print(f"{self.name}는 더 이상 싸울 수 없다!")
            self.health = 0
    def heal(self, amount=10):
        self.health += amount
        if self.health > 100:
            self.health = 100
            print(f"{self.name}가 체력을 {amount} 만큼 회복했다!")

Gold_pikachu_ = Pikachu(
    name="골드 피카츄"
)
Silver_pikachu = Pikachu(
    name="실버 피카츄"
)
print(Gold_pikachu_)
print(Silver_pikachu)

