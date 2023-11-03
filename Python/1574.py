t = int(input())
posFinal = []
for i in range(t):
    n = int(input())
    ordem = []
    pos = 0
    for i in range(n):
        tarefa = input()
        ordem.append(tarefa)
        while tarefa != 'LEFT' and tarefa != 'RIGHT':
            index = int(tarefa[8:]) - 1
            tarefa = ordem[index]
        if tarefa == 'LEFT':
            pos -= 1
        elif tarefa == 'RIGHT':
            pos += 1
    posFinal.append(pos)
for i in posFinal:
    print(i)