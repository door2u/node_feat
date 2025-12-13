import importlib.util
import os
spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py")
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)
Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene
Node = Modu.Node

def main():
	print()
	lev1 = True
	#lev1 = False
	if lev1:
		scenNew_ = False
		resx = 640
		resy = 480
		scenNew_ = Temp(scenNew_ = scenNew_, resx = resx, resy = resy)
		
def Temp(scenNew_ = False, resx = 1360, resy = 768, glsl = True):
	import bpy
	import math
	logiDire = BlenGame.LogiDireLink()
	#BlenGame.Full()
	impoComp = True
	#impoComp = False
	leve = "temp"
	scenNew_ = BlenGame.LeveInit(name = leve, scenNew_ = scenNew_, resx = resx, resy = resy, glsl = glsl)
	dic_ = Blen.Impo(blenFile = "scen/00/temp/temp_main.blend", empt = True, ligh = True)
	in__Inst = 0
	out_Inst = 0
	t_inInst = 0
	toutInst = 0
	boolInst = 0
	ifeqInst = 0
	toggInst = 0
	elboInst = 0
	spliInst = 0
	holeInst = 0
	if impoComp:
		obstList = []
		wallCoun = 58
		for a in range(wallCoun):
			obstList.append("wall." + Blen.Pad_(a))
		for a in range(8):
			obstList.append("room.path." + Blen.Pad_(a))
		obstList.append("room.path.012")
		for a in range(len(obstList)):
			Blen.Sele(obstList[a])
			dire = tuple(bpy.context.object.data.polygons[0].normal)
			dire = math.atan2(dire[1], dire[0])
			while dire < 0.0:
				dire += 2.0 * math.pi
			while dire >= 2.0 * math.pi:
				dire -= 2.0 * math.pi
			dire /= math.pi / 2.0
			dire = round(dire)
			vertList = Blen.VertList()
			radi = None
			for b in range(len(vertList)):
				if dire == 0 or dire == 2:
					axis = 1
				if dire == 1 or dire == 3:
					axis = 0
				if radi == None or vertList[b][axis] > radi:
					radi = vertList[b][axis]
			BlenGame.Prop(propName = "dire", propType = 'INT', propValu = dire)
			BlenGame.Prop(propName = "radi", propType = 'FLOAT', propValu = radi)
			BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "obst")
		in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst = Node.Impo(in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst)
		Blen.Sele("impo.comp_node")
		posi = Blen.LocaRead()
		rota = Blen.RotaRead()
		dic_ = Blen.Impo(blenFile = "scen/comp/comp/node.blend", empt = True)
		for key_ in dic_:
			Blen.Sele(key_['name'])
			loca = Blen.LocaRead()
			loca = Math.VectRota3d__(loca, rota)
			Blen.Rota(rota)
			loca = Math.VectAdd_(loca, posi)
			Blen.Loca(loca)
		Blen.Sele("impo.comp.elbo.0.000")
		Blen.Dele()
		Blen.Sele("impo.comp.elbo.0.001")
		Blen.Dele()
		Blen.Sele("impo.comp.elbo.0.002")
		Blen.Dele()
		Blen.Sele("impo.comp.elbo.0.003")
		Blen.Dele()
		Blen.Sele("impo.comp.spli.0.000")
		Blen.Dele()
		Blen.Sele("impo.comp.spli.0.001")
		Blen.Dele()
		in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst = Node.Impo(in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst)
		Blen.Sele("comp.hole.000")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.elbo.0.002")
		BlenGame.PropSet_(propName = "objeType", propValu = "elbo")
		Blen.Sele("comp.hole.001")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.spli.0.000")
		BlenGame.PropSet_(propName = "objeType", propValu = "spli")
		Blen.Sele("comp.hole.002")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.elbo.0.003")
		BlenGame.PropSet_(propName = "objeType", propValu = "elbo")
		Blen.Sele("comp.hole.003")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.elbo.0.004")
		BlenGame.PropSet_(propName = "objeType", propValu = "elbo")
		Blen.Sele("comp.hole.004")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.spli.0.001")
		BlenGame.PropSet_(propName = "objeType", propValu = "spli")
		Blen.Sele("comp.hole.005")
		BlenGame.PropSet_(propName = "obje", propValu = "temp.comp.elbo.0.005")
		BlenGame.PropSet_(propName = "objeType", propValu = "elbo")
	physList = []
	name = "matt"
	charList = []
	charList.append(name)
	scenObje = BlenGame.ScenObje(charList = charList)
	BlenGame.Prop(propName = "phas", propType = 'INT')
	BlenGame.Prop(propName = "set_Star", propType = 'INT')
	sens = 'MOUSE'
	sensOpti = BlenGame.LogiSensOpti()
	sensDict = BlenGame.LogiSensDict(typ_ = sens)
	sensOpti["use_tap"] = True
	sensOpti["invert"] = True
	BlenGame.Logi(sensName = "clii", sensOpti = sensOpti, sensDict = sensDict, contDict = None)
	Blen.Sele(scenObje)
	BlenGame.Scri("scri" + os.sep + "scen.py")
	sensList = ["W", "A", "S", "D", "W_T", "A_T", "S_T", "D_T", "LEFT_SHIFT", "RIGHTAXIS", "UPAXIS", "joysAxisRigh", "joysAxisUp__", "look"]
	sensList.append("clii")
	sensList.append("clir")
	sens = "MOUSE"
	sensOpti = BlenGame.LogiSensOpti()
	sensOpti["use_tap"] = True
	sensDict = BlenGame.LogiSensDict(typ_ = sens)
	sensDict["mouse_event"] = "WHEELUP"
	BlenGame.Logi(sensName = sensDict["mouse_event"], sensOpti = sensOpti, sensDict = sensDict, contDict = None)
	sensDict["mouse_event"] = "WHEELDOWN"
	BlenGame.Logi(sensName = sensDict["mouse_event"], sensOpti = sensOpti, sensDict = sensDict, contDict = None)
	sensList.append("WHEELUP")
	sensList.append("WHEELDOWN")
	for sens in sensList: BlenGame.Controllers()["scen"].link(BlenGame.Sensors()[sens])
	sensOpti = BlenGame.LogiSensOpti()
	sensDict = BlenGame.LogiSensDict(typ_ = 'ALWAYS')
	contDict = BlenGame.LogiContDict(typ_ = 'LOGIC_AND')
	actuDict = BlenGame.LogiActuDict(typ_ = 'SOUND')
	actuDict['mode'] = 'LOOPEND'
	actuDict['name'] = 'scen/temple.wav'
	BlenGame.Logi(sensName = "song", sensDict = sensDict, contDict = contDict, actuDict = actuDict)
	BlenGame.Controllers()["And.004"].link(BlenGame.Sensors()["song"])
	BlenGame.Prop(propName = "path", propType = 'INT')
	if impoComp:
		BlenGame.Prop(propName = "conn", propType = 'STRING')
		BlenGame.Prop(propName = "from", propType = 'BOOL')
		BlenGame.Prop(propName = "connCoun", propType = 'INT')
		connCoun = 50
		for a in range(connCoun):
			BlenGame.Prop(propName = "from." + Blen.Pad_(a), propType = 'STRING')
			BlenGame.Prop(propName = "to__." + Blen.Pad_(a), propType = 'STRING')
			BlenGame.Prop(propName = "inde." + Blen.Pad_(a), propType = 'INT')
		BlenGame.Prop(propName = "connCut_", propType = 'INT')
		objeList = []
		objeList.append("comp.func.ifeq.0.004.1101")
		objeList.append("comp.func.ifeq.0.005.1101")
		objeList.append("comp.bool.0.016.0100")
		objeList.append("comp.bool.0.017.0100")
		objeList.append("comp.bool.0.018.4010")
		objeList.append("comp.bool.0.019.0110")
		objeList.append("comp.elbo.0.002")
		objeList.append("comp.elbo.0.003")
		objeList.append("comp.elbo.0.004")
		objeList.append("comp.elbo.0.005")
		objeList.append("comp.spli.0.000")
		objeList.append("comp.spli.0.001")
		objeList.append("comp.in__.001")
		objeList.append("comp.out_.002")
		objeList += obstList[:]
		Blen.Sele(scenObje)
		BlenGame.Prop(propName = "compCoun", propType = 'INT', propValu = len(objeList))
		BlenGame.Prop(propName = "compIn__", propType = 'INT', propValu = 12)
		BlenGame.Prop(propName = "connCounCurr", propType = 'INT')
		for a in range(len(objeList)):
			Blen.Sele(scenObje)
			BlenGame.Prop(propName = "compObje." + str(a), propType = 'STRING', propValu = objeList[a])
			BlenGame.Prop(propName = "posx." + str(a), propType = 'FLOAT')
			BlenGame.Prop(propName = "posy." + str(a), propType = 'FLOAT')
			BlenGame.Prop(propName = "posxInde." + str(a), propType = 'INT')
			BlenGame.Prop(propName = "posyInde." + str(a), propType = 'INT')
			BlenGame.Prop(propName = "indx." + str(a), propType = 'INT')
			BlenGame.Prop(propName = "indy." + str(a), propType = 'INT')
			Blen.Sele(objeList[a])
			BlenGame.Prop(propName = "compInde", propType = 'INT', propValu = a)
		hideWall = True
		hideWall = False
		if hideWall:
			for a in range(wallCoun):
				Blen.Sele(obstList[a])
				bpy.context.object.hide = True
				bpy.context.object.hide_render = True
	targList = []
	for obje in bpy.context.scene.objects:
		nam_ = obje.name
		nam_ = nam_.split(".")
		ray_ = False
		for a in range(len(nam_)):
			if nam_[a] == "in__" or nam_[a] == "out_" or nam_[a] == "thr1" or nam_[a] == "thr2" or nam_[a] == "thr3":
				ray_ = True
				prop = nam_[a]
				break
		if ray_:
			Blen.Sele(obje.name)
			BlenGame.Prop(propName = prop, propType = 'BOOL', propValu = True)
			targList.append(obje.name)
	dic_ = Blen.Impo(blenFile = "scen/char/matt/matt.blend", empt = True)
	Blen.Sele("matt.arro.010")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	Blen.Sele("matt.arro.016")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	if impoComp:
		Blen.Sele(name)
		BlenGame.Prop(propName = "obje", propType = 'STRING')
		BlenGame.Prop(propName = "objeType", propType = 'STRING')
	Blen.Sele(name)
	acti = BlenGame.ActiDict()
	acti = BlenGame.ActiDict()
	acti["armsRadi"] = 0.607
	acti["armsRati"] = 3.854
	acti["legsRadi"] = 2.748
	acti["osci"] = 0.032
	acti["tilt"] = 0.219
	acti["cyclSpee"] = 8.65
	acti["spee"] = 0.25
	BlenGame.Char(loca = (0.0, 0.0, 0.0), dire = "scen/char/matt/", acti = [acti])
	Blen.Sele(name)
	BlenGame.Cont(faci = (1.0, 0.0), tracHeig = 4.0)
	Blen.Sele(name)
	lookY___Uppe = 3.0
	lookY___Lowe = 0.1
	BlenGame.CharCame(cameName = "Camera", tab = False, faci = (1.0, 0.0), lookY___Uppe = lookY___Uppe, lookY___Lowe = lookY___Lowe, charList = [name])
	Blen.Sele(name)
	Cycl()
	Blen.Sele(scenObje)
	sens = 'KEYBOARD'
	sensOpti = BlenGame.LogiSensOpti()
	sensDict = BlenGame.LogiSensDict(typ_ = sens)
	sensOpti["use_tap"] = True
	sensDict["key"] = 'ONE'
	BlenGame.Logi(sensName = "one_", sensOpti = sensOpti, sensDict = sensDict, contDict = 'linkSens')
	sensDict["key"] = 'TWO'
	BlenGame.Logi(sensName = "two_", sensOpti = sensOpti, sensDict = sensDict, contDict = 'linkSens')
	sensDict["key"] = 'THREE'
	BlenGame.Logi(sensName = "thre", sensOpti = sensOpti, sensDict = sensDict, contDict = 'linkSens')
	sensList = ["one_", "two_", "thre", "clic"]
	for sens in sensList: BlenGame.Controllers()["scen"].link(BlenGame.Sensors()[sens])
	Blen.Sele(name)
	BlenGame.Prop(propName = "weap", propType = 'INT')
	BlenGame.Prop(propName = "animStar", propType = 'INT', propValu = -1)
	BlenGame.Prop(propName = "animEnd_", propType = 'INT', propValu = -1)
	BlenGame.Prop(propName = "reveRead", propType = 'BOOL')
	BlenGame.Prop(propName = "set_Phas", propType = 'BOOL', propValu = True)
	BlenGame.Prop(propName = "inde", propType = 'INT')
	BlenGame.Prop(propName = "leftLeg_", propType = 'BOOL', propValu = True)
	BlenGame.Prop(propName = "righLeg_", propType = 'BOOL', propValu = True)
	BlenGame.Prop(propName = "leftArm_", propType = 'BOOL', propValu = True)
	BlenGame.Prop(propName = "righArm_", propType = 'BOOL', propValu = True)
	BlenGame.Prop(propName = "ani0Phas", propType = 'INT')
	BlenGame.Prop(propName = "ani0Time", propType = 'INT')
	BlenGame.Prop(propName = "pos0", propType = 'INT')
	BlenGame.Prop(propName = "ani1Phas", propType = 'INT')
	BlenGame.Prop(propName = "ani1Time", propType = 'INT')
	BlenGame.Prop(propName = "pos1", propType = 'INT')
	BlenGame.Prop(propName = "arroInde", propType = 'INT', propValu = -1)
	BlenGame.Prop(propName = "clicStar", propType = 'BOOL')
	sens = 'MOUSE'
	sensOpti = BlenGame.LogiSensOpti()
	sensDict = BlenGame.LogiSensDict(typ_ = sens)
	sensOpti["use_tap"] = True
	sensDict["mouse_event"] = 'LEFTCLICK'
	BlenGame.Logi(sensName = "clic", sensOpti = sensOpti, sensDict = sensDict, contDict = 'linkCont')
	sensOpti["invert"] = True
	BlenGame.Logi(sensName = "clii", sensOpti = sensOpti, sensDict = sensDict, contDict = 'linkCont')
	loca = Blen.LocaRead()
	Blen.Empt()
	Blen.Name(name + "." + "trac.shou")
	Blen.Loca(Math.VectAdd_(loca, (-0.8, -0.4, 1.8)))
	Blen.Pare(name + "." + "look")
	Blen.Sele(name + "." + "trac.posi")
	BlenGame.Prop(propName = "pathPoly", propType = 'INT')
	BlenGame.Prop(propName = "out_", propType = 'BOOL')
	BlenGame.Prop(propName = "use_Prop", propType = 'BOOL', propValu = True)
	pathNorm = True
	#pathNorm = False
	if pathNorm:
		pathObje = "room.main"
		variObje = "scen_obje"
		Blen.Sele(pathObje)
		Blen.Tria()
		minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1 = BlenGame.MMXY()
		markList = ["mark.path.000", "mark.path.001", "mark.path.002", "mark.path.003", "mark.path.004", "mark.path.005", "mark.path.006", "mark.path.007", "mark.path.008"]
		for a in range(9, 31):
			markList.append("mark.path." + Blen.Pad_(a))
		hideList = BlenGame.PathUnwa(pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, markList, leve, [])
		# cut
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.cut_.000", "cut_")
		# push
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.000", "push")
		# pull
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.001", "pull")
		# toggle
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.002", "togg.000")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.003", "togg.001")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.004", "togg.002")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.005", "togg.003")
		# elbo.002 / hole.000
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.006", "hole.000.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.007", "hole.000.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.008", "hole.000.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.009", "hole.000.3")
		# spli.000 / hole.001
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.026", "hole.001.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.027", "hole.001.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.028", "hole.001.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.029", "hole.001.3")
		# elbo.003 / hole.002
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.022", "hole.002.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.023", "hole.002.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.024", "hole.002.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.025", "hole.002.3")
		# elbo.004 / hole.003
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.010", "hole.003.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.011", "hole.003.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.012", "hole.003.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.013", "hole.003.3")
		# spli.001 / hole.004
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.014", "hole.004.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.015", "hole.004.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.016", "hole.004.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.017", "hole.004.3")
		# elbo.005 / hole.005
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.018", "hole.005.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.019", "hole.005.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.020", "hole.005.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.021", "hole.005.3")
		# hole.006
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.050", "hole.006.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.051", "hole.006.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.052", "hole.006.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.053", "hole.006.3")
		# hole.007
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.030", "hole.007.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.031", "hole.007.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.032", "hole.007.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.033", "hole.007.3")
		# hole.008
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.038", "hole.008.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.039", "hole.008.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.040", "hole.008.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.041", "hole.008.3")
		# hole.009
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.046", "hole.009.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.047", "hole.009.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.048", "hole.009.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.049", "hole.009.3")
		# hole.010
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.034", "hole.010.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.035", "hole.010.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.036", "hole.010.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.037", "hole.010.3")
		# hole.011
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.042", "hole.011.0")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.043", "hole.011.1")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.044", "hole.011.2")
		BlenGame.PolySet_(variObje, pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.touc.045", "hole.011.3")
		Blen.Sele(pathObje)
		hideList = BlenGame.PathGeom(scenName = leve, retu = hideList)
		polyList = BlenGame.PolyMark(pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.star")
		Blen.Sele(name)
		BlenGame.Prop(propName = "pathPoly", propType = 'INT', propValu = polyList[0])
		BlenGame.Prop(propName = "pathPolyOffs", propType = 'INT', propValu = polyList[0])
		BlenGame.Prop(propName = "offs", propType = 'FLOAT', propValu = 0.6)
		pathObje = "wall.path"
		Blen.Sele(pathObje)
		Blen.Tria()
		minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1 = BlenGame.MMXY()
		hideList = BlenGame.PathGeom(scenName = leve, retu = hideList)
		polyList = BlenGame.PolyMark(pathObje, minxLis1, minxInd1, maxxLis1, maxxInd1, minyLis1, minyInd1, maxyLis1, maxyInd1, "mark.star")
		Blen.Sele(name)
		BlenGame.Prop(propName = "pathPoly", propType = 'INT', propValu = polyList[0])
		Blen.Sele("mark.star")
		Blen.Dele()
		Blen.Sele(name + "." + "trac.posi")
		BlenGame.PropSet_(propName = "pathPoly", propValu = polyList[0])
		wallCoun = 58
		polyWall = BlenGame.WallList(wallCoun = wallCoun)
		Blen.Sele("wall.path")
		centList = Blen.CentList()
		loca = Blen.LocaRead()
		Blen.Sele("wall.outl")
		vertList = Blen.VertList()
		edgeList = Blen.EdgeList()
		in__List = []
		for a in range(len(centList)):
			if Math.Surr(Math.VectAdd_(loca, centList[a]), vertList, edgeList): in__List.append(a)
		Blen.Dele()
		out_List = []
		for a in range(len(polyWall)):
			if (a in in__List) == False: out_List.append(a)
		Blen.Empt()
		Blen.Name("wall.path.polyWall")
		BlenGame.Prop(propName = "polyWall", propType = 'INT', propValu = len(polyWall))
		for a in range(len(polyWall)):
			if a in out_List:
				BlenGame.Prop(propName = "polyWall." + str(a), propType = 'INT', propValu = 1)
				BlenGame.Prop(propName = "polyWall." + str(a) + ".0", propType = 'INT', propValu = -1)
			else:
				BlenGame.Prop(propName = "polyWall." + str(a), propType = 'INT', propValu = len(polyWall[a]))
				for b in range(len(polyWall[a])):
					BlenGame.Prop(propName = "polyWall." + str(a) + "." + str(b), propType = 'INT', propValu = polyWall[a][b])
		hideList.append(leve + "." + "wall.path.polyWall")
		hideList.append(leve + "." + "wall.path")
	Blen.Sele("Camera")
	Blen.Loca((-3.5, 0.0, 1.8))
	Blen.RotaSet_((90.0, 0.0, -90.0))
	Blen.Name("came")
	BlenGame.Prop(propName = "targName", propType = "STRING")
	dic_ = Blen.Impo(blenFile = "scen/conn/bool_conn.blend")
	Blen.Sele("bool.conn")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	Blen.Sele("trig")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	Blen.Sele("blue")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	Blen.Sele("red_")
	bpy.ops.object.move_to_layer(layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	Blen.Sele("came")
	bpy.ops.transform.translate(value = (0.0, 0.0, 3.0), constraint_axis = (False, False, True), constraint_orientation = 'LOCAL')
	bpy.context.object.data.clip_end = 200.0
	loca = Blen.LocaRead()
	physList = Targ(targList, physList)
	Blen.Sele("reti")
	Blen.RotaSet_((0.0, -90.0, 0.0))
	bpy.ops.transform.translate(value = (0.2, 0.0, 0.0), constraint_axis = (True, False, False), constraint_orientation = 'GLOBAL')
	Blen.Sele(name)
	Blen.Loca((0.0, -80.0, 0.0))
	Blen.RotaSet_((0.0, 0.0, 90.0))
	Blen.Sele(name + "." + "trac.dist")
	bpy.ops.transform.translate(value = (0.0, 1.0, 0.0), constraint_axis = (False, True, False), constraint_orientation = 'GLOBAL')
	bpy.ops.transform.translate(value = (0.0, 0.0, -0.5), constraint_axis = (False, False, True), constraint_orientation = 'GLOBAL')
	Phys(physList)
	Blen.Sele("matt.trac.posi")
	Blen.Loca((-6.0, 0.0, 3.0))
	Blen.Sele("came")
	Blen.Loca((-2.0, 0.0, 1.97606))
	BlenGame.Pref(leve)
	Blen.HideList(hideList)
	Blen.Sele("temp.reti")
	Blen.Hide()
	impoModu = ["acti.py", "anim.py", "came.py", "came_path.py", "cycl.py", "game.py", "look_x.py", "look_y.py", "Math.py", "move.py", "orie.py", "path.py", "Pyth.py", "GameNode.py", "ray_.py"]
	impoModu.append("temp.py")
	for a in range(len(impoModu)):
		bpy.ops.text.open(filepath = "scri" + os.sep + impoModu[a])
		bpy.data.texts[impoModu[a]].use_module = True
	return scenNew_

def Cycl():
	BlenGame.PropSet_(propName = "jog_LegsX00", propValu = -1.1715012788772583)
	BlenGame.PropSet_(propName = "jog_LegsY00", propValu = -0.006090658716857433)
	BlenGame.PropSet_(propName = "jog_LegsX01", propValu = -1.133657693862915)
	BlenGame.PropSet_(propName = "jog_LegsY01", propValu = 0.12255960702896118)
	BlenGame.PropSet_(propName = "jog_LegsX02", propValu = -0.6972678899765015)
	BlenGame.PropSet_(propName = "jog_LegsY02", propValu = 0.37646549940109253)
	BlenGame.PropSet_(propName = "jog_LegsX03", propValu = -0.45101505517959595)
	BlenGame.PropSet_(propName = "jog_LegsY03", propValu = 0.39450353384017944)
	BlenGame.PropSet_(propName = "jog_LegsX04", propValu = -0.09052211791276932)
	BlenGame.PropSet_(propName = "jog_LegsY04", propValu = 0.20272567868232727)
	BlenGame.PropSet_(propName = "jog_LegsX05", propValu = 0.05977433919906616)
	BlenGame.PropSet_(propName = "jog_LegsY05", propValu = 0.26926273107528687)
	BlenGame.PropSet_(propName = "jog_LegsX06", propValu = 0.6383165121078491)
	BlenGame.PropSet_(propName = "jog_LegsY06", propValu = 0.3466039299964905)
	BlenGame.PropSet_(propName = "jog_LegsX07", propValu = 0.5497186183929443)
	BlenGame.PropSet_(propName = "jog_LegsY07", propValu = 0.10148997604846954)
	BlenGame.PropSet_(propName = "jog_LegsX08", propValu = 0.7705233693122864)
	BlenGame.PropSet_(propName = "jog_LegsY08", propValu = -0.0678902268409729)
	BlenGame.PropSet_(propName = "jog_LegsX09", propValu = 0.9093456268310547)
	BlenGame.PropSet_(propName = "jog_LegsY09", propValu = -0.003694202285259962)
	BlenGame.PropSet_(propName = "jog_LegsX10", propValu = 0.5004748106002808)
	BlenGame.PropSet_(propName = "jog_LegsY10", propValu = -0.2482115477323532)
	BlenGame.PropSet_(propName = "jog_LegsX11", propValu = 0.15416473150253296)
	BlenGame.PropSet_(propName = "jog_LegsY11", propValu = -0.4601432681083679)
	BlenGame.PropSet_(propName = "jog_LegsX12", propValu = -0.04775390774011612)
	BlenGame.PropSet_(propName = "jog_LegsY12", propValu = -0.12878575921058655)
	BlenGame.PropSet_(propName = "jog_LegsX13", propValu = -0.6007677912712097)
	BlenGame.PropSet_(propName = "jog_LegsY13", propValu = -0.17720341682434082)
	BlenGame.PropSet_(propName = "jog_LegsX14", propValu = -0.8619587421417236)
	BlenGame.PropSet_(propName = "jog_LegsY14", propValu = -0.3732094168663025)
	BlenGame.PropSet_(propName = "jog_LegsX15", propValu = -1.1164268255233765)
	BlenGame.PropSet_(propName = "jog_LegsY15", propValu = -0.23773682117462158)

def Targ(targList, physList = []):
	import bpy
	import math
	Blen.Sele("came")
	Blen.PareClea()
	loca = Blen.LocaRead()
	dic_ = Blen.Impo(blenFile = "scen/reti.blend")
	Blen.Sele("reti")
	Blen.Loca(loca)
	Blen.Scal((0.02, 0.02, 0.02))
	Blen.Pare("came")
	Blen.Sele("came")
	Blen.Pare("matt.trac.posi")
	for targ in targList:
		Blen.Sele(targ)
		BlenGame.Prop(propName = "targ", propType = 'BOOL')
		BlenGame.Prop(propName = "hit_", propType = 'BOOL')
		physList.append(targ)
	return physList

def Phys(physList = []):
	import bpy
	for obje in bpy.context.scene.objects:
		if (obje.name in physList) == False:
			obje.game.physics_type = 'NO_COLLISION'

main()

