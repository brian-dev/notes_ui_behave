import os
import yaml


class YamlUtils:
    def __init__(self):
        pass

    def get_env_urls(self):
        with open(f'./features/yaml/urls.yaml') as file_read:
            file = yaml.load(file_read, Loader=yaml.FullLoader)
        return file[os.getenv('ENVIRONMENT')]

    def get_user_info(self, user):
        with open(f'./features/yaml/users.yaml') as file_read:
            file = yaml.load(file_read, Loader=yaml.FullLoader)
        return file[user]
