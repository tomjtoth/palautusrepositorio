class Project:
    def __init__(
        self,
        name,
        description,
        lic,
        auths,
        dependencies,
        dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = lic
        self.authors = auths
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, arr):
        return "\n" + "\n".join(["- " + x for x in arr]) if len(arr) > 0 else "-"

    def __str__(self):
        return (
            f"""\
Name: {self.name}
Description: {self.description or '-'}
License: {self.license or '-'}

Authors: {self._stringify_list(self.authors)}

Dependencies: {self._stringify_list(self.dependencies)}

Development dependencies: {self._stringify_list(self.dev_dependencies)}
"""
        )
