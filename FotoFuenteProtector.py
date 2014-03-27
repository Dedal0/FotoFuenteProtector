#!/usr/bin/env python

#By Dedalo (@SeguridadBlanca)

import pyexiv2
import sys
import os 

END = "\033[0m"
blue = "\033[0;34m"
red = "\033[1;91m"
green = "\033[1;32m"

def readdata():
	extractdata = pyexiv2.ImageMetadata(foto)
	extractdata.read()
	for valorexif in extractdata.exif_keys:
		valordata = extractdata[valorexif]
		print red + valorexif + END + green + " -----> " + END + blue + valordata.raw_value + END

def joder():
	writedata = pyexiv2.ImageMetadata(foto)
	writedata.read()
	a = writedata.exif_keys
	for prueba in a:
		try:
			writedata[prueba] = "NOT"
		except:
			try:
				writedata[prueba] = 0
			except:
				pass

	writedata.write()
	print green + "La metadata de la imagen fue modificada con exito" + END

def nohayfile():
	print "Ese archivo no existe"

def hayfile():
	if action == "read":
		readdata()
	elif action == "write":
		joder()
	else:
		print "Elije una accion conocida"

def existef():
	if existe == True:
		hayfile()
	else:
		nohayfile()

def help():
	print red
	print "======= Modo de uso: =======" + END
	print green + "python FotoFuenteProtector.py rutadelaimagen.jpg" + END + blue + " opcion" + END
	print red + "opciones:" + END
	print blue + "read:" + END + " leer la metadata de la imagen"
	print blue + "write:" + END + " sobreescribir la metadata de la imagen"


if len(sys.argv) < 3:
	help()
else:
	foto = sys.argv[1]
	action = sys.argv[2]
	existe = os.path.isfile(foto)
	existef()
