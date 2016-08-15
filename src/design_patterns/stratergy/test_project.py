from .project import Project, PythonProject, JavaProject

def test_projects_can_be_created():
    project = Project()
    python_project = PythonProject()
    java_project = JavaProject()
    assert project is not None
    assert java_project is not None
    assert python_project is not None

