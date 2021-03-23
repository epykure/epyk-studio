
import urllib.request
import json
import logging
import os


class GitHub:

  def __init__(self, user, project):
    self.user = user
    self.project = project

  def trees(self, tempFolder=None):
    """
    Description:
    ------------
    Get the tree structure of the project from Github directly.
    This will try to use the free Github API to retrieve the information.

    Usage:
    -----

      repo_templates = git("epykure", "epyk-templates")
      git_files = repo_templates.trees(tempFolder=os.path.join(os.getcwd(), "temps"))

    Related Pages:

      https://docs.github.com/en/rest

    Attributes:
    ----------
    :param tempFolder: String. Optional. The sub folder.
    """
    try:
      with urllib.request.urlopen('https://api.github.com/repos/%s/%s/git/trees/master?recursive=1' % (self.user, self.project)) as response:
        result = json.loads(response.read())
        if tempFolder is not None:
          temp_file = os.path.join(tempFolder, "git_tree_template.json")
          with open(temp_file, "w") as fp:
            json.dump(result, fp)
        return result

    except urllib.error.HTTPError as err:
      logging.warning("Github API error - %s" % err)
      if tempFolder is not None:
        temp_file = os.path.join(tempFolder, "git_tree_template.json")
        with open(temp_file, "r") as fp:
          return json.loads(fp.read())
      else:
        return {"tree": []}

  def metadata(self):
    """
    Description:
    ------------
    Get the repository meta data.

    Usage:
    -----

    Related Pages:

      https://docs.github.com/en/rest
    """
    with urllib.request.urlopen('https://api.github.com/repos/%s/%s' % (self.user, self.project)) as response:
      return json.loads(response.read())

  def get_file_path(self, path, branch='master'):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param path: String. The project path.
    :param branch: String. Optional. The branch name. Default master.
    """
    return "https://raw.githubusercontent.com/%s/%s/%s/%s" % (self.user, self.project, branch, path)

  def get_file_content(self, path, branch='master'):
    """
    Description:
    ------------
    Get the script content from a branch in the Github repository.

    Usage:
    -----

    Attributes:
    ----------
    :param path: String. The project path.
    :param branch: String. Optional. The branch name. Default master.
    """
    if path is None:
      return ""

    self.get_file_path(path, branch)
    with urllib.request.urlopen(self.get_file_path(path, branch)) as response:
      return response.read()

  def picture_path(self, path):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param path: String. The project path.
    """
    return "https://github.com/%s/%s/blob/master/%s?raw=true" % (self.user, self.project, path)

  @property
  def path(self):
    """
    Description:
    ------------
    Get the repository path.

    Usage:
    -----

    """
    return "https://github.com/%s/%s" % (self.user, self.project)

  @property
  def main(self):
    """
    Description:
    ------------
    Get the repository path of the master branch in the repository.

    Usage:
    -----

    """
    return "https://github.com/%s/%s/tree/master" % (self.user, self.project)
