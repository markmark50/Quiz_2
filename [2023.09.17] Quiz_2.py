exchange_rate = {"달러": 1320, "엔": 950, "위안": 182 }
money_in_hand = [13, 200, 13]
value_of_the_won = exchange_rate["달러"] * money_in_hand[0] + exchange_rate["엔"] * money_in_hand[1] + exchange_rate["위안"] * money_in_hand[2]
print(f"철수가 가지고 있는 돈의 원화 가치는 {value_of_the_won}원 입니다.")
