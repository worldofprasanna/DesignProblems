class Project:
    "This project directly uses behaviours passed as functions, instead of wrapping it around classes. It is possible because python respects functions as first class citizen"
    def __init__(self):
        self.strategy = DeploymentFactory.get_deployer()

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def deploy(self):
        return self.strategy()

class PythonProject(Project):
    def __init__(self, deployer=None):
        super().__init__()
        if deployer:
            self.strategy = deployer

    def deploy(self):
        return 'python - ' + super().deploy()

class JavaProject(Project):
    def __init__(self, deployer=None):
        super().__init__()
        if deployer:
            self.strategy = deployer

    def deploy(self):
        return 'java - ' + super().deploy()

class DeploymentFactory:

    @staticmethod
    def ansible():
        return 'ansible provisioning done'

    @staticmethod
    def puppet():
        return 'puppet provisioning done'

    @staticmethod
    def default():
        raise NotImplementedError('This method is not implemented')

    @staticmethod
    def get_deployer(name=None):
        if name == 'ansible':
            return DeploymentFactory.ansible
        elif name == 'puppet':
            return DeploymentFactory.puppet
        else:
            return DeploymentFactory.default

