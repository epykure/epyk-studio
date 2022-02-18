
from epyk_studio.utils import github


def git(username, project):
  """

  :param username:
  :param project:

  :return:
  """
  return github.GitHub(username, project)
