
import urllib.request
import json


class GitHub(object):

  def __init__(self, user, project):
    self.user = user
    self.project = project

  def trees(self):
    """

    https://docs.github.com/en/rest
    """
    with urllib.request.urlopen(
      'https://api.github.com/repos/%s/%s/git/trees/master?recursive=1' % (self.user, self.project)) as response:
      return json.loads(response.read())

  def metadata(self):
    """

    https://docs.github.com/en/rest
    """
    with urllib.request.urlopen('https://api.github.com/repos/%s/%s' % (self.user, self.project)) as response:
      return json.loads(response.read())

  def get_file_path(self, path, branch='master'):
    return "https://raw.githubusercontent.com/%s/%s/%s/%s" % (self.user, self.project, branch, path)

  def get_file_content(self, path, branch='master'):
    if path is None:
      return ""

    self.get_file_path(path, branch)
    with urllib.request.urlopen(self.get_file_path(path, branch)) as response:
      return response.read()

  def picture_path(self, path):
    """

    :param path:
    """
    return "https://github.com/%s/%s/blob/master/%s?raw=true" % (self.user, self.project, path)

  @property
  def path(self):
    return "https://github.com/%s/%s" % (self.user, self.project)

  @property
  def main(self):
    return "https://github.com/%s/%s/tree/master" % (self.user, self.project)
