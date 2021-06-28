def grid(tic):
  l = []
  for i in range(5):
    x = []
    for j in range(9):
      if (i == 0 or i == 4):
        print("-", end='')
      else:
        if (j == 0 or j == 8):
          print('|', end='')
        elif (j % 2 == 0):
          print(tic[(j // 2) + (3 * (i - 1)) - 1], end='')
          x += tic[(j // 2) + (3 * (i - 1)) - 1]
        else:
          print(" ", end='')
    l += [x]
    print()

def check(tic):
    counter= 0
    char = ''
    xno = tic.count('X')
    ono = tic.count('O')
    _no = tic.count(' ')
    l=[list(tic[:3]),list(tic[3:6]), list(tic[6:])]
    for i in range(0,3):
        res =[sub[i] for sub in l if len(sub)>0]
        if res == ['X']*3 or l[i] == ['X']*3:
            char = 'X'
            counter += 1
        elif res == ['O']*3 or l[i] == ['O']*3:
            char = "O"
            counter += 1
    diag1 = [l[i][i] for i in range(0,3)]
    diag2 = [l[i][2-i] for i in range(0,3)]
    if diag1 == ['X']*3 or diag2 == ['X']*3:
        char = 'X'
        counter += 1
    elif diag1 == ['O']*3 or diag2 == ['O']*3:
        char = 'O'
        counter += 1
    if counter == 2 or abs(xno-ono) > 1 :
        return ("Impossible")
    elif counter == 1:
        return (char+" wins")
    else:
        if _no == 0:
            return ("Draw")
        else:
            return ("Game not finished")


def game(tac, cindex):
    flag = True
    toe = ''
    cstr = 'XO'
    while flag:
        coord = input('Enter the coordinates:').split(" ")
        if coord[0].isnumeric() and coord[1].isnumeric():
            coord = [int(x) for x in coord]
            if 0 < coord[0] < 4 and 0 < coord[1] < 4:
                x = (coord[0]-1)*3 + (coord[1]-1)
                if tac[x] == ' ':
                    toe = tac[:x] + cstr[cindex] + tac[x+1:]
                    flag = False
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    grid(toe)
    if check(toe) == "Game not finished":
        game(toe, cindex+((-1)**cindex))
    else:
        print(check(toe))


basic = ' '*9
grid(basic)
game(basic,0)
