from easygui import *

list1 = '【*真实姓名】为必填项\n'+'【*手机号码】为必填项\n'+'【*电子邮箱】为必填项\n'
list2 = ['【*用户名】', '【*真实姓名】', '【固定电话】', '【*手机号码】', '【QQ】', '【*电子邮箱】']

while 1:
    msg = multenterbox(list1, '账号中心', list2)
    if msg[0] != '' and msg[1] != '' and msg[3] != '' and msg[5]:
        break
    else:
        msgbox('带*项目为必填项，请重新填写！', '提示')

msgbox('账号信息登记完成！','账户中心')
