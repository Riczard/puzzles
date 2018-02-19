def import_data():    
    spread_sheet = []
    with open("spreadsheet.txt", 'r') as f:
        for line in f.readlines():
            spread_sheet.append(line.strip())
    for i in range(len(spread_sheet)):
        spread_sheet[i] = spread_sheet[i].split("\t")
    return spread_sheet


def change_type_to_int(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    return data


def diff_min_max(data):
    return max(data) - min(data)


def main():
    check_sum = 0
    spread_sheet = import_data()
    spread_sheet = change_type_to_int(spread_sheet)
    for i in range(len(spread_sheet)):
        check_sum += diff_min_max(spread_sheet[i])
    print(check_sum)

if __name__ == "__main__":
    main()