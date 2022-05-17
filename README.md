# S-DISCORD-BOT

星魂秋夢委託之Discord Bot  
我的Python首作 寫得不好請見諒><  

V1版本更新
加入/退出訊息 Embed
對新發出的訊息按表情獲得身分組

V2版本更新  
-user @用戶 - 查詢用戶資料  
-clear 數字 - 刪除訊息功能(需有權限mange.message)  
-sayd 文字 - 代公告系統(需有權限mange.message)  

V3版本
最新更新移除了原本繁雜的重開就跳訊息通知
改成直接對指定訊息按表情即可獲得身分組

*使用注意事項  
需修改處 setting.json 中的TOKEN，與CHANNEL_ID  
還有bot.py中 給予身分組的地方 把權限組名、指定訊息改成你想要的(ROLE_ID, MESSAGE_ID)  