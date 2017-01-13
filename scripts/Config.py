{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
        {
            AFWConst.Name: "Browser",
            AFWConst.Type: AFWConst.UIWeb,
            AFWConst.Plugin: AFWConst.PluginSelenium,
            AFWConst.Browser: AFWConst.BrowserChrome,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "URLLogin",
                AFWConst.Type: AFWConst.WebURL,
                AFWConst.URL: "http://pan.baidu.com",
                AFWConst.BreakTime: 1000
            },
                ImportFile("ConfigLogin.py"),
                ImportFile("ConfigMain.py")
            ]
        }]
    },

    AFWConst.Action: {
        AFWConst.SubAction: [
        {
            AFWConst.Script: "Script.py"
        }]
    }
}
