# Переведём код из Java в Python и сократим код от повторяющихся условий благодаря циклу
def Method(*conditions):
    x = [1]

    if conditions[0]:
        x.append(2)
        if conditions[1]:
            x.append(3)
        x.append(4)
        if conditions[2]:
            x.append(5)

    if conditions[3]:
        x.append(6)

    for i in range(4, 40):
        if conditions[i]:
            x.append(i + 3)

    print(x)