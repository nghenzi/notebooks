from svgpath2mpl import parse_path

import matplotlib.pyplot as plt      
import numpy as np                   
# Use Inkscape to edit SVG, 
# Path -> Combine to convert multiple paths into a single path
# Use Path -> Object to path to convert objects to SVG path
smiley = parse_path("""m 739.01202,391.98936 c 13,26 13,57 9,85 -6,27 -18,52 -35,68 -21,20 -50,23 -77,18 -15,-4 -28,-12 -39,-23 -18,-17 -30,-40 -36,-67 -4,-20 -4,-41 0,-60 l 6,-21 z m -302,-1 c 2,3 6,20 7,29 5,28 1,57 -11,83 -15,30 -41,52 -72,60 -29,7 -57,0 -82,-15 -26,-17 -45,-49 -50,-82 -2,-12 -2,-33 0,-45 1,-10 5,-26 8,-30 z M 487.15488,66.132209 c 121,21 194,115.000001 212,233.000001 l 0,8 25,1 1,18 -481,0 c -6,-13 -10,-27 -13,-41 -13,-94 38,-146 114,-193.000001 45,-23 93,-29 142,-26 z m -47,18 c -52,6 -98,28.000001 -138,62.000001 -28,25 -46,56 -51,87 -4,20 -1,57 5,70 l 423,1 c 2,-56 -39,-118 -74,-157 -31,-34 -72,-54.000001 -116,-63.000001 -11,-2 -38,-2 -49,0 z m 138,324.000001 c -5,6 -6,40 -2,58 3,16 4,16 10,10 14,-14 38,-14 52,0 15,18 12,41 -6,55 -3,3 -5,5 -5,6 1,4 22,8 34,7 42,-4 57.6,-40 66.2,-77 3,-17 1,-53 -4,-59 l -145.2,0 z m -331,-1 c -4,5 -5,34 -4,50 2,14 6,24 8,24 1,0 3,-2 6,-5 17,-17 47,-13 58,9 7,16 4,31 -8,43 -4,4 -7,8 -7,9 0,0 4,2 8,3 51,17 105,-20 115,-80 3,-15 0,-43 -3,-53 z m 61,-266 c 0,0 46,-40 105,-53.000001 66,-15 114,7 114,7 0,0 -14,76.000001 -93,95.000001 -76,18 -126,-49 -126,-49 z""")
smiley.vertices -= smiley.vertices.mean(axis=0)
x = np.linspace(-3, 3, 20)          
plt.plot(x, np.sin(x), marker=smiley, markersize=20, color='c')
plt.show()


#%%
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np, os, re
import matplotlib.pyplot as plt

os.chdir('C:/corina/states')

xmin, xmax = -3, 3 
ymin, ymax = -3, 3 

Ef = [-3.77, -2.99]
Nstates = 142
Natoms = 190

with open('pdos.out') as fp: data = fp.readlines() 
    
_#%% File parsing 
for num, line in enumerate(data,1):
    if 'psi = ' in line:
        
        Nstate = int(re.findall('[0-9]+', data[num-2])[0])
        energy = float(re.findall('-?\d+\.\d+', data[num-2])[0])
        print(num, Nstate, energy)
        psi = [line]
        for jkl in range(num+1, num+20):
            if 
 
        #%%
l = ' ==== e( 142) =     1.38556 eV ==== '

float(re.findall('-?\d+\.\d+', l)[0])


#%%
lst = [0.1, 0.4, 0.2, 0.8, 0.7, 1.1, 2.2, 4.1, 4.9, 5.2, 4.3, 3.2]

pred = lambda cur, prev: abs(cur-prev) <= 1
p = None
res = [p := i for i in lst if p is None or pred(p, i)]
print (res)

#%%

from matplotlib import pyplot as plt
plt.style.use(['science','nature'])
for e in [0.9999,0.9999,0.999,0.99,0.9,0.7]:
    plt.semilogx([p:= e*p  if (i!=0) else (p:=1) for i in range(100000) ],'o')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('N',fontsize=18)
plt.ylabel('h [m]',fontsize=18)
plt.tight_layout()
#%%

