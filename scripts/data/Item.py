class Item:
    def __init__(self):
        self.__name = ""
        self.__basePath = ""
        self.__fullPath = ""
        self.__isDir = False
        self.__isChecked = False

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @Name.deleter
    def Name(self):
        del self.__name

    @property
    def BasePath(self):
        return self.__basePath

    @BasePath.setter
    def BasePath(self, value):
        self.__basePath = value

    @BasePath.deleter
    def BasePath(self):
        del self.__basePath

    @property
    def FullPath(self):
        return self.__fullPath

    @FullPath.setter
    def FullPath(self, value):
        self.__fullPath = value

    @FullPath.deleter
    def FullPath(self):
        del self.__fullPath

    @property
    def IsDir(self):
        return self.__isDir

    @IsDir.setter
    def IsDir(self, value):
        self.__isDir = value

    @IsDir.deleter
    def IsDir(self):
        del self.__isDir

    @property
    def IsChecked(self):
        return self.__isChecked

    @IsChecked.setter
    def IsChecked(self, value):
        self.__isChecked = value

    @IsChecked.deleter
    def IsChecked(self):
        del self.__isChecked
