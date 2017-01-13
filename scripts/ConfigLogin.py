{
    AFWConst.Name: "PageLogin",
    AFWConst.Type: AFWConst.WebPage,
    AFWConst.SubUI: [
    {
        AFWConst.Name: "LinkAccountLogin",
        AFWConst.Type: AFWConst.WebLink,
        AFWConst.Text: "帐号登录",
        AFWConst.BreakTime: 20000 # 20000 is need to set proxy in VM
    },
    {
        AFWConst.Name: "EditUserName",
        AFWConst.Type: AFWConst.WebEditBox,
        AFWConst.AttrID: "TANGRAM__PSP_4__userName",
        AFWConst.BreakTime: 1000
    },
    {
        AFWConst.Name: "EditPassword",
        AFWConst.Type: AFWConst.WebEditBox,
        AFWConst.AttrID: "TANGRAM__PSP_4__password",
        AFWConst.BreakTime: 1000
    },
    {
        AFWConst.Name: "ButtonLogin",
        AFWConst.Type: AFWConst.WebButton,
        AFWConst.AttrID: "TANGRAM__PSP_4__submit",
        AFWConst.BreakTime: 1000
    }]
}