import pandas as pd 
csv =""" particle,symbol,cols,rows,generation,category,class,particle_type,mass,charge,spin,statistics,symbolgray,symbolwhite 987
up,u,1,1,I,fermion,quark,Matter particle,≃ 2.2 MeV,⅔,½,Fermi–Dirac,https://mlwild.net/images/upquark-gray.svg,https://mlwild.net/images/upquark-white.svg 987
charm,c,2,1,II,fermion,quark,Matter particle,≃ 1.28 GeV,⅔,½,Fermi–Dirac,https://mlwild.net/images/charmquark-gray.svg,https://mlwild.net/images/charmquark-white.svg 987
top,t,3,1,III,fermion,quark,Matter particle,≃ 73.1 GeV,⅔,½,Fermi–Dirac,https://mlwild.net/images/topquark-gray.svg,https://mlwild.net/images/topquark-white.svg 987
down,d,1,2,I,fermion,quark,Matter particle,≃ 4.7 MeV,-⅓,½,Fermi–Dirac,https://mlwild.net/images/downquark-gray.svg,https://mlwild.net/images/downquark-white.svg 987
strange,s,2,2,II,fermion,quark,Matter particle,≃ 96 MeV,-⅓,½,Fermi–Dirac,https://mlwild.net/images/strangequark-gray.svg,https://mlwild.net/images/strangequark-white.svg 987
bottom,b,3,2,III,fermion,quark,Matter particle,≃ 4.18 GeV,-⅓,½,Fermi–Dirac,https://mlwild.net/images/bottomquark-gray.svg,https://mlwild.net/images/bottomquark-white.svg 987
electron,e,1,3,I,fermion,lepton,Matter particle,≃ 0.511 MeV,-1,½,Fermi–Dirac,https://mlwild.net/images/electron-gray.svg,https://mlwild.net/images/electron-white.svg 987
muon,μ,2,3,II,fermion,lepton,Matter particle,≃ 105.66 MeV,-1,½,Fermi–Dirac,https://mlwild.net/images/muon-gray.svg,https://mlwild.net/images/muon-white.svg 987
tauon,τ,3,3,III,fermion,lepton,Matter particle,≃ 1.7768 GeV,-1,½,Fermi–Dirac,https://mlwild.net/images/tauon-gray.svg,https://mlwild.net/images/tauon-white.svg 987
electron neutrino,ν_e,1,4,I,fermion,lepton,Matter particle,< 1.0 eV,0,½,Fermi–Dirac,https://mlwild.net/images/eneutrino-gray.svg,https://mlwild.net/images/eneutrino-white.svg 987
muon neutrino,ν_μ,2,4,II,fermion,lepton,Matter particle,< 0.17 MeV,0,½,Fermi–Dirac,https://mlwild.net/images/muneutrino-gray.svg,https://mlwild.net/images/muneutrino-white.svg 987
tauon neutrino,ν_τ,3,4,III,fermion,lepton,Matter particle,< 18.2 MeV,0,½,Fermi–Dirac,https://mlwild.net/images/tauneutrino-gray.svg,https://mlwild.net/images/tauneutrino-white.svg 987
gluon,g,4,1,vb,boson,vector boson,Force carrier,= 0 GeV,0,1,Bose-Einstein,https://mlwild.net/images/gluon-gray.svg,https://mlwild.net/images/gluon-white.svg 987
photon,γ,4,2,vb,boson,vector boson,Force carrier,= 0 GeV,0,1,Bose-Einstein,https://mlwild.net/images/photon-gray.svg,https://mlwild.net/images/photon-white.svg 987
Z boson,Z,4,3,vb,boson,vector boson,Force carrier,≃ 91.19 GeV,0,1,Bose-Einstein,https://mlwild.net/images/zboson-gray.svg,https://mlwild.net/images/zboson-white.svg 987
W boson,W,4,4,vb,boson,vector boson,Force carrier,≃80.39 GeV,±1,1,Bose-Einstein,https://mlwild.net/images/wboson-gray.svg,https://mlwild.net/images/wboson-white.svg 987
higgs,H,5,1,sb,boson,scalar boson,Scalar particle,≃124.97 GeV,0,0,Bose-Einstein,https://mlwild.net/images/higgs-gray.svg,https://mlwild.net/images/higgs-white.svg 987
"""

a = csv.split('987')

