
def brute_force_search(pattern,text):

    #Definimos el tañamo del patron a buscar y del texto donde debemos buscar el patron
    m = len(pattern)
    n = len(text)

    #Como sabemos que el patrón está compuesto de m letras, no debemos examinar las ultimas m letras
    #de n
    #Esta operación tiene una complejidad de O(n) en el peor de los casos
    for i in range(n-m+1):

        #Revisamos las letras en el patrón empezando en 0
        #desde izquierda a derecha
        j=0

        #Todas las letras del patrón O(m) en el peor de los casos
        #Por lo que la complejidad de esta solución es de O(n*m)
        while j < m:

            #Tenemos que comparar cada caracter
            if text[i+j] != pattern[j]:
                break

            #Consideramos el siguiente caracter
            j += 1
        
        if j == m:
            print('Se encontró una coincidencia en el índice %s' % i)

if __name__ == '__main__':

    brute_force_search('neas','Sabaneta es el mejor lugar del mundo entero que vivan las neas')




