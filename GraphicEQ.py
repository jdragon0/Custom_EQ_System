import numpy as np
import BiquadFilter
import scipy.signal as ss
import scipy.linalg 

"""
reference : All About Audio Equalization: Solutions and Frontiers
author : Vesa Välimäki , Joshua D. Reiss 2

library reconstruction : Jinyong Kim
email : jy9886.kim@samsung.com / jdragon0@naver.com
copyright : CC-BY
"""


def db(arg):
    return 20*np.log10(np.abs(arg))

class EQ:
    def __init__(self,fs,fc,Q,filterType):
        self.fs = fs
        self.fc = fc
        self.Q = Q
        self.filterType = filterType
    
    def getMatrix(self):
        l = len(self.fc)
        unitGain = np.ones(l)

        myEQ = BiquadFilter.BiquadEQ(self.fs,self.fc,unitGain,self.Q,self.filterType,0)
        sos = myEQ.getSOS()
        
        arr = np.zeros([l,l])
        for i in range(l):
            _,h = ss.sosfreqz(sos[i,:],self.fc,False,self.fs)
            arr[i] = db(h)
            
        invM = scipy.linalg.inv(arr).transpose()
        return invM
        
    def getEQgain(self,Matrix,reqGain):
        realGain = np.dot(Matrix,reqGain)  
        return realGain
    
