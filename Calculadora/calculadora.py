class Calculadora:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sumar(self):
        return self.x + self.y
    
    def restar(self):
        return self.x - self.y
    
    def multiplicar(self):
        return self.x * self.y
    
    def dividir(self):
        return self.x / self.y

def menu():
    print("""

    ######################
          Calculadora
    ######################
          
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    5.Salir
          
Seleccione una opcion: """)

#Funcion que recibe el resultado de la operacion y lo mana a imprimir
def resultado(x):
       print(f"""

################            
Resultado: {x}
################

""")    

#Funcion encargada de recolectar datos del usuario
def recibir_datos():
    x = int(input("Proporciona x: "))
    y = int(input("Proporciona y: "))
    operacion = Calculadora(x,y)
    #Devuelve el objeto instanciado de Calculadora
    return operacion

#Funcion encargada de imprimir la operacion que se esta realizando
def imprimir_operaciones(operacion):
            print(f"""
###################
##### {operacion} ####
###################
              """)


if __name__ == "__main__":
    
    ciclo = True

    while ciclo == True:

        menu() 
        opcion = int(input())

        if opcion == 1:

            imprimir_operaciones("Sumar")
            #Resultado es la funcion encargada de mandar a imprimir en pantalla el resultado
            #recibe como parametro a la funcion recibir_datos que devuelve el objeto y .sumar accede a su metodo
            resultado(recibir_datos().sumar())

        elif opcion == 2:

            imprimir_operaciones("Restar")
            resultado(recibir_datos().restar())

        elif opcion == 3:

            imprimir_operaciones("Multiplicar")
            resultado(recibir_datos().multiplicar())

        elif opcion == 4:

            imprimir_operaciones("Dividir")
            resultado(recibir_datos().dividir())

        elif opcion == 5:
             ciclo = False
         
        else: print("Has seleccionado una opcion incorrecta")


