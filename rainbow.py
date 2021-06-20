north = 0
south = 1
east = 2
west = 3


def rotate_player(num, step, tables):
    tens = num // 10
    units = num % 10
    new_units = (units + step + tables) % tables
    if new_units == 0:
        new_units = tables
    return new_units + tens * 10


def rotate_table(num, step, tables):
    num = (num + step + tables) % tables
    return tables if num == 0 else num


def rainbow_paralel_boards(tables):
    def pad(any): return str(any).rjust(2)

    def rotate(num, step): return rotate_player(num, step, tables)
    def rotate_t(num, step): return rotate_table(num, step, tables)

    table_rotations = {
        north: -1,
        south: 2,
        east: 3,
        west: 1
    }

    rounds = {
        0:  [[rotate(1 + 10*index + table, (index) * table) for index in range(4)] for table in range(tables)]
    }

    for round in range(1, tables):
        rounds[round] = [[rotate(player, 1) for player in table]
                         for table in rounds[round-1]]

    for table in range(tables):
        print('\n\n')
        print(
            f'Individuál - {tables * 4} hráčů - {tables * 3} rozdání (Rainbow parallel)')
        print('\n')
        print(f'Stůl číslo {table + 1}')
        print('\n')
        print('Kolo   |   N (-->) |   S (-->) |   E (-->) |   W (-->) |   Rozdání')
        print('=======================================================================')

        change = {
            key: pad(rotate_t(table + 1, table_rotations[key])) for key in [north, south, east, west]
        }

        for round in rounds:
            data = rounds[round][table]
            last = True if round == len(rounds) - 1 else False
            print(
                f'{pad(round * 3 + 1)}     |  {pad(data[north])} ( ..) |  {pad(data[south])} ( .E) |  {pad(data[east])} ( .S) |  {pad(data[west])} ( ..) |  {pad(round*3 + 1)}')
            print(
                f'{pad(round * 3 + 2)}     |  {pad(data[north])} ( ..) |  {pad(data[east])} ( .W) |  {pad(data[south])} ( ..) |  {pad(data[west])} ( .S) |  {pad(round*3 + 2)} ')
            print(
                f'{pad(round * 3 + 3)}     ' +
                "".join([f'|  {pad(data[key])} ' + (f'({change[key]}N) ' if not last else "      ") for key in [north, west, south, east]]) +
                f'|  {pad(round*3 + 3)}')
            # print(f'{pad("")}     |' + f'  {pad("")}       |'*4 + f'  {pad("")}')
            print('\n')


rainbow_paralel_boards(7)
