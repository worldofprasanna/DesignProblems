import pytest
from .pythonic_project import Project, PythonProject, JavaProject
from .pythonic_project import DeploymentFactory

def test_projects_can_be_created():
    project = Project()
    python_project = PythonProject()
    java_project = JavaProject()
    assert project is not None
    assert java_project is not None
    assert python_project is not None

def test_base_project_cannot_be_deployed():
    with pytest.raises(NotImplementedError):
        project=Project()
        project.deploy()

def test_python_project_cannot_be_deployed_unless_strategy_specified():
    with pytest.raises(NotImplementedError):
        project = PythonProject()
        project.deploy()

@pytest.mark.parametrize('deployer', ['ansible', 'puppet'])
def test_python_project_deployed(deployer):
    deployment_type = DeploymentFactory.get_deployer(deployer)
    project = PythonProject(deployment_type)
    #project.strategy = ansible
    result = project.deploy()
    assert result == 'python - {0} provisioning done'.format(deployer)
    assert project.strategy == deployment_type

@pytest.mark.parametrize('deployer', ['ansible', 'puppet'])
def test_java_project_deployed_with_puppet(deployer):
    deployment_type = DeploymentFactory.get_deployer(deployer)
    project = JavaProject(deployment_type)
    #project.strategy = ansible
    result = project.deploy()
    assert result == 'java - {0} provisioning done'.format(deployer)
    assert project.strategy == deployment_type


