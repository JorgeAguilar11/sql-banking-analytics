# 🏦 GUÍA PRÁCTICA SQL BANCARIO
## Tu Resumen Completo de Aprendizaje

---

## 📋 **TABLA DE CONTENIDO**

1. [✅ Ejercicios Completados](#ejercicios-completados)
2. [🎯 Conceptos Dominados](#conceptos-dominados)
3. [📊 Casos de Uso Bancarios](#casos-de-uso-bancarios)
4. [🚀 Consultas Avanzadas](#consultas-avanzadas)
5. [💡 Tips y Buenas Prácticas](#tips-y-buenas-prácticas)

---

## ✅ **EJERCICIOS COMPLETADOS**

### **EJERCICIO 1: Selección Básica** ✅
```sql
SELECT nombres, apellidos, ciudad 
FROM clientes;
```
**📝 Lo que aprendiste:**
- Estructura básica de `SELECT`
- Seleccionar columnas específicas
- Sintaxis correcta con `;`

---

### **EJERCICIO 2: Conteo Total** ✅
```sql
SELECT COUNT(*) as total_clientes 
FROM clientes;
```
**📝 Lo que aprendiste:**
- Función de agregación `COUNT(*)`
- Uso de alias con `AS`
- Resultado: **20 clientes** total

---

### **EJERCICIO 3: Filtros con WHERE** ✅
```sql
SELECT * 
FROM clientes 
WHERE ciudad = 'Bogotá';
```
**📝 Lo que aprendiste:**
- Filtrado con `WHERE`
- Importancia de mayúsculas/minúsculas
- Corrección de errores de sintaxis
- Resultado: **1 cliente** en Bogotá inicialmente

---

### **EJERCICIO 4: Ordenamiento** ✅
```sql
SELECT nombres, apellidos, ingresos_mensuales
FROM clientes
ORDER BY ingresos_mensuales DESC;
```
**📝 Lo que aprendiste:**
- Ordenamiento con `ORDER BY`
- `DESC` para orden descendente
- Ranking de clientes por ingresos

---

### **EJERCICIO 5: Agrupación** ✅
```sql
SELECT ciudad, COUNT(*) as total_clientes 
FROM clientes
GROUP BY ciudad;
```
**📝 Lo que aprendiste:**
- Agrupación con `GROUP BY`
- Combinación de `SELECT`, `COUNT()` y `GROUP BY`
- Distribución por ciudades:
  - **Bucaramanga**: 6 clientes
  - **Medellín**: 6 clientes
  - **Bogotá**: 3 clientes
  - **Cali**: 3 clientes
  - **Barranquilla**: 2 clientes

---

### **EJERCICIO 6: Filtros Numéricos** ✅
```sql
SELECT nombres, apellidos, ingresos_mensuales, ciudad
FROM clientes
WHERE ingresos_mensuales > 4000000
ORDER BY ingresos_mensuales DESC;
```
**📝 Lo que aprendiste:**
- Filtros numéricos con operadores (`>`, `<`, `>=`, `<=`)
- Combinación de `WHERE` y `ORDER BY`
- Identificación de clientes de altos ingresos
- **12 de 20 clientes** (60%) ganan más de 4M

---

## 🎯 **CONCEPTOS DOMINADOS**

### **1. SELECT - Selección de Datos**
```sql
-- Seleccionar todas las columnas
SELECT * FROM tabla;

-- Seleccionar columnas específicas
SELECT columna1, columna2 FROM tabla;

-- Con alias
SELECT columna1 AS nombre_nuevo FROM tabla;
```

### **2. WHERE - Filtrado**
```sql
-- Filtro de texto
WHERE ciudad = 'Bogotá'

-- Filtro numérico
WHERE ingresos_mensuales > 4000000

-- Filtros múltiples
WHERE ciudad = 'Medellín' AND ingresos_mensuales > 5000000
```

### **3. ORDER BY - Ordenamiento**
```sql
-- Ascendente (por defecto)
ORDER BY ingresos_mensuales

-- Descendente
ORDER BY ingresos_mensuales DESC

-- Múltiples columnas
ORDER BY ciudad, ingresos_mensuales DESC
```

### **4. GROUP BY - Agrupación**
```sql
-- Agrupar y contar
SELECT ciudad, COUNT(*) as total
FROM clientes
GROUP BY ciudad;

-- Agrupar y promediar
SELECT ciudad, AVG(ingresos_mensuales) as promedio
FROM clientes
GROUP BY ciudad;
```

### **5. Funciones de Agregación**
```sql
COUNT(*)           -- Contar filas
SUM(columna)       -- Sumar valores
AVG(columna)       -- Promedio
MAX(columna)       -- Valor máximo
MIN(columna)       -- Valor mínimo
```

---

## 📊 **CASOS DE USO BANCARIOS**

### **🏪 Análisis de Sucursales**
```sql
-- ¿Qué ciudad tiene más clientes?
SELECT ciudad, COUNT(*) as total_clientes 
FROM clientes 
GROUP BY ciudad 
ORDER BY total_clientes DESC;
```

### **💰 Segmentación de Clientes**
```sql
-- Clientes VIP (>8M)
SELECT nombres, apellidos, ingresos_mensuales
FROM clientes 
WHERE ingresos_mensuales > 8000000
ORDER BY ingresos_mensuales DESC;
```

### **📈 Análisis de Ingresos**
```sql
-- Promedio de ingresos por ciudad
SELECT ciudad, 
       AVG(ingresos_mensuales) as promedio_ingresos,
       COUNT(*) as cantidad_clientes
FROM clientes 
GROUP BY ciudad 
ORDER BY promedio_ingresos DESC;
```

### **🎯 Targeting de Marketing**
```sql
-- Clientes de clase media (3M-7M)
SELECT nombres, apellidos, ciudad, ingresos_mensuales
FROM clientes 
WHERE ingresos_mensuales BETWEEN 3000000 AND 7000000
ORDER BY ciudad, ingresos_mensuales DESC;
```

---

## 🚀 **CONSULTAS AVANZADAS**

### **TOP N Consultas**
```sql
-- Top 5 clientes más ricos
SELECT nombres, apellidos, ingresos_mensuales, ciudad
FROM clientes 
ORDER BY ingresos_mensuales DESC 
LIMIT 5;
```

### **Rangos de Ingresos**
```sql
-- Clasificación por rangos
SELECT 
    CASE 
        WHEN ingresos_mensuales > 8000000 THEN 'VIP'
        WHEN ingresos_mensuales > 4000000 THEN 'Premium'
        ELSE 'Estándar'
    END as categoria,
    COUNT(*) as cantidad
FROM clientes 
GROUP BY categoria;
```

### **Análisis Combinado**
```sql
-- Resumen ejecutivo por ciudad
SELECT 
    ciudad,
    COUNT(*) as total_clientes,
    AVG(ingresos_mensuales) as promedio_ingresos,
    MAX(ingresos_mensuales) as ingreso_maximo,
    MIN(ingresos_mensuales) as ingreso_minimo
FROM clientes 
GROUP BY ciudad 
ORDER BY promedio_ingresos DESC;
```

---

## 💡 **TIPS Y BUENAS PRÁCTICAS**

### **✅ Errores Comunes que Evitaste:**
1. **Nombres de columnas**: `ingreso` vs `ingresos_mensuales`
2. **Punto y coma**: No dividir consultas con `;` en medio
3. **Mayúsculas**: `'BOGOTÁ'` vs `'Bogotá'`
4. **GROUP BY**: Incluir todas las columnas no agregadas

### **🎯 Estructura Recomendada:**
```sql
SELECT columnas         -- Qué quieres ver
FROM tabla             -- De dónde
WHERE condiciones      -- Filtros
GROUP BY columnas      -- Agrupaciones
ORDER BY columnas      -- Ordenamiento
LIMIT numero;          -- Limitaciones
```

### **📝 Consejos para el Futuro:**
- **Siempre verifica** los nombres exactos de las columnas
- **Usa alias** para hacer resultados más legibles
- **Combina filtros** para análisis más específicos
- **Ordena resultados** para mejor interpretación
- **Prueba incrementalmente** - agrega complejidad paso a paso

---

## 🏆 **TU PROGRESO**

### **Nivel Alcanzado: INTERMEDIO** ⭐⭐⭐
✅ Selecciones básicas  
✅ Filtrado con WHERE  
✅ Ordenamiento  
✅ Agrupaciones  
✅ Funciones de agregación  
✅ Consultas combinadas  

### **Próximos Desafíos:**
- 🔄 JOINs entre tablas
- 📊 Subconsultas
- 🎯 Funciones de ventana
- 📈 CTEs (Common Table Expressions)

---

## 🎉 **¡FELICITACIONES!**

Has completado exitosamente **6 ejercicios SQL** progresivos y dominado los conceptos fundamentales para análisis bancario. Tu práctica con datos reales te ha preparado para consultas más avanzadas.

**Total de clientes analizados:** 20  
**Consultas ejecutadas:** 6+  
**Conceptos dominados:** 8  
**Errores corregidos:** 4  

---

*📅 Completado: Julio 2025*  
*🎯 Siguiente paso: Explorar JOINs y relaciones entre tablas*

---

**¿Listo para el siguiente nivel? ¡Sigamos practicando! 🚀**
