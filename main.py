import command_center


def main():
    while True:
        print("Enter 3 to display help menu")
        user_command = input("What would you like to do? ")
        if user_command == "4":
            print("Closing Application")
            break
        print(command_center.command_list(user_command))


if __name__ == "__main__":
    main()
