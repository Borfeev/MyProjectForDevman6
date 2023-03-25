def main():
    my_str = input("Введите пароль: ")
    print(my_str)
    print(len(my_str))
    if len(my_str) < 12:
        print("Короткий")
    if len(my_str) > 12:
        print("Длинный")


if __name__ == "__main__":
    main()
