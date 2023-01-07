class Radio():
    #Atributos
    on_off="desligado"
    vol_atual=0
    vol_max=None
    canal="AM"
    radioname=None

    #Métodos
    def power(self):
        if self.on_off=="desligado":
            self.on_off = "ligado"
            print("O {} está: {}".format(self.radioname, self.on_off))
        elif self.on_off=="ligado":
            self.on_off = "desligado"
            print("O {} está: {}".format(self.radioname ,self.on_off))
            
    def mudar_canal(self):
        if self.on_off == "ligado":
            if self.canal=="AM":
                self.canal = "FM"
                print("{} canal atual: {}".format(self.radioname, self.canal))
            elif self.canal=="FM":
                self.canal= "AM"
                print("{} canal atual: {}".format(self.radioname, self.canal))
            
    def mudar_vol(self,valor):
        if self.on_off=="ligado":
            if 0<=valor<=self.vol_max:
                self.vol_atual=valor 
                print("{} volume atual: {}".format(self.radioname, self.vol_atual)) 
        
radio1 = Radio()
radio1.radioname="radio1"
radio1.vol_max=15
radio1.power()
radio1.mudar_canal()
radio1.mudar_vol(12)
radio2 = Radio() 
radio2.radioname="radio2"
radio2.vol_max=15
radio2.mudar_canal()
radio2.mudar_vol(12)
radio2.power()
radio1.power()