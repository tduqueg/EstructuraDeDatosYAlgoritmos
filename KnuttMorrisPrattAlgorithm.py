
#Debemos construir la tabla de pi
def construct_pi(pattern):

    pi_table = [0]*len(pattern)
    prefix_counter = 0
    i = 1

    #O(m) Lineal
    while i < len(pattern):
        
        if pattern[i] == pattern[prefix_counter]:

            prefix_counter += 1
            pi_table[i] = prefix_counter
            i += 1
        
        else:

            if prefix_counter != 0:

                prefix_counter = pi_table[prefix_counter - 1]

            else:

                pi_table[i] = 0
                i += 1
    
    return pi_table

def search(text, pattern):

    pi_table = construct_pi(pattern)
    #El índice i recorre el texto mientras que el índice j recorre el patrón
    i = 0
    j = 0

    #Tenemos que iterar hasta que el índice i sea igual que la longitud(n) del texto
    #y además tenemos que asegurarnos que j sea menor a la longitud(m) del patrón
    while i < len(text) and j < len(pattern):

        if text[i] == pattern[j]:
            
            i += 1
            j += 1

        #Esto significa que se encotró el patrón en el texto
        if j ==len(pattern):
            
            print('El patrón se encontró en el indice %s' % (i - j))
            j = pi_table[j-1]
        
        #Si no hay coincidencia entonces
        elif i < len(text) and text[i] != pattern[j]:
            
            #si podemos decrementar el índice j lo hacemos
            if j != 0:

                j = pi_table[j-1]
            
            #Si no podemos decrementar j porque ya es cero entonces incrementamos i
            else:

                i += 1








if __name__ == '__main__':

    search('Esto es una texto que será utilizado de prueba en esta ocación ocación ocación', 'ocación')

