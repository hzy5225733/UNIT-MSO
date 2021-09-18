
import pyvisa

class api:

    def __init__(self):
        self.rm=pyvisa.ResourceManager()

    def ip_login(self,ip):
        try:
            global a
            self.a= self.rm.open_resource('TCPIP0::%s::INSTR' % (ip))
            if self.a.write('*IDN?') == 7:
                return '连接成功'
            else:
                return '连接失败'
        except:
            return '请输入正确的ip'

    def scpi_wt(self,scpi,ip):
        try:
            Le = self.rm.open_resource('TCPIP0::%s::INSTR' % (ip)).write('%s?' % (scpi))
            if Le  == len('%s?' % (scpi).encode('utf-8'))-1 and len(scpi) != 0:
                return '发送成功'
            else:
                print(self.rm.open_resource('TCPIP0::%s::INSTR' % (ip)).write('%s?' % (scpi)))
                print(len('%s?' % (scpi).encode('utf-8')))
                return '发送失败'
        except:
            print(scpi)
            return '请发送正确的指令'

    def scpi_qy(self,scpi,ip):
        if len(scpi) != 0:
            try:
                Le = self.rm.open_resource('TCPIP0::%s::INSTR' % (ip)).query('%s?' % (scpi))
                if len(scpi) != 0:
                    return Le + '查询成功'
                else:
                    return 'SCPI不能为空'
            except:
                return '请输入正确的命令'
        else:
            return '请输入正确的命令'

    def scpi_rd(self,scpi,ip):
        if len(scpi) != 0:
            try:
                self.rm.open_resource('TCPIP0::%s::INSTR' % (ip)).write('%s?' % (scpi))
                Le = self.rm.open_resource('TCPIP0::%s::INSTR' % (ip)).read()
                return Le
            except:
                return '请输入正确的命令'
        else:
            return '请输入正确的命令'
