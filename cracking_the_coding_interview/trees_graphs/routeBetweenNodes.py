# Route Between Nodes: Given a directed graph, design an algorithm to find out whether 
# there is a route between two nodes.
# so bfs is a better solution for this problem
from graphAdjacencyList import Directed_Graph
from collections import deque


def solution(source,destination):
	if(source == None or destination == None):
		print("The source or destination is empty")
		return
	queue = deque([])
	# print()
	queue.append(obj.graph[source])
	while(len(queue) != 0):
		currentNode = queue.popleft()
		# print(currentNode.vertex)
		if(currentNode.vertex == destination):
			return True
		# print(queue)
		if(obj.graph[currentNode.vertex] != None):
			queue.append(obj.graph[currentNode.vertex])
	return False

obj = Directed_Graph(5)
obj.add_edge(1,2)
obj.add_edge(2,4)
obj.add_edge(2,3)
obj.add_edge(4,3)
# obj.print_graph()
print(solution(1,2))
print(solution(2,1))
print(solution(4,1))
print(solution(1,3))