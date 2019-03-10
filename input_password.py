# CH3_44 Try to input password
# 密碼重試程式
# 1. 先在程式碼中, 設定好密碼 password = 'a123456'
# 2. 讓使用者[最多輸入3次密碼]
# 3. 不對的話, 就印出"密碼錯誤"! 還有_次輸入機會
# 4. 對的話, 就印出"登入成功!"
# 建立GitHub專案

password = 'a123456'

input_account = 3;  # 剩餘機會

while input_account > 0:
    user_password = input("請輸入密碼: ")

    input_account = input_account - 1

    if password == user_password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if input_account > 0:
            print('還有', input_account, '次機會')
        else:
            print('沒機會嘗試了!!!')

  








