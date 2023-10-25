def Pascal_triangle(k):
    top = [[1],[1,1]]
    for i in range(2,k):
        pre = top[i-1]
        lines = [1]
        for j in range(i-1):
            lines.append(pre[j]+pre[j+1])
        lines.append(1)
        top.append(lines)
    print(lines)
Pascal_triangle(100)
Pascal_triangle(200)