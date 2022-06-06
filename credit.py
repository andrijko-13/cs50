card = input(str("Number: "))
card_list = list(card.split(" "))
card_len = len(card)
first_digit = int(card[slice(1)])
two_first_digits = int(card[slice(2)])
if (first_digit == 4) and (card_len >= 13) and (card_len <= 16):
    print("VISA")
elif (two_first_digits >= 51) and (two_first_digits <= 55) and (card_len == 16):
    print("MASTERCARD")
elif (two_first_digits == 34) or (two_first_digits == 37) and (card_len == 15):
    print("AMEX")
else:
    print("INVALID")
