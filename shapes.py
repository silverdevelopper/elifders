import math

csv = ""
with open("shapes.csv") as fp:
    csv = fp.read()
line_list = csv.split("\n")

rects = []
trapezoids = []
circles = []

for ind,line in enumerate(line_list):
    r = line.strip()
    if "#" in r:
        continue
    
    if ind < 7 :
        rect = [ float(x) for x in r.split(",") ]
        rect.append(rect[0]*rect[1])
        rects.append(rect)
        
    if 7<ind < 14:
        trp = []
        for x in r.split(','):
            if x!='':
                trp.append(float(x))
        try:
            trp.append( 0.5*(trp[0]+trp[1])*trp[2] )
            trapezoids.append(trp)
        except:
            print("Error in line: ",r)
            
    if 14<ind < 24:
        c = []
        c.append(float(r))
        c.append(math.pi*(c[0]**2))
        circles.append(c)
        
with open("rectangles.csv","w") as fp:
    for r in rects:
        fp.write(",".join([str(x) for x in r ])+"\n")

with open("trapezoids.csv","w") as fp:
    for r in trapezoids:
        fp.write(",".join([str(x) for x in r ])+"\n")
        
with open("circles.csv","w") as fp:
    for r in circles:
        fp.write(",".join([str(x) for x in r ])+"\n")
