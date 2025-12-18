
def Gate(phas, set_Star, phasTrig, gate, raisSpee, game):
	import bge
	scen = bge.logic.getCurrentScene()
	if phas == phasTrig:
		posi = scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition
		if posi[2] < 8.0:
			scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition = (scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[0], scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[1], scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[2] + raisSpee)
		if posi[2] >= 2.0:
			phas += 1
			set_Star += 1
			scen.objects[scen.name + "." + "unwa"]["unwa." + str(gate)] = False
	if phas == phasTrig + 1:
		posi = scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition
		if posi[2] < 8.0:
			scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition = (scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[0], scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[1], scen.objects[scen.name + "." + "room.path." + game.Pad_(gate)].worldPosition[2] + raisSpee)
	return phas, set_Star

def main(bge, math, cont, scen, owne, Math, game, Pyth, vari, GameNode, mathutils):
	clic = owne.sensors["clic"].positive
	clir = owne.sensors["clir"].positive
	phasTrig = 0
	phas = owne["phas"]
	gate = 0
	set_Star = owne["set_Star"]
	raisSpee = 0.025
	scenObje = scen.name + "." + "scen_obje"
	charName = scen.name + "." + "matt"
	if phas == phasTrig:
		if scen.objects[charName]["weap"] == 2 and scen.objects[scen.name + "." + "comp" + "." + "out_.000"]["hit_"]:
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	gate += 1
	phasTrig += 1
	if phas == phasTrig:
		obj1 = "temp.comp.out_.001"
		obj2 = "temp.comp.in__.000"
		if scen.objects[charName]["weap"] == 2 and len(vari["connList"]) > 0 and obj1 in vari["connList"][0] and obj2 in vari["connList"][0]:
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		obj1 = "temp.comp.bool.0.001.out_"
		obj2 = "temp.comp.bool.0.000.in__"
		if scen.objects[charName]["weap"] == 2 and len(vari["connList"]) > 0 and obj1 in vari["connList"][0] and obj2 in vari["connList"][0]:
			vari["connList"] = []
			obj1 = "temp.comp.bool.0.003.out_"
			obj2 = "temp.comp.bool.0.002.in__"
			vari = GameNode.ConnAdd_(obj1, obj2, 0, game, Math, vari, bge, math, mathutils, scen)
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		polyList = []
		coun = scen.objects[scenObje]["cut_"]
		for a in range(coun):
			polyList.append(scen.objects[scenObje]["cut_." + str(a)])
		pathPoly = scen.objects[charName]["pathPolyOffs"]
		obj1 = "temp.comp.bool.0.003.out_"
		obj2 = "temp.comp.bool.0.002.in__"
		dire = GameNode.Angl(charName + "." + "body")
		dire = (math.cos(dire), math.sin(dire))
		loc1 = scen.objects[obj1].worldPosition
		loc2 = scen.objects[obj2].worldPosition
		loc2 = GameNode.VectCent(loc1, loc2, Math)
		loc1 = scen.objects[charName].worldPosition
		faci = Math.Faci(dire, loc1, loc2)
		if scen.objects[charName]["weap"] == 1 and clic and (pathPoly in polyList) and faci and len(vari["connList"]) > 0:
			out_ = 7
			in__ = 6
			scen.objects[vari["connList"][0][2]].endObject()
			obj1 = "temp.comp.bool.1.014.out_"
			obj2 = "temp.comp.bool.0.004.in__"
			vari = GameNode.ConnAdd_(obj1, obj2, 0, game, Math, vari, bge, math, mathutils, scen)
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		polyList = []
		coun = scen.objects[scenObje]["push"]
		for a in range(coun):
			polyList.append(scen.objects[scenObje]["push." + str(a)])
		pathPoly = scen.objects[charName]["pathPolyOffs"]
		dire = GameNode.Angl(charName + "." + "body")
		dire = (math.cos(dire), math.sin(dire))
		faci = Math.Faci(dire, scen.objects[charName].worldPosition, scen.objects["temp.comp.bool.0.004.in__"].worldPosition)
		if scen.objects[charName]["weap"] == 0 and clic and (pathPoly in polyList) and faci:
			vari = GameNode.ConnList([["temp.comp.bool.0.005.out_", "temp.comp.bool.1.015.in__"]], game, Math, vari, bge, scen, math, mathutils)
			GameNode.BoolTogg("temp.comp.bool.0.004", "1000", False)
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		polyList = []
		coun = scen.objects[scenObje]["pull"]
		for a in range(coun):
			polyList.append(scen.objects[scenObje]["pull." + str(a)])
		pathPoly = scen.objects[charName]["pathPolyOffs"]
		dire = GameNode.Angl(charName + "." + "body")
		dire = (math.cos(dire), math.sin(dire))
		faci = Math.Faci(dire, scen.objects[charName].worldPosition, scen.objects["temp.comp.bool.0.005.out_"].worldPosition)
		if scen.objects[charName]["weap"] == 0 and clic and (pathPoly in polyList) and faci:
			connList = []
			connList.append(["temp.comp.func.0.003.out_", "temp.comp.bool.0.009.in__"])
			connList.append(["temp.comp.bool.0.009.out_.001", "temp.comp.func.0.003.in__"])
			connList.append(["temp.comp.func.0.002.out_", "temp.comp.bool.0.008.in__"])
			connList.append(["temp.comp.bool.0.008.out_.001", "temp.comp.func.0.002.in__"])
			connList.append(["temp.comp.func.0.001.out_", "temp.comp.bool.0.007.in__"])
			connList.append(["temp.comp.bool.0.007.out_.001", "temp.comp.func.0.001.in__"])
			connList.append(["temp.comp.func.0.000.out_", "temp.comp.bool.0.006.in__"])
			connList.append(["temp.comp.bool.0.006.out_.001", "temp.comp.func.0.000.in__"])
			connList.append(["temp.comp.bool.0.009.out_", "temp.comp.ifeq.0.003.in__.001"])
			connList.append(["temp.comp.bool.0.008.out_", "temp.comp.ifeq.0.002.in__.001"])
			connList.append(["temp.comp.bool.0.007.out_", "temp.comp.ifeq.0.001.in__.001"])
			connList.append(["temp.comp.bool.0.006.out_", "temp.comp.ifeq.0.000.in__.001"])
			connList.append(["temp.comp.bool.0.013.out_", "temp.comp.ifeq.0.003.in__"])
			connList.append(["temp.comp.bool.0.012.out_", "temp.comp.ifeq.0.002.in__"])
			connList.append(["temp.comp.bool.0.011.out_", "temp.comp.ifeq.0.001.in__"])
			connList.append(["temp.comp.bool.0.010.out_", "temp.comp.ifeq.0.000.in__"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils)
			connList = []
			connList.append(["temp.comp.tout.000", "temp.comp.elbo.0.000.thr2"])
			connList.append(["temp.comp.elbo.0.000.thr1", "temp.comp.ifeq.0.000.t_in"])
			connList.append(["temp.comp.ifeq.0.000.tout", "temp.comp.ifeq.0.001.t_in"])
			connList.append(["temp.comp.ifeq.0.001.tout", "temp.comp.ifeq.0.002.t_in"])
			connList.append(["temp.comp.ifeq.0.002.tout", "temp.comp.ifeq.0.003.t_in"])
			connList.append(["temp.comp.ifeq.0.003.tout", "temp.comp.elbo.0.001.thr2"])
			connList.append(["temp.comp.elbo.0.001.thr1", "temp.comp.tout.001"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils, typ_ = 3)
			GameNode.BoolTogg("temp.comp.bool.1.015", "1000", False)
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		valuList = []
		targValu = []
		for a in range(4):
			polyList = []
			coun = scen.objects[scenObje]["togg." + game.Pad_(a)]
			for b in range(coun):
				polyList.append(scen.objects[scenObje]["togg." + game.Pad_(a) + "." + str(b)])
			pathPoly = scen.objects[charName]["pathPolyOffs"]
			name = "temp.comp.bool.0.00" + str(6 + a)
			node = "3100"
			valu = scen.objects[name + "." + node]["valu"]
			dire = GameNode.Angl(charName + "." + "body")
			dire = (math.cos(dire), math.sin(dire))
			faci = Math.Faci(dire, scen.objects[charName].worldPosition, scen.objects[name + "." + node].worldPosition)
			if scen.objects[charName]["weap"] == 0 and clic and (pathPoly in polyList) and faci:
				valu = GameNode.BoolTogg(name, node, valu)
			targValu.append(valu)
			valuList.append(scen.objects["temp.comp.bool.0.0"+ str(10 + a) + ".0100"]["valu"])
		if valuList == targValu:
			connList = []
			connList.append(["temp.comp.bool.0.016.out_", "temp.comp.ifeq.0.004.in__.001"])
			connList.append(["temp.comp.bool.0.017.out_", "temp.comp.ifeq.0.005.in__"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils)
			connList = []
			connList.append(["temp.comp.ifeq.0.004.tout", "temp.comp.bool.0.018.t_in"])
			connList.append(["temp.comp.ifeq.0.005.tout", "temp.comp.bool.0.019.t_in"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils, typ_ = 3)
			GameNode.CompUpda(Pyth)
			vari["connList"] = []
			connList = []
			connList.append(["temp.comp.out_.002", "temp.comp.in__.001"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils)
			connList = []
			connList.append(["temp.comp.bool.0.018.4010", "temp.comp.bool.0.019.0110"])
			vari = GameNode.ConnList(connList, game, Math, vari, bge, scen, math, mathutils, typ_ = 1)
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	if phas == phasTrig:
		import mathutils
		upda = False
		pathPoly = scen.objects[charName]["pathPolyOffs"]
		nextPhas = True
		updaList = True
		carr = -1
		for a in range(12):
			polyList = []
			for b in range(4):
				coun = scen.objects[scenObje]["hole." + game.Pad_(a) + "." + str(b)]
				for c in range(coun):
					polyList.append(scen.objects[scenObje]["hole." + game.Pad_(a) + "." + str(b) + "." + str(c)])
			stri = str(a)
			if a < 10: stri = "0" + stri
			holeName = scen.name + ".comp.hole.0" + stri
			dire = GameNode.Angl(charName + "." + "body")
			dire = (math.cos(dire), math.sin(dire))
			faci = Math.Faci(dire, scen.objects[charName].worldPosition, scen.objects[holeName].worldPosition)
			if scen.objects[charName]["weap"] == 0 and clic and (pathPoly in polyList) and faci:
				emph = False
				empc = False
				if scen.objects[holeName]["obje"] == "": emph = True
				if scen.objects[charName]["obje"] == "": empc = True
				if emph and empc == False:
					upda = True
					obje = scen.objects[scen.objects[charName]["obje"]]
					obje.worldPosition = scen.objects[holeName].worldPosition
					obje.visible = True
					for chil in obje.children: chil.visible = True
					scen.objects[holeName]["obje"] = scen.objects[charName]["obje"]
					scen.objects[holeName]["objeType"] = scen.objects[charName]["objeType"]
					scen.objects[charName]["obje"] = ""
					scen.objects[charName]["objeType"] = ""
					if updaList:
						inde = obje["compInde"]
						indx = GameNode.LineGet_(inde, 0, 0)
						indy = GameNode.LineGet_(inde, 0, 2)
						if indx != -1 and indy != -1:
							prex = GameNode.LineGet_(indx, 0, 1)
							prey = GameNode.LineGet_(indy, 0, 3)
							x = obje.worldPosition[0]
							y = obje.worldPosition[1]
							axisList = ["x", "y"]
							for axis in axisList:
								if axis == "x":
									loca = x
									prev = prex
									inde = indx
								if axis == "y":
									loca = y
									prev = prey
									inde = indy
								if loca < prev:
									incr = -1
									brea = -1
								if loca > prev:
									incr = 1
									brea = owne["compCoun"]
								if loca != prev:
									b = inde + incr
									comp = owne["pos" + axis + "." + str(b)]
									while b != brea and ((incr == -1 and loca > comp) or (incr == 1 and loca <= comp)):
										owne["pos" + axis + "." + str(b + incr)] = comp
										owne["pos" + axis + "Inde." + str(b + incr)] = owne["pos" + axis + "Inde." + str(b)]
										b += incr
										comp = owne["pos" + axis + "." + str(b)]
									owne["pos" + axis + "." + str(b + incr)] = loca
									owne["pos" + axis + "Inde." + str(b + incr)] = inde
				if emph == False and empc:
					upda = True
					scen.objects[scen.objects[holeName]["obje"]].visible = False
					for chil in scen.objects[scen.objects[holeName]["obje"]].children:
						chil.visible = False
					scen.objects[charName]["obje"] = scen.objects[holeName]["obje"]
					scen.objects[charName]["objeType"] = scen.objects[holeName]["objeType"]
					if updaList:
						inde = scen.objects[scen.objects[holeName]["obje"]]["compInde"]
						carr = inde
					scen.objects[holeName]["obje"] = ""
					scen.objects[holeName]["objeType"] = ""
			if scen.objects[charName]["weap"] == 0 and clir and (pathPoly in polyList) and faci:
				stri = str(a)
				if a < 10: stri = "0" + stri
				holeName = scen.name + ".comp.hole.0" + stri
				if scen.objects[holeName]["obje"] != "":
					upda = True
					orie = mathutils.Matrix(scen.objects[scen.objects[holeName]["obje"]].orientation)
					orie = orie.to_euler()
					orie[2] += math.pi / 2.0
					scen.objects[scen.objects[holeName]["obje"]].orientation = orie.to_matrix()
			if a >= 6:
				nextPhasObje = "0" + str(a)
				if a < 10: nextPhasObje = "0" + nextPhasObje
				nextPhasObje = "temp.comp.hole." + nextPhasObje
				if a == 6 or a == 8 or a == 9 or a == 11:
					if scen.objects[nextPhasObje]["objeType"] != "elbo":
						nextPhas = False
				if a == 7 or a == 10:
					if scen.objects[nextPhasObje]["objeType"] != "spli":
						nextPhas = False
				tole = 0.0001
				orie = scen.objects[nextPhasObje]["obje"]
				if orie != "":
					orie = GameNode.Angl(orie)
					orie = GameNode.Dire(orie)
					if a == 6:
						if orie != 0: nextPhas = False
					elif a == 7 or a == 9:
						if orie != 3: nextPhas = False
					elif a == 8 or a == 10:
						if orie != 1: nextPhas = False
					elif a == 11:
						if orie != 2: nextPhas = False
		if upda:
			GameNode.CompUpda(Pyth)
			if carr != -1:
				owne["indx." + str(carr)] = -1
				owne["indy." + str(carr)] = -1
			in__ = owne["compIn__"]
			dire = GameNode.Angl(scen.name + "." + owne["compObje." + str(in__)])
			dire -= math.pi / 2.0
			dire = GameNode.Dire(dire)
			for a in range(len(vari["connList"])):
				fro_ = vari["connList"][a][0]
				if fro_ != "":
					inde = vari["connList"][a][2]
					if inde < len(scen.objects):
						scen.objects[inde].endObject()
						vari["objeDele"].append(inde)
					else:
						print("overflow", len(scen.objects))
			vari["connList"] = []
			indeList = [[[in__, dire]], [[4, 3]]]
			branList = [[0, -1, -1], [1, -1, -1]]
			connList = []
			fro_ = ""
			leng = len(indeList)
			a = 0
			while a < leng:
				b = 0
				while b < len(indeList[a]):
					fro_ = scen.name + "." + owne["compObje." + str(indeList[a][b][0])]
					if branList[a][1] == -1:
						branList[a][1] = fro_
					tole = 0.01
					objeInde = indeList[a][b][0]
					direIn__ = indeList[a][b][1]
					# 0 - +x
					# 1 - +y
					# 2 - -x
					# 3 - -y
					if direIn__ >= 0 and direIn__ < 4:
						ind1 = GameNode.LineGet_(objeInde, direIn__, 0)
						inda = GameNode.LineGet_(objeInde, direIn__, 2)
						pos1 = GameNode.LineGet_(ind1, direIn__, 1)
						axis = GameNode.LineGet_(inda, direIn__, 3)
						if direIn__ == 0 or direIn__ == 1:
							incr = 1
							brea = owne["compCoun"]
						if direIn__ == 2 or direIn__ == 3:
							incr = -1
							brea = -1
						ind1 += incr
						foun = False
						while ind1 != brea:
							ind_ = GameNode.LineGet_(ind1, direIn__, 4)
							if ind_ != -1:
								pos2 = GameNode.LineGet_(ind1, direIn__, 1)
								if ind_ != objeInde and math.fabs(pos1 - pos2) >= tole:
									ind2 = GameNode.LineGet_(ind_, direIn__, 2)
									axi2 = GameNode.LineGet_(ind2, direIn__, 3)
									obje = scen.name + "." + owne["compObje." + str(ind_)]
									typ_ = scen.objects[obje]["objeType"]
									faci = False
									if typ_ == "obst":
										radi = scen.objects[obje]["radi"]
										faci = scen.objects[obje]["dire"]
										if round(math.fabs(faci - direIn__)) == 2: faci = True
										else: faci = False
									else:
										radi = 0.075
										faci = True
									if math.fabs(axi2 - axis) < radi and faci:
										foun = True
										break
							ind1 += incr
						if foun:
							if typ_ == "elbo" or typ_ == "spli":
								indeList[a].pop(b)
								if b > 0: b -= 1
								dire = GameNode.Angl(scen.name + "." + owne["compObje." + str(ind_)])
								dire -= math.pi / 2.0
								dire = GameNode.Dire(dire)
								if typ_ == "elbo":
									appe = False
									dirn = dire - 1
									if dirn < 0: dirn += 4
									if direIn__ == dirn:
										dir1 = dire
										appe = True
									dirn = dire + 2
									if dirn > 3: dirn -= 4
									if direIn__ == dirn:
										dir1 = dire + 1
										appe = True
									if appe:
										if dir1 > 3: dir1 -= 4
										indeList[a].append([ind_, dir1])
								if typ_ == "spli":
									conn = False
									if (direIn__ == 0 and dire == 1) or (direIn__ == 1 and dire == 0):
										dir1 = 0
										dir2 = 1
										conn = True
									if (direIn__ == 0 and dire == 2) or (direIn__ == 2 and dire == 0):
										dir1 = 1
										dir2 = 3
										conn = True
									if (direIn__ == 0 and dire == 3) or (direIn__ == 3 and dire == 0):
										dir1 = 0
										dir2 = 3
										conn = True
									if (direIn__ == 1 and dire == 2) or (direIn__ == 2 and dire == 1):
										dir1 = 1
										dir2 = 2
										conn = True
									if (direIn__ == 1 and dire == 3) or (direIn__ == 3 and dire == 1):
										dir1 = 0
										dir2 = 2
										conn = True
									if (direIn__ == 2 and dire == 3) or (direIn__ == 3 and dire == 2):
										dir1 = 2
										dir2 = 3
										conn = True
									if conn:
										indeList.append(indeList[a][:])
										leng = len(indeList)
										indeList[leng - 1].append([ind_, dir2])
										indeList[a].append([ind_, dir1])
										branList.append([a, branList[a][1], -1])
							elif typ_ == "obst":
								indeList[a].pop(b)
								if b > 0: b -= 1
							else:
								dire = -3
								if ind_ == 0: dire = 1
								if ind_ == 1: dire = 3
								if ind_ == 4: dire = 3
								if ind_ == 5: dire = 1
								if ind_ == 12: dire = 0
								if ind_ == 13: dire = 2
								dire += 2
								if dire > 3: dire -= 4
								if dire != direIn__:
									indeList[a].pop(b)
									if b > 0: b -= 1
								else:
									indeList[a][b] = [ind_, -1]
									b += 1
					for c in range(len(indeList[a])):
						to__ = scen.name + "." + owne["compObje." + str(indeList[a][c][0])]
						connList.append([to__, fro_, a, coun])
						branList[a][2] = to__
						fro_ = to__
				a += 1
			for a in range(len(connList)):
				typ_ = -1
				begi = branList[connList[a][2]][1]
				end_ = branList[connList[a][2]][2]
				begi = begi.split(".")
				if begi[2] != "func": begi = begi[2]
				else:
					if len(begi) > 3: begi = begi[3]
				end_ = end_.split(".")
				if end_[2] != "func": end_ = end_[2]
				else:
					if len(end_) > 3: end_ = end_[3]
				if (begi == "out_" or begi == "bool") and (end_ == "in__" or end_ == "ifeq"): typ_ = 4
				if (begi == "in__" or begi == "ifeq") and (end_ == "out_" or end_ == "bool"): typ_ = 0
				if (begi == "out_" or begi == "bool") and (end_ == "out_" or end_ == "bool" or end_ == "spli" or end_ == "elbo"): typ_ = 1
				if (begi == "in__" or begi == "ifeq") and (end_ == "in__" or end_ == "ifeq" or end_ == "spli" or end_ == "elbo"): typ_ = 2
				if typ_ != -1:
					if typ_ != 4: vari = GameNode.ConnList([[connList[a][0], connList[a][1]]], game, Math, vari, bge, scen, math, mathutils, typ_ = typ_)
					else: vari = GameNode.ConnList([[connList[a][1], connList[a][0]]], game, Math, vari, bge, scen, math, mathutils)
				else: print("-1", begi, end_)
		if nextPhas:
			vari["connList"] = []
			phas += 1
	phasTrig += 1
	phas, set_Star = Gate(phas, set_Star, phasTrig, gate, raisSpee, game)
	phasTrig += 1
	gate += 1
	phasPrev = owne["phas"]
	# TODO
	if phas != phasPrev:
		scen.objects[scenObje]["conn"] = ""
		scen.objects[scenObje]["from"] = ""
	owne["set_Star"] = set_Star
	owne["phas"] = phas
	return phas, vari

