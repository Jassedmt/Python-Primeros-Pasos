# Para avanzar hoy, vamos a dar el salto al Data Cleaning Real. 
# Imagina que te llega un archivo de Recursos Humanos con datos de nuevos empleados en Madrid, 
# pero el sistema falló y los nombres, correos y salarios están "sucios".

# Datos tal cual vienen del sistema fallido
raw_employees = [
    ["  ALBERTO garcia  ", " ALBERTO@GMAIL.COM ", " 2.500,00€ "],
    ["  marta SANCHEZ  ", "marta.sanz@HOTMAIL.COM", " 3.100,50€ "],
    [" javier LOPEZ  ", " Javi_Lo@yahoo.es", " 1.850,25€ "],
    ["  lucia MARTINEZ ", "LUCIA.MTZ@gmail.com ", " 4.200,00€ "]
]

# Tu misión (Paso a paso):Tienes que crear una función llamada clean_employee_data(data_list) que transforme esa lista en algo profesional.
# Lo que debe hacer la función por cada empleado:Nombre: Quitar espacios y ponerlo en formato de nombre propio 
# (Ej: "  ALBERTO garcia  " $\rightarrow$ "Alberto Garcia"). 
# Pista: usa .strip().title().Email: Quitar espacios y ponerlo todo en minúsculas.
# Salario: Usar la lógica de clean_price que perfeccionamos antes para que sea un número (float).
# Cálculo Extra: Calcular el salario neto (réstale un 15% de impuestos al salario limpio).
# Resultado: Por cada empleado, imprime una frase clara:"Empleado: Alberto Garcia | Email: alberto@gmail.com | Neto: 2125.00€"

def clean_employee_data(raw_employees):

    for name, email, salary in raw_employees:
        name = name.strip().title()
        email = email.strip().lower()
        salary = salary.replace("€", "").strip().replace(".", "").replace(",", ".")
        salary = float(salary)
        net_salary = salary * 0.85
        print(f"Empleado: {name} | Email: {email} | Neto: {net_salary}€")

clean_employee_data(raw_employees)

#------------------------------------------------------------
print(f"-"*30)

# El código "Nivel Junior Pro"
# Para que tu función no solo "grite" los datos, sino que los "entregue" en una bandeja, necesitamos tres pasos:
# Crear una lista vacía al principio de la función.
# Limpiar los datos (esto ya lo haces de lujo).
# Añadir (.append()) esos datos limpios a la lista nueva en cada vuelta del bucle.

def clean_employee_data(raw_employees):
    # 1. Creamos la "bandeja" vacía
    cleaned_list = []

    for name, email, salary in raw_employees:
        #2. La limpieza
        name = name.strip().title()
        email = email.strip().lower()
        salary_clean = float(salary.replace("€", "").strip().replace(".", "").replace(",", "."))
        net_salary = salary_clean * 0.85

        # 3. Creamos una pequeña lista con los datos YA LIMPIOS
        employee_clean = [name, email, net_salary]

        # 4. Metemos al empleado limpio en la bandeja
        cleaned_list.append(employee_clean)

    # 5. Al final, entregamos la bandeja llena
    return cleaned_list

# --- ASÍ SE USA AHORA ---

# Ahora 'empleados_finales' es una lista real con la que puedes trabajar
empleados_finales = clean_employee_data(raw_employees)

# Por ejemplo, ahora podrías contar cuántos hay o sacar solo el primer nombre
print(f"Hemos procesado {len(empleados_finales)} empleados.")
print(f"El primer empleado de la lista limpia es: {empleados_finales[0][0]}")


 #Reto crear OTRA función pequeña que sume todos los salarios netos de esa lista

def calculate_total_payroll(cleaned_list):
    #Calcula la suma total de los salarios netos de una lista limpia.
    total = 0
    for employee in cleaned_list:
        total += employee[2]
    return total

# 1. Limpiamos los datos y guardamos el resultado
empleados_listos = clean_employee_data(raw_employees)

# 2. Le pasamos esos datos listos a la función de sumar
nomina_total = calculate_total_payroll(empleados_listos)

print(f"Informe generado para {len(empleados_listos)} empleados.")
print(f"El coste total de nóminas netas es: {nomina_total:.2f}€")