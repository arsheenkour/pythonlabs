#PICKLING:
import pickle
animalDict = {'Cat':2,'Dog':7 ,'Lion': 4 ,'Tiger':9,'leopard':11}
outfile=open('animals','wb')
pickle.dump(animalDict,outfile)
outfile.close()
fst=open("animals",'rb')
data = pickle.load(fst)
print(data)