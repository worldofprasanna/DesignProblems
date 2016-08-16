import pytest
from .project import Project, PythonProject, JavaProject
from .project import Deployment, Puppet, Ansible


def test_projects_can_be_created():
    project = Project()
    python_project = PythonProject()
    java_project = JavaProject()
    assert project is not None
    assert java_project is not None
    assert python_project is not None

def test_deployments_can_be_created():
    deployment = Deployment()
    puppet = Puppet()
    ansible = Ansible()

    assert deployment is not None
    assert puppet is not None
    assert ansible is not None

def test_base_project_cannot_be_deployed():
    with pytest.raises(NotImplementedError):
        project=Project()
        project.deploy()

def test_python_project_cannot_be_deployed_unless_strategy_specified():
    with pytest.raises(NotImplementedError):
        project = PythonProject()
        project.deploy()

def test_python_project_deployed_with_ansible():
    ansible = Ansible()
    project = PythonProject(ansible)
    #project.strategy = ansible
    result = project.deploy()
    assert result == 'ansible provisioning done'
    assert project.strategy == ansible

def test_java_project_deployed_with_puppet():
    puppet = Puppet()
    project = JavaProject(puppet)
    #project.strategy = ansible
    result = project.deploy()
    assert result == 'puppet provisioning done'
    assert project.strategy == puppet


