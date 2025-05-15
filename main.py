import time
lista = [-7, 23, -1, 0, 3, -101, -99, 45, 12]

lista_positivo = []
lista_negativo = []


for i in range(len(lista)):
    if(lista[i] >= 0):
        lista_positivo.append(lista[i])
    else:
        lista_negativo.append(lista[i])
    

def merge_sort(lista):    
    
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    n2 = merge_sort(lista[:meio])
    n1 = merge_sort(lista[meio:])
    
    
    return merge_list(n1,n2)


def merge_list(n1,n2):
    
    lista_merged = []
    i = j = 0
    
    while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                lista_merged.append(n1[i])
                i += 1
            else:
                lista_merged.append(n2[j])
                j += 1
        
    lista_merged.extend(n1[i:])
    lista_merged.extend(n2[j:])
        
    return lista_merged





def radix_sort(lista):
    absolutos = list(map(abs, lista))
    maior_comprimento = max(map(lambda num: len(str(num)), absolutos))

    all_digits_list = list(map(lambda num: f"{num:0{maior_comprimento}}", absolutos))

    for i in range(maior_comprimento):
        buckets = [[] for _ in range(10)]

        for item in all_digits_list:
            digito = int(item[-(i+1)])  
            buckets[digito].append(item)  

        all_digits_list = [item for bucket in buckets for item in bucket]


    resultado = [-int(item) for item in reversed(all_digits_list)]
    return resultado



inicio_radix = time.time()
lista_negativo_ordenada = radix_sort(lista_negativo)
fim_radix = time.time()

inicio_merge = time.time()
lista_positivo_ordenada = merge_sort(lista_positivo)
fim_merge = time.time()

lista_geral_organizada = []
lista_geral_organizada.extend(lista_negativo_ordenada)
lista_geral_organizada.extend(lista_positivo_ordenada)

print("- Lista positiva ordenada por Merge Sort:", lista_positivo_ordenada)
print("- Lista negativa ordenada por Radix Sort:", lista_negativo_ordenada)
print("- Lista final concatenada:", lista_geral_organizada)
print("- Complexidade de Merge Sort: O(n log n)")
print("- Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)")

tempo_radix = (fim_radix - inicio_radix) * 1000
tempo_merge = (fim_merge - inicio_merge) * 1000

print(f"- Tempo de execução Radix Sort: {tempo_radix:.3f} ms")
print(f"- Tempo de execução Merge Sort: {tempo_merge:.3f} ms")

