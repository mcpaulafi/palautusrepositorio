import requests
#import sys, pdb

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password, password_confirmation):
#        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password_confirmation
        }

        requests.post(f"{self._base_url}/register", data=data)
