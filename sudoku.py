import random

base = 3

sudoku = []

setfiller = set([i for i in range(1, (base*base)+1)])
rows = {}
columns = {}

box = []

for i in range(base):
    check = []
    for j in range(base):
        check.append(set())
    box.append(check)

for i in range(base*base):
    rows[i] = set()
    columns[i] = set()

for i in range(base*base):
    choice = []
    for j in range(base*base):

        if random.random() < 0.3: 
            consider = setfiller - box[i//base][j//base] - rows[i] - columns[j]
            
            if len(consider) != 0:
                number = random.choice(list(consider))
                box[i//base][j//base].add(number)
                rows[i].add(number)
                columns[j].add(number)
                choice.append(number)
            else:
                choice.append(' ')
        else:
            choice.append(' ')
        
    sudoku.append(choice)
    print(sudoku[i])

