# эта программа отвечает за отправку увидомлений в Windows


import plyer

def notification(messeage):
    try:
        plyer.notification.notify( message=f'{messeage}',
            app_name='Programmers dating',
            app_icon='program\icons\client.ico',
            title='Programmers dating', )
        return True
    except:
        return False

def notification2(messeage):
    try:
        plyer.notification.notify( message=f'{messeage}',
            app_name='Programmers dating',
            app_icon='icons\client.ico',
            title='Programmers dating', )
        return True
    except:
        return False

if __name__ == '__main__':
    notification(messeage="1 новое сообщение")