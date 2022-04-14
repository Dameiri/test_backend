from cgitb import grey
from curses import color_content
from distutils.command.upload import upload
import enum
import pickle
import numpy as np
import json
from Colors import Colors 
from Trames import Trames
import requests

# dump -> enregistrer un dic  != dumps
class Meshes:
    trame='T2Ra1M2E2'
    mass_surf=0
    is_compat_interior_wall=False
    mesh_height=0
    mesh_width=0
    mesh_height=0
    comb=0
    roll_pallet=0
    colors_names=[]
    i=0
   
    def __init__(self, trame,mass_surf,is_compainterwall,height, width, comb,roll_pallet,uniqueColor):
        #essayer avec try except 
        if trame in Trames:
                self.trame=trame
        else:
            print("erreur de création du meshe")
        if  uniqueColor.lower() in Colors.value:
                self.colors_names=uniqueColor.lower()
        else:
            print("erreur de création du meshe")
        if   width>-1 and height>-1 and mass_surf>-1:
            self.mass_surf=mass_surf
            self.mesh_height=height
            self.mesh_width=width
            self.is_compat_interior_wall=is_compainterwall
            self.roll_pallet=roll_pallet
            self.comb=comb
            self.id="variant_"+str(i)
            i=i+1
        else:
            print("erreur de création du meshe")    
     
       
    def __repr__(self):
        return f'Meshe(trame={self.trame},width={self.mesh_width},height={self.mesh_height}, )'


    def MappingToDict(self):
        return {"id":self.id,
                "trame":self.trame,
                "mass_surf":self.mass_surf
                "colors":self.colors_names,
                "mass_surf":self.mass_surf,
                "is_compainterwall":self.is_compat_interior_wall,
                "height": self.mesh_height,
                "width": self.mesh_width,
                "roll_pallet":self.roll_pallet,
                "comb":self.comb,
                   }


  
    def StockerMeshes(self):
        output=open("outpout.pickle","wb")
        pickle.dump( self.MappingToDict(),output)
        output.close()



r=Meshes('T2Ra1M2E2',1,True,1,1,3,1,grey)
#r=Meshes('T2Ra1M2E2',1,True,1,1,3,1,green) -- couleur inexistante


                    