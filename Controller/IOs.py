import serial
import time
import random

class FakeRPiGPIO:
    BCM = "BCM"
    PUD_UP = "PUD_UP"
    IN = "IN"
    OUT = "OUT"
    HIGH = 1
    LOW = 0

    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        self.mode = mode

    def setwarnings(self, state):
        self.warnings = state

    def setup(self, pin, direction, pull_up_down=None):
        self.pins[pin] = {'direction': direction, 'state': self.HIGH if pull_up_down == self.PUD_UP else self.LOW}

    def input(self, pin):
        if pin in self.pins:
            return self.pins[pin]['state']
        raise ValueError(f"Pin {pin} not set up.")

    def output(self, pin, state):
        if pin in self.pins and self.pins[pin]['direction'] == self.OUT:
            self.pins[pin]['state'] = state
        else:
            raise ValueError(f"Pin {pin} not set up or not set as output.")

    def cleanup(self):
        self.pins.clear()


class InOut:
    def __init__(self):
        self.CORTINA_LUZ = 10
        self.SINALEIRO_VERDE = 13
        self.SINALEIRO_VERMELHO = 19
        self.BOTAO_EMERGENCIA = 23
        self.BOT_ACIO_E = 22
        self.BOT_ACIO_D = 24

        self.RELE_4 = 16

        try:
            import RPi.GPIO as GPIO
            self.GPIO = GPIO
        except ImportError:
            print("RPi.GPIO not found. Using fake GPIO.")
            self.GPIO = FakeRPiGPIO()

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)

        self.GPIO.setup(self.BOT_ACIO_E, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)
        self.GPIO.setup(self.BOT_ACIO_D, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)


        self.GPIO.setup(self.CORTINA_LUZ, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)
        self.GPIO.setup(self.BOTAO_EMERGENCIA, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)

        self.GPIO.setup(self.RELE_4, self.GPIO.OUT)
        self.GPIO.setup(self.SINALEIRO_VERDE, self.GPIO.OUT)
        self.GPIO.setup(self.SINALEIRO_VERMELHO, self.GPIO.OUT)

    @property
    # off_app
    def bot_acio_e(self):
        return self.GPIO.input(self.BOT_ACIO_E)

    @property
    def bot_acio_d(self):
        return self.GPIO.input(self.BOT_ACIO_D)

    @property
    def bot_emergencia(self):
        return self.GPIO.input(self.BOTAO_EMERGENCIA)

    @property
    def cortina_luz(self):
        return self.GPIO.input(self.CORTINA_LUZ)
    
    def aciona_rele_4(self, status):
        if status == 1:
            self.GPIO.output(self.RELE_4,1)
        else:
            self.GPIO.output(self.RELE_4,0)

    def sinaleiro_verde(self):
        self.GPIO.output(self.SINALEIRO_VERMELHO, 1)
        self.GPIO.output(self.SINALEIRO_VERDE, 0)

    def sinaleiro_vermelho(self):
        self.GPIO.output(self.SINALEIRO_VERDE, 1)
        self.GPIO.output(self.SINALEIRO_VERMELHO, 0)

    def desliga_torre(self):
        self.GPIO.output(self.SINALEIRO_VERDE, 1)
        self.GPIO.output(self.SINALEIRO_VERMELHO, 1)
        
            
    
    
