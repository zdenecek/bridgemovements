north = 0
east = 2
south = 1
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
    pad = lambda any: str(any).rjust(2)
    
    rotate = lambda num, step: rotate_player(num, step, tables)
    rotate_t = lambda num, step: rotate_table(num, step, tables)

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
        rounds[round] = [[rotate(player, 1) for  player in table] for table in rounds[round-1]]

    for table in range(tables):
        print('\n\n')
        print(f'Individuál - {tables * 4} hráčů - {tables * 3} rozdání (Rainbow parallel)')
        print('\n')
        print(f'Stůl číslo {table + 1}')
        print('\n')
        print('Kolo   |   N (-->) |   S (-->) |   E (-->) |   W (-->) |   Rozdání')
        print('=======================================================================')

        change = {
            key: pad(rotate_t(table + 1, table_rotations[key])) for key in [north,south,east,west]
        }

        for round in rounds:
            data = rounds[round][table]
            last = True if round == len(rounds) else False
            print(
                f'{pad(round * 3 + 1)}     |  {pad(data[north])} ( ..) |  {pad(data[south])} ( .E) |  {pad(data[east])} ( .S) |  {pad(data[west])} ( ..) |  {pad(round*3 + 1)}')
            print(
                f'{pad(round * 3 + 2)}     |  {pad(data[north])} ( ..) |  {pad(data[east])} ( .W) |  {pad(data[south])} ( ..) |  {pad(data[west])} ( .S) |  {pad(round*3 + 2)} ')
            print(
                f'{pad(round * 3 + 3)}     ' +
                    f'|  {pad(data[north])} ({"  " if last else change[north]}N) ' +
                    f'|  {pad(data[west])} ({"  " if last else change[west]}W) ' +
                    f'|  {pad(data[south])} ({"  " if last else change[south]}S) ' +
                    f'|  {pad(data[east])} ({"  " if last else change[east]}E) ' +
                    f'|  {pad(round*3 + 3)}')
            print(
                f'{pad("")}     |  {pad("")}       |  {pad("")}       |  {pad("")}       |  {pad("")}       |  {pad("")}')

rainbow_paralel_boards(7)