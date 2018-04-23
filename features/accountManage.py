__author__ = 'sunny.yu2'
from Configs.ConfigYaml import ConfigYaml
import os


class AccountManage:
    config_yaml = ConfigYaml()
    username = ''
    password = ''
    url = ''

    def __init__(self, environment='qa'):
        if environment == 'qa':
            cf = self.load_config_file()
        else:
            cf = self.load_staging_config_file()
        self.global_timeout = float(cf.get("timeout"))
        AccountManage.username = cf.get("username")
        AccountManage.password = cf.get("password")
        AccountManage.userName1 = cf.get("username1")
        AccountManage.password1 = cf.get("password1")
        AccountManage.url = cf.get("url")

    def load_config_file(self):
        config_file = self.get_relative_path("Configs", "config_QA.yaml")
        config = self.config_yaml.get_config(config_file)
        return config

    def load_staging_config_file(self):
        config_file = self.get_relative_path("Configs", "Config_STG.yaml")
        config = self.config_yaml.get_config(config_file)
        return config

    def get_relative_path(self, path, file_name):
        prepath = os.getcwd()
        return os.path.join(prepath, path, file_name)
