#! /usr/bin/env python
from ppclass import pp

# we define a "planetoplot" object
u = pp()

# we define its attributes
u.file = "/home/aymeric/Big_Data/DATAPLOT/diagfired.nc"
u.var = "u"
u.t = "0.5" #NB: also works without quotes
u.z = "10" #NB: also works without quotes

# we get data
u.get()

## we smooth the field a little bit
#u.smooth(15)

# we define the plot
u.title = "This is what we name $u$"
u.proj = "robin"
u.filename = "simple"
u.defineplot() 

# we plot
u.makeplot()

# we simply change the colorbar
# ... no need to reload data
u.colorbar = "RdBu"
u.filename = "myplot"
u.makeplot()

# we remove map projection
# ... idem, no need to reload data
# ... but have to redefine plot
u.noproj = True
u.defineplot()
u.makeplot()

# we multiply the field by two
# ... and redefine+remake the plot
u = u * 2.
u.defineplot()
u.makeplot()
