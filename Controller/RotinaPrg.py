import time
import sys

# Condutividade
"""
"ligacao1":[0,[0,0,0],0,"NOME_CONECAO"]
        |   |  | | |  |    |
        |   |  | | |  |    |_Nome da conexão 
        |   |  | | |  |______Pino da tomada dos eletrodos
        |   |  | | |_________Coordenada y do label do eletrodo na imagem
        |   |  | |___________Coordenada x do label do eletrodo na imagem
        |   |  |_____________Número do eletrodo a ser usado
        |   |________________Pino da tomada dos conectores
        |____________________Número da conexão
"""

# Isolação
"""
"ligacao1":[0,0,"NOME_CONECAO",0,0]
        |   | |   |            | |
        |   | |   |            | |___Eletrodo associado ao conector do Pino da tomada do eletrodo
        |   | |   |            |_____Eletrodo associado ao conector do Pino da tomada dos conectores
        |   | |   |__________________Nome da Conexão
        |   | |______________________Pino da tomada do eletrodo
        |   |________________________Pino da tomada dos conectores
        |____________________________Número da conexão
"""
class RotinaPrg:
    def __init__(self, dado=None, io=None, db=None):

        self.TEMPO_DESCIDA_PISTAO = 1500
        self.TEMPO_SUBIDA_PISTAO = 100
        self.TEMPO_ACIONAMENTO_RELE = 25
        self.TEMPO_ACIONAMENTO_RELE_ISO = 100

        self.dado=dado
        self.io=io
        self.database=db

        # Variável que vai ser acessado por outra classe que contém o eletrodo que esta sendo testado sua condutividade
        self.eletrodo_testando_condu_e = [0,0]
        self.eletrodo_testando_condu_d = [0,0]

        # Veriável que vai ser acessado por outra classe [0,0] -> indice 0 = associado com o conector da peça -> indice 1 associado com conector de eletrodos
        self.eletrodo_testando_iso_e = [0,0]
        self.eletrodo_testando_iso_d = [0,0]

        # Essas variáveis serão usadas em ExecucaoPrograma para monitorar erros
        self.flag_erro_porta_traseira = False # Para indicar que porta traseira está aberta
        self.flag_erro_cortina_luz = False # Para indicar se cortina de luz acionou
        self.flag_erro_pistao = False # Para indicar se pistão está na posição certa
        self.flag_erro_geral = False
        #************************************************************************************

        self.nome_programa = ""
        self.url_img_esquerdo = ""
        self.url_img_direito = ""
    
        self.coord_eletrodo_esquerdo = [ None for _ in range(14) ]
        self.coord_eletrodo_direito = [ None for _ in range(14) ]
        
        self.condutividade_esquerdo = {
            "ligacao1":[0,[0,0,0],0, ""],
            "ligacao2":[0,[0,0,0],0, ""],
            "ligacao3":[0,[0,0,0],0, ""],
            "ligacao4":[0,[0,0,0],0, ""],
            "ligacao5":[0,[0,0,0],0, ""],
            "ligacao6":[0,[0,0,0],0, ""],
            "ligacao7":[0,[0,0,0],0, ""],
            "ligacao8":[0,[0,0,0],0, ""],
            "ligacao9":[0,[0,0,0],0, ""],
            "ligacao10":[0,[0,0,0],0, ""],
            "ligacao11":[0,[0,0,0],0, ""],
            "ligacao12":[0,[0,0,0],0, ""],
            "foi_testado": False
        }
        self.isolacao_esquerdo = {
            "ligacao1":[0,0,"",0,0],
            "ligacao2":[0,0,"",0,0],
            "ligacao3":[0,0,"",0,0],
            "ligacao4":[0,0,"",0,0],
            "ligacao5":[0,0,"",0,0],
            "ligacao6":[0,0,"",0,0],
            "ligacao7":[0,0,"",0,0],
            "ligacao8":[0,0,"",0,0],
            "ligacao9":[0,0,"",0,0],
            "ligacao10":[0,0,"",0,0],
            "ligacao11":[0,0,"",0,0],
            "ligacao12":[0,0,"",0,0],
            "ligacao13":[0,0,"",0,0],
            "ligacao14":[0,0,"",0,0],
            "ligacao15":[0,0,"",0,0],
            "ligacao16":[0,0,"",0,0],
            "ligacao17":[0,0,"",0,0],
            "ligacao18":[0,0,"",0,0],
            "ligacao19":[0,0,"",0,0],
            "ligacao20":[0,0,"",0,0],
            "foi_testado": False
        }
        self.condutividade_direito = {
            "ligacao1":[0,[0,0,0],0, ""],
            "ligacao2":[0,[0,0,0],0, ""],
            "ligacao3":[0,[0,0,0],0, ""],
            "ligacao4":[0,[0,0,0],0, ""],
            "ligacao5":[0,[0,0,0],0, ""],
            "ligacao6":[0,[0,0,0],0, ""],
            "ligacao7":[0,[0,0,0],0, ""],
            "ligacao8":[0,[0,0,0],0, ""],
            "ligacao9":[0,[0,0,0],0, ""],
            "ligacao10":[0,[0,0,0],0, ""],
            "ligacao11":[0,[0,0,0],0, ""],
            "ligacao12":[0,[0,0,0],0, ""],
            "foi_testado": False
        }
        self.isolacao_direito = {
            "ligacao1":[0,0,"",0,0],
            "ligacao2":[0,0,"",0,0],
            "ligacao3":[0,0,"",0,0],
            "ligacao4":[0,0,"",0,0],
            "ligacao5":[0,0,"",0,0],
            "ligacao6":[0,0,"",0,0],
            "ligacao7":[0,0,"",0,0],
            "ligacao8":[0,0,"",0,0],
            "ligacao9":[0,0,"",0,0],
            "ligacao10":[0,0,"",0,0],
            "ligacao11":[0,0,"",0,0],
            "ligacao12":[0,0,"",0,0],
            "ligacao13":[0,0,"",0,0],
            "ligacao14":[0,0,"",0,0],
            "ligacao15":[0,0,"",0,0],
            "ligacao16":[0,0,"",0,0],
            "ligacao17":[0,0,"",0,0],
            "ligacao18":[0,0,"",0,0],
            "ligacao19":[0,0,"",0,0],
            "ligacao20":[0,0,"",0,0],
            "foi_testado": False
        }

    def clear_dados_esquerdo(self):
        self.url_img_esquerdo=""
        self.coord_eletrodo_esquerdo = [ None for _ in range(10) ]

        self.condutividade_esquerdo = {
            "ligacao1":[0,[0,0,0],0, ""],
            "ligacao2":[0,[0,0,0],0, ""],
            "ligacao3":[0,[0,0,0],0, ""],
            "ligacao4":[0,[0,0,0],0, ""],
            "ligacao5":[0,[0,0,0],0, ""],
            "ligacao6":[0,[0,0,0],0, ""],
            "ligacao7":[0,[0,0,0],0, ""],
            "ligacao8":[0,[0,0,0],0, ""],
            "ligacao9":[0,[0,0,0],0, ""],
            "ligacao10":[0,[0,0,0],0, ""],
            "ligacao11":[0,[0,0,0],0, ""],
            "ligacao12":[0,[0,0,0],0, ""],
            'foi_testado':False
        }
        self.isolacao_esquerdo = {
            "ligacao1":[0,0,"",0,0],
            "ligacao2":[0,0,"",0,0],
            "ligacao3":[0,0,"",0,0],
            "ligacao4":[0,0,"",0,0],
            "ligacao5":[0,0,"",0,0],
            "ligacao6":[0,0,"",0,0],
            "ligacao7":[0,0,"",0,0],
            "ligacao8":[0,0,"",0,0],
            "ligacao9":[0,0,"",0,0],
            "ligacao10":[0,0,"",0,0],
            "ligacao11":[0,0,"",0,0],
            "ligacao12":[0,0,"",0,0],
            "ligacao13":[0,0,"",0,0],
            "ligacao14":[0,0,"",0,0],
            "ligacao15":[0,0,"",0,0],
            "ligacao16":[0,0,"",0,0],
            "ligacao17":[0,0,"",0,0],
            "ligacao18":[0,0,"",0,0],
            "ligacao19":[0,0,"",0,0],
            "ligacao20":[0,0,"",0,0],
            "foi_testado": False
        }

    def clear_dados_direito(self):
        self.url_img_direito="" 

        self.coord_eletrodo_direito = [ None for _ in range(10) ]

        self.condutividade_direito = {
            "ligacao1":[0,[0,0,0],0, ""],
            "ligacao2":[0,[0,0,0],0, ""],
            "ligacao3":[0,[0,0,0],0, ""],
            "ligacao4":[0,[0,0,0],0, ""],
            "ligacao5":[0,[0,0,0],0, ""],
            "ligacao6":[0,[0,0,0],0, ""],
            "ligacao7":[0,[0,0,0],0, ""],
            "ligacao8":[0,[0,0,0],0, ""],
            "ligacao9":[0,[0,0,0],0, ""],
            "ligacao10":[0,[0,0,0],0, ""],
            "ligacao11":[0,[0,0,0],0, ""],
            "ligacao12":[0,[0,0,0],0, ""],
            'foi_testado':False
        }
        self.isolacao_direito = {
            "ligacao1":[0,0,"",0,0],
            "ligacao2":[0,0,"",0,0],
            "ligacao3":[0,0,"",0,0],
            "ligacao4":[0,0,"",0,0],
            "ligacao5":[0,0,"",0,0],
            "ligacao6":[0,0,"",0,0],
            "ligacao7":[0,0,"",0,0],
            "ligacao8":[0,0,"",0,0],
            "ligacao9":[0,0,"",0,0],
            "ligacao10":[0,0,"",0,0],
            "ligacao11":[0,0,"",0,0],
            "ligacao12":[0,0,"",0,0],
            "ligacao13":[0,0,"",0,0],
            "ligacao14":[0,0,"",0,0],
            "ligacao15":[0,0,"",0,0],
            "ligacao16":[0,0,"",0,0],
            "ligacao17":[0,0,"",0,0],
            "ligacao18":[0,0,"",0,0],
            "ligacao19":[0,0,"",0,0],
            "ligacao20":[0,0,"",0,0],
            "foi_testado": False
        }

    def check_flags_erros(self):
        if self.flag_erro_porta_traseira == True or self.flag_erro_cortina_luz == True or self.flag_erro_pistao == True or self.flag_erro_geral == True:
            return True
        else:
            return False
        
    def sleep_check_erro(self, tempo):
        for _ in range(tempo):
            if self.check_flags_erros() == False: #  se não houver erros
                time.sleep(0.001)
            else:
                return True
        return False

    def teste_esquerdo_direito_condutividade(self, lado):
        result = []
        self.limpa_saidas_esquerda_direita() # desliga todas as saídas para evitar curto
        if lado == 0: # Corresponde ao lado esquerdo
            # Abaixa pistão - Liga válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 1)
            self.abaixa_pistao()

            # Desliga contator que selaciona tensão - desligado seleciona 12VCC
            self.io.wp_8027(self.io.ADR_4,1,0)
            
            #Aguarda pistão descer
            if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:

                # realiza testes de condutividade
                result = self.combinacao_condutividade_esquerdo()

                # Sobe pistão - Liga Válvula
                # self.io.wp_8027(self.io.ADR_4, 5, 1) 
                self.sobe_pistao()

                #Aguarda pistão subir
                if self.sleep_check_erro(self.TEMPO_SUBIDA_PISTAO) == False:   
                    # Sobe pistão - Desliga Válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
                    pass
                else:
                    result = []
                    # Sobe pistão - Desliga Válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
            else:
                result = []
                # Abaixa pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 4, 0)

            return result

        elif lado == 1: # Corresponde ao lado direito
            # Abaixa pistão - Liga válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 1)
            self.abaixa_pistao()

            # Desliga contator que selaciona tensão - desligado seleciona 12VCC
            self.io.wp_8027(self.io.ADR_4,1,0)
            
            #Aguarda pistão descer
            if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:
                # Abaixa pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 4, 0)

                # realiza testes de condutividade
                result = self.combinacao_condutividade_direito()

                # Sobe pistão - Liga Válvula
                # self.io.wp_8027(self.io.ADR_4, 5, 1) 
                self.sobe_pistao()

                #Aguarda pistão subir
                if self.sleep_check_erro(self.TEMPO_SUBIDA_PISTAO) == False:    
                    # Sobe pistão - Desliga Válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
                    pass
                else:
                    result = []
                    # Sobe pistão - Desliga Válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
            else:
                result = []
                # Abaixa pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 4, 0)

            return result
    
    def esquerdo_direito_condutividade(self, lado):
        result = []
        if lado == 0: # Corresponde ao lado esquerdo
            # Desliga contator que selaciona tensão - desligado seleciona 12VCC
            self.io.wp_8027(self.io.ADR_4,1,0)

            # realiza testes de condutividade
            result = self.combinacao_condutividade_esquerdo()
            self.eletrodo_testando_condu_e[0]=0
            self.eletrodo_testando_condu_e[1]=0
            return result

        elif lado == 1: # Corresponde ao lado direito
            # Desliga contator que selaciona tensão - desligado seleciona 12VCC
            self.io.wp_8027(self.io.ADR_4,1,0)

            # realiza testes de condutividade
            result = self.combinacao_condutividade_direito()
            self.eletrodo_testando_condu_d[0]=0
            self.eletrodo_testando_condu_d[1]=0
            return result

    """
    "ligacao1":[0,[0,0,0],0,"NOME_CONECAO"]
            |   |  | | |  |_Pino da tomada dos eletrodos
            |   |  | | |____Coordenada y do label do eletrodo na imagem
            |   |  | |______Coordenada x do label do eletrodo na imagem
            |   |  |________Número do eletrodo a ser usado
            |   |___________Pino da tomada dos conectores
            |_______________Nome da conexão
    """

    def aciona_combinacao(self, i, lado):
        if lado == "esquerdo":
            adr = self.io.ADR_1_X
            ligacao = self.condutividade_esquerdo[f"ligacao{i}"]
        elif lado == "direito":
            adr = self.io.ADR_2_X
            ligacao = self.condutividade_direito[f"ligacao{i}"]
        else:
            raise ValueError("Lado deve ser 'esquerdo' ou 'direito'")

        # Aciona pino da tomada de conectores - DO_0x do ADR_X
        if self.io.wp_8027(adr, ligacao[0], 1) == -1:
            return False
        # Aciona pino da tomada de eletrodos - DO_0x+12 do ADR_X - Tem que adicionar 12 para ir de 13-24 que é 1+12 - 12+12
        if self.io.wp_8027(adr, ligacao[2] + 12, 1) == -1:
            return False

        return True
    
    def desaciona_combinacao(self, i, lado):
        if lado == "esquerdo":
            adr = self.io.ADR_1_X
            ligacao = self.condutividade_esquerdo[f"ligacao{i}"]
        elif lado == "direito":
            adr = self.io.ADR_2_X
            ligacao = self.condutividade_direito[f"ligacao{i}"]
        else:
            raise ValueError("Lado deve ser 'esquerdo' ou 'direito'")

        # desliga saída para não conflitar com o próximo
        self.io.wp_8027(adr, ligacao[0], 0)
        self.io.wp_8027(adr, ligacao[2] + 12, 0)

    def combinacao_condutividade_esquerdo(self):
        result = []

        for i in range(1,13):
            if self.condutividade_esquerdo[f"ligacao{i}"][3] != "":
                # Associa qual eletrodo está sendo associado, para acesso externo à classe
                self.eletrodo_testando_condu_e[0]= self.condutividade_esquerdo[f"ligacao{i}"][1][0]

                for _ in range(10):
                    if self.aciona_combinacao(i, "esquerdo") == True:
                        break

                # Aguarda um pequeno tempo para acionamento do rele
                if self.sleep_check_erro(self.TEMPO_ACIONAMENTO_RELE) == False:

                    # faz leitura e associa a variável
                    # índice 0 = número da ligação índice 1 = Nome da ligação índice 2 = status de ligaçao - 0=não passou 1=passou
                    for _ in range(10):
                        self.eletrodo_testando_condu_e[1] = self.io.wp_8026(self.io.ADR_4, 1)  # Associa se eletrodo passou ou não passou
                        if self.eletrodo_testando_condu_e[1] == 1:
                            break
                    
                    if self.eletrodo_testando_condu_e[1] == 0:
                        # Liga contator que selaciona tensão - desligado seleciona 12VCC
                        self.io.wp_8027(self.io.ADR_4,1,1)
                        # Inicia megômetro
                        self.start_megometro()
                        # Aguarda um tempo para megômetro ser acionado
                        time.sleep(0.5)
                        # Faz leitura do megômetro
                        self.eletrodo_testando_condu_e[1] = self.io.wp_8026(self.io.ADR_4, 8)  # Associa se eletrodo passou ou não passou                     
                        # Desliga contator que selaciona tensão - desligado seleciona 12VCC
                        self.io.wp_8027(self.io.ADR_4,1,0)  
                        # Para megômetro
                        self.stop_megometro()

                    
                    result.append( [i,self.condutividade_esquerdo[f"ligacao{i}"][3],self.eletrodo_testando_condu_e[1]] )

                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao(i, "esquerdo")
                else:
                    result = []
                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao(i, "esquerdo")

            else:
                break
        return result

    def combinacao_condutividade_direito(self):
        result = []

        for i in range(1,13):
            if self.condutividade_direito[f"ligacao{i}"][3] != "":
                # Associa qual eletrodo está sendo assiciado, para acesso externo à classe
                self.aciona_combinacao(i, "direito")

                # Aguarda um pequeno tempo para acionamento do rele
                if self.sleep_check_erro(self.TEMPO_ACIONAMENTO_RELE) == False:

                    # faz leitura e associa a variável
                    # índice 0 = número da ligação índice 1 = Nome da ligação índice = status de ligaçao - 0=não passou 1=passou
                    for _ in range(10):
                        self.eletrodo_testando_condu_d[1] = self.io.wp_8026(self.io.ADR_4, 1)  # Associa se eletrodo passou ou não passou
                        if self.eletrodo_testando_condu_d[1] == 1:
                            break
                    result.append( [i,self.condutividade_direito[f"ligacao{i}"][3],self.eletrodo_testando_condu_d[1]] )

                    if self.eletrodo_testando_condu_d[1] == 0:
                        # Liga contator que selaciona tensão - desligado seleciona 12VCC
                        self.io.wp_8027(self.io.ADR_4,1,1)
                        # Inicia megômetro
                        self.start_megometro()
                        # Aguarda um tempo para megômetro ser acionado
                        time.sleep(0.5)
                        # Faz leitura do megômetro
                        self.eletrodo_testando_condu_d[1] = self.io.wp_8026(self.io.ADR_4, 8)

                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao(i, "direito")
                else:
                    result = []
                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao(i, "direito")
                    break
            else:
                break

        return result 
    def reset_megometro(self):
        # Depois de conferido a isolação pelo megômetro, reseta relé que liga entrada
        self.io.wp_8027(self.io.ADR_4,8,1)
        time.sleep(0.1)
        self.io.wp_8027(self.io.ADR_4,8,0)             
    
    def teste_esquerdo_direito_isolacao(self, lado):
        result = []
        self.limpa_saidas_esquerda_direita() # desliga todas as saídas para evitar curto
        if lado == 0: # Corresponde ao lado esquerdo
            # Abaixa pistão - Liga Válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 1)
            self.abaixa_pistao()

            #Aguarda pistão descer
            if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:
                # Abaixa pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 4, 0)

                # Garante o Stop do megômetro - pulso
                self.stop_megometro()

                # Liga contator que seleciona tensão - ligado seleciona Megômetro
                self.io.wp_8027(self.io.ADR_4,1,1)

                # Reseta relé que liga entrada de mêgometro atuado
                self.reset_megometro()
            
                # self.start_megometro()

                result = self.combinacao_isolacao_esquerdo()

                self.stop_megometro()

                # Desliga contator que seleciona tensão - ligado seleciona Megômetro
                self.io.wp_8027(self.io.ADR_4,1,0)

                # Sobe pistão - Liga válvula
                # self.io.wp_8027(self.io.ADR_4, 5, 1) 
                self.sobe_pistao()
                #Aguarda pistão subir
                if self.sleep_check_erro(self.TEMPO_SUBIDA_PISTAO) ==  False:
                    # Sobe pistão - Desliga válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
                    pass
                else:
                    result = []
                    # Sobe pistão - Desliga válvula
                    # self.io.wp_8027(self.io.ADR_4, 5, 0)
            else:
                result = []
                # Sobe pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 5, 0)

        elif lado == 1: # se for lado direito
            # Abaixa pistão - Liga Válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 1)
            self.abaixa_pistao()

            #Aguarda pistão descer
            if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:
                # Abaixa pistão - Desliga válvula
                # self.io.wp_8027(self.io.ADR_4, 4, 0)

                # Garante o Stop do megômetro - pulso
                self.stop_megometro()

                # Liga contator que seleciona tensão - ligado seleciona Megômetro
                self.io.wp_8027(self.io.ADR_4,1,1)

                # Reseta relé que liga entrada de mêgometro atuado
                self.reset_megometro()

                # self.start_megometro()
                result = self.combinacao_isolacao_direito()
                self.stop_megometro()

                # Desliga contator que seleciona tensão - ligado seleciona Megômetro
                self.io.wp_8027(self.io.ADR_4,1,0)

                # Sobe pistão - Liga válvula
                # self.io.wp_8027(self.io.ADR_4, 5, 1) 
                self.sobe_pistao()
                #Aguarda pistão subir
                if self.sleep_check_erro(self.TEMPO_SUBIDA_PISTAO) == False: 
                    # Sobe pistão - Desliga válvula
                    self.io.wp_8027(self.io.ADR_4, 5, 0) 
                else:
                    result = []
                    # Sobe pistão - Desliga válvula
                    self.io.wp_8027(self.io.ADR_4, 5, 0) 
            else:
                result = []
                # Abaixa pistão - Desliga válvula
                self.io.wp_8027(self.io.ADR_4, 4, 0)
        
        return result
    
    def start_megometro(self):
        # Garante o Stop do megômetro - pulso
        self.io.wp_8027(self.io.ADR_4, 2, 1)# liga
        time.sleep(0.1)
        # Garante um reset antes que o megômetro seja acionado
        self.reset_megometro()

    def stop_megometro(self):
        # Reseta relé que liga entrada de mêgometro atuado
        self.io.wp_8027(self.io.ADR_4,2,0)
        self.reset_megometro()

    def acende_verde(self):
        self.io.io_rpi.sinaleiro_verde()
        
    def acende_vermelho(self):
        self.io.io_rpi.sinaleiro_vermelho()

    def apaga_torre(self):
        self.io.io_rpi.desliga_torre()
    
    def esquerdo_direito_isolacao(self, lado):
        result = []
        if lado == 0: # Corresponde ao lado esquerdo

            # Garante o Stop do megômetro - pulso
            self.stop_megometro()

            # Liga contator que seleciona tensão - ligado seleciona Megômetro
            self.io.wp_8027(self.io.ADR_4,1,1)

            # Reseta relé que liga entrada de mêgometro atuado
            self.reset_megometro()
        
            # self.start_megometro()
            result = self.combinacao_isolacao_esquerdo()
            self.stop_megometro()


            self.eletrodo_testando_iso_e[0] = 0
            self.eletrodo_testando_iso_e[1] = 0

            # Desliga contator que seleciona tensão - ligado seleciona Megômetro
            self.io.wp_8027(self.io.ADR_4,1,0)

        elif lado == 1: # se for lado direito

            # Garante o Stop do megômetro - pulso
            self.stop_megometro()

            # Liga contator que seleciona tensão - ligado seleciona Megômetro
            self.io.wp_8027(self.io.ADR_4,1,1)

            # Reseta relé que liga entrada de mêgometro atuado
            self.reset_megometro()

            # self.start_megometro()
            result = self.combinacao_isolacao_direito()
            self.stop_megometro()

            self.eletrodo_testando_iso_d[0] = 0
            self.eletrodo_testando_iso_d[1] = 0

            # Desliga contator que seleciona tensão - ligado seleciona Megômetro
            self.io.wp_8027(self.io.ADR_4,1,0)
        
        return result

    """
"ligacao1":[0,0,"NOME_CONECAO",0,0]
"ligacao1":[0,0,"NOME_CONECAO"]
        |   | |   |
        |   | |   |____Nome da Conexão
        |   | |________Pino da tomada do eletrodo
        |   |__________Pino da tomada dos conectores
        |______________Número da conexão
"""

    def aciona_combinacao_iso(self, i, lado):
        if lado == "esquerdo":
            adr = self.io.ADR_1_X
            ligacao = self.isolacao_esquerdo[f"ligacao{i}"]
        elif lado == "direito":
            adr = self.io.ADR_2_X
            ligacao = self.isolacao_direito[f"ligacao{i}"]
        else:
            raise ValueError("Lado deve ser 'esquerdo' ou 'direito'")

        # Aciona pino da tomada de conectores - DO_0x do ADR_X
        if self.io.wp_8027(adr, ligacao[0], 1) == -1:
            return False
        # Aciona pino da tomada de eletrodos - DO_0x+12 do ADR_X - Tem que adicionar 12 para ir de 13-24 que é 1+12 - 12+12
        if self.io.wp_8027(adr, ligacao[1] + 12, 1) == -1:
            return False

        return True
    
    def desaciona_combinacao_iso(self, i, lado):
        if lado == "esquerdo":
            adr = self.io.ADR_1_X
            ligacao = self.isolacao_esquerdo[f"ligacao{i}"]
        elif lado == "direito":
            adr = self.io.ADR_2_X
            ligacao = self.isolacao_direito[f"ligacao{i}"]
        else:
            raise ValueError("Lado deve ser 'esquerdo' ou 'direito'")

        # desliga saída para não conflitar com o próximo
        self.io.wp_8027(adr, ligacao[0], 0)
        self.io.wp_8027(adr, ligacao[1] + 12, 0)

    def combinacao_isolacao_esquerdo(self):
        result = []
        # Aciona megômetro
        self.start_megometro()

        for i in range(1,21):
            if self.isolacao_esquerdo[f"ligacao{i}"][2] != "":

                self.aciona_combinacao_iso(i, "esquerdo")

                # Aguarda um pequeno tempo para acionamento do rele que é setado pelo sensor ótico
                if self.sleep_check_erro(self.TEMPO_ACIONAMENTO_RELE_ISO) == False:
                    # faz leitura e associa a variável
                    # índice 0 = número da ligação / índice 1 = Nome da ligação / índice 2 = status de ligaçao - 0=passou 1=não passou
                    result.append( [i,self.isolacao_esquerdo[f"ligacao{i}"][2],self.io.wp_8026(self.io.ADR_4, 8)] )
                    self.eletrodo_testando_iso_e[0] = self.isolacao_esquerdo[f"ligacao{i}"][3]
                    self.eletrodo_testando_iso_e[1] = self.isolacao_esquerdo[f"ligacao{i}"][4]

                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao_iso(i, "esquerdo")
                    
                    # Depois de conferido a isolação pelo megômetro, reseta relé que liga entrada
                    self.reset_megometro()
                else:
                    result = []
                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao_iso(i, "esquerdo")
                    break
            else:
                break


        self.stop_megometro()

        return result

    def fake_isolacao_esquerdo(self):
        result = []

        for i in range(1,21):
            if self.isolacao_esquerdo[f"ligacao{i}"][2] != "":
                    # faz leitura e associa a variável
                    # índice 0 = número da ligação / índice 1 = Nome da ligação / índice 2 = status de ligaçao - 0=passou 1=não passou
                result.append( [i,self.isolacao_esquerdo[f"ligacao{i}"][2],1] )

        return result
    
    def combinacao_isolacao_direito(self):
        result = []
        # # Aciona Megômetro
        self.start_megometro()

        for i in range(1,21):
            if self.isolacao_direito[f"ligacao{i}"][2] != "":

                self.aciona_combinacao_iso(i, "direito")

                # Aguarda um pequeno tempo para acionamento do rele que é setado pelo sensor ótico
                if self.sleep_check_erro(self.TEMPO_ACIONAMENTO_RELE_ISO) == False:


                    # faz leitura e associa a variável
                    # índice 0 = número da ligação / índice 1 = Nome da ligação / índice 2 = status de ligaçao - 0=passou 1=não passou
                    result.append( [i,self.isolacao_direito[f"ligacao{i}"][2],self.io.wp_8026(self.io.ADR_4, 8)] )
                    self.eletrodo_testando_iso_d[0] = self.isolacao_direito[f"ligacao{i}"][3]
                    self.eletrodo_testando_iso_d[1] = self.isolacao_direito[f"ligacao{i}"][4]

                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao_iso(i, "direito")
                    
                    # Depois de conferido a isolação pelo megômetro, reseta relé que liga entrada
                    self.reset_megometro()
                else:
                    result = []
                    # desliga saída para não conflitar com o próximo
                    self.desaciona_combinacao_iso(i, "direito")
                    break
            else:
                break

        # Desliga Megômetro
        self.stop_megometro()

        return result
    
    def fake_isolacao_direito(self):
        result = []

        for i in range(1,21):
            if self.isolacao_direito[f"ligacao{i}"][2] != "":
                    # faz leitura e associa a variável
                    # índice 0 = número da ligação / índice 1 = Nome da ligação / índice 2 = status de ligaçao - 0=passou 1=não passou
                result.append( [i,self.isolacao_direito[f"ligacao{i}"][2],1] )

        return result

    def abaixa_pistao(self):
        result = False
        self.io.wp_8027(self.io.ADR_4, 7, 0)
        time.sleep(0.1)
        self.io.wp_8027(self.io.ADR_4, 6, 1)
        
        #Aguarda pistão descer
        if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:
            # Abaixa pistão - Desliga válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 0) 
            result = True
        else:
            result = False
            # Abaixa pistão - Desliga válvula
            # self.io.wp_8027(self.io.ADR_4, 4, 0)  
        return result    
     
    def sobe_pistao(self):
        result = False
        self.io.wp_8027(self.io.ADR_4, 6, 0)
        time.sleep(0.1)
        self.io.wp_8027(self.io.ADR_4, 7, 1)
        
        #Aguarda pistão descer
        if self.sleep_check_erro(self.TEMPO_DESCIDA_PISTAO) == False:
            # Sobe pistão - Desliga válvula
            # self.io.wp_8027(self.io.ADR_4, 5, 0) 
            result = True
        else:
            result = False
            # Sobe pistão - Desliga válvula
            # self.io.wp_8027(self.io.ADR_4, 5, 0)  
        return result    

    def marca_peca_esquerda(self):
        # self.operacao.io.wp_8027(self.io.ADR_4, 2, 1) # Aciona pistão de marcação esquerdo
        self.io.wp_8027(self.io.ADR_4, 4, 1) # Aciona pistão de marcação esquerdo
        time.sleep(0.5)
        self.io.wp_8027(self.io.ADR_4, 4, 0) # Desliga pistão de marcação esquerdo 

    def marca_peca_direita(self):
        self.io.wp_8027(self.io.ADR_4, 5, 1) # Aciona pistão de marcação esquerdo
        time.sleep(0.5)
        self.io.wp_8027(self.io.ADR_4, 5, 0) # Desliga pistão de marcação esquerdo

    def mola_esquerda(self):
        print(f"Valor mola equerda{self.io.wp_8026(self.io.ADR_4, 4)}")
        return self.io.wp_8026(self.io.ADR_4, 4) # Leitura do sensor de mola esquerda
    
    def mola_direita(self):
        print(f"Valor mola direita{self.io.wp_8026(self.io.ADR_4, 5)}")
        return self.io.wp_8026(self.io.ADR_4, 5) # Leitura do sensor de mola direita

    def limpa_saidas_esquerda_direita(self):
        for i in range(1,25):
            self.io.wp_8027(self.io.ADR_1_X,i,0)
            
            self.io.wp_8027(self.io.ADR_2_X,i,0)
