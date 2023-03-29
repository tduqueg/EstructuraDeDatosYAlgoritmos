
class ZAlgorithm:

    def __init__(self, pattern, text):

        self.pattern = pattern
        self.text = text
        #Concatenamos el patrón con el texto
        self.S = pattern + text
        #Creamos la tabla Z
        self.Z = [0 for _ in range(len(self.S))]

    def construct_z_table(self):

        #El primer ítem siempre tiene la longitud de S
        self.Z[0] = len(self.S)
        
        #El primer y ultimo ítem de la caja z
        left = 0
        right = 0

        #Consideramos todas las letras de S empezando en el indice1
        for k in range(1,len(self.S)):

            #No estamos en una caja Z por lo que tenemos que utilizar un acercamiento Naive
            if k > right:

                n = 0

                while n + k < len(self.S) and self.S[n] == self.S[n+k]:

                    n += 1

                self.Z[k] = n

                if n > 0:

                    left = k
                    right = k + n - 1
            
            else:

                #Estamos dentro de una caja z por lo que dependiendo del caso podremos copiar los valores
                p = k - left

                if self.Z[p] < right- k + 1:
                    
                    self.Z[k] = self.Z[p]
                
                else:
                    
                    #No podemos copiar los valores
                    i = right + 1

                    while i < len(self.S) and self.S[i] == self.S[i - k]:

                        i += 1
                    
                    self.Z[k] = i - k 
                    left = k
                    right = i - 1






    def search(self):

        self.construct_z_table()

        #Tenemos que considerar los valores de la tabla Z en O(m+n)
        for i in range(1, len(self.Z)):

            if self.Z[i] >= len(self.pattern):

                print('Coincidencia encontrada en el índice %s' %(i - len(self.pattern)))

if __name__ == '__main__':

    algorithm = ZAlgorithm('pra','Me acostumbré al Sour ya no patea, me llegan a casa no se capea, solo modelos como Barea, multiplicar cienes es la tarea, yo soy el cacique en tu propia aldea valgo más que todo lo que te rodea no te la creas, recuerda que Curry la mete, hasta que Lebron lo caldea, ando con la orquesta, cabrón no es la sexta, yo nunca estoy abajo en las apuestas, y menos en esta dile a Vico que de la recta final estamos en el final de la recta el diablo me inyecta, y saco la que suena y los acuesta pra pra')
    algorithm.search()




                    
