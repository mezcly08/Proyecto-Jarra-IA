from Node import Node
from BreadthFirstSearch import BreadthFirstSearch
from Jarra import Jarra



inicial = Node((0, 0))
final = Node((2, 0))

jarra = Jarra(inicial, final)

bfs = BreadthFirstSearch(jarra)
solution = bfs.run()
print(solution)






