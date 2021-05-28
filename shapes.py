import random 

t = True
f = False

shapes = [
[
    [t,t],
    [t,f],
    [t,f]
],
[
    [t,t],
    [f,t],
    [f,t]
],
[
    [f,t], 
    [t,t], 
    [t,f]
],
[
    [t,f],
    [t,t], 
    [f,t] 
],
[
    [t],
    [t],
    [t],
    [t]
],
[
    [t,t],
    [t,t]
],
[
    [f,t,f],
    [t,t,t]
]
]


def random_shape():
    return shapes[random.randint(0,6)]