for row in a: print(len(row.split(',')))
#%%
from functools import wraps 

from time import time, sleep
def decorator(func):
    @wraps(func)
    def actual_func(*args, **kwargs):
        """Inner function within decorator, which does the actual work"""
        print(f"Before Calling {func.__name__}")
        start=time()
        func(*args, **kwargs)
        sleep(0.2)
        print(f"After Calling {func.__name__}",time()-start)

    return actual_func

@decorator
def greet(name):
    """Says hello to somebody"""
    print(f"Hello, {name}!")

greet("Martin")


#%%

dates = [
    "2020-01-01",
    "2020-02-04",
    "2020-02-01",
    "2020-01-24",
    "2020-01-08",
    "2020-02-10",
    "2020-02-15",
    "2020-02-11",
]

counts = [1, 4, 3, 8, 0, 7, 9, 2]

from itertools import compress
bools = [n > 3 for n in counts]
print(list(compress(dates, bools)))  # Compress returns iterator!
#  ['2020-02-04', '2020-01-24', '2020-02-10', '2020-02-15']
counts[bools]
bools

#%%
from itertools import cycle

for j, i in zip(range(7),cycle(['red','blue','yellow'])):
    print (j,i)
    sleep(0.2)

#%%
import svgutils

h, color = 70, '#8e8e94'
svg_vsc = f""" <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 48 48" width="{h}px" height="{h}px"><path fill="#29b6f6" d="M44,11.11v25.78c0,1.27-0.79,2.4-1.98,2.82l-8.82,4.14L34,33V15L33.2,4.15l8.82,4.14 C43.21,8.71,44,9.84,44,11.11z"/><path fill="#0277bd" d="M9,33.896L34,15V5.353c0-1.198-1.482-1.758-2.275-0.86L4.658,29.239 c-0.9,0.83-0.849,2.267,0.107,3.032c0,0,1.324,1.232,1.803,1.574C7.304,34.37,8.271,34.43,9,33.896z"/><path fill="#0288d1" d="M9,14.104L34,33v9.647c0,1.198-1.482,1.758-2.275,0.86L4.658,18.761 c-0.9-0.83-0.849-2.267,0.107-3.032c0,0,1.324-1.232,1.803-1.574C7.304,13.63,8.271,13.57,9,14.104z"/></svg>"""
svg_settings = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M19.43 12.98c.04-.32.07-.64.07-.98 0-.34-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.09-.16-.26-.25-.44-.25-.06 0-.12.01-.17.03l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.06-.02-.12-.03-.18-.03-.17 0-.34.09-.43.25l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98 0 .33.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.09.16.26.25.44.25.06 0 .12-.01.17-.03l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.06.02.12.03.18.03.17 0 .34-.09.43-.25l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zm-1.98-1.71c.04.31.05.52.05.73 0 .21-.02.43-.05.73l-.14 1.13.89.7 1.08.84-.7 1.21-1.27-.51-1.04-.42-.9.68c-.43.32-.84.56-1.25.73l-1.06.43-.16 1.13-.2 1.35h-1.4l-.19-1.35-.16-1.13-1.06-.43c-.43-.18-.83-.41-1.23-.71l-.91-.7-1.06.43-1.27.51-.7-1.21 1.08-.84.89-.7-.14-1.13c-.03-.31-.05-.54-.05-.74s.02-.43.05-.73l.14-1.13-.89-.7-1.08-.84.7-1.21 1.27.51 1.04.42.9-.68c.43-.32.84-.56 1.25-.73l1.06-.43.16-1.13.2-1.35h1.39l.19 1.35.16 1.13 1.06.43c.43.18.83.41 1.23.71l.91.7 1.06-.43 1.27-.51.7 1.21-1.07.85-.89.7.14 1.13zM12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 6c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/></svg>"""
svg_ar = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24" x="0" y="0"/></g><g><g><path d="M3,4c0-0.55,0.45-1,1-1h2V1H4C2.34,1,1,2.34,1,4v2h2V4z"/><path d="M3,20v-2H1v2c0,1.66,1.34,3,3,3h2v-2H4C3.45,21,3,20.55,3,20z"/><path d="M20,1h-2v2h2c0.55,0,1,0.45,1,1v2h2V4C23,2.34,21.66,1,20,1z"/><path d="M21,20c0,0.55-0.45,1-1,1h-2v2h2c1.66,0,3-1.34,3-3v-2h-2V20z"/><path d="M19,14.87V9.13c0-0.72-0.38-1.38-1-1.73l-5-2.88c-0.31-0.18-0.65-0.27-1-0.27s-0.69,0.09-1,0.27L6,7.39 C5.38,7.75,5,8.41,5,9.13v5.74c0,0.72,0.38,1.38,1,1.73l5,2.88c0.31,0.18,0.65,0.27,1,0.27s0.69-0.09,1-0.27l5-2.88 C18.62,16.25,19,15.59,19,14.87z M11,17.17l-4-2.3v-4.63l4,2.33V17.17z M12,10.84L8.04,8.53L12,6.25l3.96,2.28L12,10.84z M17,14.87l-4,2.3v-4.6l4-2.33V14.87z"/></g></g></svg>"""
svg_table = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/><path d="M19,7H9C7.9,7,7,7.9,7,9v10c0,1.1,0.9,2,2,2h10c1.1,0,2-0.9,2-2V9C21,7.9,20.1,7,19,7z M19,9v2H9V9H19z M13,15v-2h2v2H13z M15,17v2h-2v-2H15z M11,15H9v-2h2V15z M17,13h2v2h-2V13z M9,17h2v2H9V17z M17,19v-2h2v2H17z M6,17H5c-1.1,0-2-0.9-2-2V5 c0-1.1,0.9-2,2-2h10c1.1,0,2,0.9,2,2v1h-2V5H5v10h1V17z"/></g></svg>"""
svg_triangle = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M17.99 11.57H20V0L0 20h11.56v-2H4.83L17.99 4.83v6.74zm5.78 8.75l-1.07-.83c.02-.16.04-.32.04-.49 0-.17-.01-.33-.04-.49l1.06-.83c.09-.08.12-.21.06-.32l-1-1.73c-.06-.11-.19-.15-.31-.11l-1.24.5c-.26-.2-.54-.37-.85-.49l-.19-1.32c-.01-.12-.12-.21-.24-.21h-2c-.12 0-.23.09-.25.21l-.19 1.32c-.3.13-.59.29-.85.49l-1.24-.5c-.11-.04-.24 0-.31.11l-1 1.73c-.06.11-.04.24.06.32l1.06.83c-.02.16-.03.32-.03.49 0 .17.01.33.03.49l-1.06.83c-.09.08-.12.21-.06.32l1 1.73c.06.11.19.15.31.11l1.24-.5c.26.2.54.37.85.49l.19 1.32c.02.12.12.21.25.21h2c.12 0 .23-.09.25-.21l.19-1.32c.3-.13.59-.29.84-.49l1.25.5c.11.04.24 0 .31-.11l1-1.73c.06-.11.03-.24-.06-.32zm-4.78.18c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>"""
svg_dev = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M7 5h10v2h2V3c0-1.1-.9-1.99-2-1.99L7 1c-1.1 0-2 .9-2 2v4h2V5zm8.41 11.59L20 12l-4.59-4.59L14 8.83 17.17 12 14 15.17l1.41 1.42zM10 15.17L6.83 12 10 8.83 8.59 7.41 4 12l4.59 4.59L10 15.17zM17 19H7v-2H5v4c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2v-4h-2v2z"/></svg>"""
svg_drive_file = f""" <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/></g><g><g><polygon points="15,16 11,20 21,20 21,16"/><path d="M12.06,7.19L3,16.25V20h3.75l9.06-9.06L12.06,7.19z M5.92,18H5v-0.92l7.06-7.06l0.92,0.92L5.92,18z"/><path d="M18.71,8.04c0.39-0.39,0.39-1.02,0-1.41l-2.34-2.34C16.17,4.09,15.92,4,15.66,4c-0.25,0-0.51,0.1-0.7,0.29l-1.83,1.83 l3.75,3.75L18.71,8.04z"/></g></g></svg>"""
svg_logout = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M17,8l-1.41,1.41L17.17,11H9v2h8.17l-1.58,1.58L17,16l4-4L17,8z M5,5h7V3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h7v-2H5V5z"/></g></svg>"""

