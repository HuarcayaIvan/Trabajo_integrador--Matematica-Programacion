# Trabajo_integrador--Matematica

# Filtro Binario para Seguros Automotores

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## Descripción del Proyecto
Este proyecto contiene dos implementaciones diferentes de un sistema de filtrado de clientes para seguros automotores, basado en:
1. **Circuitos lógicos digitales** (Álgebra de Boole)
2. **Estructuras condicionales anidadas** (Lógica procedural)

Ambas implementaciones determinan la aceptación o rechazo de clientes según tres criterios:
- Estado en Veraz
- Tipo de uso (comercial/personal)
- Presupuesto (para uso personal)

## Estructura del Proyecto
```bash
.
├── circuito_logico_seguros.py # Versión con simulación de circuito lógico
├── seguros.py # Versión con estructura condicional clásica
└── README.md # Documentación del proyecto
```

## Características Principales
### 1. `circuito_logico_seguros.py`
- Implementa un circuito digital usando compuertas lógicas booleanas
- Estructura:
  ```python
  salida = (
      ((presupuesto and not comercial)  # AND1
       or comercial)                    # OR 
      and not veraz                     # AND_FINAL
  )

- Diagrama lógico:
```bash
    VERAZ ───[NOT]───────────────────┐
                                     AND_FINAL ─── Salida
    COMERCIAL ────────────────┐      │
         │                    OR ────┘
         └─[NOT]─┐            │
                  AND1 ───────┘        
    PRESUPUESTO ───┘
```

### 2. `seguros.py`
- Utiliza estructuras condicionales anidadas
- Flujo de decisión:
```python
if veraz → Rechazar
else:
    if comercial → Aceptar
    else:
        if presupuesto > 100000 → Aceptar
        else → Rechazar
```

## Instalación y uso
1. Requisitos:
- Python 3.8 o superior
- No se requieren dependencias externas
2. Ejecución:
```bash
# Versión con circuito lógico
python circuito_logico_seguros.py

# Versión condicional
python seguros.py
```
## Fundamentos Matemáticos
El proyecto aplica:

**Álgebra de Boole**:
- Operadores lógicos: AND, OR, NOT
- Tablas de verdad

**Lógica proposicional**:
- Proposiciones compuestas
- Implicaciones lógicas

**Comparaciones numéricas**:
- Operadores relacionales (>)

---

## Participantes

- Nikolas Barroso
- Natascha Berger
- Gabriel Gudiño
- Ignacio Herbel
- Ivan Huarcaya