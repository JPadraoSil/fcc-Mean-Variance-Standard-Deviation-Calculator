import numpy as np

def calculate(list):

    # If a list containing less than 9 elements is passed into the function, 
    # it should raise a ValueError exception with the message: 
    # "List must contain nine numbers."
    if len(list) != 9:
        raise ValueError ("List must contain nine numbers.")
    else:
        mat = np.array(list).reshape(3,3)
   
    # The values in the returned dictionary 
    # should be lists and not Numpy arrays.
    media = [(mat.mean(axis=0).tolist()), (mat.mean(axis=1).tolist()), mat.flatten().mean()]
    varianza = [(mat.var(axis=0).tolist()), (mat.var(axis=1).tolist()), mat.flatten().var()]
    destip = [(mat.std(axis=0).tolist()), (mat.std(axis=1).tolist()), mat.flatten().std()]
    maximo = [(mat.max(axis=0).tolist()), (mat.max(axis=1).tolist()), mat.flatten().max()]
    minimo = [(mat.min(axis=0).tolist()), (mat.min(axis=1).tolist()), mat.flatten().min()]
    suma = [(mat.sum(axis=0).tolist()), (mat.sum(axis=1).tolist()), mat.flatten().sum()]

    calculations = {
        "mean" : media,
        "variance" : varianza,
        "standard deviation" : destip,
        "max" : maximo,
        "min" : minimo,
        "sum" : suma,
    }

    return calculations