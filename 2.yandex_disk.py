import requests
import os

# with open('token.txt') as file:
#     token1 = file.read().strip()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        href = self._get_upload_link(file_path=file_path.split('\\')[-1]).get("href", "")
        response = requests.put(href, data=open(str(file_path.split('\\')[-1]), 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Successful uploaded")

    def rename(self, old_name, new_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/move'
        headers = self.get_headers()
        params = {"from": old_name, "path": new_name, "overwrite": "true"}
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print("Successful renamed")


if __name__ == '__main__':
    token =
    file_name = 'hello.txt'
    base_path = os.getcwd()
    path_to_file = os.path.join(base_path, file_name)

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

    # old_path = 'hello.txt'
    # new_path = 'goodbye.txt'
    # result = uploader.rename(old_path, new_path)
