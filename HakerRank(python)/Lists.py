if __name__ == '__main__':
    N = int(input())
    l =[]

    for i in range(N):
        x = input().split(" ")
        command = x[0]
        if command == "insert":
            l.insert(int(x[1]),int(x[2]))
        if command == "remove":
            l.remove(int(x[1]))
        if command == "append":
            l.append(int(x[1]))
        if command == "sort":
            l.sort()
        if command == "pop":
                l.pop()
        if command == "reverse":
            l.reverse()
        if command == "print":
            print(l)
