import yaml


class ConfigYaml:
    def get_config(self, path):
        filename = path
        f = open(filename)
        mapping = yaml.load(f)
        return mapping
