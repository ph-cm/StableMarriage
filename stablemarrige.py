# Problema dos Casamentos Estáveis
n = 4 


# Preferências dos homens (linhas) para as mulheres (colunas)
wmr = [
    [0, 1, 2, 3],  
    [1, 0, 3, 2],  
    [2, 3, 0, 1],  
    [3, 2, 1, 0],  
]

# Preferências das mulheres (linhas) para os homens (colunas)
mwr = [
    [0, 1, 2, 3],  
    [1, 2, 0, 3],  
    [2, 0, 3, 1],  
    [3, 1, 2, 0],  
]

# indicar qual posição o homem está na preferência da mulher
rmw = [[0] * n for _ in range(n)]  
# indicar qual posição a mulher está na preferência do homem
rwm = [[0] * n for _ in range(n)]  
x = [-1] * n  
y = [-1] * n  
single = [True] * n 

# Preenchendo os rankings
for m in range(n):
    for r in range(n):
        rmw[m][wmr[m][r]] = r  

for w in range(n):
    for r in range(n):
        rwm[w][mwr[w][r]] = r  

def print_result():
    print("\nResultado dos Casamentos:")
    print(f"{'Homem':<10} {'Mulher':<10} {'Rank Homem':<15} {'Rank Mulher':<15}")
    print("-" * 50)
    
    total_rank_men = 0
    total_rank_women = 0
    
    for m in range(n):
        woman = x[m] + 1  
        rank_man = rmw[m][x[m]]
        rank_woman = rwm[x[m]][m]
        
        print(f"{m + 1:<10} {woman:<10} {rank_man:<15} {rank_woman:<15}")
        
        total_rank_men += rank_man
        total_rank_women += rank_woman
    
    print(f"{'Total':<10} {'':<10} {total_rank_men:<15} {total_rank_women:<15}")

def stable(m, w, r):
    # Verifica se a mulher 'w' é uma escolha estável para o homem 'm'
    for i in range(1, r):  
        pw = wmr[m][i - 1]  
        if not single[pw] and rwm[pw][m] > rwm[pw][y[pw]]:
            return False 

    # Verifica se a mulher 'w' prefere algum homem que não seja 'm'
    lim = rwm[w][m] 
    for i in range(1, lim): 
        pm = mwr[w][i - 1]  
        if pm < m and rmw[pm][w] > rmw[pm][x[pm]]:
            return False  

    return True

def try_match(m):
    """Tenta casar o homem m com uma mulher."""
    for r in range(n):  
        w = wmr[m][r]  
        if single[w] and stable(m, w, r):
            x[m] = w
            y[w] = m
            single[w] = False
            
            if m < n - 1:
                try_match(m + 1)  
            else:
                print_result()  

            single[w] = True 

# Programa principal
if __name__ == "__main__":
    try_match(0)
#vai resultar em duas tabelas com casamentos diferentes pois, há estas duas configurações de casamento estável para as preferências escolhidas