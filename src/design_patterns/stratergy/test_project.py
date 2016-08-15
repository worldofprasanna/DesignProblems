from .project import Project

def test_project_can_be_created():
    project = Project()
    assert project
