#打印扫描一体机
class Printer:
    def status(self):
        print("打印机就绪")
    def print_file(self):
        print("打印完成")

class Scanner:
    def status(self):
        print("扫描仪就绪")
    def scan_file(self):
        print("扫描完成")

class AllInOne(Printer, Scanner):
    pass

a = AllInOne()
a.print_file()
a.scan_file()
a.status()