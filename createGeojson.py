from ladybug_geometry import geometry3d, geometry2d
from dragonfly.building import Building
import dragonfly_energy
from honeybee_energy.lib.programtypes import program_type_by_identifier, building_program_type_by_identifier
from honeybee_energy.lib.constructionsets import construction_set_by_identifier
import geopandas as gpd


def extrude_footprint(base):
    base.set_index("Name", inplace=True)
    raw = base.transpose().to_dict()
    for i in raw:
        temp = [geometry3d.Point3D(j[0], j[1], 0) for j in raw[i]['geometry'].boundary.coords]
        temp.append(temp[0])
        raw[i]['geom_new'] = temp
    buildings = [Building.from_footprint(i, [geometry3d.Face3D(raw[i]['geom_new'])],
                                         [raw[i]['height_ag']],
                                         0, 0.001) for i in raw]
    # print(type(raw['B001']['geom_new']))
    # a = list(raw['B001']['geometry'].boundary.coords)
    # print(a)


if __name__ == "__main__":
    df = gpd.read_file("/Volumes/reworkshop2022/Umlet/sample.shp")
    extrude_footprint(df)
