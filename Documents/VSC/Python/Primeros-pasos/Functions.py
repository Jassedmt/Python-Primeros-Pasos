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

    #------------------------------------------------------------
print(f"-"*30)

# Ejercicio 3. El Validador de Emails (Limpieza básica)
# En las bases de datos de marketing, a veces los emails vienen mal escritos 
# (con espacios o en mayúsculas).

# Instrucciones:

# Crea una función llamada clean_email.
# Debe recibir un parámetro: raw_email.
# Dentro de la función:
# Usa .strip() para quitar espacios al principio y al final.
# Usa .lower() para ponerlo todo en minúsculas.
# Return: Devuelve el email ya limpio.

# Prueba: Crea una lista emails_sucios = ["  Jassed@Gmail.com", "CONTACTO@empresa.ES  ", "  admin@Madrid.Tech  "] y usa un bucle para limpiar cada uno e imprimirlos.

def clean_email(dirty_email):

    emails = []

    for email in dirty_email:
        clean_space_email = email.strip().lower()
        emails.append(clean_space_email)
    return emails

dirty_email = ["  Jassed@Gmail.com ", "CONTACTO@empresa.ES  ", "  admin@Madrid.Tech  "]

print(f"{clean_email(dirty_email)}")


    #------------------------------------------------------------
print(f"-"*30)

# Ejercicio 4: El Buscador de "Talento Top"
# Ahora que tienes la "fábrica de limpieza" dominada, vamos a por la 
# "fábrica de decisiones". Este ejercicio no usa listas ni .append(),
# sino que evalúa una sola persona cada vez que lo llamas.

# Instrucciones:
# Crea la función is_senior_candidate(years_exp, language).
# Si tiene más de 5 años y el lenguaje es "Python" (ojo con las mayúsculas), devuelve: "High Priority".
# Si tiene más de 5 años pero otro lenguaje, devuelve: "Medium Priority".
# En cualquier otro caso, devuelve: "Junior Developer".

def is_senior_candidate(years_exp, language):
    language = language.title()

    if years_exp > 5 and language == "Python":
        return "High Priority"
    elif years_exp > 5 and language != "Python":
        return "Medium Priority"
    else:
        return "Junior developer"

print(is_senior_candidate(8, "Python"))
print(is_senior_candidate(10, "Java"))
print(is_senior_candidate(2, "Python"))

    #------------------------------------------------------------
print(f"-"*30)

# Como quieres machacar la base, aquí tienes dos retos que mezclan Listas + Funciones + Lógica Acumulativa.

# 5. El "Calculador de Comisiones" (Ventas Madrid)En una empresa de software en Madrid, 
# los comerciales tienen diferentes comisiones según lo que vendan.

# Instrucciones: 
# Crea una función calculate_commission(sales_list).
# Lógica: * Si la venta es mayor a 10.000€, la comisión es del 10% ($0.10$).
# Si la venta es menor o igual a 10.000€, la comisión es del 5% ($0.05$).
# Objetivo: La función debe recibir la lista de ventas, calcular la comisión de cada una y devolver la suma total de todas las comisiones.

def calculate_commission1(sales_list):
     total_commissions = 0 # Esta es nuestra hucha

     for sale in sales_list:
         # 1. Calculamos la comisión de ESTA venta
         if sale > 10000:
             current_comm = sale * 0.10
         else:
             current_comm = sale * 0.05
        
         # 2. Metemos esa comisión en la hucha
         total_commissions += current_comm
        
     # 3. Al final, devolvemos la hucha llena
     return total_commissions

sales_list = [12000, 5000, 25000, 10000, 800, 15000]
print(f"Total a pagar en comisiones: {calculate_commission1(sales_list)}€")

    #------------------------------------------------------------
print(f"-"*30)


#Para hacerlo mas entretenido de la siguiente manera:

