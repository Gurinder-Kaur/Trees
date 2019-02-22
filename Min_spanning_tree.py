l={'A':[('B', 7),('E', 5),('C', 2)],'B':[('A', 7),('D', 3),
      ('E', 10)],'C':[('A', 2),('E', 3),('D', 2),('F', 10)],
      'D':[('B',3),('E',4),('F',7),('C',2)],'E':[('A',5),
      ('B',10),('C',3),('D',4)],'F':[('C',10),('D',7)]}
print(l)


def mst(T):
    vertices=[v for v in T]
    edge_weight=[][]
    for item in T:
        for n in T[item]:
            edge_weight[]
                edge_weight.append(e,n[1])
    return edge_weight

print(mst(l))
