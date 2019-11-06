{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
        {
            # Web Config
            AFWConst.Name: "Browser",
            AFWConst.Type: AFWConst.UIBrowser,
            AFWConst.Plugin: {
                AFWConst.PluginName: AFWConst.PluginSelenium
            },
            AFWConst.Browser: AFWConst.BrowserChrome,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "URLLogin",
                AFWConst.Type: AFWConst.UIWebEntry,
                AFWConst.URL: "https://pan.baidu.com",
                AFWConst.BreakTime: 2000,
                AFWConst.SubUI: [
                    ImportFile("login/Config.py"),
                    ImportFile("main/Config.py")
                ]
            }]
        },
        {
            # App Config
            AFWConst.Name: "Desktop",
            AFWConst.Type: AFWConst.UIDesktop,
            AFWConst.Plugin: {
                AFWConst.PluginName: AFWConst.PluginProxyApp,
                AFWConst.Proxy: {
                    AFWConst.ProxyType: AFWConst.ProxyLocal,
                    AFWConst.ProxyLauncher: "c:/App/IronPython-2.7.5/ipy.exe",
                    AFWConst.PluginName: "PluginMSApp"
                }
            },
            AFWConst.SubUI: [
                ImportFile("win/Config.py")
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
