from pathlib import Path

def get_project_path() -> str:
    """
    Create project path
    :return: str with path to project
    """
    return Path(__file__).parent