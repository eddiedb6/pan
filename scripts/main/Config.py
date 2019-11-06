{
    AFWConst.Name: "PageMain",
    AFWConst.Type: AFWConst.UIWebPage,
    AFWConst.SubUI: [
    {
        AFWConst.Name: "NewFolderWrapper",
        AFWConst.Type: AFWConst.UICommon,
        AFWConst.AttrClass: "ExFGye",
        AFWConst.SubUI: [
        {
            AFWConst.Name: "NewFolderInput",
            AFWConst.Type: AFWConst.UIInputable,
            AFWConst.AttrClass: "GadHyA"
        },
        {
            AFWConst.Name: "NewFolderInputConfirm",
            AFWConst.Type: AFWConst.UIClickable,
            AFWConst.AttrClass: "iibZwl4"
        }]
    },
        ImportFile("main/bar/Config.py"),
        ImportFile("main/panel/Config.py"),
        ImportFile("main/area/Config.py"),
        ImportFile("main/uploader/Config.py")
    ]
}
