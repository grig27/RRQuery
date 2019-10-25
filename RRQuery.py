import argparse
import RRQuertyCore
import testgeom
import GeoTool
import time

parser = argparse.ArgumentParser(description='process query rosreestr.')
parser.add_argument('--layercode', type=int,
                    default=1,
                    help='code layer')
parser.add_argument('--querytype', type=str,
                    default='kn_by_geom_split',
                    help='type query kn_by_geom - list kn by geometry; kn_by_geom_split (default kn_by_geom_split)')
args = parser.parse_args()
lid = args.layercode
qtype = args.querytype 
geometry = testgeom.biggeom
def query_kn_bygeom(layerid, geometry):
    print('start query_kn_bygeom')
    print('layerid = {0}'.format(layerid))
    rrq = RRQuertyCore.PKK5RosreestrAPIClient()
    res = rrq.get_kns_by_geom_all(lid, geometry)
    return res

def query_kn_bygeom_split(layerid, geometry):
    res = []
    print('start query_kn_bygeom_split')
    print('layerid = {0}'.format(layerid))  
    geoarr = GeoTool.SplitGeometry(geometry)
    for i in range(len(geoarr)):
        geo = geoarr[i]
        print('process {index} of {len}'.format(index=i, len = len(geoarr)))
        tempres = query_kn_bygeom(lid, geo)
        time.sleep(3)
        res = res + tempres

    uniqueres = [] 
      
    for x in res: 
        # check if exists in unique_list or not 
        if x not in uniqueres: 
            uniqueres.append(x) 


    return uniqueres


if qtype == 'kn_by_geom':
    res = query_kn_bygeom(lid, geometry)
    print(res)
if qtype == 'kn_by_geom_split':
    res = query_kn_bygeom_split(lid, geometry)
    print(res)