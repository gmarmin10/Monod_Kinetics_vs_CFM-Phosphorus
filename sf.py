'''
Created on May 18, 2014
This one reads dpi
@author: Keisuke
'''
from pylab import * 
from matplotlib.pyplot import savefig

def sf(figName):
    First_part="C:/Users/19046/Documents/General_Research/Monod_Kinetics/phosphorus/figures/model_output/"
    Figure_name=str(figName)
    Last_part=".png"
    savefig(First_part+Figure_name+Last_part,dpi=500)
