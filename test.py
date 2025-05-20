import plotly.graph_objs as go
import numpy as np

x = np.arange(0,1.1,0.1)
y = np.arange(0,1.1,0.1)
z = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1,.8,.8,.8,.8,.8,.8,.8,.8,.8, 1],
    [1,.8,.6,.6,.6,.6,.6,.6,.6,.8, 1],
    [1,.8,.6,.4,.4,.4,.4,.4,.6,.8, 1],
    [1,.8,.6,.4,.2,.2,.2,.4,.6,.8, 1],
    [1,.8,.6,.4,.2,.0,.2,.4,.6,.8, 1],
    [1,.8,.6,.4,.2,.2,.2,.4,.6,.8, 1],
    [1,.8,.6,.4,.4,.4,.4,.4,.6,.8, 1],
    [1,.8,.6,.6,.6,.6,.6,.6,.6,.8, 1],
    [1,.8,.8,.8,.8,.8,.8,.8,.8,.8, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

fig = go.Figure(go.Surface(x=x, y=y, z=z))

scene = dict(xaxis_title='w<sub>1</sub>',
             yaxis_title='w<sub>2</sub>',
             zaxis_title='mean of squared errors',
             aspectratio= {"x": 1, "y": 1, "z": 0.6},
             camera_eye= {"x": 1, "y": -1, "z": 0.5})

####~~~ Uncomment in binder or locally to see 3D plot ~~~~####

fig.layout.update(scene=scene,
                   width=700,
                   margin=dict(r=20, b=10, l=10, t=10))


fig.show()
