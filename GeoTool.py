import shapely
import shapely.geometry

wgs84metter = 8.983111749910168882500898311175e-6
wgs84kmetter = wgs84metter * 10000

def SplitGeometry(jsonobj, splitter = wgs84kmetter):
    res = []
    shgeo = shapely.geometry.shape(jsonobj)
    b = shgeo.bounds

    xmin = b[0]
    ymin = b[1]
    xmax = b[2]
    ymax = b[3]

    xmincut = xmin
    ymincut = ymin

    while (ymincut < ymax):
        xmaxcut = xmincut + splitter
        ymaxcut = ymincut + splitter
        cutgeo = shapely.geometry.box(xmincut, ymincut, xmaxcut, ymaxcut)
        xmincut = xmincut + splitter
        if (xmincut > xmax):
            xmincut = xmin
            ymincut = ymincut + splitter

        cutresgeo = cutgeo.intersection(shgeo)
        if not cutresgeo.is_empty:
            gcol = shapely.geometry.GeometryCollection([cutresgeo])
            cutj = gcol.__geo_interface__
            res.append(cutj)

    return res