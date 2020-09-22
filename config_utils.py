import os
import yaml

'''

'''
class Config(object):
    def __init__(self, dict_config):
        super().__init__()
        self.set_attribute(dict_config)

    @staticmethod
    def from_yaml(path):
        with open(path, 'r') as stream:
            return Config(yaml.load(stream, Loader=yaml.FullLoader))

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.set_attribute({key:value})

    def set_attribute(self, dict_config):
        for key in dict_config.keys():
            if isinstance(dict_config[key], dict):
                self.__dict__[key] = Config(dict_config[key])
            else:
                self.__dict__[key] = dict_config[key]

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

