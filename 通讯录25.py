print('欢迎进入通讯录程序')
print('1 ：查询联系人资料')
print('2 :插入新的联系人')
print('3 ：删除已有联系人')
print('4 ：退出通讯录程序')
dict1 = {}
while 1:
    i = input('请输入相关的指令代码：')
    if i == '1':
        name = input('请输入联系人名字：')
        if name in dict1:
            print(name +' : '+dict1[name])
        else:
            print('你所输入的用户 '+name+' 不存在')
    if i == '2':
        name = input('请输入联系人名字：')
        if name in dict1:
            print('您输入的用户已存在-->> '+name+' : '+dict1[name])
            judgement = input('是否修改用户资料（YES/NO）')
            if judgement == 'YES':
                dict1[name] = input('请输入用户联系电话')
        else:
            dict1[name] = input('请输入用户联系电话')
            print('创建联系人 '+name+' 成功！')
    if i =='3':
        name = input('请输入联系人名字：')
        if name in dict1:
            dict1.pop(name)
            print(name+' 已删除成功！')
        else:
            print('不存在该联系人！')
    if i == '4':
        break
print('感谢使用通讯录程序')



