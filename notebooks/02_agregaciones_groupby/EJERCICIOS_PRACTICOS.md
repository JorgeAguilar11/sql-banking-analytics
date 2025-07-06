# 💪 Ejercicios Prácticos: Agregaciones y GROUP BY

## 🎯 **Instrucciones**
Estos ejercicios te ayudarán a dominar las agregaciones en el contexto bancario. Cada ejercicio incluye:
- 🎪 **Contexto** del problema bancario
- 📋 **Requisitos** específicos
- 💡 **Pistas** para la solución
- ✅ **Validación** de resultados

---

## 🔰 **Nivel Básico**

### **Ejercicio 1: Métricas Fundamentales**
**Contexto**: El gerente general necesita un reporte básico del estado del banco.

**Requisitos**:
1. Total de clientes activos
2. Total de cuentas activas
3. Saldo total del banco
4. Saldo promedio por cuenta
5. Cliente con mayor saldo total

**Pista**: Combina varias consultas simples con agregaciones básicas.

```sql
-- Tu solución aquí:
-- Consulta 1: Clientes activos
SELECT COUNT(*) as clientes_activos FROM clientes WHERE estado = 'ACTIVO';

-- Consulta 2: Cuentas activas
-- Continúa...
```

---

### **Ejercicio 2: Análisis por Producto**
**Contexto**: El área de productos quiere evaluar el performance de cada categoría.

**Requisitos**:
1. Por cada categoría de producto mostrar:
   - Número de cuentas
   - Saldo total
   - Saldo promedio
   - Saldo máximo
   - Saldo mínimo
2. Ordenar por saldo total descendente

**Pista**: Usa JOIN entre `productos_financieros` y `cuentas`, luego GROUP BY por categoría.

```sql
-- Tu solución aquí:
SELECT 
    pf.categoria,
    -- Completa las agregaciones...
FROM productos_financieros pf
JOIN cuentas c ON pf.producto_id = c.producto_id
WHERE c.estado = 'ACTIVA'
GROUP BY pf.categoria
ORDER BY /* ¿por qué campo? */;
```

---

## 📊 **Nivel Intermedio**

### **Ejercicio 3: Segmentación de Clientes**
**Contexto**: Marketing necesita entender mejor a los clientes para campañas dirigidas.

**Requisitos**:
1. Crear segmentación por ingresos:
   - 'Básico': hasta $2,000,000
   - 'Medio': $2,000,001 - $5,000,000
   - 'Alto': más de $5,000,000
2. Para cada segmento mostrar:
   - Cantidad de clientes
   - Porcentaje del total
   - Ingreso promedio
   - Número total de cuentas
   - Saldo promedio por cliente

**Pista**: Usa CASE para crear los segmentos y subconsultas para los porcentajes.

```sql
-- Tu solución aquí:
SELECT 
    CASE 
        WHEN cl.ingresos_mensuales <= 2000000 THEN 'Básico'
        WHEN cl.ingresos_mensuales <= 5000000 THEN 'Medio'
        ELSE 'Alto'
    END as segmento_ingresos,
    -- Completa las métricas...
FROM clientes cl
LEFT JOIN cuentas c ON cl.cliente_id = c.cliente_id AND c.estado = 'ACTIVA'
WHERE cl.estado = 'ACTIVO'
GROUP BY /* ¿qué columna? */
ORDER BY /* ¿cómo ordenar? */;
```

---

### **Ejercicio 4: Análisis Temporal**
**Contexto**: La dirección quiere entender las tendencias de crecimiento del banco.

**Requisitos**:
1. Análisis mensual de los últimos 12 meses:
   - Cuentas abiertas por mes
   - Saldo inicial promedio
   - Saldo total acumulado
2. Identificar el mes con mayor crecimiento
3. Solo considerar cuentas que siguen activas

**Pista**: Usa funciones de fecha y considera usar subconsultas para validaciones.

```sql
-- Tu solución aquí:
SELECT 
    strftime('%Y-%m', fecha_apertura) as periodo,
    -- Agrega las métricas necesarias...
FROM cuentas
WHERE fecha_apertura >= date('now', '-12 months')
  AND estado = 'ACTIVA'
GROUP BY strftime('%Y-%m', fecha_apertura)
ORDER BY periodo DESC;
```

---

## 🚀 **Nivel Avanzado**

### **Ejercicio 5: Análisis de Concentración**
**Contexto**: Riesgos necesita evaluar la concentración de cartera por cliente.

**Requisitos**:
1. Identificar el top 10% de clientes por saldo total
2. Calcular qué porcentaje de la cartera representan
3. Análisis por segmento de estos top clientes
4. Usar HAVING para filtrar solo clientes con más de $1M

**Pista**: Usa ventanas deslizantes (percentiles) y múltiples agregaciones.

```sql
-- Tu solución aquí:
WITH clientes_saldos AS (
    SELECT 
        cl.cliente_id,
        cl.nombre || ' ' || cl.apellidos as nombre_completo,
        cl.segmento_cliente,
        -- ¿Qué más necesitas calcular?
    FROM clientes cl
    JOIN cuentas c ON cl.cliente_id = c.cliente_id
    WHERE cl.estado = 'ACTIVO' AND c.estado = 'ACTIVA'
    GROUP BY cl.cliente_id, cl.nombre, cl.apellidos, cl.segmento_cliente
    HAVING /* ¿qué condición? */
)
SELECT 
    -- ¿Qué campos mostrar en el resultado final?
FROM clientes_saldos
ORDER BY /* ¿cómo ordenar? */;
```

---

### **Ejercicio 6: KPI Dashboard Completo**
**Contexto**: Crear un dashboard ejecutivo con los KPIs más importantes.

