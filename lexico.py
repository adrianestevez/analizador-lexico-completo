import constantes

class Lexico:
    cadena = ""
    simbolo = ""
    tipo = 0
    estado = 0
    ind = 0
    hayPunto = False

    tipoDatos = ["int", "float", "void"]
    reservadas = ["if", "while", "return", "else"]

    def __init__(self, cadena):
        self.cadena = cadena
        self.ind = 0

    def definir(self):

        while(self.ind < len(self.cadena)):
            self.procesar(self.cadena[self.ind])
            self.ind += 1

    def procesar(self, c):
        if(self.estado==constantes.INICIAL):
            if(self.es_Letra(c)):
                self.estado = constantes.IDENTIFICADOR
                self.simbolo += c #agrego a la cadena del simbolo
                self.tipo = constantes.IDENTIFICADOR

            elif (self.isReal(c)):
                self.estado = constantes.ENTERO
                self.simbolo += c  # agrego a la cadena del simbolo
                self.tipo = constantes.ENTERO

            elif (c == '"'):
                self.estado = constantes.CADENA
                self.simbolo += c

            elif (c == '+' or c == '-'):
                self.simbolo += c
                self.tipo = constantes.OPSUMA
                self.imprimirSimbolo()
                self.estado = constantes.INICIAL
                self.simbolo = ""

            elif (c == '*' or c == '/'):
                self.simbolo += c
                self.tipo = constantes.OPMUL
                self.imprimirSimbolo()
                self.estado = constantes.INICIAL
                self.simbolo = ""

            elif (c == '<' or c == '>'):
                if (self.cadena[self.ind + 1] == '='):
                    self.simbolo += c
                    self.simbolo += self.cadena[self.ind + 1]
                    self.tipo = constantes.OPRELAC
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL
                    self.ind += 1
                else:
                    self.simbolo += c
                    self.tipo = constantes.OPRELAC
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL


            elif (c == '|'):
                if (self.cadena[self.ind + 1] == '|'):
                    self.simbolo += c
                    self.simbolo += self.cadena[self.ind + 1]
                    self.tipo = constantes.OPOR
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL
                    self.ind += 1
                else:
                    self.simbolo += c
                    self.tipo = constantes.ERROR
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL

            elif (c == '&'):
                if (self.cadena[self.ind + 1] == '&'):
                    self.simbolo += c
                    self.simbolo += self.cadena[self.ind + 1]
                    self.tipo = constantes.OPAND
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL
                    self.ind += 1
                else:
                    self.simbolo += c
                    self.tipo = constantes.ERROR
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.estado = constantes.INICIAL

            elif (c == '=' or c == '!'):
                if(self.cadena[self.ind+1] == '='):
                    if(c == '='):
                        self.simbolo += c
                        self.simbolo += self.cadena[self.ind+1]
                        self.tipo = constantes.OPIGUALDAD
                        self.imprimirSimbolo()
                        self.simbolo = ""
                        self.estado = constantes.INICIAL
                        self.ind += 1

                    elif (c == '!'):
                        self.simbolo += c
                        self.simbolo += self.cadena[self.ind + 1]
                        self.tipo = constantes.OPIGUALDAD
                        self.imprimirSimbolo()
                        self.simbolo = ""
                        self.estado = constantes.INICIAL
                        self.ind += 1
                else:
                    if(c == '!'):
                        self.simbolo += c
                        self.tipo = constantes.OPNOT
                        self.imprimirSimbolo()
                        self.simbolo = ""
                        self.estado = constantes.INICIAL
                    else:
                        self.simbolo += c
                        self.tipo = constantes.ASIGNACION
                        self.imprimirSimbolo()
                        self.simbolo = ""
                        self.estado = constantes.INICIAL

            elif (c==';'):
                self.simbolo += c
                self.tipo = constantes.PUNTOCOMA
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c==','):
                self.simbolo += c
                self.tipo = constantes.COMA
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c == '('):
                self.simbolo += c
                self.tipo = constantes.PARENTESISAPERT
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c == ')'):
                self.simbolo += c
                self.tipo = constantes.PARENTESISCIERRE
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c == '{'):
                self.simbolo += c
                self.tipo = constantes.CORCHETEAPERT
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c == '}'):
                self.simbolo += c
                self.tipo = constantes.CORCHETECIERRE
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL

            elif (c == '$'):
                self.simbolo += c
                self.tipo = constantes.PESOS
                self.imprimirSimbolo()
                self.simbolo = ""
                self.estado = constantes.INICIAL


        elif(self.estado==constantes.IDENTIFICADOR):
            if(self.es_Letra(c) or self.isReal(c)):
                self.simbolo += c  # agrego a la cadena del simbolo
            else:
                if(self.esTipodeDato()):
                    self.imprimirSimbolo()
                    self.estado = constantes.INICIAL
                    self.simbolo = ""
                    self.ind -= 1
                elif(self.esReservada()):
                    self.imprimirSimbolo()
                    self.estado = constantes.INICIAL
                    self.simbolo = ""
                    self.ind -= 1
                else:
                    self.tipo = constantes.IDENTIFICADOR
                    self.estado = constantes.INICIAL
                    self.imprimirSimbolo()
                    self.simbolo = ""
                    self.ind -= 1

        elif (self.estado == constantes.ENTERO):
            if(self.isReal(c)):
                self.estado = constantes.ENTERO
                self.simbolo += c
            elif(c=="."):
                if(self.hayPunto == False):
                    self.estado = constantes.REAL
                    self.simbolo += c
                    self.hayPunto = True
                else:
                    self.simbolo += c
                    self.tipo = constantes.ERROR
                    self.imprimirSimbolo()
                    self.estado = constantes.INICIAL
                    self.simbolo = ""
            else:
                self.tipo = constantes.ENTERO
                self.imprimirSimbolo()
                self.estado = constantes.INICIAL
                self.simbolo = ""
                self.ind -= 1

        elif (self.estado == constantes.REAL):
            if (self.isReal(c)):
                self.estado = constantes.REAL
                self.simbolo += c
            elif (c == "."):
                if (self.hayPunto):
                    self.simbolo += c
                    self.tipo = constantes.ERROR
                    self.imprimirSimbolo()
                    self.estado = constantes.INICIAL
                    self.hayPunto = False
                    self.simbolo = ""
            else:
                self.tipo = constantes.REAL
                self.imprimirSimbolo()
                self.estado = constantes.INICIAL
                self.simbolo = ""
                self.ind -= 1

        elif (self.estado == constantes.CADENA):
            if(c == '"'):
                self.simbolo += c
                self.tipo = constantes.CADENA
                self.imprimirSimbolo()
            else:
                self.estado = constantes.CADENA
                self.simbolo += c

    def esTipodeDato(self):
        for t in self.tipoDatos:
            if(t == self.simbolo):
                self.tipo = constantes.TIPO
                return True
        return False

    def esReservada(self):
        for r in self.reservadas:
            if(r == self.simbolo):
                self.tipoReservada()
                return True
        return False

    def tipoReservada(self):

        if(self.simbolo == "if"):
            self.tipo = constantes.IF
        elif (self.simbolo == "while"):
            self.tipo = constantes.IF
        elif (self.simbolo == "return"):
            self.tipo = constantes.IF
        elif (self.simbolo == "else"):
            self.tipo = constantes.IF
        else:
            self.tipo = constantes.ERROR


    def imprimirSimbolo(self):
        cad = self.retornarTipo()

        print(self.simbolo + "\t\t" + cad)



    def retornarTipo(self):
        cad = ""

        if (self.tipo == constantes.ERROR):
            cad = "Error"
        elif (self.tipo == constantes.IDENTIFICADOR):
            cad = "Identificador"
        elif (self.tipo == constantes.ENTERO):
            cad = "Entero"
        elif (self.tipo == constantes.REAL):
            cad = "Real"
        elif (self.tipo == constantes.CADENA):
            cad = "Cadena"
        elif (self.tipo == constantes.TIPO):
            cad = "Tipo de dato"
        elif (self.tipo == constantes.OPSUMA):
            cad = "Operacion Suma"
        elif (self.tipo == constantes.OPMUL):
            cad = "Operacion Multiplicacion"
        elif (self.tipo == constantes.OPRELAC):
            cad = "Operador Relacional"
        elif (self.tipo == constantes.OPOR):
            cad = "Operador OR"
        elif (self.tipo == constantes.OPAND):
            cad = "Operador AND"
        elif (self.tipo == constantes.OPNOT):
            cad = "Operador NOT"
        elif (self.tipo == constantes.OPIGUALDAD):
            cad = "Operador Igualdad"
        elif (self.tipo == constantes.PUNTOCOMA):
            cad = "Punto y Coma"
        elif (self.tipo == constantes.COMA):
            cad = "Coma"
        elif (self.tipo == constantes.PARENTESISAPERT):
            cad = "Parentesis Abierto"
        elif (self.tipo == constantes.PARENTESISCIERRE):
            cad = "Parentesis Cierre"
        elif (self.tipo == constantes.CORCHETEAPERT):
            cad = "Corchete Abierto"
        elif (self.tipo == constantes.CORCHETECIERRE):
            cad = "Corchete Cerrado"
        elif (self.tipo == constantes.ASIGNACION):
            cad = "Operador Asignacion"
        elif (self.tipo == constantes.IF):
            cad = "Palabra reservada if"
        elif (self.tipo == constantes.WHILE):
            cad = "Palabra reservada while"
        elif (self.tipo == constantes.RETURN):
            cad = "Palabra reservada return"

        return cad


    #Si la cadena no es nula y está entre los caracteres ascii del 48 al 57 significa que entonces el primer caracter de la
        #cadena es un numero por tanto lo mandamos a la funcion que define los reales
    def isReal(self, c):
        if (ord(c) >= 48 and ord(c) <= 57):
            return True
        else:
            return False

        # Si la cadena no es nula y está entre los caracteres ascii del 65 al 90 (letras minusculas) o desde el 97 al 122 (letras mayusculas)
        #además admitimos el guion bajo "_"
    def es_Letra(self, c):
        if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
            return True
        else:
            return False
