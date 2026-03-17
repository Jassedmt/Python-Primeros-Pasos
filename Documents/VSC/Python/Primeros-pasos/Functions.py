#primera función: La estructura básica

#Definamos la función.

def evaluate_attendace(days_list):
    total = len(days_list)

    if total >= 4:
        return "Allowed to take the exam"
    else:
        return "Not allowed"
    
#2 Usamos la funcion con diferentes alumnos
jassed_attendance = ["Mon", "Tue", "Wed", "Thu"]
carlos_attendance = ["Mon", "fri"]

print(f"Jassed: {evaluate_attendace(jassed_attendance)}")
print(f"Carlos: {evaluate_attendace(carlos_attendance)}")

#Conceptos clave:
# def: Es la palabra mágica para decirle a Python "voy a crear una función".

# days_list: Es un parámetro. Es un nombre genérico que la función usará internamente. No importa si fuera le pasas la lista de Jassed o la de Carlos, dentro de la función se llamará days_list.

# return: Es lo que la función "suelta" al terminar. Si no pones return, la función hace el trabajo pero no te devuelve nada (sería como una máquina de café que se bebe el café ella misma).

#------------------------------------------------------------
print(f"-"*30)
#Reto
# Instrucciones:

# Crea una función llamada check_salary_level.

# Debe recibir un solo número como parámetro (el salario).

# Si el salario es > 2500, debe devolver el texto "High Salary".

# Si no, debe devolver "Regular Salary".


def check_salary_level(salary):
    if salary > 2500:
        return"High Salary"
    else:
        return"Regular salary"

first_salary = 2800
second_salary = 3000
third_salary = 1000

print(f"the first salary is {first_salary}, {check_salary_level(first_salary)}")
print(f"The second salary is {second_salary}, {check_salary_level(second_salary)}")
print(f"The third salary is {third_salary}, {check_salary_level(third_salary)}")

#------------------------------------------------------------
print(f"-"*30)

# Funciones con Bucles (for)
# Ahora que sabes crear una "máquina" que procesa un solo dato (un salario), vamos a crear una "fábrica" que procese una lista entera y nos devuelva un informe.

def analyze_all_salaries(salary_list):
    count_high = 0
    for s in salary_list:
        if s > 2500:
            count_high +=1
    return f"Analysis complete: We found {count_high} high salaries."

#probemos la fábrica
my_ofice_salaries = [2100, 2800, 3200, 1800, 4000, 2000, 1100, 2550]
print(analyze_all_salaries(my_ofice_salaries))



#------------------------------------------------------------
print(f"-"*30)

# El Calculador de Ahorros
# Vamos a mezclar tus dos pasiones de estos días: Dinero y Funciones.

# Instrucciones:

# Crea una función llamada calculate_savings.

# Debe recibir dos parámetros: una lista de gastos y un sueldo_mensual.

# Dentro de la función:

# Suma todos los gastos (usa un bucle for o el truco de sum(gastos) si te sientes valiente).

# Resta ese total al sueldo_mensual.

# Return: Devuelve el dinero que te sobra a final de mes.

# El objetivo es que funcione así:
# mis_gastos = [100, 200, 50]
# mi_sueldo = 2000

# ahorro = calculate_savings(mis_gastos, mi_sueldo)
# print(f"Este mes he ahorrado: {ahorro}€")


def calculate_savings(expenses, salary):
   # A veces, cuando el cálculo es muy sencillo, podemos hacerlo todo en la misma línea del return.
    return salary - sum(expenses)

expenses = [100, 200, 50, 20]
salary = 2000



print(f"This month i have saved {calculate_savings(expenses, salary)}")


#------------------------------------------------------------
print(f"-"*30)

# Instrucciones:
# Modifica tu función calculate_savings para que, además de calcular el ahorro, imprima un consejo según el resultado:

# Si el ahorro es mayor a 500€, que imprima: "Great! You can invest this month."

# Si el ahorro es menor a 500€ pero mayor a 0, que imprima: "Good, but be careful with your expenses."

# Si el ahorro es menor o igual a 0, que imprima: "Danger! You are spending more than you earn."

def calculate_savings(expenses, salary):
    total = salary - sum(expenses)

    if total > 500:
        return f"This month i have saved {total}. Great, you can invest this month"
    elif 0 < total < 500 :
        return f"This month i have saved {total}. Good, but be careful with your expenses"
    else:
        return f"This month i have saved {total}. Danger, you are speding more than you can earn"
    

expenses = [100, 200, 50, 20, 900, 500, 200, 30]
salary = 2000

print(f"{calculate_savings(expenses, salary)}")


# En programación seguimos el principio DRY (Don't Repeat Yourself). Si el día de mañana quieres cambiar "This month" por "Current month", tendrías que cambiarlo en tres sitios.

# Mira cómo podrías optimizarlo (Refactorización):

def calculate_savings(expenses, salary):
    total = salary - sum(expenses)
    message = f"This month I have saved {total}€. " # Parte común
    
    if total > 500:
        advice = "Great! You can invest."
    elif total > 0:
        advice = "Good, but be careful."
    else:
        advice = "Danger! Overspending."
        
    return message + advice # Unimos la parte común con el consejo



#------------------------------------------------------------
print(f"-"*30)

# Ejercicio 1: El Convertidor de Moneda (Múltiples Parámetros)
# En Madrid, muchas veces trabajamos con empresas de fuera. Imagina que recibes una lista de facturas en Dólares (USD) y quieres saber cuánto es en Euros (EUR).

# Instrucciones:

# Crea una función llamada convert_to_eur.

# Debe recibir dos parámetros: una lista de amounts_usd y el exchange_rate (el valor del dólar hoy, por ejemplo 0.92).

# Dentro de la función:

# Crea una lista vacía llamada amounts_eur = [].

# Recorre la lista de dólares con un for.

# Multiplica cada cantidad por el exchange_rate y añade el resultado a la nueva lista usando .append().

# Return: Devuelve la nueva lista de euros.


def convert_to_eur(amounts_usd, exchange_rate):

    amount_eur_list = []

    for usd in amounts_usd:
       eur = usd * exchange_rate
       amount_eur_list.append(eur)
    return amount_eur_list
    
amount_usd = [100, 1500, 2000, 800, 300, 200, 500, 20000]
exchange_rate = 0.92

result =convert_to_eur(amount_usd, exchange_rate)
print(f"Facturas en EUR: {result}")



#------------------------------------------------------------
print(f"-"*30)

# Ejercicio 2: El Filtro de Invitados (Lógica y Seguridad)
# Imagina que estás organizando un evento de networking tecnológico en Madrid. Solo pueden entrar personas que estén en la "Lista VIP" o que tengan más de 18 años.

# Instrucciones:

# Crea una función llamada can_access_event.

# Debe recibir tres parámetros: name, age y is_vip (este último será un Booleano: True o False).

# Lógica interna:

# Si is_vip es True, devuelve: "Welcome [name], you are on the VIP list! 🌟"

# Si no es VIP, pero la age es mayor o igual a 18, devuelve: "Welcome [name], please show your ID. ✅"

# En cualquier otro caso, devuelve: "Sorry [name], access denied. ❌"

def can_access_event(name, age, is_vip):
        if is_vip:
            return f"Welcome {name}, you are on the VIP list"
        elif age >= 18:
            return f"Welcome {name}, please show your ID"
        else:
            return f"Sorry {name}, access denied"
        
access_list = [["Pepito", 21, False], ["Jassed", 25, True], ["Pepe", 17, False]]

for guest in access_list:
    n = guest[0]
    a = guest[1]
    v = guest[2]
    
    print(can_access_event(n, a, v))