filepath = 'geo.csv'  
f= open("test.txt","w+")
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cols = line.split(";")
       f.write('{ "type": "Feature", "properties": { "idPlace": "'+cols[2]+'", "nome": "'+cols[2]+'" }, "geometry": { "type": "Point", "coordinates": [  '+cols[4]+','+cols[3]+', 0.0 ] } },\n');