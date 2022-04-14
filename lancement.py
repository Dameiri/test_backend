
import json
import csv
import pandas as pd
from scipy.fftpack import idct 
 
data= csv.DictReader('dummy_meshes.csv')

id = []
height= []
weight=[]
trames=[]
colors_names = []
mass_surf=[]
is_compat_interior_wall= []
comb=   []     
roll_pallet=[]     
mass_surf=[]

for col in  data:
    id.append(col['id'])
    height.append(col['mesh_height'])
    weight.append(col['mesh_width'])
    trames.append(col['trame'])
    colors_names.append(col['color_names'])
    is_compat_interior_wall.append(col['is_compat_interior_wall'])
    comb.append(col['mass_comb;'])
    roll_pallet.append(col['roll_pallet'])
    mass_surf.append(col['mass_surf'])
  
  