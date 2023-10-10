import json
import jsonlines
import yaml


class YamlUtils:
    def __init__(self):
        self.yaml_dir = 'features/yaml/'

    def get_env_urls(self):
        with open(f"{self.yaml_dir}/urls.yaml") as file_read:
            file = yaml.safe_load(file_read)
        return file['notes']

    def get_user_info(self):
        file = open(f"{self.yaml_dir}/users.json")
        json_data = json.load(file)
        return json_data

    def write_to_json(self, file_name, file_data):
        with open(f"{self.yaml_dir}/{file_name}", 'w') as file:
            json.dump(file_data, file, indent=4)

    def append_to_json(self, file_name, file_data):
        with jsonlines.open(f"{self.yaml_dir}/{file_name}", 'a') as updated_file:
            updated_file.write(file_data)

    def get_user_token(self, token_location=''):
        if token_location == 'ui':
            file = open(f"{self.yaml_dir}/active_user_test.json")
        else:
            file = open(f"{self.yaml_dir}/active_user.json")

        json_data = json.load(file)
        return json_data['token']

    def get_test_creds(self, user_type):
        with open(f"{self.yaml_dir}/test_creds.yaml") as file_read:
            file = yaml.safe_load(file_read)
        return file[user_type]
