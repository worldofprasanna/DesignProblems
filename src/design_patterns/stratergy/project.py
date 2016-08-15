# Base classes
class Project:
    def __init__(self):
        self.deployment_statergy = Deployment()

    def deploy(self):
        self.deployment_statergy.deploy()

class PythonProject(Project):
    pass

class JavaProject(Project):
    pass

# Behaviours

class Deployment:
    def deploy(self):
        raise NotImplementedError('This is an abstract deployment')

class Puppet(Deployment):
    pass

class Ansible(Deployment):
    pass

