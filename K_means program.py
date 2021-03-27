import cv2
img1 = cv2.imread("random.png")
W = int(input())
H = int(input())

tedad_noghat = H*W
tedad_khoshe = int(input())
# generat random points
import random

points = dict()
k = 1
for i in range(0,H):
    for j in range(0, W):
        points['point' + str(k)] = img1[i, j]
        k += 1

# centroids
centroids = dict()
noghat_random = []
q = 1
while q <= tedad_khoshe:
    n = random.randint(1, tedad_noghat)
    if n in noghat_random:
        continue
    else:
        noghat_random += [n]
        centroids['centr' + str(q)] = points['point' + str(n)]
        q += 1


# distance
def distance_noghte(point, center, j):
    dis = ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 + (point[2] - center[2]) ** 2) ** (1 / 2)
    return (('c' + str(j), dis),)


faseleha = dict()


def dict_fasele():
    global faseleha
    for z in range(1, tedad_noghat + 1):
        faseleha['p' + str(z)] = ()

    for j in range(1, tedad_khoshe + 1):
        for i in range(1, tedad_noghat + 1):
            faseleha['p' + str(i)] += distance_noghte(points['point' + str(i)], centroids['centr' + str(j)], j)
    return faseleha


# clustering and new centroids
def new_centroids():
    global centroids
    j = 0
    for i in clusters.keys():
        j += 1
        new_x = 0
        new_y = 0
        new_z = 0
        for k in clusters[i]:
            new_x += points[k][0]
            new_y += points[k][1]
            new_z += points[k][2]
        if len(clusters[i]) == 0:
            continue
        else:
            centroids['centr' + str(j)] = (round(new_x / len(clusters[i])), round(new_y / len(clusters[i])), round(new_z / len(clusters[i])))
    return centroids


def clustering(faseleha):
    clusters = {}
    for k in range(1, tedad_khoshe + 1):
        clusters['cluster' + str(k)] = ()
    for i in range(1, tedad_noghat + 1):
        temp = []
        for a in faseleha['p' + str(i)]:
            temp += [a[1]]
        index_kamtarin = temp.index(min(temp))
        clusters['cluster' + str(index_kamtarin + 1)] += ('point' + str(i),)

    return clusters


faseleha = dict_fasele()
clusters = clustering(faseleha)

#########################
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
        clusters = clusters2
        centroids = new_centroids()
        faseleha = dict_fasele()
        clusters2 = clustering(faseleha)
        return update()

    
print(centroids)
update()
shomarande_points=1

for i in points.keys():
    shomarande_center=1
    for j in clusters.keys():
        if i in clusters[j]:
            points['point'+str(shomarande_points)] = centroids['centr'+str(shomarande_center)]
            break
        shomarande_center+=1
    shomarande_points+=1
        
lst = [points.values()]
lst1 = []
for i in lst :
    lst1 += i
print(lst1)
r = 0
for k in range(W):
    for f in range(H):
        img1[f,k] = lst1[r]
        r += 1
cv2.imshow('random.PNG',img1)
cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('new.jpg' , img1)
