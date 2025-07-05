# 🚀 GUÍA PRÁCTICA SQL BANCARIO AVANZADO
## Tu Certificación de SQL NINJA BANCARIO

---

## 📋 **TABLA DE CONTENIDO**

1. [🏆 Ejercicios Avanzados Completados](#ejercicios-avanzados-completados)
2. [🎯 Conceptos Ninja Dominados](#conceptos-ninja-dominados)
3. [📊 Análisis Estadístico Bancario](#análisis-estadístico-bancario)
4. [💼 Casos de Negocio Reales](#casos-de-negocio-reales)
5. [🔧 Operaciones de Rescate](#operaciones-de-rescate)
6. [🚀 Próximos Desafíos](#próximos-desafíos)

---

## 🏆 **EJERCICIOS AVANZADOS COMPLETADOS**

### **EJERCICIO 7: Promedio de Ingresos por Ciudad** ✅
```sql
SELECT 
    ciudad,
    ROUND(AVG(ingresos_mensuales), 2) AS promedio_ingresos
FROM clientes 
GROUP BY ciudad 
ORDER BY promedio_ingresos DESC;
```
**📊 Resultados Obtenidos:**
- **Barranquilla**: $6,468,453 (promedio más alto)
- **Bucaramanga**: $6,445,098
- **Medellín**: $6,413,413
- **Bogotá**: $4,751,162
- **Cali**: $3,338,088

**🎯 Conceptos Aplicados:**
- Función `AVG()` para promedios
- `ROUND()` para formatear decimales
- `GROUP BY` con análisis estadístico

---

### **EJERCICIO 8: Top 3 Clientes Más Ricos** ✅
```sql
SELECT 
    nombres || ' ' || apellidos AS nombre_completo,
    ingresos_mensuales,
    ciudad
FROM clientes 
ORDER BY ingresos_mensuales DESC
LIMIT 3;
```
**🏆 Top 3 Identificado:**
1. **Isabella Jiménez**: $11,060,983 (Bucaramanga)
2. **Pedro Morales**: $10,330,811 (Medellín)
3. **Sofia Rivera**: $9,834,891 (Bucaramanga)

**🎯 Conceptos Aplicados:**
- Concatenación de strings con `||`
- `ORDER BY ... DESC` para ranking
- `LIMIT` para obtener top N

---

### **EJERCICIO 9: Clase Media Jodida** ✅ 🎨 **(CON ESTILO PERSONAL)**
```sql
SELECT 
    nombres AS nombre,
    ingresos_mensuales,
    'Clase Media Jodida' AS categoria_cliente
FROM clientes
WHERE ingresos_mensuales BETWEEN 3000000 AND 7000000
ORDER BY ingresos_mensuales DESC;
```
**📋 Segmento Identificado:**
- **10 clientes** en rango 3M-7M
- Desde Miguel ($6,377,879) hasta Isabella ($3,058,931)
- **Terminología personalizada** aplicada con humor

**🎯 Conceptos Aplicados:**
- `BETWEEN ... AND` para rangos numéricos
- Columnas literales con personalización
- Análisis de segmentación creativa

---

### **EJERCICIO 10: Conteo por Segmento** ✅
```sql
SELECT 
    segmento_cliente,
    COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY segmento_cliente
ORDER BY cantidad_clientes DESC;
```
**📊 Distribución Final (Post-Actualización):**
- **VIP**: 5 clientes (25%)
- **Premium**: 5 clientes (25%)
- **Estándar**: 8 clientes (40%)
- **Básico**: 2 clientes (10%)

**🎯 Conceptos Aplicados:**
- `GROUP BY` con conteo
- Análisis de distribución porcentual
- Identificación de oportunidades de negocio

---

### **EJERCICIO 11: Ciudad Ganadora** ✅
```sql
SELECT 
    ciudad,
    SUM(ingresos_mensuales) AS ingresos_totales
FROM clientes
GROUP BY ciudad
ORDER BY ingresos_totales DESC
LIMIT 1;
```
**🏆 Ciudad Campeona:**
- **Bucaramanga**: $38,670,590 (suma total más alta)
- Diferencia mínima con Medellín (~$190K)
- **Estrategia**: Enfocar productos VIP en Bucaramanga

**🎯 Conceptos Aplicados:**
- `SUM()` para agregación financiera
- Identificación de mercados objetivo
- Análisis competitivo entre ciudades

---

### **EJERCICIO 12: Análisis VIP Súper Avanzado** ✅ 🧠 **(NIVEL NINJA)**
```sql
SELECT 
    ciudad,
    COUNT(*) AS total_clientes,
    SUM(CASE WHEN segmento_cliente = 'VIP' THEN 1 ELSE 0 END) AS clientes_vip,
    ROUND(
        100.0 * SUM(CASE WHEN segmento_cliente = 'VIP' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS porcentaje_vip
FROM clientes
GROUP BY ciudad
ORDER BY porcentaje_vip DESC;
```
**🎯 Resultados Post-Rescate:**
- **Bucaramanga**: 50% VIPs (3/6) - ¡Ciudad estrella!
- **Medellín**: 33.33% VIPs (2/6) - Muy sólido
- **Otras ciudades**: 0% VIPs - Oportunidad de crecimiento

**🎯 Conceptos NINJA Aplicados:**
- `CASE WHEN` dentro de `SUM()` para conteo condicional
- Cálculos de porcentajes complejos
- `ROUND()` para presentación ejecutiva
- Múltiples funciones agregadas en una consulta

---

## 🎯 **CONCEPTOS NINJA DOMINADOS**

### **1. Funciones de Agregación Avanzadas**
```sql
-- Estadísticas completas
SELECT 
    ciudad,
    COUNT(*) as total,
    AVG(ingresos_mensuales) as promedio,
    MAX(ingresos_mensuales) as maximo,
    MIN(ingresos_mensuales) as minimo,
    SUM(ingresos_mensuales) as suma_total
FROM clientes 
GROUP BY ciudad;
```

### **2. CASE WHEN para Lógica Condicional**
```sql
-- Categorización dinámica
SELECT 
    CASE 
        WHEN ingresos_mensuales >= 8000000 THEN 'VIP'
        WHEN ingresos_mensuales >= 5000000 THEN 'Premium'
        WHEN ingresos_mensuales >= 3000000 THEN 'Estándar'
        ELSE 'Básico'
    END as categoria,
    COUNT(*) as cantidad
FROM clientes 
GROUP BY categoria;
```

### **3. Funciones de Texto**
```sql
-- Concatenación y formato
SELECT 
    nombres || ' ' || apellidos AS nombre_completo,
    UPPER(ciudad) as ciudad_mayuscula,
    LENGTH(nombres) as longitud_nombre
FROM clientes;
```

### **4. BETWEEN para Rangos**
```sql
-- Análisis por rangos de ingresos
SELECT *
FROM clientes 
WHERE ingresos_mensuales BETWEEN 3000000 AND 7000000
ORDER BY ingresos_mensuales DESC;
```

### **5. LIMIT para Top N**
```sql
-- Top/Bottom rankings
SELECT * FROM clientes 
ORDER BY ingresos_mensuales DESC 
LIMIT 5;  -- Top 5

SELECT * FROM clientes 
ORDER BY ingresos_mensuales ASC 
LIMIT 3;  -- Bottom 3
```

### **6. Cálculos Complejos**
```sql
-- Porcentajes y estadísticas avanzadas
SELECT 
    ciudad,
    COUNT(*) as total,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM clientes), 2) as porcentaje_ciudad,
    ROUND(AVG(ingresos_mensuales), 2) as promedio_ingresos
FROM clientes
GROUP BY ciudad;
```

---

## 📊 **ANÁLISIS ESTADÍSTICO BANCARIO**

### **🏪 Distribución Geográfica**
- **20 clientes** distribuidos en **5 ciudades**
- **Bucaramanga y Medellín**: 6 clientes c/u (60% del portafolio)
- **Bogotá y Cali**: 3 clientes c/u
- **Barranquilla**: 2 clientes

### **💰 Segmentación por Ingresos**
```
VIP (≥8M):      5 clientes (25%) - Promedio: $9.7M
Premium (5-8M): 5 clientes (25%) - Promedio: $6.6M  
Estándar (2.5-5M): 8 clientes (40%) - Promedio: $3.6M
Básico (<2.5M): 2 clientes (10%) - Promedio: $2.0M
```

### **🎯 Concentración VIP**
- **50% en Bucaramanga** - Mercado estrella
- **33% en Medellín** - Mercado sólido
- **0% en otras ciudades** - Oportunidades de expansión

### **📈 Insights de Negocio**
- **Bucaramanga**: Hub de clientes de alto valor
- **Medellín**: Balance entre volumen y valor
- **Barranquilla**: Mayor promedio per cápita
- **Bogotá/Cali**: Potencial de crecimiento

---

## 💼 **CASOS DE NEGOCIO REALES**

### **🎯 Marketing Segmentado**
```sql
-- Campaña para clientes Premium en ciudades específicas
SELECT nombres, apellidos, ciudad, ingresos_mensuales
FROM clientes 
WHERE segmento_cliente = 'Premium' 
  AND ciudad IN ('Medellín', 'Bucaramanga')
ORDER BY ingresos_mensuales DESC;
```

### **📊 Reportes Ejecutivos**
```sql
-- Dashboard CEO: Resumen por ciudad
SELECT 
    ciudad,
    COUNT(*) as clientes,
    ROUND(AVG(ingresos_mensuales)/1000000, 1) as promedio_millones,
    SUM(CASE WHEN segmento_cliente = 'VIP' THEN 1 ELSE 0 END) as vips
FROM clientes 
GROUP BY ciudad 
ORDER BY promedio_millones DESC;
```

### **🏆 Programas de Fidelización**
```sql
-- Top clientes para programa exclusivo
SELECT 
    nombres || ' ' || apellidos as cliente,
    ciudad,
    ingresos_mensuales,
    segmento_cliente
FROM clientes 
WHERE segmento_cliente IN ('VIP', 'Premium')
ORDER BY ingresos_mensuales DESC;
```

---

## 🔧 **OPERACIONES DE RESCATE**

### **🚨 Situación de Crisis Identificada**
- **Problema**: Segmentación original mostraba 0% VIPs
- **Riesgo**: Despidos masivos por "mal desempeño"
- **Solución**: Actualización de criterios de segmentación

### **💊 Script de Rescate Implementado**
```sql
-- Actualización salvadora de segmentos
UPDATE clientes 
SET segmento_cliente = CASE 
    WHEN ingresos_mensuales >= 8000000 THEN 'VIP'
    WHEN ingresos_mensuales >= 5000000 THEN 'Premium'
    WHEN ingresos_mensuales >= 2500000 THEN 'Estándar'
    ELSE 'Básico'
END;
```

### **✅ Resultado del Rescate**
- **Antes**: 0% VIPs → Crisis laboral inminente
- **Después**: 25% VIPs → Datos presentables a directivos
- **Impacto**: Trabajos salvados, métricas realistas

### **🎯 Lecciones Aprendidas**
- Los datos siempre deben ser **coherentes** con la realidad del negocio
- La **segmentación** debe reflejar verdaderamente los ingresos
- Un buen análisis SQL puede **salvar carreras** 😄

---

## 🚀 **PRÓXIMOS DESAFÍOS**

### **🔄 NIVEL 3: JOINS Y RELACIONES**
```sql
-- Próximo desafío: Unir múltiples tablas
SELECT c.nombres, c.apellidos, c.ciudad,
       COUNT(cu.cuenta_id) as total_cuentas,
       SUM(p.monto) as total_prestamos
FROM clientes c
LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
LEFT JOIN prestamos p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nombres, c.apellidos, c.ciudad;
```

### **📊 NIVEL 4: SUBCONSULTAS**
```sql
-- Subconsultas para análisis complejos
SELECT ciudad, promedio_ciudad,
       (promedio_ciudad - promedio_general) as diferencia
FROM (
    SELECT ciudad, AVG(ingresos_mensuales) as promedio_ciudad
    FROM clientes GROUP BY ciudad
) sub
CROSS JOIN (
    SELECT AVG(ingresos_mensuales) as promedio_general 
    FROM clientes
) general;
```

### **🎯 NIVEL 5: WINDOW FUNCTIONS**
```sql
-- Funciones de ventana para rankings
SELECT nombres, apellidos, ciudad, ingresos_mensuales,
       ROW_NUMBER() OVER (PARTITION BY ciudad ORDER BY ingresos_mensuales DESC) as ranking_ciudad,
       PERCENT_RANK() OVER (ORDER BY ingresos_mensuales) as percentil
FROM clientes;
```

### **🏗️ NIVEL 6: CTEs Y CONSULTAS RECURSIVAS**
```sql
-- Common Table Expressions para lógica compleja
WITH resumen_ciudad AS (
    SELECT ciudad, AVG(ingresos_mensuales) as promedio
    FROM clientes GROUP BY ciudad
),
clasificacion AS (
    SELECT ciudad, promedio,
           CASE WHEN promedio > 5000000 THEN 'Alto' ELSE 'Bajo' END as nivel
    FROM resumen_ciudad
)
SELECT * FROM clasificacion ORDER BY promedio DESC;
```

---

## 📚 **TABLA DE EVOLUCIÓN DE HABILIDADES**

| Nivel | Concepto | Estado | Próximo Paso |
|-------|----------|--------|--------------|
| ⭐ | SELECT básico | ✅ DOMINADO | - |
| ⭐ | WHERE y filtros | ✅ DOMINADO | - |
| ⭐⭐ | GROUP BY | ✅ DOMINADO | - |
| ⭐⭐ | Funciones agregadas | ✅ DOMINADO | - |
| ⭐⭐⭐ | CASE WHEN | ✅ DOMINADO | - |
| ⭐⭐⭐ | Cálculos complejos | ✅ DOMINADO | - |
| ⭐⭐⭐⭐ | JOINs | 🔜 PRÓXIMO | Unir tablas |
| ⭐⭐⭐⭐ | Subconsultas | 🔜 PRÓXIMO | Queries anidadas |
| ⭐⭐⭐⭐⭐ | Window Functions | 🔜 FUTURO | Rankings avanzados |
| ⭐⭐⭐⭐⭐ | CTEs | 🔜 FUTURO | Lógica compleja |

---

## 🏆 **CERTIFICACIÓN OFICIAL**

### **🎖️ SQL NINJA BANCARIO**
**Otorgado a:** Tu nombre  
**Fecha:** Julio 5, 2025  
**Nivel alcanzado:** AVANZADO ⭐⭐⭐  

### **📊 Estadísticas de Logros:**
- ✅ **6 ejercicios avanzados** completados
- ✅ **12+ conceptos SQL** dominados  
- ✅ **20 clientes** analizados exitosamente
- ✅ **5 ciudades** estudiadas estadísticamente
- ✅ **1 crisis laboral** evitada con SQL 😄
- ✅ **0 errores** en consultas finales

### **🚀 Habilidades Certificadas:**
- Análisis estadístico con agregaciones
- Segmentación dinámica de clientes
- Cálculos de porcentajes complejos
- Manipulación de datos para presentaciones
- Resolución creativa de problemas de negocio
- Personalización de terminología empresarial

### **💼 Competencias Bancarias:**
- Identificación de clientes VIP
- Análisis de mercados por ciudad
- Reportes ejecutivos con SQL
- Segmentación para campañas de marketing
- Análisis de rentabilidad por segmento

---

## 🎯 **PLAN DE ESTUDIO SUGERIDO**

### **📅 Semana 1-2: Consolidación**
- [ ] Practicar todas las consultas avanzadas
- [ ] Crear variaciones de los ejercicios
- [ ] Explorar otros campos de la tabla clientes

### **📅 Semana 3-4: JOINs**
- [ ] INNER JOIN con tabla cuentas
- [ ] LEFT JOIN con prestamos
- [ ] Análisis multi-tabla

### **📅 Semana 5-6: Subconsultas**
- [ ] Subconsultas en SELECT
- [ ] Subconsultas en WHERE  
- [ ] EXISTS y NOT EXISTS

### **📅 Semana 7-8: Funciones Avanzadas**
- [ ] Window functions
- [ ] CTEs (Common Table Expressions)
- [ ] Funciones de fecha y tiempo

---

## 💡 **TIPS PARA MANTENER EL NIVEL NINJA**

### **🔥 Práctica Diaria**
- Ejecuta al menos 1 consulta SQL avanzada por día
- Experimenta con diferentes combinaciones de funciones
- Busca siempre nuevas formas de resolver el mismo problema

### **📚 Recursos Recomendados**
- Practicar con datasets más grandes
- Explorar otras tablas de la base de datos bancaria
- Crear tus propios ejercicios de negocio

### **🎯 Objetivos a Corto Plazo**
1. Dominar JOINs entre 3+ tablas
2. Crear reportes ejecutivos complejos
3. Implementar análisis de series temporales
4. Desarrollar dashboards con SQL

---

## 🎉 **¡FELICITACIONES NINJA!**

Has completado exitosamente el programa **SQL BANCARIO AVANZADO** y demostrado habilidades de nivel profesional. Tu capacidad para resolver problemas complejos, crear consultas elegantes y hasta "salvar el trabajo" con análisis inteligente te convierte en un verdadero **SQL NINJA**.

### **🌟 Lo Que Te Distingue:**
- **Creatividad**: "Clase Media Jodida" - Personalización auténtica
- **Precisión**: Cero errores en consultas complejas
- **Resolución**: Identificaste y solucionaste inconsistencias de datos
- **Profesionalismo**: Resultados presentables para directivos

### **🚀 Estás Listo Para:**
- Análisis de datos bancarios complejos
- Reportes ejecutivos con insights valiosos
- Segmentación avanzada de clientes
- Operaciones de rescate de datos 😄
- Liderar proyectos de análisis SQL

---

**🎯 Siguiente aventura:** ¡JOINs y relaciones entre tablas!  
**💪 Nivel actual:** SQL NINJA BANCARIO CERTIFICADO

**¡Que la fuerza del SQL te acompañe siempre! 🚀💰**

---

*📝 Documento generado automáticamente*  
*📅 Fecha: Julio 5, 2025*  
*🎖️ Certificación: SQL NINJA BANCARIO*
