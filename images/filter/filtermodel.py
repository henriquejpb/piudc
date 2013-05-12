# -*- coding: utf-8 -*-
import sys
import re
import os
import time
import subprocess
from py4j.java_gateway import JavaGateway
from py4j.protocol import Py4JJavaError
from practica_PI import settings

class FilterModel:
    def __init__(self): 
        #
        # aqui iniciara aquela funções do GtkBuilder pra carregar a imagem aqui
        # Esse módulo é onde vai ficar a interface
        #
        app = os.path.join(settings.BASE_DIR, 'lib/executavel.jar')
        os.system("java -jar " + app +  " &") # executa em segundo plano
        time.sleep(3)	# espera 3 segundos para a JVM executar a aplicação
        gateway = JavaGateway()   #conexion con Java
        self.filtros = gateway.entry_point.getFiltros()	# retorna objeto para acceder los filtros

    def openImage(self,directory):     # esa funcion va abrir la imagen e cargar el directorio
        absolute_path = os.path.join(settings.BASE_DIR, directory[1:])
        self.dirImage = absolute_path

    def callMethod(self, methodName, *args):
        # try:
        if len(args) > 0 and args[0]:
            getattr(self, methodName)(int(args[0])) 
        else:
            getattr(self, methodName)() 
        # except Py4JJavaError, e:
            # raise e
        # finally:
        self.finish()

    def finish(self):
        killapp = os.path.join(settings.BASE_DIR, 'lib/killjvm.sh')
        pid = subprocess.Popen(['/bin/sh', os.path.join(settings.APP_DIR, killapp)])	# crea proceso para matar processo em porta 25333
        pid.communicate() # o processo pai espera ele terminar  

    def bandaRed(self):
        print "bandaRed"
        self.filtros.bandaRed(self.dirImage)

    def bandaRedMono(self):
        print "bandaRedMono"
        self.filtros.bandaRedMono(self.dirImage)

    def bandaBlue(self):
        print "bandaBlue"
        self.filtros.bandaBlue(self.dirImage)   

    def bandaBlueMono(self):
        print "bandaBlueMono"
        self.filtros.bandaBlueMono(self.dirImage)

    def bandaGreen(self):
        print "bandaGreen"
        self.filtros.bandaGreen(self.dirImage)

    def bandaGreenMono(self):
        print "bandaGreenMono"
        self.filtros.bandaGreenMono(self.dirImage)

    def brilhoAditivo(self,constant):
        print "brilhoAditivo " + str(constant)
        self.filtros.brilhoAditivo(self.dirImage,constant)

    def brilhoAditivoRed(self,constant):
        print "brilhoAditivoRed " + str(constant)
        self.filtros.brilhoAditivoRed(self.dirImage,constant)

    def brilhoAditivoBlue(self,constant):
        print "brilhoAditivoBlue " + str(constant)
        self.filtros.brilhoAditivoBlue(self.dirImage,constant)

    def brilhoAditivoGreen(self,constant):
        print "brilhoAditivoGree " + str(constant)
        self.filtros.brilhoAditivoGreen(self.dirImage,constant)

    def brilhoMultiplicativo(self,constant):
        print "brilhoMultiplicativo " + str(constant)
        self.filtros.brilhoMultiplicativo(self.dirImage,constant)

    def brilhoMultiplicativoR(self,constant):
        print "brilhoMultiplicativoR" + str(constant)        
        self.filtros.brilhoMultiplicativoR(self.dirImage,2)

    def brilhoMultiplicativoB(self,constant):
        print "brilhoMultiplicativoB " + str(constant)
        self.filtros.brilhoMultiplicativoB(self.dirImage,constant)

    def brilhoMultiplicativoG(self,constant):
        print "brilhoMultiplicativoG " + str(constant)
        self.filtros.brilhoMultiplicativoG(self.dirImage,constant)

    def media(self,constant):
        print "media " + str(constant)
        self.filtros.media(self.dirImage,constant)

    def mediana(self,constant):
        print "mediana " + str(constant)
        self.filtros.mediana(self.dirImage,constant)

    def negativo(self):
        print "negativo"
        self.filtros.negativo(self.dirImage)                     

    def negativoBanda(self,banda):
        print "negativoBanda " + str(banda)
        self.filtros.negativoBanda(self.dirImage,banda)

