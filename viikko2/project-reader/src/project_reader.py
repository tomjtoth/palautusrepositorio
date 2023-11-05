from urllib import request
from project import Project
from toml import loads, dumps


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        obj = loads(content)["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        return Project(
            obj["name"],
            obj["description"],
            [
                dep[0] for dep in
                obj["dependencies"].items()
            ],
            [
                dep[0] for dep in
                obj["group"]["dev"]["dependencies"].items()
            ]
        )
