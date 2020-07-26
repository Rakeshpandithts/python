# Python program to print all paths from a source to destination. 
# ABdominal pain graph
from collections import defaultdict 

#This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		#No. of vertices 
		self.V= vertices 
		
		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	'''A recursive function to print all paths from 'u' to 'd'. 
	visited[] keeps track of vertices in current path. 
	path[] stores actual vertices and path_index is current 
	index in path[]'''
	def printAllPathsUtil(self, u, d, visited, path): 

		# Mark the current node as visited and store in path 
		visited[u]= True
		path.append(u) 

		# If current vertex is same as destination, then print 
		# current path[] 
		if u ==d: 
			print(path) 
		else: 
			# If current vertex is not destination 
			#Recur for all the vertices adjacent to this vertex 
			for i in self.graph[u]: 
				if visited[i]==False: 
					self.printAllPathsUtil(i, d, visited, path) 
					
		# Remove current vertex from path[] and mark it as unvisited 
		path.pop() 
		visited[u]= False


	# Prints all paths from 's' to 'd' 
	def printAllPaths(self,s, d): 

		# Mark all the vertices as not visited 
		visited =[False]*(self.V) 

		# Create an array to store paths 
		path = [] 

		# Call the recursive helper function to print all paths 
		self.printAllPathsUtil(s, d,visited, path) 



# Create a graph given in the above diagram 
g = Graph(16) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 

g.addEdge(1, 3) 
g.addEdge(1, 4)

g.addEdge(2, 3) 
g.addEdge(2, 4)

g.addEdge(3, 5) 
g.addEdge(3, 6) 

g.addEdge(4, 5) 
g.addEdge(4, 6) 

g.addEdge(5, 7) 
g.addEdge(5, 8)

g.addEdge(6, 7) 
g.addEdge(6, 8) 

g.addEdge(7, 9) 
g.addEdge(7, 10) 

g.addEdge(8, 9) 
g.addEdge(8, 10) 

g.addEdge(9, 11) 
g.addEdge(9, 12) 

g.addEdge(10, 11) 
g.addEdge(10, 12) 

g.addEdge(11, 13) 
g.addEdge(11, 14) 

g.addEdge(12, 13) 
g.addEdge(12, 14)

g.addEdge(13, 15) 
# g.addEdge(13, 16)

g.addEdge(14, 15)
# g.addEdge(14, 18) 

# g.addEdge(15, 39) 
# # g.addEdge(15, 18)

# g.addEdge(16, 39) 
# # g.addEdge(16, 32)

# g.addEdge(17, 19) 
# g.addEdge(17, 20) 

# g.addEdge(18, 25) 
# g.addEdge(18, 26)

# g.addEdge(19, 21) 
# g.addEdge(19, 22)

# g.addEdge(20, 21) 
# g.addEdge(20, 22)

# g.addEdge(21, 23) 
# g.addEdge(21, 24)

# g.addEdge(22, 23) 
# g.addEdge(22, 24)

# g.addEdge(23, 25) 
# g.addEdge(23, 26)

# g.addEdge(24, 25) 
# g.addEdge(24, 26)

# g.addEdge(25, 27) 
# g.addEdge(25, 28) 

# g.addEdge(26, 27) 
# g.addEdge(26, 28) 

# g.addEdge(27, 29) 
# g.addEdge(27, 30) 

# g.addEdge(28, 29) 
# g.addEdge(28, 30) 

# g.addEdge(29, 39) 
# # g.addEdge(29, 32) 

# g.addEdge(30, 39) 
# # g.addEdge(30, 32) 

# g.addEdge(31, 33) 
# g.addEdge(31, 34) 

# g.addEdge(32, 33) 
# g.addEdge(32, 34) 

# g.addEdge(33, 35) 
# g.addEdge(33, 36) 

# g.addEdge(34, 35) 
# g.addEdge(34, 36) 

# g.addEdge(35, 39) 
# # g.addEdge(35, 38) 

# g.addEdge(36, 39) 
# # g.addEdge(36, 38) 

# # g.addEdge(39, 39) 
# # g.addEdge(39, 40) 

# g.addEdge(38, 39) 
# g.addEdge(37, 5) 
# g.addEdge(37, 6) 

# # g.addEdge(33, 41) 
# # g.addEdge(31, 41) 
# # g.addEdge(39, 41) 
# # g.addEdge(40, 41) 
# # g.addEdge(29, 41) 
# # g.addEdge(30, 41) 


s = 0; d = 15
print ("Following are all different paths from %d to %d :" %(s, d)) 
g.printAllPaths(s, d) 
#This code is contributed by Neelam Yadav 
