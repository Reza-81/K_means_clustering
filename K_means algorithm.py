tedad_noghat=int(input())
tedad_khoshe=int(input())
#generat random points
import random
random_x = []
random_y = []
random_z = []

for i in range(tedad_noghat):
    n = random.randint(1,10)
    random_x.append(n)
    y = random.randint(1,10)
    random_y.append(y)
    z = random.randint(1,10)
    random_z.append(z)
points=dict()
for i in range(len(random_x)):
   points['point'+str(i+1)]=(random_x[i],random_y[i],random_z[i])
#centroids
centroids=dict()
noghat_random=[]
q=1
while q<=tedad_khoshe:
    n = random.randint(1,tedad_noghat)
    if n in noghat_random:  
        continue
    else:
        noghat_random+=[n]
        centroids['centr'+str(q)]=points['point'+str(n)]
        q+=1
#distance
def distance_noghte(point,center,j):
    dis = ((point[0]-center[0])**2 + (point[1]-center[1])**2 + (point[2]-center[2])**2)**(1/2)
    return (('c'+str(j),dis),)

faseleha=dict()

def dict_fasele():
    global faseleha
    for z in range(1,tedad_noghat+1):
        faseleha['p'+str(z)]=()
    
    for j in range(1,tedad_khoshe+1):    
        for i in range(1,tedad_noghat+1):
            faseleha['p'+str(i)]+=distance_noghte(points['point'+str(i)],centroids['centr'+str(j)],j)
    return faseleha
#clustering and new centroids
def new_centroids():
    global centroids
    j=0
    for i in clusters.keys():
        j+=1
        new_x=0
        new_y=0
        new_z=0
        for k in clusters[i]:
            new_x+=points[k][0]
            new_y+=points[k][1]
            new_z+=points[k][2]
        if len(clusters[i])==0:
            continue
        else:
            centroids['centr'+str(j)]=(new_x/len(clusters[i]),new_y/len(clusters[i]),new_z/len(clusters[i]))
    return  centroids    
               
def clustering(faseleha):
    clusters={}
    for k in range(1,tedad_khoshe+1):
        clusters['cluster'+str(k)]=()
    for i in range(1,tedad_noghat+1):
        temp=[]
        for a in faseleha['p'+str(i)]:
            temp+=[a[1]]
        index_kamtarin=temp.index(min(temp))
        clusters['cluster'+str(index_kamtarin+1)]+=('point'+str(i),)
                
    return clusters

faseleha=dict_fasele()
clusters=clustering(faseleha)

###########################
centroids = new_centroids()
faseleha = dict_fasele()
clusters2 = clustering(faseleha)


def update():
    global centroids
    global clusters
    global clusters2
    global faseleha
    
    if clusters2 == clusters:
        return clusters
        
    else:
        clusters=clusters2
        centroids = new_centroids()
        faseleha = dict_fasele()
        clusters2 = clustering(faseleha)
        return update()  
# print(points)
# print(clusters)
# print(centroids)
#
#
#
print(update())
