inputFileName = sys.argv[1]

with open(inputFileName) as inputFile:
    with open('results.txt', 'a+') as outputFile:
        line = inputFile.readline()

        edgesList = list()

        while line:

            newEdgeInfo = line.split()

            newEdgeBeginning = int(newEdgeInfo[0])

            newEdgeEnd = int(newEdgeInfo[1])

            newEdgesList = [newEdgeBeginning, newEdgeEnd]

            edgesList.append(newEdgesList)

            line = inputFile.readline()

        inputGraph = dict()

        bipartiteFromGraphSet = list()

        bipartiteToGraphSet = list()

        bipartiteEdgesList = list()

        for [key, value] in edgesList:

            if not(key in inputGraph.keys()):

                inputGraph[key] = list()

            inputGraph[key].append(value)

            if not(value in inputGraph.keys()):

                inputGraph[value] = list()
