class Vector:
  def __init__(self, *components):
      self.components = components
  def __mul__(self, other):
    # if not isinstance(other, float):
      # raise NotImplemented
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
    def __add__(self, other):
      for i in range(len(self)):
        added = tuple( a + b for a, b in zip(self, other) )
        return Vector(*added)
    # def __add__(self, other):
      # # other.args is the correct analog of self.args
      # a = [arg1 + arg2 for arg1, arg2 in zip(self.components, other.components)]
      # return self.__class__(*a)
    def __repr__(self):
        return str(self.components)
        
    # # __repr__ and __str__ must return string
    # def __repr__(self):
      # # return str(self.components)
      # # return f"Vector{self.components}"
      # return str(self.components)

    # def __str__(self):
      # # return str(self.components)
      # # return f"Vector{self.components}"
      # return str(self.components)
      
# def __add__(self, other):
  # if isinstance(other, Vector):
    # new_vec = Vector()
    # new_vec.X = self.X + other.X
    # new_vec.Y = self.X + other.Y
    # return new_vec
  # else:
    # raise TypeError("value must be a vector.")
        
class Mesh:
  node_count = (int) (0.0)
  elem_count = (int) (0.0)
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
    f.write('/SHELL/' + str(self.id) + '\n')
    for i in range (self.elem_count):
      line = self.writeIntField(i,10)
      for d in range (4):
        line = line + self.writeIntField(self.elnod[i][d],10)
      f.write(line + '\n')

   
	# static const Vector3 rights[6] =
	# {
		# Vector3(2.0, 0.0, 0.0),
		# Vector3(0.0, 0.0, 2.0),
		# Vector3(-2.0, 0.0, 0.0),
		# Vector3(0.0, 0.0, -2.0),
		# Vector3(2.0, 0.0, 0.0),
		# Vector3(2.0, 0.0, 0.0)
	# };
	# static const Vector3 ups[6] =
	# {
		# Vector3(0.0, 2.0, 0.0),
		# Vector3(0.0, 2.0, 0.0),
		# Vector3(0.0, 2.0, 0.0),
		# Vector3(0.0, 2.0, 0.0),
		# Vector3(0.0, 0.0, 2.0),
		# Vector3(0.0, 0.0, -2.0)
	# };  
      
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
class Sphere_Mesh(Mesh):
 
  def __init__(self, divisions):
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
    step3 = [(step, step, step)]

    right = CubeToSphere_rights[0]
    # right = Vector(0)
    print (right)
      
    # for face in range (6):
      # origin = CubeToSphere_origins[face]
      # right = CubeToSphere_rights[face]
      # print (right)
      # up = CubeToSphere_ups[face]
      # for j in range (divisions+1):
        # j3 = [(j,j,j)]
        # for i in range (divisions+1):
          # i3 = [(i,i,i)]
          # test = right * up  
          # # print (test)
          # # const Vector3 p = origin + step3 * (i3 * right + j3 * up);
          # # p = origin + 2.0 * (right * i + up *j ) / div_count
          # # p2 = p * p
          # # rx = sqrt(1.0 - 0.5 * (p2.y + p2.z) + p2.y*p2.z/3.0)
          # # ry = sqrt(1.0 - 0.5 * (p2.z + p2.x) + p2.z*p2.x/3.0)
          # # rz = sqrt(1.0 - 0.5 * (p2.x + p2.y) + p2.x*p2.y/3.0)

      # print (origin)
      
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
  