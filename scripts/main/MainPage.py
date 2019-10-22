
class MainPage:
    def __init__(self, browser):
        if browser is None:
            raise Exception("None browser for MainPage")
        self.__browser = browser

    ### Properties ###

    def GetUploadFileButton(self):
        mainPage = self.__browser.FindSubUI("PageMain")
        uploadFileButton = mainPage.FindSubUI("ButtonUploadFile")
        return uploadFileButton

    def GetAllFileButton(self):
        mainPage = self.__browser.FindSubUI("PageMain")
        allFileButton = mainPage.FindSubUI("ButtonAllFile")
        return allFileButton

    def OpenAlbum(self):
        mainPage = self.__browser.FindSubUI("PageMain")
        folderAlbum = mainPage.FindSubUI("FolderAlbum")
        folderAlbum.Click()
