def draw_rectangle(width, height):
    for i in range(int(height)):
        for j in range(int(width)):
            if (j == 0 or j== width - 1):
                print('|', end="")
                if(j == width - 1):
                    print('\n', end="")
            elif (j != 0 or j != width - 1):
                if (i != 0 and i != height - 1):
                    print(' ', end="")
                if (i == 0 or i == height - 1):
                    print("-", end="")
    return 0
draw_rectangle(10, 3)