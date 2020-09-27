
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

  def picture_path(self, path):
    """

    :param path:
    """
    return "https://github.com/%s/%s/blob/master/%s?raw=true" % (self.user, self.project, path)
