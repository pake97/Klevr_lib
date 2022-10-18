


class XML_writer():
    def __init__(self) -> None:
        self.output = "ontology.txt"
        self.output1 = "ontology_sameas.txt"
        self.output2 = "ontology_has.txt"


    def write_class(self,name):
        with open(self.output, 'a') as f:
            f.write('<Declaration>\n\t<Class IRI="#'+name+'"/>\n</Declaration>\n')

    def write_subclass(self,name1,name2):
        with open(self.output, 'a') as f:
            f.write("<SubClassOf>\n\t<Class IRI=\"#"+name2+"\"/>\n\t<Class IRI=\"#"+name1+"\"/>\n</SubClassOf>")

    def write_sameas(self,name1,name2):
        with open(self.output1, 'a') as f:
            f.write("<owl:Class rdf:about=\"http://www.semanticweb.org/amedeo/ontologies/2022/7/KlevR_EL#"+name1+"\"><owl:equivalentClass rdf:resource=\"http://www.semanticweb.org/amedeo/ontologies/2022/7/KlevR_EL#"+name2+"\"/></owl:Class>")