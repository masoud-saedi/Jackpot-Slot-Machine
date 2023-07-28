import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 5
COLS = 3

symbol_count = {
    "\U0001F34E": 2,
    "\U0001F350": 4,
    "\U0001F353": 6,
    "\U0001F349": 8
}

symbol_value = {
    "\U0001F34E": 5,
    "\U0001F350": 4,
    "\U0001F353": 3,
    "\U0001F349": 2
}


def check_winnings(columns, lines, bet, values):  # values is the symbol_values dictionary
    winnings = 0
    winning_lines = []  # to return which line the user won
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # else statement in for loop. if you break, else won't run, if not break, else statement will execute
            winnings += values[symbol] * bet
            winning_lines.append(line+1)  # plus 1 because line is the index number

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # bringing all the values from the dictionary to a list
    for symbol, symbol_count in symbols.items():  # .items() gives you both the key and value associated with dictionary  / symbol  -> key, symbol_count -> value, symbols -> dictionary
        for _ in range(symbol_count):  # just want to iterate in list, use _ (anonymous variable) to not have unused vrbl
            all_symbols.append(symbol)

    columns = []  # creating a random list of values from 'all_symbols' list for our columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # creating a copy of all_symbols list to not affect it
        for _ in range(rows):
            value = random.choice(current_symbols)  # picking a random value from the copied dictionary
            current_symbols.remove(value)  # remove that value, so we won't have more than what we have of a value
            column.append(value)  # creating the columns one by one

        columns.append(column)

    return columns


def print_slot_machine(columns):  # show the result of spinning the slot machine to the use
    for row in range(len(columns[0])):  # 0 because at least we have one column
        for i, column in enumerate(columns):  # enumerate because we have a condition for each item's index, i -> index, column -> the item in the list
            if i != len(columns) - 1:  # -1 because we want to print "|" NOT after the last iteration
                print(column[row], end="|")  # default: end=\n (going to a new line)
            else:
                print(column[row], end="")
        print()  # going to a new line


def deposit():
    while True:
        amount = input("How much would you like to deposit? €")
        if amount.isdigit():  # method to use on strings to see if it's valid number. -9 is not!
            amount = int(amount)  # do it after isdigit() method, we're sure user already input a valid number
            if amount > 0:
                break  # break out the while True loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? (€{MIN_BET}-€{MAX_BET})? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between €{MIN_BET} and €{MAX_BET}")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, your current balance is: €{balance}")
        else:
            break
    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won €{winnings}.")
    print(f"You won on lines:", *winning_lines)  # winning_lines is a list, so *before that iterates in the list and print all the list elements
    return winnings - total_bet


def main():  # define the main function here, if we ask user you want to play again, we will re-run the program
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}")
        answer = input("Press enter to play (Q to quit).").lower()
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with €{balance}.")


main()

