# Machine_Learning_Project_Victor_Manuel_De_Sousa_Sanchez
En este proyecto de Machine Learning usaremos el dataset de Credit Risk. En este problema queremos saber si concederles un credito conlleva un riesgo de no devolución y, por lo tanto, si se lo daremos o no. Usaremos un clasificacdor binario para este problema. Veamos un poco la descripción del dataset.

Aquí un poco de información para este dataset:


1. **person_age:** Edad de la persona solicitante del crédito (entero).
2. **person_income:** Ingreso anual de la persona solicitante (entero, en alguna unidad monetaria no especificada).
3. **person_home_ownership:** Tipo de propiedad de vivienda del solicitante (categoría: RENT, OWN, MORTGAGE, etc.).
4. **person_emp_length:** Años de experiencia laboral de la persona (float, algunos valores faltantes).
5. **loan_intent:** Propósito del préstamo (categoría: PERSONAL, EDUCATION, MEDICAL, etc.).
6. **loan_grade:** Grado del préstamo (categoría: A, B, C, etc.).
7. **loan_amnt:** Monto solicitado del préstamo (entero).
8. **loan_int_rate:** Tasa de interés del préstamo (float, algunos valores faltantes).
9. **loan_status:** Indicador del estatus del préstamo (1 = aprobado, 0 = rechazado).
10. **loan_percent_income:** Proporción del préstamo respecto al ingreso anual del solicitante (float).
11. **cb_person_default_on_file:** Indicador de historial de incumplimiento (categoría: Y = Sí, N = No).
12. **cb_person_cred_hist_length:** Duración del historial crediticio de la persona en años (entero).

Con esta información podemos sacar en claro cual será el **target**: **loan_status.**