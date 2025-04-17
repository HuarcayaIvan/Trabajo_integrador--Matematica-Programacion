# Trabajo_integrador--Matematica

# Sistema de Recomendación de Seguros para Automotores

## Descripción General

Este sistema está diseñado para ayudar a los usuarios a elegir el seguro de automotor más adecuado según su presupuesto, la frecuencia con la que usan el vehículo y el tipo de actividad que realizan (urbana, rural o comercial).

A través de un sistema interactivo por consola, el programa guía al usuario ingresando información clave y luego recomienda un plan personalizado entre diferentes aseguradoras y niveles de cobertura. Ideal para quienes buscan tomar decisiones informadas y eficientes sin complicaciones.

---

# Documentación del Programa

## Funcionamiento
1. Ingresa tu presupuesto mensual (mínimo **$45,000**).
2. Selecciona la **frecuencia de uso**: `ALTA`, `MEDIA` o `BAJA`.
3. Selecciona el **tipo de actividad**: `RURAL`, `URBANA` o `COMERCIAL`.
4. El sistema evalúa y devuelve una **recomendación personalizada** de aseguradora y plan.

## Aseguradoras Disponibles
- **La gente aseguradora SA**
- **La Caja de ahorro y seguro**
- **Golden Seguros SRL**

## Planes Disponibles
1. **Terceros cobertura C** (Básico)  
   Daños a terceros. Cobertura mínima obligatoria.
2. **Todo riesgo parcial** (Intermedio)  
   Cobertura amplia con franquicias.
3. **Todo riesgo** (Completo)  
   Cobertura total, incluye asistencia en viaje y beneficios extra.

## Requisitos
```bash
Python 3.11
```

## Ejecución
```bash
python seguros.py
```

## Ejemplo de Uso
```bash
------------------------------------------------------------------
Bienvenido al Sistema de Recomendación de Seguros para Automotores
------------------------------------------------------------------
Ingrese el monto mensual disponible a pagar: 100000
Ingrese la frecuencia de uso [ALTA] [MEDIA] [BAJA]: MEDIA  
Ingrese el tipo de actividad [RURAL] [URBANA] [COMERCIAL]: URBANA
Le recomendamos contratar La gente aseguradora SA con el plan Todo riesgo parcial.
```

## Notas
- **Presupuesto mínimo requerido:** $45.000 (pesos).
- **Formato de entrada:**
  - Frecuencia: `ALTA`, `MEDIA` o `BAJA` (escrito en MAYÚSCULAS).
  - Actividad: `RURAL`, `URBANA` o `COMERCIAL` (también en MAYÚSCULAS).
- Si el presupuesto no alcanza el mínimo, el programa termina indicando que no hay planes disponibles.

---

## Participantes

- Nikolas Barroso
- Natascha Berger
- Gabriel Gudiño
- Ignacio Herbel
- Ivan Huarcaya