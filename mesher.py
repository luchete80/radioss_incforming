class Mesh:
  node_count = 0
  nodes = [(0.0,0.0,0.0)]
  def __init__(self, largo, delta):
    elem_xy = largo/delta
    self.node_count = elem_xy
      # self.r = realpart
      # self.i = imagpart
  def __init__(self):
    self.data = []
    
  def alloc_nodes(nod_count):
    for i in range (nod_count-1):
      node_count.append((0.,0.,0.))

class Plane_Mesh(Mesh):
  def __init__(self, largo, delta):
    elem_xy = largo/delta
    self.node_count = elem_xy
    nc = (int)((elem_xy+1)*(elem_xy+1) -1)
    for i in range (nc):
      x = 0.0
      for i in range (nc):
        self.nodes.append((0.,0.,0.))
    # print(self.nodes)
      
import numpy as np
def plane_mesh(length, delta, nodos, elnod, mesh):
  num_nodos = 10
  num_elem_xy = ()
  # nodos = np.empty(num_nodos,dtype=object)
  # y = np.arange(30).reshape((10, 3)) 
  nodos.append((1,1,1))
  # print("\nArray y : ", y) 
  # np.reshape(nodos,(20,num_nodos))
  print (nodos)
  print (nodos[0][2])
  