def get_text():
    with open("text.txt", "r") as f:
        a = f.readlines()
        for i in range(len(a)):
            if "\n" in a[i]:
                a[i] = a[i][:-1]
        return a


def analiz(text, user_ans):
    for i in range(len(text)):
        text[i] = text[i].split(" ")

    for i in text:
        if int(i[1]) > user_ans:
            print(f"Time - {i[0]} XXX - {i[1]}")


def printer():
    while True:
        user_ans = input("AAA = ")
        if user_ans.isdigit():
            user_ans = int(user_ans)
            analiz(get_text(), user_ans)
            break
        else:
            print("Введіть тільки числа, не букви!\n")


def main():
    printer()


main()