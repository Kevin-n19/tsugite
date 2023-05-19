#!/usr/bin/env python3

GeoID = 0

def Progleadingline(file_name,real_tim_dims):
	strprog = ""
	strprog = strprog + "BEGIN ID CID3\n"
	strprog = strprog + "REL=5.0\n"
	strprog = strprog + "END ID\n"
	strprog = strprog + "BEGIN MAINDATA\n"
	strprog = strprog + f"	LPX={real_tim_dims[0]}\n"
	strprog = strprog + f"	LPY={real_tim_dims[2]}+500\n"
	strprog = strprog + f"	LPZ={real_tim_dims[1]}\n"
	strprog = strprog + "	ORLST=\"\"\n"
	strprog = strprog + "	SIMMETRY=0\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "	\n"
	strprog = strprog + "END MAINDATA\n"
	strprog = strprog + "\n"
	
	strprog = strprog + "BEGIN VB\n"
	strprog = strprog + f"	VBline=\"'{file_name}\"\n"
	strprog = strprog + "END VB\n"
	
	return strprog

def ProgTrailingLine():
	strprog = ""
	strprog = strprog + "BEGIN VB\n"
	strprog = strprog + "	VBline=\"\"\n"
	strprog = strprog + "END VB\n"
	return strprog
	
def OutputFeed(move):
	global GeoID
	strprog = ""
	
		#Description class MillMove, each move is line or Ard with start and end point.
		#FirstMouv = False ; #LastMove = False
		#Start_X ; #Start_Y  ;#Start_Z 
		#End_X  ;#End_Y ; #End_Z 
		#Center_X ; Center_Y  ; Center_Z 
		#Is_Arc = False ; Clockwise = False ; R = 0
		#Modal_X = False ; Modal_Y = False ; Modal_Z = False  
		# Vect_X ; Vect_Y ; Vect_X 
		#ToolDia = 0 ; ToolName = ''

	if move.ToolName == '': move.ToolName = "DIAM" + str(move.ToolDia)

	if move.FirstMouv:
		strprog = strprog + "\n"
		strprog = strprog + "BEGIN MACRO\n"
		strprog = strprog + "	NAME=ROUT\n"
		strprog = strprog + "	PARAM,NAME=SIDE,VALUE=0\n" 	#FACE
		strprog = strprog + "	PARAM,NAME=CRN,VALUE=1\n" 	#CORNER REF
		strprog = strprog + "	PARAM,NAME=Z,VALUE=0\n"
		strprog = strprog + "	PARAM,NAME=DP,VALUE=\n"		#PROF
		strprog = strprog + "	PARAM,NAME=ISO,VALUE=\"\"\n"
		strprog = strprog + "	PARAM,NAME=RSP,VALUE=0\n"
		strprog = strprog + "	PARAM,NAME=VTR,VALUE=0\n"
		strprog = strprog + "	PARAM,NAME=OPT,VALUE=NO\n"
		strprog = strprog + "	PARAM,NAME=THR,VALUE=0\n"	
		strprog = strprog + f"	PARAM,NAME=TNM,VALUE=\"{move.ToolName}\"\n"	#TOOLNAME
		strprog = strprog + "	PARAM,NAME=CRC,VALUE=0\n"		#TOOL COMP
		strprog = strprog + "	PARAM,NAME=LAY,VALUE=\"ROUT\"\n"
		strprog = strprog + "END MACRO\n"

		GeoID += 1

		strprog = strprog + "\n"
		strprog = strprog + "BEGIN MACRO\n"
		strprog = strprog + "	NAME=START_POINT\n"
		strprog = strprog + f"	PARAM,NAME=ID,VALUE={GeoID}\n"	#ID INCREMENTIEL
		strprog = strprog + f"	PARAM,NAME=X,VALUE={move.Start_X}\n"
		strprog = strprog + f"	PARAM,NAME=Y,VALUE={move.Start_Y}\n"
		strprog = strprog + f"	PARAM,NAME=Z,VALUE={move.Start_Z}\n"
		strprog = strprog + "END MACRO\n"

	else:
		if move.Is_Arc:
			strprog = strprog + "\n"
		else:
			GeoID += 1

			strprog = strprog + "\n"
			strprog = strprog + "BEGIN MACRO\n"
			strprog = strprog + "	NAME=LINE_EP\n"
			strprog = strprog + f"	PARAM,NAME=ID,VALUE={GeoID}\n"	#ID INCREMENTIEL
			strprog = strprog + f"	PARAM,NAME=XE,VALUE={move.End_X}\n"
			strprog = strprog + f"	PARAM,NAME=YE,VALUE={move.End_Y}\n"
			strprog = strprog + "	PARAM,NAME=ZS,VALUE=0\n"
			strprog = strprog + f"	PARAM,NAME=ZE,VALUE={move.Vect_Z}\n"
			strprog = strprog + "END MACRO\n"

	if move.LastMove:
		GeoID += 1

		strprog = strprog + "\n"
		strprog = strprog + "BEGIN MACRO\n"
		strprog = strprog + "	NAME=ENDPATH\n"
		strprog = strprog + f"	PARAM,NAME=ID,VALUE={GeoID}\n"	#ID INCREMENTIEL
		strprog = strprog + "END MACRO\n"
	
	return strprog









