import sys


def dijkstra(init, dest, graph):
    u=0
    dest=0
    distVal={}
    prev={}
    for n in graph:
        distVal[n]=float('inf')
        prev[n]=None
    distVal.update({init: 0})
    Q=distVal.copy()
    while len(Q)is not 0:
        minW=min(Q.values())
        for key,val in Q.iteritems():
            if(val == minW):
                u=key
                Q.pop(u, None)
                break
        try:
            for v in graph[u]:
                edgeVal=distVal[u]+float(graph[u][v])
                if(edgeVal<distVal[v]):
                    distVal[v]=edgeVal
                    prev[v]=u
        except KeyError as err:
            sys.stderr.write("KeyError: %s" % str(err))
            sys.stderr.write("Node not in dictionary\n")
            exit()
    return distVal,prev


def dijkPath(init, dest, graph):
    distVal, prev=dijkstra(init, dest, graph)
    path=[]
    try:
        totalDist=distVal[dest]

    except KeyError:
        sys.stderr.write('Destination does not exist\r\n')
        exit()

    while 1:
        path.append(dest)
        if(dest==init):
            break
        dest=prev[dest]
    path.reverse()
    totalDist=round(totalDist,4)
    dStr=str(totalDist)
    pathStr='['+(' '.join(map(str,path)))+']'
    print 'distance = '+dStr+'\nroute = '+pathStr


def main():
    initNode = int(sys.argv[1])  #scans startpoint
    destNode = int(sys.argv[2])  # scans destpoint
    matrix = open(sys.argv[3], "rU")  #name of file
    graphFile= matrix.readlines()
    ####### makes dictionary from csv file ########
    graph = {}
    vertIndex=1
    for x in range(0,len(graphFile)):
        horizontalIndex=1
        graph.update({vertIndex: {}})
        if '\n' in graphFile[x]:
            graphFile[x]=graphFile[x].replace('\n','')
        graphX=graphFile[x].split(',')
        for y in range(0,len(graphX)):
            if (float(graphX[y]) != 0):
                graph[vertIndex].update({horizontalIndex: float(graphX[y])})
            horizontalIndex+=1
        if len(graph[vertIndex]) == 0:
            del graph[vertIndex]#graph.pop(graph[vertIndex])

        vertIndex+=1
    dijkPath(initNode,destNode,graph)


if __name__ == '__main__':
    main()