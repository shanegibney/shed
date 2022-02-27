import bpy
shedwidth = 8
shedlength =16
shedheight = 7
inchesinfeet = 12
lengthx = shedlength*inchesinfeet
widthy = 4
heightz = 2
oncenter = 18
floorthickz = 1
floorwidth = 6
n = 3 #numer of lats beneath floor
blockwidth = 6
blocklength = 9
blockheight = 4
blockspacing = 61
latsspacing = shedwidth*inchesinfeet/n
thickness = 0.5

#front side bottom
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,widthy/2,heightz/2), scale=(lengthx,widthy,heightz))

#back end bottom
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-widthy/2,shedwidth*inchesinfeet/2,heightz/2), scale=(widthy,shedwidth*inchesinfeet-2*widthy,heightz))

#back side bottom
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,shedwidth*inchesinfeet-widthy/2,heightz/2), scale=(lengthx,widthy,heightz))

#front end bottom
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2,shedwidth*inchesinfeet/2,heightz/2), scale=(widthy,shedwidth*inchesinfeet-2*widthy,heightz))

#front side top
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,widthy/2,shedheight*inchesinfeet-heightz/2), scale=(lengthx,widthy,heightz))

#back end top
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-widthy/2,shedwidth*inchesinfeet/2,shedheight*inchesinfeet-heightz/2), scale=(widthy,shedwidth*inchesinfeet-2*widthy,heightz))

#back side top
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,shedwidth*inchesinfeet-widthy/2,shedheight*inchesinfeet-heightz/2), scale=(lengthx,widthy,heightz))

#front end top
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2,shedwidth*inchesinfeet/2,shedheight*inchesinfeet-heightz/2), scale=(widthy,shedwidth*inchesinfeet-2*widthy,heightz))

# front sides
for x in range(1,11):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x*oncenter,widthy/2,(shedheight*inchesinfeet)/2), scale=(heightz,widthy,shedheight*inchesinfeet-2*heightz))
 
# back sides
for x in range(1,11):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x*oncenter,shedwidth*inchesinfeet-widthy/2,(shedheight*inchesinfeet)/2), scale=(heightz,widthy,shedheight*inchesinfeet-2*heightz))

# back end sides
for x in range(1,6):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-widthy/2,x*oncenter,(shedheight*inchesinfeet)/2), scale=(widthy,heightz,shedheight*inchesinfeet-2*heightz))
'''
# front end sides
for x in range(1,6):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2,x*oncenter,(shedheight*inchesinfeet/2)), scale=(widthy,heightz,shedheight*inchesinfeet-2*heightz))
'''
 # back end corners
 # right side as you look at it from inside
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-heightz/2,widthy/2,(shedheight*inchesinfeet)/2), scale=(heightz,widthy,shedheight*inchesinfeet-2*heightz))

 # left side as you look at it from inside
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-heightz, shedwidth*inchesinfeet-heightz/2, shedheight*inchesinfeet/2), scale=(widthy,heightz,shedheight*inchesinfeet-2*heightz))

 # front end corners
 # left side as you look at it from inside
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2,shedwidth*inchesinfeet-heightz/2, shedheight*inchesinfeet/2), scale=(widthy, heightz,shedheight*inchesinfeet-2*heightz))

# right side as you look at it from inside
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2, heightz/2, shedheight*inchesinfeet/2), scale=(widthy, widthy/2, shedheight*inchesinfeet-2*heightz))

#floor
for x in range(16):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,x*floorwidth+floorwidth/2,-floorthickz/2), scale=(lengthx,floorwidth,floorthickz))
    
#Under floor
#front rail
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,heightz/2,-floorthickz-heightz), scale=(lengthx,widthy/2,widthy))

#back end rail
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx-heightz/2,shedwidth*inchesinfeet/2,-floorthickz-heightz), scale=(heightz,shedwidth*inchesinfeet-2*heightz,widthy))

#back side rail
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,shedwidth*inchesinfeet-heightz/2,-floorthickz-heightz), scale=(lengthx,widthy/2,widthy))

#front end rail to do
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(heightz/2,shedwidth*inchesinfeet/2,-floorthickz-heightz), scale=(heightz,shedwidth*inchesinfeet-2*heightz,widthy))

#floor joists
for x in range(11):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-x*oncenter+lengthx-heightz/2,shedwidth*inchesinfeet/2,-floorthickz-heightz), scale=(heightz,shedwidth*inchesinfeet-2*heightz,widthy))
    
#floor lats
for x in range(n):
   bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,x*latsspacing-shedwidth*inchesinfeet+shedwidth*inchesinfeet+latsspacing-floorwidth/2,-floorthickz-heightz-floorthickz/2-heightz), scale=(lengthx,floorwidth,floorthickz))  
   
#extra lat
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,floorwidth/2,-floorthickz-heightz-floorthickz/2-heightz), scale=(lengthx,floorwidth,floorthickz))  
   
#blocks
for y in range(3):
    for x in range(4):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x*blockspacing+blocklength/2,y*latsspacing-shedwidth*inchesinfeet+shedwidth*inchesinfeet+latsspacing-floorwidth/2,-blockheight/2-(2*floorthickz)-widthy), scale=(blocklength,blockwidth,blockheight))  
        
for x in range(4):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x*blockspacing+blocklength/2,blockwidth/2,-blockheight/2-(2*floorthickz)-widthy), scale=(blocklength,blockwidth,blockheight))

#outside cladding

#front sides
for x in range(15):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,-thickness/2,shedheight*inchesinfeet-blockwidth/2-x*blockwidth), scale=(lengthx,thickness,blockwidth)) 
    
#back sides
for x in range(15):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx/2,shedwidth*inchesinfeet+thickness/2,shedheight*inchesinfeet-blockwidth/2-x*blockwidth), scale=(lengthx,thickness,blockwidth)) 
    
#back ends
for x in range(15):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(lengthx+thickness,shedwidth*inchesinfeet/2,shedheight*inchesinfeet-x*blockwidth-blockwidth/2), scale=(thickness,shedwidth*inchesinfeet,blockwidth))
    
#front end top piece
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-thickness/2,shedwidth*inchesinfeet/2,shedheight*inchesinfeet-blockwidth/2), scale=(thickness,shedwidth*inchesinfeet,blockwidth))

# Front end left from outside
for x in range(2,15):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-thickness/2,oncenter/2+4*oncenter+1.5+1,shedheight*inchesinfeet-x*blockwidth+blockwidth/2), scale=(thickness,oncenter+widthy+4+2-1-2,blockwidth)) 

#Front end right from outside
for x in range(2,15):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-thickness/2,oncenter-2*widthy-heightz-heightz/2+heightz/2+widthy/2-thickness/2-heightz/8,shedheight*inchesinfeet-x*blockwidth+blockwidth/2-thickness/2), scale=(thickness,oncenter+widthy-thickness-heightz-thickness-heightz/4,blockwidth))

#front end bottom piece
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-thickness/2,shedwidth*inchesinfeet/2,-blockwidth/2), scale=(thickness,shedwidth*inchesinfeet,blockwidth))
'''
#test piece
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(-0,4*oncenter-widthy/2,widthy/2), scale=(lengthx,widthy/2,blockwidth))
'''
'''
#test piece II
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(6,oncenter/2+4*oncenter+1.5+1,4), scale=(4,oncenter+widthy+4+2-1-2,8))
'''
'''
#test piece III
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(widthy/2+2,4*oncenter+oncenter/2+widthy-2-0.25/2-2/2+4-2-1-1+2+0.25+1-0.5,12-4-0.25+1), scale=(1,oncenter+widthy,2))
'''