# 1.- Texto (Strings) - Siempre entre comillas
job_title = "Data Analyst"

# 2.- Números enteros (Integers) - Para contar cosas
age = 25

#3.- Números con decimales (Floats) - para porcentajes
target_salary = 2500.50

#Booleanos (Boolean) - Verdadero o Falso
is_studying_in_madrid = True

#Para ver que tenemos dentro, usamos print()
print(f"I am a {job_title}, I am {age} years old and it is {is_studying_in_madrid} that I study in Madrid")


# Primer Reto "Future Profile"

user_name = "Jassed"
weekly_study_hours = 2
target_month = 9
total_hours = 336

print(f"Hello, I am {user_name}. By {target_month} i will have studied {total_hours} hours and i will be ready for my new job")


# Matemáticas con Python

weekly_study_hours = 2
weeks_per_month = 4
month_to_study = 6

# Python hace el cálculo automáticamente 

total_hours = weekly_study_hours * weeks_per_month * month_to_study


# Hagámoslo dinámico (Input)

# 1.- Inputs (Colección de dartos)
user_name = input("Enter your name: ")
weekly_hours = int(input("How many hours will you study per week? "))
target_month_name = input("In which month do you want to start working? ")

# 2.- Lógica
# 4 a¡semanas por mes * 6 meses
total_hours = weekly_hours * 4 * 6

# Outputs (El resultado)

print("-" * 30) # Esto imprime una línea decorativa
print(f"Hello, I am {user_name}.")
print(f"By {target_month_name}, I will have studied {total_hours} hours.")
print(f"I will be ready for my new job in Madrid!")
print(f"-" * 30)

# Condicionales (if / else)

# Reto 2 "The intensity Checker"
#Vamos a modificar tu archivo para que, 
# dependiendo de cuántas horas totales hayas calculado, 
# el programa te dé un consejo diferente.

# Desicion making (flow Control)

if total_hours >= 500:
    print(f"STATUS: You are going for a Senior path! High intensity.🔥")
elif total_hours >= 200:
    print(f"STATUS: Solid progress. You will have a great portfolio for Novembre.💪")
else:
    print(f"STATUS: Maybe you shuld increase your hours to be more competitive in Madrid.")

print("-" * 30)


# Listas (Arrays)
#Una variable guarda un dato. Una Lista guarda una colección. En programación de IA,
# las listas son donde guardamos los datos que vamos a procesar.

# 1 Definir una lista (se usan con corchetes[])
months = ["September", "October", "November", "December"]

#2 Acceder a un elemento de la lista
#Python comienza a contar desde 0
first_month = months[0]


# Bucles (Loops)

#Imagina que quieres imprimir tu progreso mes a mes. 
# En lugar de escribir 6 veces el print, usamos un for. 
# Es la forma de decirle a Python:
# "Para cada elemento en esta lista, haz lo siguiente"

#Definimos los proximos meses de estudio
study_plan = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]

print("YOUR STUDY CALENDAR:")

# Por cada 'month' en la lista 'study_plan'...

for month in study_plan:
    #Calculamos las horas acumuladas por mes (suponiendo 4 semanas)
    accumulated_hours = weekly_hours * 4
    print(f"-> In {month} you will add {accumulated_hours} hours to yout Knowledge.")

print("End of the plan")

# 1 Definimos el punto de partida (Hucha vacía)
total_hours_so_far = 0

print("YOUR PROGRESSIVE STUDY CALENDAR:")

#2 El bucle 'for' con memoria
for month in study_plan:
    #calculamos las hora de ESTE mes
    hour_this_month = weekly_hours * 4

    #Actualizamos la hucha: lo que había + lo nuevo
    total_hours_so_far = total_hours_so_far + hour_this_month

    #imprimimos el total acumulado
    print(f"-> In {month}: You add {hour_this_month}h. Accumulated knwoledge: {total_hours_so_far}h")
    
print(f"--- Final result after 6 months: {total_hours_so_far} hours ---")

#-------------------------Reto-----------------------------

knowledge_goal = 200 #horas que se necesitan para ser 'Junior'

if total_hours_so_far >= knowledge_goal:
    print("You are ready for the Madrid tech market")
else: 
    print("Keep studying, you need more hours")
