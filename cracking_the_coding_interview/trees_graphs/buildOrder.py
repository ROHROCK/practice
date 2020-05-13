# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies:
# (a, d), (f, b), (b, d), (f, a),(d, c)
# Output: f, e, a, b, d, c
import graphAdjacencyList

def topologicalSort(graphObject,numberOfNode):
	visited = [False] * numberOfNode
	ordering = [0] * numberOfNode
	i = numberOfNode - 1
	state = [-1] * numberOfNode
	stackRec = [False] * numberOfNode

	if(checkLoop(0,graphObject,stackRec,visited)):
		print("Loop exist !")
		return
	else:
		print('No loop detected .. Proceeding with ordering')

	visited = [False] * numberOfNode	
	for at in range(numberOfNode):
		if(visited[at] == False):
			i = dfs(i,at,visited,ordering,graphObject)
	for order in ordering:
		print(mappedIndexToProject[order])
	return ordering

# create states of node to track the node where 1 is is_visiting , 0 is
# visited
def dfs(i,at,visited,ordering,graphObject):
	visited[at] = True
	vertexsConnected = graphObject.getEdges(at)
	if(vertexsConnected != None):
		for vertexConnected in vertexsConnected:
			if(visited[vertexConnected] == False):
				i = dfs(i,vertexConnected,visited,ordering,graphObject)
	ordering[i] = at
	return i - 1

def checkLoop(at,graphObject,stackRec,visited):
	visited[at] = True
	stackRec[at] = True

	vertexsConnected = graphObject.getEdges(at)
	if(vertexsConnected != None):
		for vertexConnected in vertexsConnected:
			if(visited[vertexConnected] == False):
				if checkLoop(vertexConnected,graphObject,stackRec,visited):
					return True
			elif stackRec[vertexConnected] == True:
				return True

	stackRec[at] = False
	return False

if __name__ == '__main__':
	# input for cyclic directed graph
	# standard_input = "a b c \n3 \n a b \nb c \nc b"
	# input for directed acyclic graph
	standard_input = "a b c d e f \n5 \na d \nf b \nb d \nf a \nd c"
	listOfProjects = list(input().split()) # a b c d e : name of project
	directedGraph = graphAdjacencyList.Directed_Graph(len(listOfProjects))

	# map the name of project to 0-len(listOfProject)
	index = [i for i in range(len(listOfProjects))]
	mappedProjects = dict(zip(listOfProjects,index))
	mappedIndexToProject = dict(zip(index,listOfProjects))
	for keys,value in mappedProjects.items():
		print("{0}->{1}".format(keys,value))
	numberOfDependencies = int(input())
	
	# take dependencies a b , where b is depended on a
	for _ in range(numberOfDependencies):
		source,destination = input().split()
		directedGraph.add_edge(mappedProjects[source],mappedProjects[destination])
	topologicalSort(directedGraph,len(listOfProjects))