from math import *

class Vector:
  def __init__(self, *components):
      self.components = components
  def __mul__(self, other):
    components = []
    if isinstance(other, Vector):
      # if (len(self.components)!=len(other.components)):
        # print ("Different length size")
      for i in range (len(self.components)):
        components.append(self.components[i] * other.components[i])
    else:
      components = (other * x for x in self.components)
    return Vector(*components)
  # addition is normally a binary operation between self and other object
  # def __add__(self, other):
    # if isinstance(other, Vector):
      # new_vec = Vector()
      # new_vec.X = self.X + other.X
      # new_vec.Y = self.X + other.Y
      # return new_vec
    # else:
      # raise TypeError("value must be a vector.")
  # def __add__(self, other):
    # added =[]
    # for i in range(len(self.components)):
      # #added = tuple( a + b for a, b in zip(self, other) )
      # added.append(self.components[i] + other.components[i])
      # return Vector(*added)
  def __add__(self, other):
    if isinstance(other, Vector):
    # other.args is the correct analog of self.args
      a = [arg1 + arg2 for arg1, arg2 in zip(self.components, other.components)]
    return self.__class__(*a)
  def __repr__(self):
      return str(self.components)
      
  # # __repr__ and __str__ must return string
  # def __repr__(self):
    # # return str(self.components)
    # # return f"Vector{self.components}"
    # return str(self.components)

  def __str__(self):
    # return str(self.components)
    return f"Vector{self.components}"
    # return str(self.components)
    
# def __add__(self, other):
  # if isinstance(other, Vector):
    # new_vec = Vector()
    # new_vec.X = self.X + other.X
    # new_vec.Y = self.X + other.Y
    # return new_vec
  # else:
    # raise TypeError("value must be a vector.")
    
class Node(Vector):
  def __init__(self, id, *components):
    self.components = components
    self.id = id
        
class Mesh:
  node_count = (int) (0.0)
  elem_count = (int) (0.0)
  nodes = []
  elnod = []
  ini_node_id = 0 
  # elnod = [(1,2,3,4)]
  def __init__(self, largo, delta, ininode):
    elem_xy = largo/delta
    self.node_count = (int)(elem_xy)
      # self.r = realpart
      # self.i = imagpart
    ini_node_id = ininode
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
      line = self.writeIntField(i+1,10)
      for d in range (3):
        line = line + self.writeFloatField(self.nodes[i][d],20,6) 
      # f.write("%.6e, %.6e\n" % (self.nodes[i][0],self.nodes[i][1]))
      f.write(line + '\n')
    f.write('/SHELL/' + str(self.id) + '\n')
    for i in range (self.elem_count):
      line = self.writeIntField(i+1,10)
      for d in range (4):
        line = line + self.writeIntField(self.elnod[i][d],10)
      f.write(line + '\n')

class Plane_Mesh(Mesh):
  def __init__(self, id, largo, delta):
    self.id = id
    elem_xy = (int)(largo/delta)
    nc = (int)(elem_xy+1)
    self.node_count = nc * nc
    self.elem_count = (int)((elem_xy)*(elem_xy))
    print ('Nodes Count: ' + str(self.node_count))
    print ('Elem Count: ' + str(self.node_count))
    y = 0.0
    for j in range (nc):
      x = 0.0
      for i in range (nc):
        self.nodes.append((x,y,0.))
        x = x + delta
      y = y + delta
      
    for ey in range (elem_xy):    
      for ex in range (elem_xy):   
        self.elnod.append(((elem_xy+1)*ey+ex+1,(elem_xy+1)*ey + ex+2,(elem_xy+1)*(ey+1)+ex+2,(elem_xy+1)*(ey+1)+ex+1))
                    # elem%elnod(i,:)=[(nel(1)+1)*ey + ex+1,(nel(1)+1)*ey + ex+2,(nel(1)+1)*(ey+1)+ex+2,(nel(1)+1)*(ey+1)+ex+1]         
              # print *, "Element ", i , "Elnod", elem%elnod(i,:) 
    # print(self.elnod)

