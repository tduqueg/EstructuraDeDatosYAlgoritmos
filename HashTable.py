
class HashTable:

    def __init__(self):
        
        #Basados en el el load factor esta capacidad pueda cambiar (Dynamic Resizing)
        self.capacity = 10
        self.keys = [None]*self.capacity
        self.values = [None]*self.capacity

    def insert(self,key,data):
        
        #Debemos encontrar un lugar valido para el valor
        index = self.hash_function(key)

        #Pueden haber colisiones por lo que el índice que se le asignó a la llave se encuentra ocupado
        while self.keys[index] is not None:
            
            if self.keys[index] == index:
                self.values[index] = data
                return
            
            #hay que hacer un sondeo lieal(probar el siguiente lugar en el array)
            index = (index+1) % self.capacity

        #Si encontramos un lugar valido para el item metemos los datos
        self.keys[index] = key
        self.values[index] = data
    
    def get(self, key):

        index = self.hash_function(key)

        while self.keys[index] is not None:
            #Si encontramos el ítem que estamos buscando
            if self.keys[index] == key:
                return self.values[index]

            index = (index +1) % self.capacity
        
        #La llave que se entregó no existe en la hashtable
        return None


    #Esta función se encarga de asignar un indice a cada llave
    def hash_function(self,key):

        hash_sum = 0

        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity
    

if __name__ == '__main__':
    hash = HashTable()
    hash.insert("Tomás",0)
    hash.insert("Kevin",23)
    hash.insert("Adam", 23)
    hash.insert("Daniel",34)
    print(hash.get("Daniel"))
    

