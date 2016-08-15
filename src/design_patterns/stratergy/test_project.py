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