class IO_MODBUS:
    def __init__(self):

        self.io_rpi = InOut()
        self.ADR_1 = 1 # Endereço do WP8027 - saidas digitais
        self.ADR_2 = 2 # Endereço do WP8027 - saidas digitais
        self.ADR_3 = 3 # Endereço do WP8027 - saidas digitais
        self.ADR_4 = 4 # Endereço do WP8028 - entrada e saídas digitais
        self.ADR_1_X = 5 # Endereço que representa a conbinação entre dois modulos WP8027
        self.ADR_2_X = 6 # Endereço que representa a conbinação entre dois modulos WP8027

        self.valor_saida_direito = 0
        self.valor_saida_esquerdo = 0
        self.valor_saida_geral = 0
        self.valor_saida_geral2 = 0

        self.fake_modbus = False
        self.adr = self.ADR_1
        try:
            self.ser = serial.Serial(
                                        # port='/dev/ttyUSB0',  # Porta serial padrão no Raspberry Pi 4
                                        port='/dev/ttyAMA0',  # Porta serial padrão no Raspberry Pi 4
                                        baudrate=9600,       # Taxa de baud
                                        bytesize=8,
                                        parity="N",
                                        stopbits=1,
                                        timeout=0.1,            # Timeout de leitura
                                        xonxoff=False,         # Controle de fluxo por software (XON/XOFF)
                                        rtscts=False
                                    )
        except Exception as e:
            print(f"Erro ao conectar com a serial: {e}")
            return

    def crc16_modbus(self, data):
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if (crc & 0x0001):
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc

    def wp_8027(self, adr, out, on_off):
        if adr == self.ADR_1_X:
            if out >=1 and out <=8:# Se saída for entre 1 e 8
                adr = self.ADR_1 # Usa o módulo 1
            elif out >= 9 and out <= 12:# Se saída for entre 9 e 12
                adr = self.ADR_2 # Usa o módulo 2
                out = out-8 # e corrige para a saída do módulo 2
            elif out >=13 and out <=16:
                adr = self.ADR_2
                out = out-8
            elif out >= 17 and out <= 24:
                adr = self.ADR_3
                out = out-16

        elif adr == self.ADR_2_X:
            if out >=1 and out <=8:# Se saída for entre 1 e 8
                adr = self.ADR_1 # Usa o módulo 1
                out = out+8 # e corrige para a saída do módulo 1
            elif out >= 9 and out <= 16:# Se saída for entre 9 e 16
                adr = self.ADR_2 # Usa o módulo 2
            elif out >=17 and out <=24:
                adr = self.ADR_3
                out = out-8
        
        if self.fake_modbus == False:
            return self.wp_8027_(adr=adr, out=out,on_off=on_off)
        else:
            return -1
    def wp_8027_(self, adr, out, on_off):
        dados_recebidos = None
        mask = 0
        if adr == self.ADR_1:
            mask = self.valor_saida_esquerdo
        elif adr == self.ADR_2:
            mask = self.valor_saida_direito
        elif adr == self.ADR_3:
            mask = self.valor_saida_geral
        elif adr == self.ADR_4:
            mask = self.valor_saida_geral2

        if (adr == self.ADR_1 or adr == self.ADR_2 or adr == self.ADR_3 or adr == self.ADR_4) and (on_off==1):  # Corrigindo a condição
            id_loc = hex(adr)[2:]
            id_loc = id_loc.zfill(2).upper()

            # Deslocando 1 para a esquerda pelo número de bits especificado em out
            if out < 9:
                out_loc = (1 << (out-1+8)) | (mask)
                mask = out_loc
                
                out_val_h = (out_loc) & 0xff
                out_val_l = (out_loc>>8) & 0xff
            else:
                out_loc = 1 << (out-1-8) | (mask)
                mask = out_loc

                out_val_h = (out_loc) & 0xff 
                out_val_l = (out_loc>>8) & 0xff

            if adr == self.ADR_1:
                self.valor_saida_esquerdo = mask
            elif adr == self.ADR_2:
                self.valor_saida_direito = mask
            elif adr == self.ADR_3:
                self.valor_saida_geral = mask
            elif adr == self.ADR_4:
                self.valor_saida_geral2 = mask

        elif (adr == self.ADR_1 or adr == self.ADR_2 or adr == self.ADR_3 or adr == self.ADR_4) and (on_off==0):
            id_loc = hex(adr)[2:]
            id_loc = id_loc.zfill(2).upper()
            out_loc = 0
            # Deslocando 1 para a esquerda pelo número de bits especificado em out
            if out < 9:
                out_loc = self.retorna_bit_desligar_0_8(adr,out)
                mask = out_loc
                
                out_val_h = (out_loc) & 0xff
                out_val_l = (out_loc>>8) & 0xff
            
            else:
                out_loc = self.retorna_bit_desligar_9_10(adr,out)
                mask = out_loc

                out_val_h = (out_loc) & 0xff 
                out_val_l = (out_loc>>8) & 0xff 

            if adr == self.ADR_1:
                self.valor_saida_esquerdo = mask
            elif adr == self.ADR_2:
                self.valor_saida_direito = mask
            elif adr == self.ADR_3:
                self.valor_saida_geral = mask 
            elif adr == self.ADR_4:
                self.valor_saida_geral2 = mask 

        # Invertendo a ordem dos bits
        # out_bin = out_bin[::-1]

        for i in range(3):
            try:
                # Convertendo para hexadecimal com 4 dígitos
                out_hex = hex(out_loc)[2:].zfill(4).upper()

                hex_text = f"{id_loc}0f0000001002{out_hex}"
                bytes_hex = bytes.fromhex(hex_text)  # Transforma em hexa

                crc_result = self.crc16_modbus(bytes_hex) # Retorna o CRC

                parte_superior = (crc_result >> 8) & 0xFF  # Desloca 8 bits para a direita e aplica a máscara 0xFF
                parte_inferior = crc_result & 0xFF        # Aplica a máscara 0xFF diretamente

                # Repete-se os comandos em decimal com os devidos bytes de CRC
                self.ser.write([adr,0x0f,0,0,0,16,2,out_val_l,out_val_h,parte_inferior,parte_superior])
                self.ser.flush()
                # start_time = time.time()

                while not self.ser.readable():
                    # if time.time() - start_time > self.ser.timeout:
                    #     print("Timeout: Nenhuma resposta do escravo.")
                    #     break
                    time.sleep(0.1)  # Aguarde um curto período antes de verificar novamente

                dados_recebidos = self.ser.read(8)
                self.ser.flushInput()  # Limpa o buffer de entrada após a leitura
                if dados_recebidos != b'':
                    dados_recebidos = dados_recebidos.hex()
                    hex_text = dados_recebidos[0:2]+dados_recebidos[2:4]+dados_recebidos[4:6]+dados_recebidos[6:8]+dados_recebidos[8:10]+dados_recebidos[10:12]
                    bytes_hex = bytes.fromhex(hex_text) # Transforma em hexa
                    crc_result = self.crc16_modbus(bytes_hex) # Retorna o CRC

                    parte_superior = (crc_result >> 8) & 0xFF  # Desloca 8 bits para a direita e aplica a máscara 0xFF
                    parte_inferior = crc_result & 0xFF        # Aplica a máscara 0xFF diretamente

                    superior_crc = int(dados_recebidos[14:16],16) # Transforma de hexa para int
                    inferior_crc = int(dados_recebidos[12:14],16) # Transforma de hexa para int

                    if parte_superior == superior_crc and parte_inferior == inferior_crc:
                        dados_recebidos = dados_recebidos[14:16]
                        dados_recebidos = int(dados_recebidos,16)
                        return dados_recebidos
                    else:
                        return -1
                else:
                    return -1
            except Exception as e:
                print(f"Erro de comunicação: {e}")
                return -1 # Indica erro de alguma natureza....
        return -1
        
    def wp_8026(self, adr, input):
        if self.fake_modbus == False:
            return self.wp_8026_(adr=adr, input=input)
        else:
            return random.randint(0,1)
    def wp_8026_(self, adr, input):
        dados_recebidos = None

        if adr == self.ADR_4:
            id_loc = hex(adr)[2:]
            id_loc = id_loc.zfill(2).upper()

            hex_text = f"{id_loc}0200000010"

            bytes_hex = bytes.fromhex(hex_text)  # Transforma em hexa

            crc_result = self.crc16_modbus(bytes_hex) # Retorna o CRC

            parte_superior = (crc_result >> 8) & 0xFF  # Desloca 8 bits para a direita e aplica a máscara 0xFF
            parte_inferior = crc_result & 0xFF        # Aplica a máscara 0xFF diretamente

            for i in range(3):
                try:
                    # Repete-se os comandos em decimal com os devidos bytes de CRC
                    self.ser.write([adr,2,0,0,0,16,parte_inferior, parte_superior])
                    self.ser.flush()
                    # start_time = time.time()
                    while not self.ser.readable():
                        # if time.time() - start_time > self.ser.timeout:
                        #     print("Timeout: Nenhuma resposta do escravo.")
                        #     return -1
                        time.sleep(0.1)  # Aguarde um curto período antes de verificar novamente
                    time.sleep(0.1)
                    dados_recebidos = self.ser.read(7)
                    self.ser.flushInput()  # Limpa o buffer de entrada após a leitura
                    if dados_recebidos != b'':
                        dados_recebidos = dados_recebidos.hex()
                        hex_text = dados_recebidos[0:2]+dados_recebidos[2:4]+dados_recebidos[4:6]+dados_recebidos[6:8]+dados_recebidos[8:10]
                        bytes_hex = bytes.fromhex(hex_text) # Transforma em hexa
                        crc_result = self.crc16_modbus(bytes_hex) # Retorna o CRC

                        parte_superior = (crc_result >> 8) & 0xFF  # Desloca 8 bits para a direita e aplica a máscara 0xFF
                        parte_inferior = crc_result & 0xFF        # Aplica a máscara 0xFF diretamente

                        superior_crc = int(dados_recebidos[12:14],16) # Transforma de hexa para int
                        inferior_crc = int(dados_recebidos[10:12],16) # Transforma de hexa para int

                        if parte_superior == superior_crc and parte_inferior == inferior_crc:
                            dados_recebidos = dados_recebidos[6:10]
                            dados_recebidos = int(dados_recebidos, 16)
                            # Separando em duas partes (0x01 e 0x00)
                            hex_part1 = dados_recebidos >> 8  # Primeiros 8 bits
                            hex_part2 = dados_recebidos & 0xFF  # Últimos 8 bits
                            result=0
                            if input < 9:
                                test = 0x01*( pow(2,input-1) )
                                result = ( (hex_part1 & (test))  )
                                result = result>>(input-1)
                                # if result > 2:
                                #     result=1
                            else:
                                test = 0x01*( pow(2,(input-8)-1) )
                                result = ( (hex_part2 & (test))  )
                                result = result>>((input-8)-1)

                            return result
                        else:
                            return -1
                    else:
                        return -1
                except:
                    print("Erro de comunicação")
                    return -1 # Indica erro de alguma natureza....
            return -1


        return 0

    def retorna_bit_desligar_0_8(self, adr, bit):
        out_loc = 0
        mask = 0

        if adr == self.ADR_1:
            mask = self.valor_saida_esquerdo
        elif adr == self.ADR_2:
            mask = self.valor_saida_direito
        elif adr == self.ADR_3:
            mask = self.valor_saida_geral
        elif adr == self.ADR_4:
            mask = self.valor_saida_geral2

        if bit==1:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xFEFF
        if bit==2:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xFDFF
        if bit==3:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xFBFF
        if bit==4:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xF7FF
        if bit==5:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xEFFF
        if bit==6:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xDFFF
        if bit==7:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0xBFFF
        if bit==8:
            out_loc = ( (1 << (bit-1+8)) | (mask) ) & 0x7FFF  

        return out_loc   
    def retorna_bit_desligar_9_10(self, adr, bit):
        out_loc = 0
        mask = 0

        if adr == self.ADR_1:
            mask = self.valor_saida_esquerdo
        elif adr == self.ADR_2:
            mask = self.valor_saida_direito
        elif adr == self.ADR_3:
            mask = self.valor_saida_geral
        elif adr == self.ADR_4:
            mask = self.valor_saida_geral2

        if bit==9:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFFE
        if bit==10:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFFD
        if bit==11:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFFB
        if bit==12:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFF7
        if bit==13:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFEF
        if bit==14:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFDF
        if bit==15:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFFBF
        if bit==16:
            out_loc = ( (1 << (bit-1-8)) | (mask) ) & 0xFF7F

        return out_loc 
    # def sleep_ms(self, milliseconds):
    #     ms = milliseconds*1000
    #     loop = QEventLoop()
    #     QTimer.singleShot(int(ms), loop.quit)
    #     loop.exec_()


if __name__ == '__main__':
    import time
    io = IO_MODBUS()
    cmd = ""
    while cmd != "q":
        adr = input("Digite o endereço\n")
        cmd = input("Digite a saida que queira testar.\n")
        stat = input("Digite 1=ligar 0=desligar.\n")
        try:
            io.wp_8027(int(adr),int(cmd),int(stat))
            print(f"A saida {int(cmd)} foi acionada.")
        except:
            if cmd != "q":
                print("Digite um número válido.")
        time.sleep(1)