**Requisitos**:
1. **Métricas Globales**:
   - Total clientes, cuentas, saldo
   - Crecimiento vs mes anterior
2. **Por Producto**:
   - Top 5 productos por saldo
   - Penetración de mercado
3. **Por Segmento**:
   - Distribución de clientes
   - Valor promedio por segmento
4. **Alertas**:
   - Productos con menos de 10 cuentas
   - Segmentos con crecimiento negativo

**Pista**: Usa múltiples CTEs y UNIONs para crear un reporte integral.

```sql
-- Tu solución aquí:
WITH metricas_globales AS (
    -- Calcular métricas globales
    SELECT 
        'GLOBAL' as tipo_metrica,
        'Total Clientes' as descripcion,
        COUNT(*) as valor
    FROM clientes 
    WHERE estado = 'ACTIVO'
    
    UNION ALL
    
    -- Agrega más métricas globales...
),
metricas_productos AS (
    -- Calcular métricas por producto
    SELECT 
        'PRODUCTO' as tipo_metrica,
        -- ¿Qué más?
),
alertas AS (
    -- Generar alertas
    SELECT 
        'ALERTA' as tipo_metrica,
        -- ¿Qué alertas incluir?
)
SELECT * FROM metricas_globales
UNION ALL
SELECT * FROM metricas_productos  
UNION ALL
SELECT * FROM alertas
ORDER BY tipo_metrica, descripcion;
```

---

## 🔍 **Ejercicios de Debugging**

### **Ejercicio 7: Encuentra el Error**
Estas consultas tienen errores comunes. Identifica y corrige cada uno:

```sql
-- Error 1: ¿Qué está mal aquí?
SELECT segmento_cliente, COUNT(*), AVG(saldo_actual)
FROM clientes
GROUP BY segmento_cliente;

-- Error 2: ¿Por qué falla esta consulta?
SELECT 
    pf.categoria, 
    c.cliente_id,
    SUM(c.saldo_actual)
FROM productos_financieros pf
JOIN cuentas c ON pf.producto_id = c.producto_id
GROUP BY pf.categoria;

-- Error 3: ¿Cuál es el problema lógico?
SELECT segmento_cliente, COUNT(*)
FROM clientes
WHERE COUNT(*) > 100
GROUP BY segmento_cliente;
```

**Respuestas**:
1. Error 1: Estás intentando hacer AVG en una columna que no está en la tabla clientes
2. Error 2: cliente_id debe estar en GROUP BY o ser eliminado del SELECT
3. Error 3: WHERE debe ser HAVING para filtros en agregaciones

---

## 🎓 **Ejercicios de Investigación**

### **Ejercicio 8: Análisis Exploratorio**
**Contexto**: Como analista, debes investigar patrones en los datos.

**Tu misión**:
1. Encuentra 3 insights interesantes usando solo agregaciones
2. Identifica posibles problemas de calidad de datos
3. Propón 3 nuevos KPIs que el banco debería monitorear

**Metodología sugerida**:
```sql
-- 1. Exploración inicial
SELECT 'clientes' as tabla, COUNT(*) as registros FROM clientes
UNION ALL
SELECT 'cuentas', COUNT(*) FROM cuentas
UNION ALL
SELECT 'productos_financieros', COUNT(*) FROM productos_financieros;

-- 2. Busca patrones inusuales
SELECT 
    segmento_cliente,
    MIN(ingresos_mensuales) as min_ingresos,
    MAX(ingresos_mensuales) as max_ingresos,
    -- ¿Hay inconsistencias?
FROM clientes
GROUP BY segmento_cliente;

-- 3. Continúa tu investigación...
```

---

## ✅ **Validación de Resultados**

### **Checklist de Validación**
Para cada ejercicio, verifica:

- [ ] **Sintaxis**: ¿La consulta ejecuta sin errores?
- [ ] **Lógica**: ¿Los resultados tienen sentido de negocio?
- [ ] **Completitud**: ¿Incluiste todos los requisitos?
- [ ] **Performance**: ¿La consulta es eficiente?
- [ ] **Legibilidad**: ¿El código es claro y está documentado?

### **Métricas de Referencia**
Usa estas métricas para validar tus resultados:

```sql
-- Consultas de validación rápida:
SELECT COUNT(*) as total_clientes FROM clientes WHERE estado = 'ACTIVO';
SELECT COUNT(*) as total_cuentas FROM cuentas WHERE estado = 'ACTIVA';
SELECT SUM(saldo_actual) as saldo_total FROM cuentas WHERE estado = 'ACTIVA';
SELECT COUNT(DISTINCT producto_id) as productos_activos FROM productos_financieros;
```

---

## 🏆 **Desafío Final**

### **Proyecto: Tu Propio Dashboard**
Crea un dashboard completo que incluya:

1. **Vista Ejecutiva** (5 métricas clave)
2. **Análisis de Productos** (performance por categoría)
3. **Segmentación de Clientes** (behavioral insights)
4. **Alertas y Recomendaciones** (accionables)
5. **Tendencias Temporales** (growth patterns)

**Entregables**:
- SQL script completo
- Documentación de cada KPI
- Interpretación de negocio
- Recomendaciones estratégicas

---

**💪 ¡Practica estos ejercicios y estarás listo para análisis bancarios complejos!**

**📚 Recursos adicionales**: 
- Revisa el notebook `agregaciones_groupby_bancario.ipynb` para ejemplos detallados
- Consulta `GUIA_TEORIA_AGREGACIONES.md` para conceptos teóricos
- Experimenta con variaciones de estas consultas para mayor dominio
