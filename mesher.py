class Mesh:
  node_count = (int) (0.0)
  nodes = [(0.0,0.0,0.0)]
  def __init__(self, largo, delta):
    elem_xy = largo/delta
    self.node_count = (int)(elem_xy)
      # self.r = realpart
      # self.i = imagpart
  def __init__(self):
    self.data = []
    
  def alloc_nodes(nod_count):
    for i in range (nod_count-1):
      nodes.append((0.,0.,0.))
      
  def printRadioss(self,fname):
    f = open(fname,"w+")
    for i in range (self.node_count):
      f.write("%.6e, %.6e\n" % (self.nodes[i][0],self.nodes[i][1]))

class Plane_Mesh(Mesh):
  def __init__(self, largo, delta):
    elem_xy = largo/delta
    self.node_count = (int)(elem_xy)
    nc = (int)(elem_xy+1)
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
  