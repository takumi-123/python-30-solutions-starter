try:
    user_input = input("整数を入力してください")
    number = int(user_input)
    print(f"入力された数値は{number}です")
except ValueError:
    print("入力された値を整数に変換できません。整数を入力してください。")

#2
while True:
    try:
        users_input = input("整数を入力してください")
        numbers = int(users_input)
        print(f"あなたの入力した整数は{numbers}です")
        break
    except ValueError:
        print("入力された値を整数に変換できません。整数を入力してください。") 
               