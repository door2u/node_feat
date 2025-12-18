
def ConnAdd_(fro_, to__, connCoun, game, Math, vari, bge, math, mathutils, scen, typ_ = 0, debu = False):
	scenObje = scen.name + "." + "scen_obje"
	z = 1.2
	pos1 = scen.objects[fro_].worldPosition
	pos2 = scen.objects[to__].worldPosition
	vect = Math.Vect(pos1, pos2)
	angl = math.atan2(vect[1], vect[0])
	angl -= math.pi / 2.0
	magn = Math.VectMagn(vect)
	vect = Math.VectScal(vect, 0.5)
	vect = Math.VectAdd_(vect, scen.objects[fro_].worldPosition)
	if typ_ == 0:
		obje = scen.addObject(scen.name + "." + "bool.conn", scen.name + "." + "bool.conn")
	elif typ_ == 1:
		obje = scen.addObject(scen.name + "." + "blue", scen.name + "." + "blue")
	elif typ_ == 2:
		obje = scen.addObject(scen.name + "." + "red_", scen.name + "." + "red_")
	elif typ_ == 3:
		obje = scen.addObject(scen.name + "." + "trig", scen.name + "." + "trig")
	vari["connList"].append([fro_, to__, len(scen.objects) - 1 - len(vari["objeDele"])])
	obje.worldPosition = (vect[0], vect[1], z)
	scal = magn / 2.0
	scal *= 1.02
	obje.localScale[1] = scal
	eule = mathutils.Matrix(obje.worldOrientation)
	eule = eule.to_euler()
	eule[2] = angl
	eule = eule.to_matrix()
	obje.worldOrientation = eule
	return vari

def ConnList(connList, game, Math, vari, bge, scen, math, mathutils, typ_ = 0):
	scenObje = scen.name + "." + "scen_obje"
	for a in range(len(connList)):
		vari = ConnAdd_(connList[a][0], connList[a][1], 0, game, Math, vari, bge, math, mathutils, scen, typ_ = typ_)
	return vari

def LineGet_(inde, dire, retu):
	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if inde != -1:
		if dire == 0 or dire == 2:
			axi1 = "x"
			axi2 = "y"
		if dire == 1 or dire == 3:
			axi1 = "y"
			axi2 = "x"
		if retu == 0: retu = owne["ind" + axi1 + "." + str(inde)]
		elif retu == 1: retu = owne["pos" + axi1 + "." + str(inde)]
		elif retu == 2: retu = owne["ind" + axi2 + "." + str(inde)]
		elif retu == 3: retu = owne["pos" + axi2 + "." + str(inde)]
		elif retu == 4: retu = owne["pos" + axi1 + "Inde." + str(inde)]
		elif retu == 5: retu = owne["pos" + axi2 + "Inde." + str(inde)]
	else:
		retu = -1
	return retu

def Angl(obje):
	import bge
	import mathutils
	scen = bge.logic.getCurrentScene()
	dire = mathutils.Matrix(scen.objects[obje].orientation)
	dire = dire.to_euler()
	dire = dire[2]
	return dire

def Dire(dire):
	import math
	dire /= math.pi / 2.0
	dire = round(dire)
	while dire < 0:
		dire += 4
	while dire >= 4:
		dire -= 4
	return dire

def CompUpda(Pyth):
	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	coun = owne["compCoun"]
	indx = []
	indy = []
	posx = []
	posy = []
	for a in range(coun):
		indx.append(a)
		indy.append(a)
		x = scen.objects[scen.name + "." + owne["compObje." + str(a)]].worldPosition[0]
		y = scen.objects[scen.name + "." + owne["compObje." + str(a)]].worldPosition[1]
		posx.append([x, a])
		posy.append([y, a])
	posx, indx, posy, indy = Sort(posx, indx, posy, indy, Pyth)
	for a in range(coun):
		owne["indx." + str(a)] = indx[a]
		owne["indy." + str(a)] = indy[a]
		owne["posx." + str(a)] = posx[a][0]
		owne["posy." + str(a)] = posy[a][0]
		owne["posxInde." + str(a)] = posx[a][1]
		owne["posyInde." + str(a)] = posy[a][1]

def VectCent(vec1, vec2, Math):
	vec2 = Math.Vect(vec1, vec2)
	vec2 = Math.VectScal(vec2, 0.5)
	vec2 = Math.VectAdd_(vec1, vec2)
	return vec2

def Sort(posx, indx, posy, indy, Pyth):
	posx = Pyth.SortQuic(posx, 0, len(posx) - 1)
	posy = Pyth.SortQuic(posy, 0, len(posy) - 1)
	for a in range(len(posx)):
		indx[posx[a][1]] = a
	for a in range(len(posy)):
		indy[posy[a][1]] = a
	return posx, indx, posy, indy

def BoolTogg(name, node, valu):
	import bge
	scen = bge.logic.getCurrentScene()
	scen.objects[name + ".0"].visible = int(valu)
	scen.objects[name + ".1"].visible = int(not valu)
	valu = not valu
	scen.objects[name + "." + node]["valu"] = valu
	return valu

