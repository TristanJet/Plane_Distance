from haversine import haversine, Unit

tepuia = (-38.05481607579999, 178.304291368)
leningradsky = (69.368146, 178.406343)
alkatvaam = (63.127587, 179.023771)
rabi = (-16.5337, 179.9757)
matei = (-16.690599, -179.876999)

dist = round(haversine(rabi, matei, unit=Unit.KILOMETERS), 3)
print(dist)
