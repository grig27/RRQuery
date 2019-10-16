import argparse
import RRQuertyCore

parser = argparse.ArgumentParser(description='process query rosreestr.')
parser.add_argument('--layercode', type=int,
                    default=1,
                    help='code layer')
parser.add_argument('--querytype', type=str,
                    default='kn_by_geom',
                    help='type query (default kn_by_geom - list kn by geometry)')
args = parser.parse_args()
lid = args.layercode
qtype = args.querytype
geometry =  {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[72.18383477760308,55.88442958852703],[72.18437121940607,55.884369414300934],[72.18473599983211,55.88387598212827],[72.18507932258603,55.88192626194188],[72.18338416648858,55.88139669139942],[72.18153880668629,55.88249193158671],[72.18085216117845,55.88322608628071],[72.18383477760308,55.88442958852703]]],"bbox":[72.18085216117845,55.88139669139942,72.18507932258603,55.88442958852703]}]}
def query_kn_bygeom(layerid, geometry):
    print('start query_kn_bygeom')
    print('layerid = {0}'.format(layerid))
    rrq = RRQuertyCore.PKK5RosreestrAPIClient()
    res = rrq.get_kns_by_geom_all(lid, geometry)
    print(res)
if qtype == 'kn_by_geom':
    query_kn_bygeom(lid, geometry)