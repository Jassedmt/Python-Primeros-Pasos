#Reto 1: El Filtro de Salarios (Data Filtering) 
# Imagina que tienes una lista de ofertas de trabajo en Madrid 
# con diferentes sueldos. Queremos saber cuáles son "buenas" 
# (más de 2500€) y cuáles son "promedio".

#Instrucciones:

#Crea una lista llamada salaries = [1800, 2600, 2100, 3200, 1500, 2800].

#Usa un bucle for para recorrer cada salario.

#Dentro del bucle, usa un if:

#Si el salario es mayor a 2500, imprime: "High Salary: [monto]€ - Apply now!"

#Si no, imprime: "Regular Salary: [monto]€ - Keep looking."


salaries = [1800, 2600, 2100, 3200, 1500, 2800]

for salary in salaries:
    print(f"the salary is: {salary}€ per month.")

    if salary > 2500:
        print(f"High salary: {salary}€ - Apply now!")
    else:
        print(f"Regular salary: {salary}€ - keep looking.")


#----------------------------------------------------------------------
# Reto 2: El Contador de Tecnologías (Counting Logic)
# En las ofertas de empleo suelen pedir varias tecnologías. Vamos a contar cuántas de las que tú sabes coinciden con una oferta.

# Instrucciones:

# Crea una lista con tus habilidades: my_skills = ["Python", "Git", "English"].

# Crea una variable match_count = 0 (tu hucha).

# Crea otra lista con lo que pide una oferta de trabajo: job_requirements = ["Python", "Java", "Git", "SQL", "English"].

# Usa un bucle for para recorrer job_requirements.

# Dentro, usa un if para preguntar: ¿Está este requisito en mi lista de habilidades? * Pista: Se usa if requirement in my_skills:.

# Si está, suma 1 a tu match_count.

# Al final (fuera del bucle), imprime: "You match [match_count] out of 5 requirements for this job."

my_skills = ["Python", "Git", "English"]

match_count = 0

jobs_requirements = ["Python", "Java", "Git", "SQL", "English"]

for requirements in jobs_requirements:
    #print(f"{requirements}")
    if requirements in my_skills:
        match_count+=1

if match_count == 5:
    print(f"You match {match_count} out of 5 requirements for this job. The work is yours")
elif match_count >=3:
    print(f"You match {match_count} out of 5 requirements for this job. Maybe they accept")
else:
    print("keep learning")



print(f"-"*30)
#------------------------------------------------------------------------------------------------------------------
# Reto 3: "The Attendance Checker"
# Tienes una lista con los días de la semana que un alumno asistió a clase. Queremos saber si tiene derecho a examen (necesita al menos 4 asistencias).

# Instrucciones:

# Crea una lista llamada attendance = ["Monday", "Tuesday", "Thursday", "Friday"].

# Crea una variable para contar las asistencias (tu "hucha").

# Usa un bucle para recorrer la lista y sumar 1 por cada día que aparezca.

# OJO AQUÍ: Al final, usa una estructura if/elif/else para imprimir:

# Si tiene 5 días: "Perfect attendance! 🏆"

# Si tiene 4 días: "Good job, you can take the exam. ✅"

# Si tiene menos de 4: "Sorry, you missed too many classes. ❌"

attendace = ["Monday", "Tuesday", "Thursday", "Friday"]

assists = 0

for day in attendace:
    assists+=1

if assists == 5:
    print("Perfect Attendace")
elif assists == 4:
    print("good job, you can take the exam.")
else:
    print("Sorry, you missed too many classes.")


print(f"-"*30)

# Reto 4: "The Budget Tracker"
# Tienes una lista de gastos del mes en Madrid. Quieres saber cuánto has gastado en total y si te has pasado de tu presupuesto de 500€.

# Instrucciones:

# Lista de gastos: expenses = [15.50, 200, 45, 120, 30].

# Presupuesto máximo: budget = 500.

# Necesitas una variable para ir sumando los gastos (el acumulador).

# El reto: Calcula el total y dinos cuánto dinero te ha sobrado (o por cuánto te has pasado).


expenses = [15.50, 200, 45, 120, 30, 90]

budget = 500
total_expense = 0

for expense in expenses:
   total_expense += expense

print(f"you have spent {total_expense}€")

leftover_money = budget - total_expense

if leftover_money < 0:
    print(f"You are in negative, {leftover_money}€")
else:
    print(f"You have {leftover_money}€ left over")


print(f"-"*30)

# Reto: "The Grocery List"
# Imagina que vas al supermercado con 50€. Tienes una lista de productos con sus precios, pero solo vas a comprar el producto si cuesta menos de 10€.

# Lista de precios: prices = [5, 12, 8, 20, 3, 15, 7]

# Presupuesto: wallet = 50

# Objetivo:

# Recorre los precios con un for.

# Usa un if para ver si el precio es menor a 10.

# Si es menor a 10, súmalo a una variable total_bill y réstalo de tu wallet.

# Al final, imprime cuánto dinero te queda en la wallet.

prices = [5, 12, 8, 20, 3, 15, 7, 9]

wallet = 50
total_bill= 0

for price in prices:
    if price <= 10:
        total_bill += price

money_left = wallet - total_bill

if money_left >= 0:
    print(f"Purchase successful! You spent {total_bill}€")
    print(f"You still have {money_left}€ in your wallet")
else:
    print(f"Alert: You don't have enough money")
    print(f"You need {abs(money_left)}€ more to pay the bill")