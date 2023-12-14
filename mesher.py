class Mesh:
  node_count = (int) (0.0)
  nodes = []
  elnod = []
  # elnod = [(1,2,3,4)]
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

  def writeFloatField(self,number, length, decimals):
    fmt ='%.' + str(decimals) + 'e'
    # print ('format ' + fmt)
    s = fmt % number
    spaces = ''
    for i in range ((int)(length - len(s))):
      spaces = spaces + ' '
    output = spaces + s
    # print (spaces + s)
    return output

  def writeIntField(self,number, length):
    s = '%d' % number
    spaces = ''
    for i in range ((int)(length - len(s))):
      spaces = spaces + ' '
    output = spaces + s
    # print (spaces + s)
    return output
    
  def printRadioss(self,fname):
    f = open(fname,"w+")
    # self.writeFloatField(-100.0,20,6)
    f.write('/NODES\n')
    for i in range (self.node_count):
      line = self.writeIntField(i,10)
      for d in range (3):
        line = line + self.writeFloatField(self.nodes[i][d],20,6) 
      # f.write("%.6e, %.6e\n" % (self.nodes[i][0],self.nodes[i][1]))
      f.write(line + '\n')
      


class Plane_Mesh(Mesh):
  def __init__(self, largo, delta):
    elem_xy = largo/delta
    nc = (int)(elem_xy+1)
    self.node_count = nc * nc
    self.elem_count = (int)(elem_xy)*(elem_xy)
    print ('Nodes Count: ' + str(self.node_count))
    print ('Elem Count: ' + str(self.node_count))
    y = 0.0
    for j in range (nc):
      x = 0.0
      for i in range (nc):
        self.nodes.append((x,y,0.))
        x = x + delta
      y = y + delta
      
    for ey in range (1,(int)(elem_xy)):    
      for ex in range (1,(int)(elem_xy)):   
        self.elnod.append(((elem_xy+1)*ey+ex+1,(elem_xy+1)*ey + ex+2,(elem_xy+1)*(ey+1)+ex+2,(elem_xy+1)*(ey+1)+ex+1))
                    # elem%elnod(i,:)=[(nel(1)+1)*ey + ex+1,(nel(1)+1)*ey + ex+2,(nel(1)+1)*(ey+1)+ex+2,(nel(1)+1)*(ey+1)+ex+1]         
              # print *, "Element ", i , "Elnod", elem%elnod(i,:) 
    # print(self.elnod)
      
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
  