def calculate_commission(sales_list):
    total_commissions = 0
    commissions_list = [] # Nuestra lista de porcentajes calculados
    
    for sale in sales_list:
        if sale > 10000:
            current_comm = sale * 0.10
        else:
            current_comm = sale * 0.05
        
        # Guardamos en la lista y sumamos al total
        commissions_list.append(current_comm)
        total_commissions += current_comm
    
    # IMPORTANTE: El return va fuera del for
    # Devolvemos una lista que contiene DOS cosas
    return [commissions_list, total_commissions]

# --- USO DE LA FUNCIÓN ---
sales_list = [12000, 5000, 25000, 10000, 800, 15000]

# Guardamos el resultado (que es una lista de dos posiciones)
resultado = calculate_commission(sales_list)

# Accedemos a la posición [0] para la lista y a la [1] para el total
print(f"Lista de comisiones individuales: {resultado[0]}")
print(f"Total a pagar en comisiones: {resultado[1]}€")


    #------------------------------------------------------------
print(f"-"*30)

# 6. El "Filtro de Seguridad de Contraseñas"
# Vamos a crear una función que valide si una contraseña es segura para una App.
# Instrucciones: Crea una función is_secure_password(password).
# Lógica (debe cumplir AMBAS para ser True):
# Tener más de 8 caracteres (pista: usa len()).
# No contener la palabra "123" (pista: usa if "123" not in password:).
# Return: Debe devolver True si es segura o False si no lo es.

def is_secure_password(password):

    secure_password = len(password)
    if "123" not in password and secure_password > 8 :
        return True
    else:
        return False

password = "madrid2026"
print(f"{is_secure_password(password)}")        
    #------------------------------------------------------------
print(f"-"*30)

#Cuando una condición de un if ya devuelve True o False por sí misma, 
# puedes hacer el "Súper Atajo":

def is_secure_password(password):
    # Esto devuelve directamente el resultado de la comparación
    return "123" not in password and len(password) > 8
password = "madrid123"
print(f"{is_secure_password(password)}")




#------------------------------------------------------------
print(f"-"*30)

# EJERCICIO 7. El "Filtro de Precios de Idealista" 🏠
# Imagina que trabajas en un portal inmobiliario en Madrid. 
# Tienes una lista de precios de alquileres y quieres una función que te devuelva solo los que están en tu presupuesto.

# Función: filter_rentals(price_list, max_budget)

# Tarea: La función debe recibir una lista de precios (números) y tu presupuesto máximo (un número). 
# Debe devolver una nueva lista que contenga solo los precios que son menores o iguales a tu presupuesto.

# Prueba con: rentals = [1200, 900, 1500, 850, 2000] y un presupuesto de 1000.


def filter_rentals(price_list, max_budget):
    budget_list = []
    for price in price_list:
        if price <= max_budget:
            budget_list.append(price)
        # Comprobamos si la lista está vacía DESPUÉS de revisar todos los precios
    if len(budget_list) == 0:
        return "No hay rentas con tu presupuesto indicado"
    
    return budget_list

max_budget = int(input("introduce tu presupuesto: "))
price_list = [1200, 900, 1500, 850, 2000]
print(f"{filter_rentals(price_list, max_budget)}")

# 8. El "Contador de Menciones" 📱
# Como analista de redes sociales, necesitas saber cuántas veces se menciona una palabra clave (hashtag) en una serie de posts.

# Función: count_hashtag(posts_list, hashtag)

# Tarea: La función recibe una lista de textos (strings) y una palabra clave (ej: "Python"). 
# Debe devolver el número total de veces que esa palabra exacta aparece en los posts.

# Prueba con: my_posts = ["I love Python", "Python is great", "JavaScript is ok", "Learning Python now"] y el hashtag "Python".

def count_hashtags(posts_list, hashtag):
    hashtag_count = 0

    hashtag = hashtag.lower()

    for post in posts_list:
        if hashtag in post.lower():
            hashtag_count +=1
    return hashtag_count
    
hashtag = input("Introduce el Hashtag que quieres saber cuántas veces se menciona: ")
posts_list = ["I love Python", "Python is great", "JavaScript is ok", "Learning Python now"]
print(f"se ha mencionado {count_hashtags(posts_list, hashtag)} veces")