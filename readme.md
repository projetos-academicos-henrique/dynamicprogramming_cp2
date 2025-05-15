# 🧠 Projeto: Organizador de Dados em Lista Ligada

Este projeto organiza uma lista de números inteiros, separando negativos e positivos, e ordenando com algoritmos diferentes:

* 📉 Números **negativos**: ordenados com **Radix Sort adaptado**.
* 📈 Números **positivos (e zero)**: ordenados com **Merge Sort**.

Ao final, as duas listas são **concatenadas** com os negativos primeiro.
Também é exibida a **complexidade teórica** de cada algoritmo e o **tempo de execução** real.

---

## 📦 Entrada

```python
lista = [-7, 23, -1, 0, 3, -101, -99, 45, 12]
```

---

## 🔄 Separar negativos e positivos

```python
lista_positivo = []
lista_negativo = []

for i in range(len(lista)):
    if lista[i] >= 0:
        lista_positivo.append(lista[i])
    else:
        lista_negativo.append(lista[i])
```

**Explicação:**
Divide a lista original em dois grupos: negativos e positivos.
Isso é necessário porque cada grupo será ordenado com um algoritmo diferente.

---

## 🧩 Merge Sort (usado para positivos)

### 🔹 Função principal

```python
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    n2 = merge_sort(lista[:meio])
    n1 = merge_sort(lista[meio:])
    
    return merge_list(n1, n2)
```

**Explicação:**
Divide a lista recursivamente em duas partes até que cada uma tenha apenas 1 item.
Depois, chama `merge_list` para juntar as partes ordenadas.

---

### 🔹 Mesclando as listas ordenadas

```python
def merge_list(n1, n2):
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
```

**Explicação:**
Compara os elementos de duas listas ordenadas (`n1` e `n2`) e junta tudo em ordem.

---

## ⚙️ Radix Sort (usado para negativos)

```python
def radix_sort(lista):
    absolutos = list(map(abs, lista))
```

**Explicação:**
O Radix tradicional só funciona com positivos.
Aqui, transformamos todos os negativos em positivos temporariamente para ordenar.

---

### 🧮 Padronização dos números

```python
    maior_comprimento = max(map(lambda num: len(str(num)), absolutos))
    all_digits_list = list(map(lambda num: f"{num:0{maior_comprimento}}", absolutos))
```

**Explicação:**
Identifica quantos dígitos tem o maior número e padroniza todos os números com zeros à esquerda.

---

### 🪣 Ordenação por dígito (Radix)

```python
    for i in range(maior_comprimento):
        buckets = [[] for _ in range(10)]

        for item in all_digits_list:
            digito = int(item[-(i+1)])  
            buckets[digito].append(item)

        all_digits_list = [item for bucket in buckets for item in bucket]
```

**Explicação:**
Para cada casa decimal (unidade, dezena, centena...), os números são distribuídos em "baldes" (buckets) com base no dígito atual.
Depois, os baldes são unidos novamente. Esse processo se repete para cada casa decimal.

---

### ➖ Reverter sinal

```python
    resultado = [-int(item) for item in reversed(all_digits_list)]
    return resultado
```

**Explicação:**
Após a ordenação dos absolutos, invertemos os sinais novamente e também a ordem (para ficar do menor para o maior).

---

## ⏱️ Execução e resultado

```python
import time

inicio_radix = time.time()
lista_negativo_ordenada = radix_sort(lista_negativo)
fim_radix = time.time()

inicio_merge = time.time()
lista_positivo_ordenada = merge_sort(lista_positivo)
fim_merge = time.time()
```

---

### 🧷 Juntando tudo

```python
lista_geral_organizada = []
lista_geral_organizada.extend(lista_negativo_ordenada)
lista_geral_organizada.extend(lista_positivo_ordenada)
```

---

### 📤 Saída final

```python
print("- Lista positiva ordenada por Merge Sort:", lista_positivo_ordenada)
print("- Lista negativa ordenada por Radix Sort:", lista_negativo_ordenada)
print("- Lista final concatenada:", lista_geral_organizada)
print("- Complexidade de Merge Sort: O(n log n)")
print("- Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)")

tempo_radix = (fim_radix - inicio_radix) * 1000
tempo_merge = (fim_merge - inicio_merge) * 1000

print(f"- Tempo de execução Radix Sort: {tempo_radix:.3f} ms")
print(f"- Tempo de execução Merge Sort: {tempo_merge:.3f} ms")
```

**Exemplo de Saída Esperada:**

```
- Lista positiva ordenada por Merge Sort: [0, 3, 12, 23, 45]
- Lista negativa ordenada por Radix Sort: [-101, -99, -7, -1]
- Lista final concatenada: [-101, -99, -7, -1, 0, 3, 12, 23, 45]
- Complexidade de Merge Sort: O(n log n)
- Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)
- Tempo de execução Radix Sort: 0.054 ms
- Tempo de execução Merge Sort: 0.041 ms
```

---

## 👨‍💻 Membros do Grupo

* **Andrey Nagata** - RM555339
* **Henrique Soubhia** - RM554493
* **Oliver Kanai** - RM554954
* **Pedro Gutierre** - RM555445
* **William Weile** - RM555132