if __name__ == "__main__":
    from IOs import IO_MODBUS
    io = IO_MODBUS()
    rotina = RotinaPrg( io=io )

    while True:
        comando = input("Digite 1 para subir o pistão ou 0 para descer o pistão (q para sair): ")
        if comando == '1':
            if rotina.sobe_pistao():
                print("Pistão subiu com sucesso.")
            else:
                print("Erro ao subir o pistão.")
        elif comando == '0':
            if rotina.abaixa_pistao():
                print("Pistão desceu com sucesso.")
            else:
                print("Erro ao descer o pistão.")
        elif comando == 'q':
            print("Saindo...")
            break
        else:
            print("Comando inválido.")

    # while True:
    #     comando = input("Digite 1 para acionar marcação direita ou 0 para acionar marcação esquerda (q para sair): ")
    #     if comando == '1':
    #         rotina.marca_peca_direita()
    #         print("Marcação direita acionada com sucesso.")
    #     elif comando == '0':
    #         rotina.marca_peca_esquerda()
    #         print("Marcação esquerda acionada com sucesso.")
    #     elif comando == 'q':
    #         print("Saindo...")
    #         break
    #     else:
    #         print("Comando inválido.")

    # while True:
    #     comando = input("Digite 1 para acionar o megômetro, 0 para parar o megômetro, ou 2 para resetar o megômetro (q para sair): ")
    #     if comando == '1':
    #         rotina.start_megometro()
    #         print("Megômetro acionado com sucesso.")
    #     elif comando == '0':
    #         rotina.stop_megometro()
    #         print("Megômetro parado com sucesso.")
    #     elif comando == '2':
    #         rotina.reset_megometro()
    #         print("Megômetro resetado com sucesso.")
    #     elif comando == 'q':
    #         print("Saindo...")
    #         break
    #     else:
    #         print("Comando inválido.")

  
    # while True:
    #     comando = input("Digite 1 para acender a luz verde, 0 para apagar a luz verde, 3 para acender a luz vermelha, 4 para apagar a luz vermelha (q para sair): ")
    #     if comando == '1':
    #         rotina.acende_verde()
    #         print("Luz verde acesa com sucesso.")
    #     elif comando == '0':
    #         rotina.apaga_torre()
    #         print("Luz verde apagada com sucesso.")
    #     elif comando == '3':
    #         rotina.acende_vermelho()
    #         print("Luz vermelha acesa com sucesso.")
    #     elif comando == '4':
    #         rotina.apaga_torre()
    #         print("Luz vermelha apagada com sucesso.")
    #     elif comando == 'q':
    #         print("Saindo...")
    #         break
    #     else:
    #         print("Comando inválido.")