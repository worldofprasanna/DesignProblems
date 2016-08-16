# Base classes
class Project:
    def __init__(self):
        self.strategy = DeploymentFactory.get_deployer()

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

    def deploy(self):
        return 'python - ' + super().deploy()

class JavaProject(Project):
    def __init__(self, strategy = None):
        super().__init__()
        if strategy:
            self.strategy = strategy

    def deploy(self):
        return 'java - ' + super().deploy()

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

class DeploymentFactory:

    @staticmethod
    def get_deployer(name=None):
        if name == 'ansible':
            return Ansible()
        elif name == 'puppet':
            return Puppet()
        else:
            return Deployment()
