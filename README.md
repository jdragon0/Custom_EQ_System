# Idea
![image](https://github.com/user-attachments/assets/272c5bc4-6c96-42e0-b835-4a7a778824d9)

# Useage
```python
import numpy as np
import BiquadFilter
import FilterPlot
import GraphicEQ as CEQ

fs = 192000
fc = np.array([62.5,125,250,500,1000,2000,4000,8000,16000])
Q = np.array([1,1,1,1,1,1,1,1,1])
filterType = np.array(["peak","peak","peak","peak","peak","peak","peak","peak","peak"])

myCEQ = CEQ.EQ(fs,fc,Q,filterType)

req = np.array([10,10,10,10,10,10,10,10,10])

m = myCEQ.getMatrix()
g = myCEQ.getEQgain(m,req)

myEQ = BiquadFilter.BiquadEQ(fs,fc,g,Q,filterType,0)
sos = myEQ.getSOS()

fig,ax = FilterPlot.sosMagPlot(fs,20,48000,2**15,sos)
ax.semilogx(fc,req,marker='o',linestyle='',fillstyle='none',markeredgecolor='red')
fig.set_size_inches(16,6,forward=True)
FilterPlot.show()
```

## Compare each models
### Direct model
![image](https://github.com/user-attachments/assets/52f55f59-ac33-444f-9326-2f74a92e21cc)

### Interference model
![image](https://github.com/user-attachments/assets/4c3d0e26-d445-46c7-9d46-e619dd81b82f)

## Interference model result
### request EQ = [5,9,1,-1,-5,2,6,8,-9]
![image](https://github.com/user-attachments/assets/b8548f0a-f764-4759-986d-c16c815e62de)


### request EQ = [-9,-7,-5,-3,-1,1,3,5,7]
![image](https://github.com/user-attachments/assets/f0ef4430-a80f-429d-b3f7-49798dcf6f6b)
