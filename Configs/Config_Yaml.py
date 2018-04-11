import yaml

class config_Yaml:

    def get_Config(self,path):
        filename = path
        f = open(filename)
        yamlmapping = yaml.load(f)
        return yamlmapping