h=45
svg_subject = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M14 17H4v2h10v-2zm6-8H4v2h16V9zM4 15h16v-2H4v2zM4 5v2h16V5H4z"/></svg>"""
svg_notif = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M12,18.5c0.83,0,1.5-0.67,1.5-1.5h-3C10.5,17.83,11.17,18.5,12,18.5z M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10 c5.52,0,10-4.48,10-10S17.52,2,12,2z M12,20c-4.41,0-8-3.59-8-8s3.59-8,8-8c4.41,0,8,3.59,8,8S16.41,20,12,20z M16,11.39 c0-2.11-1.03-3.92-3-4.39V6.5c0-0.57-0.43-1-1-1s-1,0.43-1,1V7c-1.97,0.47-3,2.27-3,4.39V14H7v2h10v-2h-1V11.39z M14,14h-4v-3 c0-1.1,0.9-2,2-2s2,0.9,2,2V14z"/></g></svg>"""
svg_mediation = f"""<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><rect fill="none" height="24" width="24"/><path d="M18,16l4-4l-4-4v3h-5.06c-0.34-3.1-2.26-5.72-4.94-7.05C7.96,2.31,6.64,1,5,1C3.34,1,2,2.34,2,4s1.34,3,3,3 c0.95,0,1.78-0.45,2.33-1.14C9.23,6.9,10.6,8.77,10.92,11h-3.1C7.4,9.84,6.3,9,5,9c-1.66,0-3,1.34-3,3s1.34,3,3,3 c1.3,0,2.4-0.84,2.82-2h3.1c-0.32,2.23-1.69,4.1-3.58,5.14C6.78,17.45,5.95,17,5,17c-1.66,0-3,1.34-3,3s1.34,3,3,3 c1.64,0,2.96-1.31,2.99-2.95c2.68-1.33,4.6-3.95,4.94-7.05H18V16z"/></g></svg>"""
svg_pivot = f""" <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><g><path d="M0,0h24v24H0V0z" fill="none"/></g><g><path d="M21,5c0-1.1-0.9-2-2-2h-9v5h11V5z M3,19c0,1.1,0.9,2,2,2h3V10H3V19z M3,5v3h5V3H5C3.9,3,3,3.9,3,5z M18,8.99L14,13 l1.41,1.41l1.59-1.6V15c0,1.1-0.9,2-2,2h-2.17l1.59-1.59L13,14l-4,4l4,4l1.41-1.41L12.83,19H15c2.21,0,4-1.79,4-4v-2.18l1.59,1.6 L22,13L18,8.99z"/></g></svg>"""
svg_tune = f""" <svg xmlns="http://www.w3.org/2000/svg" height="{h}px" viewBox="0 0 24 24" width="{h}px" fill="{color}"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M5 2c0-.55-.45-1-1-1s-1 .45-1 1v4H1v10c0 1.3.84 2.4 2 2.82V23h2v-4.18C6.16 18.4 7 17.3 7 16V6H5V2zM4 17c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4H3zM13 2c0-.55-.45-1-1-1s-1 .45-1 1v4H9v10c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.42 2-1.52 2-2.82V6h-2V2zm-1 15c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4h-2zm10-6V2c0-.55-.45-1-1-1s-1 .45-1 1v4h-2v10c0 1.3.84 2.4 2 2.82V23h2v-4.18c1.16-.42 2-1.52 2-2.82V6h-2zm-1 11c-.55 0-1-.45-1-1v-2h2v2c0 .55-.45 1-1 1zm-1-5V8h2v4h-2z"/></svg>"""

#%%
from svgelements import *
import svgelements
st = SVGText(svg_tune)
SVG.()s
#%%
from svg.path import parse_path
#%%
from svgutils.compose import *
Figure("16cm", "6.5cm", 
      Element(svg_subject), Element(svg_settings)).save("fig_final_compose.svg")

#%%%
from svgpathtools import Path
from svgpathtools.paths2svg import big_bounding_box
svg_path = Path(svg_tune)
xmin, xmax, ymin, ymax = big_bounding_box([svg_path])  
#%%
from svgpathtools import svg2paths, wsvg
paths, attributes = svg2paths(svg_tune)

