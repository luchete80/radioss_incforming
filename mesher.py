from math import *

def writeFloatField(number, length, decimals):
  fmt ='%.' + str(decimals) + 'e'
  # print ('format ' + fmt)
  s = fmt % number
  spaces = ''
  for i in range ((int)(length - len(s))):
    spaces = spaces + ' '
  output = spaces + s
  # print (spaces + s)
  return output

def writeIntField(number, length):
  s = '%d' % number
  spaces = ''
  for i in range ((int)(length - len(s))):
    spaces = spaces + ' '
  output = spaces + s
  # print (spaces + s)
  return output

def Norm2(v):
  norm = 0.0
  if isinstance(v, Vector):
    for i in range (len(v.components)):
      norm = norm + v.components[i] * v.components[i]
  return norm

    
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
  def __sub__(self, other):
    if isinstance(other, Vector):
    # other.args is the correct analog of self.args
      a = [arg1 - arg2 for arg1, arg2 in zip(self.components, other.components)]
    return self.__class__(*a)
  def Norm():
    norm = 0.0
    norm = [norm + arg1 for arg1 in self.components]
    norm = sqrt (norm)
    return norm
    
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

#TODO: CHANGE ALL TO NODE
class Node(Vector):
  def __init__(self, id, *components):
    self.components = components
    self.id = id
    
    
###############################################################################
#TODO: DEFINE MESH
class Mesh:
  node_count = (int) (0.0)
  elem_count = (int) (0.0)
  print_segments = False
  nodes = []
  elnod = []
  elcenter = []
  ini_node_id = 1
  ini_elem_id = 1
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
  
  def printESurfsRadioss(self,f):
    if (self.print_segments):
      for i in range (self.elem_count):
        line = "/SURF/SEG/%d\nSURF_SEG_%d\n" % (i+1,i+1)
        f.write(line)
        line = writeIntField(i+1,10)
        for d in range (4):
          line = line + writeIntField(self.elnod[i][d]+1,10)
        f.write(line + '\n')
  def printRadioss(self,fname):
    f = open(fname,"w+")
    # self.writeFloatField(-100.0,20,6)
    f.write('/NODES\n')
    for i in range (self.node_count):
      line = writeIntField(i+1,10)
      for d in range (3):
        line = line + writeFloatField(self.nodes[i][d],20,6) 
      # f.write("%.6e, %.6e\n" % (self.nodes[i][0],self.nodes[i][1]))
      f.write(line + '\n')
    f.write('/SHELL/' + str(self.id) + '\n')
    for i in range (self.elem_count):
      line = writeIntField(i+1,10)
      for d in range (4):
        line = line + writeIntField(self.elnod[i][d]+1,10)
      f.write(line + '\n')
      
  def writeCenters(self):
    print ("Writing centers ")
    # print ("self nodes size ",len(self.nodes))
    for e in range (self.elem_count):
      center = [0.,0.,0.]
      for n in range (4):
        for dim in range (3):
          # print ("elem ", e, " node ",n, "el node ", self.elnod[e][n])
          center[dim] = center[dim] + self.nodes[self.elnod[e][n]][dim]

      for dim in range (3):
        center[dim] = center[dim] / 4.0
      self.elcenter.append(Vector(center[0], center[1], center[2]))
    # for e in range (self.elem_count):
      # print ("Element centers ", self.elcenter[e])
        # elcenter
  def findNearestElem(self, x,y,z):
    mx = -1
    maxdist = 1000.0
    for e in range (self.elem_count):
      pos = Vector(x,y,z)
      dist = Norm2(pos - self.elcenter[e])
      # print ("dist: ", dist)
      if ( dist < maxdist ):
        maxdist = dist
        mx = e
    return mx

