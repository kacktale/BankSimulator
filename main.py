import os
import json
from datetime import datetime

def MainMenu():
    print("========================\n은행 계좌 관리 프로그램\n========================\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 거래 내역 조회\n5. 종료")
    while True:
        try:
            nextAct = int(input())
            if nextAct in menu :
                menu[nextAct]()
            elif nextAct == 5:
                break
            else:
                print("1~5 사이의 숫자를 입력하세요")

        except ValueError:
            print("숫자를 입력해주세요.\n")
    

def Deposit():
    try: value = int(input("입금 금액 : "))
    except ValueError: print("숫자를 입력해주세요.\n")
    if(value > 0) :
        data["user1"]["current_Balance"] += value
        print(f"{value}원이 입금되었습니다.")
        UpdateTrade(value,"입금")

    else:
        print(f"{value}원은 입금할수 없습니다.")

def Withdrawal():
    try: value = int(input("출금 금액 : "))
    except ValueError: print("숫자를 입력해주세요.\n")
    if(value <= 0):
        print("이 금액으로 출금할 수 없습니다")
        return
    if(data["user1"]["current_Balance"] > value) :
        data["user1"]["current_Balance"] -= value
        print(f"{value}원이 출금되었습니다.")
        UpdateTrade(value,"출금")
    else:
        print(f"현재 잔액이 없습니다.")

def ShowBalance():
    print(f"현재 잔액\n{data['user1']['current_Balance']:,}원")

def ShowTrade():
    if(len(data["user1"]["trade_history"]) == 0):
        print("거래 내역이 없습니다.")
    else:
        for i in data["user1"]["trade_history"]:
            print(f"[{i['time']}]")
            print(f"{i['type']}")
            print(f"{i['value']:,}원")
            print("----------------------------")

def UpdateTrade(value,type):
    resent_trade = dict()

    resent_trade["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resent_trade["type"] = type
    resent_trade["value"] = value
    data["user1"]["trade_history"].append(resent_trade)

    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent="\t", ensure_ascii=False)

menu = {
    1: Deposit,
    2: Withdrawal,
    3: ShowBalance,
    4: ShowTrade
}

user_info = dict()

user1 = dict()

user1["current_Balance"] = int()
user_info["user1"] = user1

trade_history = []
user_info["user1"]["trade_history"] = trade_history

if not os.path.exists("data.json"):
    with open("data.json", "w", encoding="utf-8") as make_file:
        json.dump(user_info, make_file, indent="\t", ensure_ascii=False)

try:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
        with open("data.json", "w", encoding="utf-8") as make_file:
            json.dump(user_info, make_file, indent="\t", ensure_ascii=False)

MainMenu()
