from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        
        # deserialisoi TOML-formaatissa oleva merkkijono 
        data = toml.loads(content)
        # ja muodosta Project-olio sen tietojen perusteella
        #print("DATA", data)

        tool = data['tool']['poetry']
        name = tool['name']
        description = tool['description']
        license1 = tool['license']
        authors = tool['authors']
        dependencies = tool['dependencies']
        dev_dependencies = tool['group']['dev']['dependencies']

        return Project(name, description, license1, authors, dependencies, dev_dependencies)