class Plane_Mesh(Mesh):
  ini_node_id = 1 
  ini_elem_id = 1
  def set_ini_nod_ele (inin, inie):
    ini_node_id = inin 
    ini_elem_id = inie
  def __init__(self, id, largo, delta):
    self.id = id
    elem_xy = (int)(largo/delta)
    nc = (int)(elem_xy+1)
    self.node_count = nc * nc
    self.elem_count = (int)((elem_xy)*(elem_xy))
    print ('Nodes Count: ' + str(self.node_count))
    print ('Elem Count: ' + str(self.node_count))
    y = -largo/2.0
    for j in range (nc):
      x = -largo/2.0
      for i in range (nc):
        self.nodes.append((x,y,0.))
        x = x + delta
      y = y + delta
      
    for ey in range (elem_xy):    
      for ex in range (elem_xy):   
        #THIS IS THE REAL NODE POSITION (FROM ZERO)
        self.elnod.append(((elem_xy+1)*ey+ex,(elem_xy+1)*ey + ex+1,(elem_xy+1)*(ey+1)+ex+1,(elem_xy+1)*(ey+1)+ex))
                    # elem%elnod(i,:)=[(nel(1)+1)*ey + ex+1,(nel(1)+1)*ey + ex+2,(nel(1)+1)*(ey+1)+ex+2,(nel(1)+1)*(ey+1)+ex+1]         
              # print *, "Element ", i , "Elnod", elem%elnod(i,:) 
    # print(self.elnod)
    self.writeCenters()
    
