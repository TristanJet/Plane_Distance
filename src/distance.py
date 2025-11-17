from geopy import distance

dist = distance.distance
tepuia = (-38.05481607579999, 178.304291368)
leningradsky = (69.368146, 178.406343)
alkatvaam = (63.127587, 179.023771)
rabi = (-16.5337, 179.9757)
matei = (-16.690599, -179.876999)

dist = round(dist(rabi, matei).kilometers, 3)
print(dist)
