#同意消息发送入口
class Notifier:
    def send(self,message):
        pass

class EmailNotifier(Notifier):
    def send(self,message):
        print(f"邮件通知:{message}")

class SmsNotifier(Notifier):
    def send(self,message):
        print(f"短信通知:{message}")

class AppNotifier:   #鸭子类型要求要拥有与调用的同名且参数匹配的方法
    def send(self,message):
        print(f"应用通知:{message}")


def notify(sender, message):
     sender.send(message)


notify(EmailNotifier(),"作业已提交")   #注意类名后面要加括号否则就只是一个类名没有创建类的对象
notify(SmsNotifier(),"作业已提交")
notify(AppNotifier(),"作业已提交")