
import urllib.request
import urllib.error
import json
import logging
import os

from epyk_studio.utils import sys_files


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
      with urllib.request.urlopen('%s/repos/%s/%s/git/trees/master?recursive=1' % (
        sys_files.GITHUB_PATHS["api"], self.user, self.project)) as response:
        result = json.loads(response.read())
        if tempFolder is not None:
          temp_file = os.path.join(tempFolder, sys_files.STUDIO_FILES["git_tree"]['file'])
          with open(temp_file, "w") as fp:
            json.dump(result, fp)
        return result

    except urllib.error.HTTPError as err:
      logging.warning("Github API error - %s" % err)
      if tempFolder is not None:
        temp_file = os.path.join(tempFolder, sys_files.STUDIO_FILES["git_tree"]['file'])
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
    with urllib.request.urlopen(
      '%s/repos/%s/%s' % (sys_files.GITHUB_PATHS["api"], self.user, self.project)) as response:
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
    return "%s/%s/%s/%s/%s" % (sys_files.GITHUB_PATHS["raw_content"], self.user, self.project, branch, path)

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
    return "%s/%s/%s/blob/master/%s?raw=true" % (sys_files.GITHUB_PATHS["website"], self.user, self.project, path)

  @property
  def path(self):
    """
    Description:
    ------------
    Get the repository path.

    Usage:
    -----

    """
    return "%s/%s/%s" % (sys_files.GITHUB_PATHS["website"], self.user, self.project)

  @property
  def main(self):
    """
    Description:
    ------------
    Get the repository path of the master branch in the repository.

    Usage:
    -----

    """
    return "%s/%s/%s/tree/master" % (sys_files.GITHUB_PATHS["website"], self.user, self.project)
