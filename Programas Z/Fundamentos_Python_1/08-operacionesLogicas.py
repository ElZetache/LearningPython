var = 1
 
 # Ejemplo 1:
print(var > 0)
print(not (var <= 0))
 
 
# Ejemplo 2:
print(var != 0)
print(not (var == 0))


print("---------------------------")
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

print("---------------------------")
x = 4
y = 1
 
100
001
000


#se hace el and a nivel de bit
#100 = 4
#001 = 1
#000 = 0, no coincide ningun 1
a = x & y
#se hace el OR a nivel de bit
#100
#001
#101 = 5, donde haya un 1 en alguno de los dos sigue habiendolo depues
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)