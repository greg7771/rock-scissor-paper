import random
logo = """
⡤⣤⠤⠒⠒⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠔⠚⠉⡉⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠋⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠜⡜⠡⢄⠀⠀⠠⠬⠆⣀⣀⡀⠀⠀⠀⠀⠀⠀⡎⡴⣁⣀⠀⠀⠈⠑⠚⠒⢦⡀⠀⠀⠀⠀⠀⠀⡸⠀⣸⠠⠤⠄⠊⠉⢱⠀⠀⠀
⠀⠸⣰⠩⡑⠢⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀⠀⢸⢰⠁⠤⣀⣀⠀⠀⠀⣀⣀⣴⠁⠀⠀⠀⠀⡐⡒⠀⡀⠀⠀⠀⡠⠴⠭⠤⢀⠀⠀
⠀⠀⠀⢆⠈⠀⠀⠀⠀⠀⠐⠲⢶⡒⠐⠃⠀⠀⠀⠘⠾⡄⠓⠶⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀⠀⠀⡇⠇⣷⡖⠀⠀⠀⣀⡀⠠⠤⠬⠂⠀
⠀⠀⠀⠈⠓⢄⡀⠀⢐⡢⢄⡀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠐⠒⡲⠊⠀⠀⠀⠀⠀⠘⠚⢄⡀⠀⠀⠀⠀⠀⠉⢲⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠈⠑⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠈⠉⠉⠀⠀
"""

print("게임은 간단합니다.\n")
print("게임의 규칙을 설명드리겠습니다.\n")
print(f"{logo}\n")
print("사진과 같이 가위는 1번 바위는 2번 보는 3번 입니다.\n")

win = 0
lose = 0
draw = 0
round = 1

want_round = int(input("가위바위보를 몇번 하고 싶나요? > ")) + 1


while round < want_round :
    ask = int(input("\n가위 바위 보 중 어떤것을 내시겠습니까?[1:가위, 2:바위, 3:보] > "))
    rock_scissor_paper = random.randint(1,4)
    if ask == rock_scissor_paper:
        print(f"{round}번째 회차입니다.\n")
        print("비겼습니다!")
        if rock_scissor_paper == 1:
            print("컴퓨터는 가위를 냈습니다!\n")
        if rock_scissor_paper == 2:
            print("컴퓨터는 바위를 냈습니다.\n")
        if rock_scissor_paper == 3:
            print("컴퓨터는 보를 냈습니다.\n")
        round += 1
        draw += 1
        continue

    if ask == 1 and rock_scissor_paper == 2:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터는 바위를 내서 졌습니다!\n")
        round += 1
        lose += 1
        print(f"지금까지 {lose}회 졌습니다!\n")
        continue

    if ask == 1 and rock_scissor_paper == 3:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터가 보를 내서 이겼습니다!\n")
        round += 1
        win += 1
        print(f"지금까지 {win}회 이겼습니다!\n")
        continue

    if ask == 2 and rock_scissor_paper == 1:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터가 가위를 내서 이겼습니다!\n")
        round += 1
        win += 1
        print(f"지금까지 {win}회 이겼습니다!\n")
        continue
    if ask == 2 and rock_scissor_paper == 3:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터가 보를 내서 졌습니다!\n")
        round += 1
        lose += 1
        print(f"지금까지 {lose}회 졌습니다!\n")
        continue

    if ask == 3 and rock_scissor_paper == 1:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터가 가위를 내서 졌습니다!\n")
        round += 1
        lose += 1
        print(f"지금까지 {lose}회 졌습니다!\n")
        continue

    if ask == 3 and rock_scissor_paper == 2:
        print(f"{round}번째 회차입니다.\n")
        print("컴퓨터가 주먹을 내서 이겼습니다!\n")
        round += 1
        win += 1
        print(f"지금까지 {win}회 이겼습니다!\n")
        continue

print(f"총 {round - 1}회의 게임이 끝났습니다\n")
print(f"{round -1}회의 게임동안 총 {win}회 이기고 {lose}회 졌습니다. 비긴횟수는 {draw}회 입니다.")    