{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
        {
            # Web Config
            AFWConst.Name: "Browser",
            AFWConst.Type: AFWConst.UIWeb,
            AFWConst.Plugin: {
                AFWConst.PluginName: AFWConst.PluginSelenium
            },
            AFWConst.Browser: AFWConst.BrowserFireFox,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "URLLogin",
                AFWConst.Type: AFWConst.WebEntry,
                AFWConst.URL: "http://pan.baidu.com",
                AFWConst.BreakTime: 1000,
                AFWConst.SubUI: [
                    ImportFile("ConfigLogin.py"),
                    ImportFile("ConfigMain.py")
                ]
            }],
        },
        {
            # App Config
            AFWConst.Name: "Desktop",
            AFWConst.Type: AFWConst.AppRoot,
            AFWConst.Plugin: {
                AFWConst.PluginName: AFWConst.PluginProxyApp,
                AFWConst.Proxy: {
                    AFWConst.ProxyType: AFWConst.ProxyLocal,
                    AFWConst.ProxyLauncher: "python",
                    AFWConst.PluginName: "PluginSelenium"
                }
            },
            AFWConst.SubUI: [
                ImportFile("ConfigWinForm.py")
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
