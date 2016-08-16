# Base classes
class Project:
    def __init__(self):
        self.strategy = Deployment()

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def deploy(self):
        return self.strategy.deploy()

class PythonProject(Project):
    def __init__(self, strategy = None):
        super().__init__()
        if strategy:
            self.strategy = strategy

class JavaProject(Project):
    pass

# Behaviours

class Deployment:
    def deploy(self):
        raise NotImplementedError('This is an abstract deployment')

class Puppet(Deployment):
    def deploy(self):
        return 'puppet provisioning done'

class Ansible(Deployment):
    def deploy(self):
        return 'ansible provisioning done'
