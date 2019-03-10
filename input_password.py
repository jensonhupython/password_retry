# CH3_44 Try to input password
# 密碼重試程式
# 1. 先在程式碼中, 設定好密碼 password = 'a123456'
# 2. 讓使用者[最多輸入3次密碼]
# 3. 不對的話, 就印出"密碼錯誤"! 還有_次輸入機會
# 4. 對的話, 就印出"登入成功!"
# 建立GitHub專案

password = 'a123456'

input_account = 1;

while input_account < 4:
    user_password = input("請輸入密碼: ")
    
    if password == user_password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!!')
        print('輸入次數: ', input_account)
        print('還有幾次輸入次數: ', 3 - input_account)
    input_account = input_account + 1
    

if input_account > 3:
    print('已經輸入3次的錯誤密碼!')    








