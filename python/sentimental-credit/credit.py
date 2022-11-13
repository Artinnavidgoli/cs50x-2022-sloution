import sys  # importing the system lib


def main():  # defining main
    credit_card = get_card_num()

    validate_card(credit_card)


def get_card_num():  # getting the number of card
    while True:
        card_num = input("Number: ")  # input
        try:
            if len(card_num) > 0 and int(card_num):  # checing the input (the len and checking it's an int)
                break
        except ValueError:
            continue

    return card_num  # returning the number of card


def validate_card(credit_card):  # cheking if the card is valid
    if len(credit_card) < 13 or 16 < len(credit_card):
        print("INVALID")
        sys.exit(0)  # if invalid finish the programm

    even, odd = 0, 0
    card_len = len(credit_card)  # getting the len

    if card_len % 2 == 0:
        for i in range(card_len):
            num = int(credit_card[i])
            if i % 2 == 0:
                multiple = num * 2
                if multiple >= 10:
                    even += multiple // 10
                    even += multiple % 10
                else:
                    even += multiple
            else:
                odd += num
    else:
        for i in range(card_len):
            num = int(credit_card[i])
            if i % 2 != 0:
                multiple = num * 2
                if multiple >= 10:
                    even += multiple // 10
                    even += multiple % 10
                else:
                    even += multiple
            else:
                odd += num

    checksum = (even + odd) % 10

    if checksum == 0:
        first_digit = int(credit_card[0])
        second_digit = int(credit_card[1])
        if first_digit == 3 and second_digit == 4 or second_digit == 7:  # cheking if the card ir for amex
            print("AMEX")
        elif first_digit == 5 and 1 <= second_digit <= 5:  # cheking if the card ir for mastercard
            print("MASTERCARD")
        elif first_digit == 4:  # cheking if the card ir for visa
            print("VISA")
        else:  # if the anwer was not one of the above print invalid
            print("INVALID")


if __name__ == "__main__":
    main()  # calling the main