#Based on: https://github.com/caosdoar/spheres/blob/master/src/spheres.cpp 
#https://medium.com/@oscarsc/four-ways-to-create-a-mesh-for-a-sphere-d7956b825db4
class Sphere_Mesh(Mesh):
 
  def __init__(self, id, radius, divisions):
    print ("Creating Sphere mesh")
    self.id = id
    CubeToSphere_origins = [
    Vector(-1.0, -1.0, -1.0),
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
    step3 = Vector(step, step, step)

    test = Vector (0.,0.,0.)
    n = 0
    for face in range (1): #CUBE FACES 
      origin = CubeToSphere_origins[face]
      right = CubeToSphere_rights[face]
      # print (right)
      up = CubeToSphere_ups[face]
      for j in range (divisions+1):
        j3 = Vector(j,j,j)
        for i in range (divisions+1):
          i3 = Vector(i,i,i)
          print ("i3 j3 ", i3, j3)
          # print (right)
          # print ("origin ")
          # print (origin)
          # print ("right * origin ")

          # test = right * origin  
          # print (test)
          # test = right + up  
          # print (test)
          # const Vector3 p = origin + step3 * (i3 * right + j3 * up);
          p = origin + ( step3 * (i3 * right  + up *j3 )  )
          p2 = p * p
          print ("p ", p)
          # rx = sqrt(1.0 - 0.5 * (p2.y + p2.z) + p2.y*p2.z/3.0)
          # ry = sqrt(1.0 - 0.5 * (p2.z + p2.x) + p2.z*p2.x/3.0)
          # rz = sqrt(1.0 - 0.5 * (p2.x + p2.y) + p2.x*p2.y/3.0)
          rx = p.components[0] * sqrt(1.0 - 0.5 * (p2.components[1] + p2.components[2]) + p2.components[1]*p2.components[2]/3.0)
          ry = p.components[1] * sqrt(1.0 - 0.5 * (p2.components[2] + p2.components[0]) + p2.components[2]*p2.components[0]/3.0)
          rz = p.components[1] *sqrt(1.0 - 0.5 * (p2.components[0] + p2.components[1]) + p2.components[0]*p2.components[1]/3.0)
          # print ("rx ry rz", (rx,ry,rz), "\n")
				# const Vector3 n
				# (
					# p.x * std::sqrt(1.0 - 0.5 * (p2.y + p2.z) + p2.y*p2.z / 3.0),
					# p.y * std::sqrt(1.0 - 0.5 * (p2.z + p2.x) + p2.z*p2.x / 3.0),
					# p.z * std::sqrt(1.0 - 0.5 * (p2.x + p2.y) + p2.x*p2.y / 3.0)
				# );
				# mesh.vertices.emplace_back(n);
          self.nodes.append((rx,ry,rz))
          print ("Sphere rx ry rz", rx,ry,rz)
          n = n +1
    print ("generated: %d", n , " nodes      ")
    self.node_count = n
      # print (origin)
    
    e = 0
    for ey in range (divisions):
      for ex in range (divisions):
        # elem%elnod(i,:)=[(nel(1)+1)*ey + ex+1,(nel(1)+1)*ey + ex+2,(nel(1)+1)*(ey+1)+ex+2,(nel(1)+1)*(ey+1)+ex+1]  
        self.elnod.append(((divisions+1)*ey+ex,(divisions+1)*ey + ex+1,(divisions+1)*(ey+1)+ex+1,(divisions+1)*(ey+1)+ex))      
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

class Prop: 
  def __init__(self, pid):
    self.pid = pid
  def printRadioss(self,f):     
    f.write("##--------------------------------------------------------------------------------------------------\n")
    f.write("## Shell Property Set (pid 1)\n")
    f.write("##--------------------------------------------------------------------------------------------------\n")
    f.write("/PROP/SHELL/1\n")
    f.write("SECTION_SHELL:1 TITLE:probe_section  \n")                                                               
    f.write("#Ishell	Ismstr	Ish3n	Idril	 	 	P_thickfail\n")
    f.write("         4         2                         \n")                                   
    f.write("#hm	hf	hr	dm	dn\n")
    f.write("\n")
    f.write("#N	Istrain	Thick	Ashear	 	Ithick	Iplas    \n")                                                                                                
    f.write("         2          5.00000000000000E-04                                       1         1\n")
             
             
         
#ASSUMING EACH PART HAS ONLY 1 MESH
class Part:
  def __init__(self, mid):
    self.id = mid
    self.mesh = []
    self.title = "PART_ID_%d\n" %mid
    self.mid = 0
  def AppendMesh(self,m):
    if (not isinstance(m, Mesh)):
      print ("part is not a mesh")
    else:
      self.mesh.append(m)
  
  def printRadioss(self,f):                          
    f.write('/SHELL/' + str(self.id) + '\n')
    for i in range (self.mesh[0].elem_count):
      line = writeIntField(i + self.mesh[0].ini_elem_id ,10)
      for d in range (4):
        # print (self.mesh[0].ini_node_id, ", ")
        line = line + writeIntField(self.mesh[0].elnod[i][d] + self.mesh[0].ini_node_id,10)
      f.write(line + '\n')   
    line = "/PART/%d\n" % self.id
    f.write(line)
    f.write(self.title)                                                                                            
    f.write("#     pid     mid\n")
    f.write("      1         2\n")    
    if (self.mesh[0].print_segments):
      self.mesh[0].printESurfsRadioss(f)
      
class Material:
  def __init__(self, mid):
    id = mid
  def printRadioss(self,f):
    f.write("/MAT/COWPER/2\n")  
    f.write("MAT_PIECEWISE_LINEAR_PLASTICITY:2 TITLE:mat_probe   \n")                                                  
    f.write("              7850.0\n")  
    f.write("      200000000000.0                0.33\n")  
    f.write("        300000000.0        2000000000.0                 1.0                 0.01.00000000000000E+30\n")  
    f.write("                0.0                 0.0         1         11.00000000000000E+30\n")  
    f.write("1.00000000000000E+211.00000000000000E+302.10000000000000E+30\n")  
    f.write("#/HEAT/MAT/mat_ID/unit_ID\n")
    f.write("/HEAT/MAT/2\n")
    f.write("#                 T0             RHO0_CP                  AS                  BS     IFORM\n")
    f.write("              20.0                 2.5e6               420.0                  0.0        1\n")
    f.write(" \n") #REQUIRED

class Function:
  val_count = 0 
  def __init__(self, id, x,y):
    self.val_count = 1
    self.vals = []
    self.vals.append((x,y))
  def Append (self,x,y):
    self.vals.append((x,y))
    self.val_count = self.val_count + 1
  def getVal(self, i):
    return self.vals[i]
  def getVal_ij(self, i, j):
    return self.vals[i][j]
    
    
class Model:
  tot_nod_count = 0
  tot_ele_count = 0
  thermal = False
  def __init__(self):
    self.part_count = 0
    self.part = []
    self.mat = []
    self.prop = []
    self.load_fnc = []
    
  
  def AppendPart(self, p):
    if (not isinstance(p, Part)):
      print ("ERROR: added object is not a part ")
    else:
      self.part.append(p)
      self.part_count = self.part_count + 1
      print ("part count ", self.part_count)
      if (self.part_count > 1):
        self.tot_nod_count = self.tot_nod_count + self.part[self.part_count-2].mesh[0].node_count
        self.part[self.part_count-1].mesh[0].ini_node_id = self.tot_nod_count + 1
        
        self.tot_ele_count = self.tot_ele_count + self.part[self.part_count-2].mesh[0].elem_count
        self.part[self.part_count-1].mesh[0].ini_elem_id = self.tot_ele_count + 1
        
    print ("Part ", self.part_count, " initial node: ", self.tot_nod_count + 1)

  def AppendMat(self, m):
    if (not isinstance(m, Material)):
      print ("ERROR: added opbject is not a part ")
    else:
      self.mat.append(m)

  def AppendLoadFunction(self, lf):
    self.load_fnc.append(lf)
    
  def AppendProp(self, p):
    if (not isinstance(p, Prop)):
      print ("ERROR: added opbject is not a part ")
    else:
      self.mat.append(p)
      
  def printRadioss(self,fname):
    f = open(fname,"w+")
    f.write("#RADIOSS STARTER\n")
    f.write("/BEGIN\n")
    f.write("test                                                        \n")                   
    f.write("      2019         0 \n")
    f.write("                  kg                   m                   s\n")
    f.write("                  kg                   m                   s\n")
    f.write('/NODE\n')
    for p in range (self.part_count):
      # print ("part node count ", self.part[p].mesh[0].node_count)
      for i in range (self.part[p].mesh[0].node_count):
        print ("Node ", self.part[p].mesh[0].nodes[i])
        line = writeIntField(i + self.part[p].mesh[0].ini_node_id,10)
        for d in range (3):
          line = line + writeFloatField(self.part[p].mesh[0].nodes[i][d],20,6) 
        f.write(line + '\n')

    # Print element connectivity
    for p in range (self.part_count):
      self.part[p].printRadioss(f)
    
    print ("printing materials: ", len(self.mat))
    for m in range (len(self.mat)):
      self.mat[m].printRadioss(f)
    
    if (self.thermal):
      # f.write("include thermal.inc\n")
      print ("Load function count: ", len(self.load_fnc))
      ### LOAD FNC
      for lf in range (len(self.load_fnc)):
        # print ("fn ", self.load_fnc[lf][0], "\n")
        line = "/FUNCT/%d\n" % (lf+1)
        line = line + "F_ELEM_%d\n" % (lf+1)
        for val in range (self.load_fnc[lf].val_count):
          line = line + writeFloatField(self.load_fnc[lf].getVal(val)[0],20,6) + \
                        writeFloatField(self.load_fnc[lf].getVal(val)[1],20,6) + "\n"
        f.write(line)

      f.write("################################### ELEMENT FLUXES #####################################\n")
      for lf in range (len(self.load_fnc)):
        # print ("fn ", self.load_fnc[lf][0], "\n")
        line = "/IMPFLUX/%d\nFLUX_ELEM%d\n" % (lf+1,lf+1)
        line = line + writeIntField(lf+1,10)+ writeIntField(lf+1,10) + "\n"
        line = line + "       1.0       1.0\n"
        f.write(line)
      
    for p in range(len(self.prop)):
      self.mat[p].printRadioss(f)
    f.write('/END\n')