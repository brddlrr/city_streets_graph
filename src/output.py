def output_to_csv(nodes, ways):
    with open("../result/nodes.csv", 'w') as f:
        f.write("id,osmID,X,Y\n")
        for i in nodes:
            string = ",".join((str(i.id), str(i.ndID), str(i.X), str(i.Y)))
            f.write(string+"\n")
    with open("../result/graph.csv", 'w') as f:
        f.write("fromID,toID\n")
        for i in ways:
            string = ",".join((str(i[0]), str(i[1])))
            f.write(string+"\n")
