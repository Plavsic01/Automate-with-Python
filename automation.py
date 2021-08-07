import time,os,shutil
import pathlib as p

# change directory to "C:\downloads"
# How it works?
# starts from Downloads directory
# you can select what type of extension you want to look up
# or the name of the directory
# finds extension and moves it from Downloads to new directory


class Automate:

    PATH = str(p.Path.home())+"\\Downloads"

    def __init__(self,name="untitled_folder",extension =".mp3") -> None:
        self.name = name
        self.extension = extension
        self.downloads_dir()
        self.list_files()
        self.create_folder()
        self.move_files()
    
    def downloads_dir(self):
        os.chdir(self.PATH)

    @staticmethod
    def list_files():
        files = os.listdir()
        return files

    def create_folder(self):
        files = self.list_files()
        if self.name not in files:
            os.mkdir(self.name)
            print(f"directory {self.name} created")
        else:
            print(f"dir {self.name} already exists")

    def move_files(self):
        # search all files ending with selected extension
        all_files = Automate.list_files()
        specific_files = []
        for file in all_files:
            if(file.endswith(self.extension)):
                specific_files.append(file)
        
        # move songs to new folder
        os.chdir(os.getcwd() + "\\" + self.name)
        for i in range(len(specific_files)):
            shutil.move(self.PATH + "\\" + specific_files[i],os.getcwd())
            print(f"{self.extension}: {i+1}: {specific_files[i]} has been moved.")


# creating Automate instances

automateSongs = Automate(name="muzika",extension=".mp3")
automatePdf = Automate(name="pdf fileovi",extension=".pdf")
automateExe = Automate(name="exe files",extension=".exe")
automateRar = Automate(name="rar files",extension=".zip")





