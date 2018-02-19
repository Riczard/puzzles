def import_sequence():
    with open("sequence_digits.txt", "r") as f:
        digits = list(f.read())
    del digits[len(digits)-1]
    return digits


def main():
    sum_digits = 0
    sequence_digits = import_sequence()
    for i in range(len(sequence_digits)):
        if sequence_digits[i-1] == sequence_digits[i]:
            sum_digits += int(sequence_digits[i])
    print(sum_digits)

if __name__ == "__main__":
    main()
