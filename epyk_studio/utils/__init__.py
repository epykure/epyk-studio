
from epyk_studio.utils import Github


def git(username, project):
  """

  :param username:
  :param project:

  :return:
  """
  return Github.GitHub(username, project)
