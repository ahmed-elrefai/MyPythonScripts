import os

def files_with_extension(ext, dir='.') -> list[str]:
    """returns all the files that end with ext
       for instance: '.py'"""
    content = os.listdir(dir)
    filtered = [file for file in content if file.endswith(ext)]
    return filtered or None
    
def dirs_with_extension(ext) -> list[str]:
    """returns all the directories containing files with ext
       hint: all the VS projects contain .sln files"""
    dirs = [file.name for file in os.scandir('.') if file.is_dir()]
    filtered_dirs = [dir for dir in dirs if files_with_extension(ext,dir) is not None]
    return filtered_dirs or None

# print("Projects found:")
# for dir in dirs_with_extension(".sln"):
#     print(f"- {dir}")
