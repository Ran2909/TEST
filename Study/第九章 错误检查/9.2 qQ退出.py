breaks=['q','Q']
while True:
    try:
        a=input('请输入被除数')
        b=input('再输入除数')
        if (a in breaks) and (b in breaks):
            print('检测到输入数据中有Q或q，已退出循环')
            break
        print('商为',float(a)/float(b))

    except ValueError:
        print('输入数据错误，请输入数字！！')

    except ZeroDivisionError:
        print('除数是0！！请重新输入')


