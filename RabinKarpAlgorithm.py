
class RabinKarp:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        # El tamaño del alfabeto es de 28 excluyendo ll
        self.d = 28
        #el número primo para el operador modulo
        self.q = 31

    def search(self):

        m = len(self.pattern)
        n = len(self.text)

        #Estas variables almacenan el valor hash de la ventana del texto
        #y el valor hash del patrón a buscar
        hash_text = 0
        hash_pattern = 0
        h = 1

        for _ in range(m-1):
            h = (h*self.d) % self.q

        #Precomputamos el hash para el patrón en O(m)
        for i in range(m):
            hash_pattern = (self.d*hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q

        #comparamos el patron  por el texto uno por uno
        for i in range(n-m+1):

            #Comparamos el valor del hash de la ventana actual del texto
            #y del patron, si los valores de hash coinciden
            #entonces  comparamos los caracteres uno por uno
            if hash_text == hash_pattern:

                # naive approach to check the characters
                j = 0

                while j < m:
                    if self.text[i+j] != self.pattern[j]:
                        break

                    j = j + 1

                if j == m:
                    print("Found match at index %s" % i)
            
            #Actualizamos el hash para el subtexto actual del texto
            #y aplicamos el rolling hash
            if i < n-m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i + m])) % self.q

                #Puede pasar que terminemos con un valor negfativo por lo que tenemos que asegurarnos de que sea positivo
                if hash_text < 0:
                    hash_text = hash_text + self.q


if __name__ == '__main__':

    algorithm = RabinKarp('que', 'Tomás Duque')
    algorithm.search()