#Based on: https://github.com/caosdoar/spheres/blob/master/src/spheres.cpp 
#https://medium.com/@oscarsc/four-ways-to-create-a-mesh-for-a-sphere-d7956b825db4
class Sphere_Mesh(Mesh):
 
  def __init__(self, id, radius, divisions, ininode):
    self.id = id
    ini_node_id = ininode
    CubeToSphere_origins = [Vector(-1.0, -1.0, -1.0),
    Vector(1.0, -1.0, -1.0),
    Vector(1.0, -1.0, 1.0),
    Vector(-1.0, -1.0, 1.0),
    Vector(-1.0, 1.0, -1.0),
    Vector(-1.0, -1.0, 1.0)]
    CubeToSphere_rights = [
    Vector(2.0, 0.0, 0.0),
    Vector(0.0, 0.0, 2.0),
    Vector(-2.0, 0.0, 0.0),
    Vector(0.0, 0.0, -2.0),
    Vector(2.0, 0.0, 0.0),
    Vector(2.0, 0.0, 0.0)]
    CubeToSphere_ups = [
		Vector(0.0, 2.0, 0.0),
		Vector(0.0, 2.0, 0.0),
		Vector(0.0, 2.0, 0.0),
		Vector(0.0, 2.0, 0.0),
		Vector(0.0, 0.0, 2.0),
		Vector(0.0, 0.0, -2.0) ]
    step = 1.0 / divisions
    self.node_count = 1
    step3 = Vector(step, step, step)

    right = CubeToSphere_rights[0]
    # right = Vector(0)
    # print (right)
    # print (step3)
    test = Vector (0.,0.,0.)
    n = 0
    for face in range (6):
      origin = CubeToSphere_origins[face]
      right = CubeToSphere_rights[face]
      # print (right)
      up = CubeToSphere_ups[face]
      for j in range (divisions+1):
        j3 = Vector(j,j,j)
        for i in range (divisions+1):
          i3 = Vector(i,i,i)
          # print ("right ")
          # print (right)
          # print ("origin ")
          # print (origin)
          # print ("right * origin ")

          # test = right * origin  
          # print (test)
          # test = right + up  
          # print (test)
          # const Vector3 p = origin + step3 * (i3 * right + j3 * up);
          p = origin + ( step3 * (right * i3 + up *j3 )  )
          p2 = p * p
          # rx = sqrt(1.0 - 0.5 * (p2.y + p2.z) + p2.y*p2.z/3.0)
          # ry = sqrt(1.0 - 0.5 * (p2.z + p2.x) + p2.z*p2.x/3.0)
          # rz = sqrt(1.0 - 0.5 * (p2.x + p2.y) + p2.x*p2.y/3.0)
          rx = sqrt(1.0 - 0.5 * (p2.components[1] + p2.components[2]) + p2.components[1]*p2.components[2]/3.0)
          ry = sqrt(1.0 - 0.5 * (p2.components[2] + p2.components[0]) + p2.components[2]*p2.components[0]/3.0)
          rz = sqrt(1.0 - 0.5 * (p2.components[0] + p2.components[1]) + p2.components[0]*p2.components[1]/3.0)
          print ("rx ry rz", (rx,ry,rz), "\n")
				# const Vector3 n
				# (
					# p.x * std::sqrt(1.0 - 0.5 * (p2.y + p2.z) + p2.y*p2.z / 3.0),
					# p.y * std::sqrt(1.0 - 0.5 * (p2.z + p2.x) + p2.z*p2.x / 3.0),
					# p.z * std::sqrt(1.0 - 0.5 * (p2.x + p2.y) + p2.x*p2.y / 3.0)
				# );
				# mesh.vertices.emplace_back(n);
          self.nodes.append((rx,ry,rz))
          n = n +1
    print ("generated: %d", n , " nodes      ")
    self.node_count = n
      # print (origin)
    
    e = 0
    for ey in range (divisions):
      for ex in range (divisions):
        # elem%elnod(i,:)=[(nel(1)+1)*ey + ex+1,(nel(1)+1)*ey + ex+2,(nel(1)+1)*(ey+1)+ex+2,(nel(1)+1)*(ey+1)+ex+1]  
        self.elnod.append(((divisions+1)*ey+ex+1,(divisions+1)*ey + ex+2,(divisions+1)*(ey+1)+ex+2,(divisions+1)*(ey+1)+ex+1))      
        e = e + 1
    self.elem_count = e
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

class Part:
  def __init__(self, mid):
    id = mid
  def AppendMesh(m):
    if (not isinstance(m, Mesh)):
      print ("part is not a mesh")
    else:
      self.mesh.append(m)
      
class DSIFModel:
  def __init__(self):
    self.part_count = 0
    self.part = []
  
  def AppendPart(p):
    if (not isinstance(p, Part)):
      print ("ERROR: added opbject is not a part ")
    else:
      self.part.append(p)
      self.part_count = self.part_count + 1
      
  def printRadioss(self,fname):
    f = open(fname,"w+")
    f.write("#RADIOSS STARTER\n")
    f.write("/BEGIN\n")
    f.write("test                                                        \n")                   
    f.write("      2019         0 \n")
    f.write("                  kg                   m                   s\n")
    f.write("                  kg                   m                   s\n")
    f.write('/NODE\n')
    for i in range (self.node_count):
      line = self.writeIntField(i+1,10)
      for d in range (3):
        line = line + self.writeFloatField(self.nodes[i][d],20,6) 
    f.write(line + '\n')
    
    for p in range(part_count):
      f.write('/SHELL/' + str(self.id) + '\n')
      for i in range (self.elem_count):
        line = self.writeIntField(i+1,10)
        for d in range (4):
          line = line + self.writeIntField(self.elnod[i][d],10)
        f.write(line + '\n')