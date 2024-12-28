import numpy as np


# Recommendation model function
def recm(name, num, b_name, model, feature):
    r_link=[]
    r_name=[]
    ind = np.where(b_name['NAME OF THE BOOK'] == name)[0][0]
    dist,suggestion = model.kneighbors(feature.iloc[ind,:].values.reshape(1,-1), n_neighbors=num)
    for i in suggestion[0]:
        r_name.append(b_name['NAME OF THE BOOK'][i])
        r_link.append(b_name['IMAGE URL'][i])
    return r_name,r_link

# Product details function

def details(name, book):
    ind = np.where(book['NAME OF THE BOOK'] == name)[0][0]
    return np.array(book)[ind]
