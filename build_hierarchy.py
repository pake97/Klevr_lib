

from itertools import *
from utils.xml_writer import XML_writer

def main():
    
    writer = XML_writer()

    attributes = ['Colored', 'Sized', 'Shaped', 'Material']
    colors = ["Gray","Cyan","Yellow","Red","Purple","Green","Blue","Brown"]
    shapes = ['Cube', 'Cylinder', 'Sphere']
    sizes = ['Small','Large']
    materials = ['Rubber','Metallic']
    obj='Object'

    
    
    
    for att1 in attributes:
        writer.write_class(att1+obj)
        writer.write_subclass(obj,att1+obj)
        for att2 in attributes:
            if att1!=att2:
                list_classes=[att1+att2,att2+att1]
                writer.write_class(att1+att2+obj)
                writer.write_class(att2+att1+obj)
                for comb1 in (combinations(list_classes,2)):
                    for perm1 in permutations(comb1,2):
                        writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                writer.write_subclass(att1+obj,att1+att2+obj)
                writer.write_subclass(att1+obj,att2+att1+obj)
                writer.write_subclass(att2+obj,att1+att2+obj)
                writer.write_subclass(att2+obj,att2+att1+obj)
            for att3 in attributes:
                if att1!=att2 and att1!=att3 and att2!=att3:
                    list_classes=[att1+att2+att3,att2+att1+att3,att3+att1+att2,att3+att2+att1,att1+att3+att2,att2+att3+att1]
                    writer.write_class(att1+att2+att3+obj)
                    writer.write_class(att2+att1+att3+obj)
                    writer.write_class(att3+att1+att2+obj)
                    writer.write_class(att3+att2+att1+obj)
                    writer.write_class(att1+att3+att2+obj)
                    writer.write_class(att2+att3+att1+obj)
                    for comb1 in (combinations(list_classes,2)):
                        for perm1 in permutations(comb1,2):
                            writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                    writer.write_subclass(att2+att1+obj,att1+att2+att3+obj)
                    writer.write_subclass(att3+att1+obj,att2+att1+att3+obj)
                    writer.write_subclass(att2+att3+obj,att3+att1+att2+obj)
                    writer.write_subclass(att3+att2+obj,att3+att2+att1+obj)
                    writer.write_subclass(att1+att2+obj,att1+att3+att2+obj)
                    writer.write_subclass(att1+att3+obj,att2+att3+att1+obj)
                for att4 in attributes:
                    if att1!=att2 and att1!=att3 and att2!=att3 and att1!=att4 and att2!=att4 and att3!=att4:
                        list_classes = [att1+att2+att3+att4,att2+att1+att3+att4,att3+att1+att2+att4,att3+att2+att1+att4,att1+att3+att2+att4,att2+att3+att1+att4,
                        att1+att2+att4+att3,att2+att1+att4+att3,att3+att1+att4+att2,att3+att2+att4+att1,att1+att3+att4+att2,att2+att3+att4+att1,
                        att1+att4+att2+att3,att2+att4+att1+att3,att3+att4+att1+att2,att3+att4+att2+att1,att1+att4+att3+att2,att2+att4+att3+att1,
                        att4+att1+att2+att3,att4+att2+att1+att3,att4+att3+att1+att2,att4+att3+att2+att1,att4+att1+att3+att2,att4+att2+att3+att1]
                        writer.write_class(att1+att2+att3+att4+obj)
                        writer.write_class(att2+att1+att3+att4+obj)
                        writer.write_class(att3+att1+att2+att4+obj)
                        writer.write_class(att3+att2+att1+att4+obj)
                        writer.write_class(att1+att3+att2+att4+obj)
                        writer.write_class(att2+att3+att1+att4+obj)

                        writer.write_class(att1+att2+att4+att3+obj)
                        writer.write_class(att2+att1+att4+att3+obj)
                        writer.write_class(att3+att1+att4+att2+obj)
                        writer.write_class(att3+att2+att4+att1+obj)
                        writer.write_class(att1+att3+att4+att2+obj)
                        writer.write_class(att2+att3+att4+att1+obj)

                        writer.write_class(att1+att4+att2+att3+obj)
                        writer.write_class(att2+att4+att1+att3+obj)
                        writer.write_class(att3+att4+att1+att2+obj)
                        writer.write_class(att3+att4+att2+att1+obj)
                        writer.write_class(att1+att4+att3+att2+obj)
                        writer.write_class(att2+att4+att3+att1+obj)
        
                        writer.write_class(att4+att1+att2+att3+obj)
                        writer.write_class(att4+att2+att1+att3+obj)
                        writer.write_class(att4+att3+att1+att2+obj)
                        writer.write_class(att4+att3+att2+att1+obj)
                        writer.write_class(att4+att1+att3+att2+obj)
                        writer.write_class(att4+att2+att3+att1+obj)
                        for comb1 in (combinations(list_classes,2)):
                            for perm1 in permutations(comb1,2):
                                writer.write_sameas(perm1[0]+obj,perm1[1]+obj)

                        for comb1 in (combinations([att1,att2,att3,att4],3)):
                            for perm1 in permutations(comb1,3):
                                superclass=''.join(perm1)+obj
                                writer.write_subclass(superclass,att1+att2+att3+att4+obj)
                                writer.write_subclass(superclass,att2+att1+att3+att4+obj)
                                writer.write_subclass(superclass,att3+att1+att2+att4+obj)
                                writer.write_subclass(superclass,att3+att2+att1+att4+obj)
                                writer.write_subclass(superclass,att1+att3+att2+att4+obj)
                                writer.write_subclass(superclass,att2+att3+att1+att4+obj)

                                writer.write_subclass(superclass,att1+att2+att4+att3+obj)
                                writer.write_subclass(superclass,att2+att1+att4+att3+obj)
                                writer.write_subclass(superclass,att3+att1+att4+att2+obj)
                                writer.write_subclass(superclass,att3+att2+att4+att1+obj)
                                writer.write_subclass(superclass,att1+att3+att4+att2+obj)
                                writer.write_subclass(superclass,att2+att3+att4+att1+obj)

                                writer.write_subclass(superclass,att1+att4+att2+att3+obj)
                                writer.write_subclass(superclass,att2+att4+att1+att3+obj)
                                writer.write_subclass(superclass,att3+att4+att1+att2+obj)
                                writer.write_subclass(superclass,att3+att4+att2+att1+obj)
                                writer.write_subclass(superclass,att1+att4+att3+att2+obj)
                                writer.write_subclass(superclass,att2+att4+att3+att1+obj)
                
                                writer.write_subclass(superclass,att4+att1+att2+att3+obj)
                                writer.write_subclass(superclass,att4+att2+att1+att3+obj)
                                writer.write_subclass(superclass,att4+att3+att1+att2+obj)
                                writer.write_subclass(superclass,att4+att3+att2+att1+obj)
                                writer.write_subclass(superclass,att4+att1+att3+att2+obj)
                                writer.write_subclass(superclass,att4+att2+att3+att1+obj)


                     
    for color in colors:
        writer.write_class(color+obj)
        writer.write_subclass(obj,color+obj)
        writer.write_subclass('ColoredObject',color+obj)
        for material in materials:

            writer.write_class(material+color+obj)
            writer.write_class(color+material+obj)
            list_classes=[material+color,color+material]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(color+obj,material+color+obj)
            writer.write_subclass(color+obj,color+material+obj)
            writer.write_subclass(material+obj,material+color+obj)
            writer.write_subclass(material+obj,color+material+obj)
            writer.write_subclass('ColoredMaterialObject',material+color+obj)
            writer.write_subclass('ColoredMaterialObject',color+material+obj)
            writer.write_subclass('MaterialColoredObject',material+color+obj)
            writer.write_subclass('MaterialColoredObject',color+material+obj)
            for size in sizes:
                writer.write_class(material+color+size+obj)
                writer.write_class(color+material+size+obj)
                writer.write_class(color+size+material+obj)
                writer.write_class(material+size+color+obj)
                writer.write_class(size+material+color+obj)
                writer.write_class(size+color+material+obj)
                list_classes=[material+color+size,color+material+size,color+size+material,material+size+color,size+material+color,size+color+material]
                for comb1 in (combinations(list_classes,2)):
                    for perm1 in permutations(comb1,2):
                        writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                writer.write_subclass('MaterialColoredSizedObject',material+color+size+obj)
                writer.write_subclass('MaterialColoredSizedObject',color+material+size+obj)
                writer.write_subclass('MaterialColoredSizedObject',color+size+material+obj)
                writer.write_subclass('MaterialColoredSizedObject',material+size+color+obj)
                writer.write_subclass('MaterialColoredSizedObject',size+material+color+obj)
                writer.write_subclass('MaterialColoredSizedObject',size+color+material+obj)

                writer.write_subclass('ColoredMaterialSizedObject',material+color+size+obj)
                writer.write_subclass('ColoredMaterialSizedObject',color+material+size+obj)
                writer.write_subclass('ColoredMaterialSizedObject',color+size+material+obj)
                writer.write_subclass('ColoredMaterialSizedObject',material+size+color+obj)
                writer.write_subclass('ColoredMaterialSizedObject',size+material+color+obj)
                writer.write_subclass('ColoredMaterialSizedObject',size+color+material+obj)

                writer.write_subclass('ColoredSizedMaterialObject',material+color+size+obj)
                writer.write_subclass('ColoredSizedMaterialObject',color+material+size+obj)
                writer.write_subclass('ColoredSizedMaterialObject',color+size+material+obj)
                writer.write_subclass('ColoredSizedMaterialObject',material+size+color+obj)
                writer.write_subclass('ColoredSizedMaterialObject',size+material+color+obj)
                writer.write_subclass('ColoredSizedMaterialObject',size+color+material+obj)

                writer.write_subclass('MaterialSizedColoredObject',material+color+size+obj)
                writer.write_subclass('MaterialSizedColoredObject',color+material+size+obj)
                writer.write_subclass('MaterialSizedColoredObject',color+size+material+obj)
                writer.write_subclass('MaterialSizedColoredObject',material+size+color+obj)
                writer.write_subclass('MaterialSizedColoredObject',size+material+color+obj)
                writer.write_subclass('MaterialSizedColoredObject',size+color+material+obj)

                writer.write_subclass('SizedMaterialColoredObject',material+color+size+obj)
                writer.write_subclass('SizedMaterialColoredObject',color+material+size+obj)
                writer.write_subclass('SizedMaterialColoredObject',color+size+material+obj)
                writer.write_subclass('SizedMaterialColoredObject',material+size+color+obj)
                writer.write_subclass('SizedMaterialColoredObject',size+material+color+obj)
                writer.write_subclass('SizedMaterialColoredObject',size+color+material+obj)

                writer.write_subclass('SizedColoredMaterialObject',material+color+size+obj)
                writer.write_subclass('SizedColoredMaterialObject',color+material+size+obj)
                writer.write_subclass('SizedColoredMaterialObject',color+size+material+obj)
                writer.write_subclass('SizedColoredMaterialObject',material+size+color+obj)
                writer.write_subclass('SizedColoredMaterialObject',size+material+color+obj)
                writer.write_subclass('SizedColoredMaterialObject',size+color+material+obj)

                for comb1 in (combinations([size,color,material],2)):
                        for perm1 in permutations(comb1,2):
                            superclass=''.join(perm1)+obj
                            writer.write_subclass(superclass,material+color+size+obj)
                            writer.write_subclass(superclass,color+material+size+obj)
                            writer.write_subclass(superclass,color+size+material+obj)
                            writer.write_subclass(superclass,material+size+color+obj)
                            writer.write_subclass(superclass,size+material+color+obj)
                            writer.write_subclass(superclass,size+color+material+obj)

                for shape in shapes:
                    writer.write_class(material+color+size+shape+obj)
                    writer.write_class(color+material+size+shape+obj)
                    writer.write_class(color+size+material+shape+obj)
                    writer.write_class(material+size+color+shape+obj)
                    writer.write_class(size+material+color+shape+obj)
                    writer.write_class(size+color+material+shape+obj)
                    writer.write_class(material+color+shape+size+obj)
                    writer.write_class(color+material+shape+size+obj)
                    writer.write_class(color+size+shape+material+obj)
                    writer.write_class(material+size+shape+color+obj)
                    writer.write_class(size+material+shape+color+obj)
                    writer.write_class(size+color+shape+material+obj)
                    writer.write_class(material+shape+color+size+obj)
                    writer.write_class(color+shape+material+size+obj)
                    writer.write_class(color+shape+size+material+obj)
                    writer.write_class(material+shape+size+color+obj)

                    writer.write_class(size+shape+material+color+obj)
                    writer.write_class(size+shape+color+material+obj)
                    writer.write_class(shape+material+color+size+obj)
                    writer.write_class(shape+color+material+size+obj)

                    writer.write_class(shape+color+size+material+obj)
                    writer.write_class(shape+material+size+color+obj)
                    writer.write_class(shape+size+material+color+obj)
                    writer.write_class(shape+size+color+material+obj)
                    list_classes=[material+color+size+shape,color+material+size+shape,color+size+material+shape,material+size+color+shape,size+material+color+shape,size+color+material+shape,material+color+shape+size,color+material+shape+size,color+size+shape+material,material+size+shape+color,size+material+shape+color,size+color+shape+material,material+shape+color+size,color+shape+material+size,color+shape+size+material,material+shape+size+color,size+shape+material+color,size+shape+color+material,shape+material+color+size,shape+color+material+size,shape+color+size+material,shape+material+size+color,shape+size+material+color,shape+size+color+material]
                    for comb1 in (combinations(list_classes,2)):
                            for perm1 in permutations(comb1,2):
                                writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                    for comb in combinations([material,color,size,shape],3):
                        for perm in permutations(comb,3):
                            superclass = ''.join(perm)+obj
                            writer.write_subclass(superclass,material+color+size+shape+obj)
                            writer.write_subclass(superclass,color+material+size+shape+obj)
                            writer.write_subclass(superclass,color+size+material+shape+obj)
                            writer.write_subclass(superclass,material+size+color+shape+obj)
                            writer.write_subclass(superclass,size+material+color+shape+obj)
                            writer.write_subclass(superclass,size+color+material+shape+obj)
                            writer.write_subclass(superclass,material+color+shape+size+obj)
                            writer.write_subclass(superclass,color+material+shape+size+obj)
                            writer.write_subclass(superclass,color+size+shape+material+obj)
                            writer.write_subclass(superclass,material+size+shape+color+obj)
                            writer.write_subclass(superclass,size+material+shape+color+obj)
                            writer.write_subclass(superclass,size+color+shape+material+obj)
                            writer.write_subclass(superclass,material+shape+color+size+obj)
                            writer.write_subclass(superclass,color+shape+material+size+obj)
                            writer.write_subclass(superclass,color+shape+size+material+obj)
                            writer.write_subclass(superclass,material+shape+size+color+obj)
                            writer.write_subclass(superclass,size+shape+material+color+obj)
                            writer.write_subclass(superclass,size+shape+color+material+obj)
                            writer.write_subclass(superclass,shape+material+color+size+obj)
                            writer.write_subclass(superclass,shape+color+material+size+obj)
                            writer.write_subclass(superclass,shape+color+size+material+obj)
                            writer.write_subclass(superclass,shape+material+size+color+obj)
                            writer.write_subclass(superclass,shape+size+material+color+obj)
                            writer.write_subclass(superclass,shape+size+color+material+obj)

                    """ 
                    for comb1 in (combinations(l1_children,4)):
                        for perm1 in permutations(comb1,4):
                            superclass=''.join(perm1)+obj   

                            writer.write_subclass(superclass,material+color+size+shape+obj)
                            writer.write_subclass(superclass,color+material+size+shape+obj)
                            writer.write_subclass(superclass,color+size+material+shape+obj)
                            writer.write_subclass(superclass,material+size+color+shape+obj)
                            writer.write_subclass(superclass,size+material+color+shape+obj)
                            writer.write_subclass(superclass,size+color+material+shape+obj)
                            writer.write_subclass(superclass,material+color+shape+size+obj)
                            writer.write_subclass(superclass,color+material+shape+size+obj)
                            writer.write_subclass(superclass,color+size+shape+material+obj)
                            writer.write_subclass(superclass,material+size+shape+color+obj)
                            writer.write_subclass(superclass,size+material+shape+color+obj)
                            writer.write_subclass(superclass,size+color+shape+material+obj)
                            writer.write_subclass(superclass,material+shape+color+size+obj)
                            writer.write_subclass(superclass,color+shape+material+size+obj)
                            writer.write_subclass(superclass,color+shape+size+material+obj)
                            writer.write_subclass(superclass,material+shape+size+color+obj)
                            writer.write_subclass(superclass,size+shape+material+color+obj)
                            writer.write_subclass(superclass,size+shape+color+material+obj)
                            writer.write_subclass(superclass,shape+material+color+size+obj)
                            writer.write_subclass(superclass,shape+color+material+size+obj)
                            writer.write_subclass(superclass,shape+color+size+material+obj)
                            writer.write_subclass(superclass,shape+material+size+color+obj)
                            writer.write_subclass(superclass,shape+size+material+color+obj)
                            writer.write_subclass(superclass,shape+size+color+material+obj)
                    
 """

    for color in colors:
        for material in materials:
            for shape in shapes:
                writer.write_class(material+color+shape+obj)
                writer.write_class(color+material+shape+obj)
                writer.write_class(color+shape+material+obj)
                writer.write_class(material+shape+color+obj)
                writer.write_class(shape+material+color+obj)
                writer.write_class(shape+color+material+obj)
                list_classes=[material+color+shape,color+material+shape,color+shape+material,material+shape+color,shape+material+color,shape+color+material]
                for comb1 in (combinations(list_classes,2)):
                    for perm1 in permutations(comb1,2):
                        writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                writer.write_subclass('MaterialColoredShapedObject',material+color+shape+obj)
                writer.write_subclass('MaterialColoredShapedObject',color+material+shape+obj)
                writer.write_subclass('MaterialColoredShapedObject',color+shape+material+obj)
                writer.write_subclass('MaterialColoredShapedObject',material+shape+color+obj)
                writer.write_subclass('MaterialColoredShapedObject',shape+material+color+obj)
                writer.write_subclass('MaterialColoredShapedObject',shape+color+material+obj)

                writer.write_subclass('ColoredMaterialShapedObject',material+color+shape+obj)
                writer.write_subclass('ColoredMaterialShapedObject',color+material+shape+obj)
                writer.write_subclass('ColoredMaterialShapedObject',color+shape+material+obj)
                writer.write_subclass('ColoredMaterialShapedObject',material+shape+color+obj)
                writer.write_subclass('ColoredMaterialShapedObject',shape+material+color+obj)
                writer.write_subclass('ColoredMaterialShapedObject',shape+color+material+obj)

                writer.write_subclass('ColoredShapedMaterialObject',material+color+shape+obj)
                writer.write_subclass('ColoredShapedMaterialObject',color+material+shape+obj)
                writer.write_subclass('ColoredShapedMaterialObject',color+shape+material+obj)
                writer.write_subclass('ColoredShapedMaterialObject',material+shape+color+obj)
                writer.write_subclass('ColoredShapedMaterialObject',shape+material+color+obj)
                writer.write_subclass('ColoredShapedMaterialObject',shape+color+material+obj)

                writer.write_subclass('MaterialShapedColoredObject',material+color+shape+obj)
                writer.write_subclass('MaterialShapedColoredObject',color+material+shape+obj)
                writer.write_subclass('MaterialShapedColoredObject',color+shape+material+obj)
                writer.write_subclass('MaterialShapedColoredObject',material+shape+color+obj)
                writer.write_subclass('MaterialShapedColoredObject',shape+material+color+obj)
                writer.write_subclass('MaterialShapedColoredObject',shape+color+material+obj)

                writer.write_subclass('ShapedMaterialColoredObject',material+color+shape+obj)
                writer.write_subclass('ShapedMaterialColoredObject',color+material+shape+obj)
                writer.write_subclass('ShapedMaterialColoredObject',color+shape+material+obj)
                writer.write_subclass('ShapedMaterialColoredObject',material+shape+color+obj)
                writer.write_subclass('ShapedMaterialColoredObject',shape+material+color+obj)
                writer.write_subclass('ShapedMaterialColoredObject',shape+color+material+obj)

                writer.write_subclass('ShapedColoredMaterialObject',material+color+shape+obj)
                writer.write_subclass('ShapedColoredMaterialObject',color+material+shape+obj)
                writer.write_subclass('ShapedColoredMaterialObject',color+shape+material+obj)
                writer.write_subclass('ShapedColoredMaterialObject',material+shape+color+obj)
                writer.write_subclass('ShapedColoredMaterialObject',shape+material+color+obj)
                writer.write_subclass('ShapedColoredMaterialObject',shape+color+material+obj)

                for comb1 in (combinations([shape,color,material],2)):
                        for perm1 in permutations(comb1,2):
                            superclass=''.join(perm1)+obj
                            writer.write_subclass(superclass,material+color+shape+obj)
                            writer.write_subclass(superclass,color+material+shape+obj)
                            writer.write_subclass(superclass,color+shape+material+obj)
                            writer.write_subclass(superclass,material+shape+color+obj)
                            writer.write_subclass(superclass,shape+material+color+obj)
                            writer.write_subclass(superclass,shape+color+material+obj)

    for color in colors:
        for size in sizes:
            writer.write_class(size+color+obj)
            writer.write_class(color+size+obj)
            list_classes=[size+color,color+size]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(color+obj,size+color+obj)
            writer.write_subclass(color+obj,color+size+obj)
            writer.write_subclass(size+obj,size+color+obj)
            writer.write_subclass(size+obj,color+size+obj)
            writer.write_subclass('ColoredSizedObject',size+color+obj)
            writer.write_subclass('ColoredSizedObject',color+size+obj)
            writer.write_subclass('SizedColoredObject',size+color+obj)
            writer.write_subclass('SizedColoredObject',color+size+obj)
            for shape in shapes:
                writer.write_class(size+color+shape+obj)
                writer.write_class(color+size+shape+obj)
                writer.write_class(color+shape+size+obj)
                writer.write_class(size+shape+color+obj)
                writer.write_class(shape+size+color+obj)
                writer.write_class(shape+color+size+obj)
                list_classes=[size+color+shape,color+size+shape,color+shape+size,size+shape+color,shape+size+color,shape+color+size]
                for comb1 in (combinations(list_classes,2)):
                    for perm1 in permutations(comb1,2):
                        writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                writer.write_subclass('ShapedColoredSizedObject',shape+color+size+obj)
                writer.write_subclass('ShapedColoredSizedObject',color+shape+size+obj)
                writer.write_subclass('ShapedColoredSizedObject',color+size+shape+obj)
                writer.write_subclass('ShapedColoredSizedObject',shape+size+color+obj)
                writer.write_subclass('ShapedColoredSizedObject',size+shape+color+obj)
                writer.write_subclass('ShapedColoredSizedObject',size+color+shape+obj)

                writer.write_subclass('ColoredShapedSizedObject',shape+color+size+obj)
                writer.write_subclass('ColoredShapedSizedObject',color+shape+size+obj)
                writer.write_subclass('ColoredShapedSizedObject',color+size+shape+obj)
                writer.write_subclass('ColoredShapedSizedObject',shape+size+color+obj)
                writer.write_subclass('ColoredShapedSizedObject',size+shape+color+obj)
                writer.write_subclass('ColoredShapedSizedObject',size+color+shape+obj)

                writer.write_subclass('ColoredSizedShapedObject',shape+color+size+obj)
                writer.write_subclass('ColoredSizedShapedObject',color+shape+size+obj)
                writer.write_subclass('ColoredSizedShapedObject',color+size+shape+obj)
                writer.write_subclass('ColoredSizedShapedObject',shape+size+color+obj)
                writer.write_subclass('ColoredSizedShapedObject',size+shape+color+obj)
                writer.write_subclass('ColoredSizedShapedObject',size+color+shape+obj)

                writer.write_subclass('ShapedSizedColoredObject',shape+color+size+obj)
                writer.write_subclass('ShapedSizedColoredObject',color+shape+size+obj)
                writer.write_subclass('ShapedSizedColoredObject',color+size+shape+obj)
                writer.write_subclass('ShapedSizedColoredObject',shape+size+color+obj)
                writer.write_subclass('ShapedSizedColoredObject',size+shape+color+obj)
                writer.write_subclass('ShapedSizedColoredObject',size+color+shape+obj)

                writer.write_subclass('SizedShapedColoredObject',shape+color+size+obj)
                writer.write_subclass('SizedShapedColoredObject',color+shape+size+obj)
                writer.write_subclass('SizedShapedColoredObject',color+size+shape+obj)
                writer.write_subclass('SizedShapedColoredObject',shape+size+color+obj)
                writer.write_subclass('SizedShapedColoredObject',size+shape+color+obj)
                writer.write_subclass('SizedShapedColoredObject',size+color+shape+obj)

                writer.write_subclass('SizedColoredShapedObject',shape+color+size+obj)
                writer.write_subclass('SizedColoredShapedObject',color+shape+size+obj)
                writer.write_subclass('SizedColoredShapedObject',color+size+shape+obj)
                writer.write_subclass('SizedColoredShapedObject',shape+size+color+obj)
                writer.write_subclass('SizedColoredShapedObject',size+shape+color+obj)
                writer.write_subclass('SizedColoredShapedObject',size+color+shape+obj)

                for comb1 in (combinations([shape,color,size],2)):
                        for perm1 in permutations(comb1,2):
                            superclass=''.join(perm1)+obj
                            writer.write_subclass(superclass,size+color+shape+obj)
                            writer.write_subclass(superclass,color+size+shape+obj)
                            writer.write_subclass(superclass,color+shape+size+obj)
                            writer.write_subclass(superclass,size+shape+color+obj)
                            writer.write_subclass(superclass,shape+size+color+obj)
                            writer.write_subclass(superclass,shape+color+size+obj)

    for shape in shapes:
        writer.write_class(shape+obj)
        writer.write_subclass(obj,shape+obj)
        for material in materials:
            writer.write_class(material+shape+obj)
            writer.write_class(shape+material+obj)
            list_classes=[material+shape,shape+material]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(shape+obj,shape+material+obj)
            writer.write_subclass(shape+obj,material+shape+obj)
            writer.write_subclass(material+obj,shape+material+obj)
            writer.write_subclass(material+obj,material+shape+obj)
            writer.write_subclass('MaterialShapedObject',shape+material+obj)
            writer.write_subclass('ShapedMaterialObject',material+shape+obj)
            writer.write_subclass('ShapedMaterialObject',shape+material+obj)
            writer.write_subclass('MaterialShapedObject',material+shape+obj)
            for size in sizes:
                writer.write_class(material+shape+size+obj)
                writer.write_class(shape+material+size+obj)
                writer.write_class(shape+size+material+obj)
                writer.write_class(material+size+shape+obj)
                writer.write_class(size+material+shape+obj)
                writer.write_class(size+shape+material+obj)
                list_classes=[material+shape+size,shape+material+size,shape+size+material,material+size+shape,size+material+shape,size+shape+material]
                for comb1 in (combinations(list_classes,2)):
                    for perm1 in permutations(comb1,2):
                        writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
                writer.write_subclass('ShapedMaterialSizedObject',shape+material+size+obj)
                writer.write_subclass('ShapedMaterialSizedObject',material+shape+size+obj)
                writer.write_subclass('ShapedMaterialSizedObject',material+size+shape+obj)
                writer.write_subclass('ShapedMaterialSizedObject',shape+size+material+obj)
                writer.write_subclass('ShapedMaterialSizedObject',size+shape+material+obj)
                writer.write_subclass('ShapedMaterialSizedObject',size+material+shape+obj)

                writer.write_subclass('MaterialShapedSizedObject',shape+material+size+obj)
                writer.write_subclass('MaterialShapedSizedObject',material+shape+size+obj)
                writer.write_subclass('MaterialShapedSizedObject',material+size+shape+obj)
                writer.write_subclass('MaterialShapedSizedObject',shape+size+material+obj)
                writer.write_subclass('MaterialShapedSizedObject',size+shape+material+obj)
                writer.write_subclass('MaterialShapedSizedObject',size+material+shape+obj)

                writer.write_subclass('MaterialSizedShapedObject',shape+material+size+obj)
                writer.write_subclass('MaterialSizedShapedObject',material+shape+size+obj)
                writer.write_subclass('MaterialSizedShapedObject',material+size+shape+obj)
                writer.write_subclass('MaterialSizedShapedObject',shape+size+material+obj)
                writer.write_subclass('MaterialSizedShapedObject',size+shape+material+obj)
                writer.write_subclass('MaterialSizedShapedObject',size+material+shape+obj)

                writer.write_subclass('ShapedSizedMaterialObject',shape+material+size+obj)
                writer.write_subclass('ShapedSizedMaterialObject',material+shape+size+obj)
                writer.write_subclass('ShapedSizedMaterialObject',material+size+shape+obj)
                writer.write_subclass('ShapedSizedMaterialObject',shape+size+material+obj)
                writer.write_subclass('ShapedSizedMaterialObject',size+shape+material+obj)
                writer.write_subclass('ShapedSizedMaterialObject',size+material+shape+obj)

                writer.write_subclass('SizedShapedMaterialObject',shape+material+size+obj)
                writer.write_subclass('SizedShapedMaterialObject',material+shape+size+obj)
                writer.write_subclass('SizedShapedMaterialObject',material+size+shape+obj)
                writer.write_subclass('SizedShapedMaterialObject',shape+size+material+obj)
                writer.write_subclass('SizedShapedMaterialObject',size+shape+material+obj)
                writer.write_subclass('SizedShapedMaterialObject',size+material+shape+obj)

                writer.write_subclass('SizedMaterialShapedObject',shape+material+size+obj)
                writer.write_subclass('SizedMaterialShapedObject',material+shape+size+obj)
                writer.write_subclass('SizedMaterialShapedObject',material+size+shape+obj)
                writer.write_subclass('SizedMaterialShapedObject',shape+size+material+obj)
                writer.write_subclass('SizedMaterialShapedObject',size+shape+material+obj)
                writer.write_subclass('SizedMaterialShapedObject',size+material+shape+obj)

                for comb1 in (combinations([shape,material,size],2)):
                        for perm1 in permutations(comb1,2):
                            superclass=''.join(perm1)+obj
                            writer.write_subclass(superclass,size+material+shape+obj)
                            writer.write_subclass(superclass,material+size+shape+obj)
                            writer.write_subclass(superclass,material+shape+size+obj)
                            writer.write_subclass(superclass,size+shape+material+obj)
                            writer.write_subclass(superclass,shape+size+material+obj)
                            writer.write_subclass(superclass,shape+material+size+obj)

    for size in sizes:
        writer.write_class(size+obj)
        writer.write_subclass(obj,size+obj)
        for shape in shapes:
            writer.write_class(shape+size+obj)
            writer.write_class(size+shape+obj)
            list_classes=[shape+size,size+shape]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(shape+obj,shape+size+obj)
            writer.write_subclass(shape+obj,size+shape+obj)
            writer.write_subclass(size+obj,shape+size+obj)
            writer.write_subclass(size+obj,size+shape+obj)
            writer.write_subclass('SizedShapedObject',shape+size+obj)
            writer.write_subclass('ShapedSizedObject',size+shape+obj)
            writer.write_subclass('ShapedSizedObject',shape+size+obj)
            writer.write_subclass('SizedShapedObject',size+shape+obj)

    for size in sizes:
        for material in materials:
            writer.write_class(material+size+obj)
            writer.write_class(size+material+obj)
            list_classes=[material+size,size+material]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(size+obj,size+material+obj)
            writer.write_subclass(size+obj,material+size+obj)
            writer.write_subclass(material+obj,size+material+obj)
            writer.write_subclass(material+obj,material+size+obj)
            writer.write_subclass('MaterialSizedObject',size+material+obj)
            writer.write_subclass('SizedMaterialObject',material+size+obj)
            writer.write_subclass('SizedMaterialObject',size+material+obj)
            writer.write_subclass('MaterialSizedObject',material+size+obj)

    for material in materials:
        writer.write_class(material+obj)
        writer.write_subclass(obj,material+obj)
        for shape in shapes:
            writer.write_class(material+shape+obj)
            writer.write_class(shape+material+obj)
            list_classes=[material+shape,shape+material]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(shape+obj,shape+material+obj)
            writer.write_subclass(shape+obj,material+shape+obj)
            writer.write_subclass(material+obj,shape+material+obj)
            writer.write_subclass(material+obj,material+shape+obj)
            writer.write_subclass('MaterialShapedObject',shape+material+obj)
            writer.write_subclass('ShapedMaterialObject',material+shape+obj)
            writer.write_subclass('ShapedMaterialObject',shape+material+obj)
            writer.write_subclass('MaterialShapedObject',material+shape+obj)

            

    for color in colors:
        for shape in shapes:
            list_classes=[color+shape,shape+color]
            for comb1 in (combinations(list_classes,2)):
                for perm1 in permutations(comb1,2):
                    writer.write_sameas(perm1[0]+obj,perm1[1]+obj)
            writer.write_subclass(shape+obj,shape+color+obj)
            writer.write_subclass(shape+obj,color+shape+obj)
            writer.write_subclass(color+obj,shape+color+obj)
            writer.write_subclass(color+obj,color+shape+obj)
            writer.write_subclass('ColoredShapedObject',shape+color+obj)
            writer.write_subclass('ShapedColoredObject',color+shape+obj)
            writer.write_subclass('ShapedColoredObject',shape+color+obj)
            writer.write_subclass('ColoredShapedObject',color+shape+obj)

        
      

if __name__ == '__main__':
    main()


    
    
    
  