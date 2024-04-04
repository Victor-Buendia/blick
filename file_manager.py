import os

class FileManager():
  @classmethod
  def create_dir(self,dir_name,path=os.getcwd()):
    dir_path = "{path}/{name}".format(
      name = dir_name,
      path = path
    )
    os.mkdir(dir_path) if not os.path.isdir(dir_path) else None