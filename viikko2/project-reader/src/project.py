class Project:
    def __init__(self, name, description, license1, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license1 = license1
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors1 = "\n" + "\n".join(f"- {author}" for author in self.authors) + "\n"
        dep1 = "\n" + "\n".join(f"- {dep}" for dep in self.dependencies) + "\n"
        dev_dep1 = "\n" + "\n".join(f"- {dev_dep}" for dev_dep in self.dev_dependencies) + "\n"
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license1 or '-'}"
            f"\n\nAuthors: {authors1 or '-'}"
            f"\nDependencies: {dep1}"
            f"\nDevelopment dependencies: {dev_dep1}"
        )
#            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
#            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
