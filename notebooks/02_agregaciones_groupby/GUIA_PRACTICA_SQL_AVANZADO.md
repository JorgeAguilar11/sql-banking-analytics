# 🎯 Guía Práctica: SQL Avanzado con Agregaciones Bancarias

## 📋 **Introducción**
Esta guía práctica te acompañará paso a paso para dominar las agregaciones SQL en el contexto bancario. Cada sección incluye ejercicios progresivos, casos reales y validaciones.

---

## 🛠️ **Configuración Inicial**

### **📁 Estructura de Trabajo**
```
notebooks/02_agregaciones_groupby/
├── agregaciones_groupby_bancario.ipynb    # Tutorial principal
├── GUIA_TEORIA_AGREGACIONES.md           # Base teórica
├── GUIA_PRACTICA_SQL_AVANZADO.md         # Esta guía práctica
├── EJERCICIOS_PRACTICOS.md               # Retos adicionales
├── practica_sql_avanzada.py              # Scripts automatizados
└── README.md                             # Navegación del módulo
```

### **🚀 Preparación del Entorno**
```bash
# 1. Activar entorno virtual
source ../../venv_banking_sql/bin/activate

# 2. Verificar base de datos
ls -la ../../data/banking_core.db

# 3. Abrir notebook principal
jupyter notebook agregaciones_groupby_bancario.ipynb
```

---

## 🔢 **Nivel 1: Funciones de Agregación Básicas**

### **🎯 Objetivo**: Dominar COUNT, SUM, AVG, MAX, MIN

### **Ejercicio 1.1: Explorando Conteos**
```sql
-- Práctica básica con COUNT
SELECT COUNT(*) as total_registros FROM clientes;
SELECT COUNT(DISTINCT segmento_cliente) as segmentos_unicos FROM clientes;
SELECT COUNT(ingresos_mensuales) as clientes_con_ingresos FROM clientes;
```

**💡 Punto clave**: `COUNT(*)` cuenta todas las filas, `COUNT(columna)` excluye NULLs.

### **Ejercicio 1.2: Sumando Valores Monetarios**
```sql
-- Saldos totales por estado de cuenta
SELECT 
    estado,
    COUNT(*) as numero_cuentas,
    SUM(saldo_actual) as saldo_total,
    SUM(CASE WHEN saldo_actual > 1000000 THEN saldo_actual ELSE 0 END) as saldo_premium
FROM cuentas
GROUP BY estado;
```

**🎯 Validación**: El saldo total debe cuadrar con la suma de todos los saldos individuales.

### **Ejercicio 1.3: Calculando Promedios Inteligentes**
```sql
-- Promedios por segmento con análisis de dispersión
SELECT 
    segmento_cliente,
    COUNT(*) as cantidad_clientes,
    AVG(ingresos_mensuales) as ingreso_promedio,
    MIN(ingresos_mensuales) as ingreso_minimo,
    MAX(ingresos_mensuales) as ingreso_maximo,
    MAX(ingresos_mensuales) - MIN(ingresos_mensuales) as rango_ingresos
FROM clientes
WHERE estado = 'ACTIVO' AND ingresos_mensuales IS NOT NULL
GROUP BY segmento_cliente
ORDER BY ingreso_promedio DESC;
```

**📊 Insight**: Un rango amplio indica mayor heterogeneidad en el segmento.

---

## 📈 **Nivel 2: GROUP BY Progresivo**

### **🎯 Objetivo**: Agrupar datos para generar insights de negocio

### **Ejercicio 2.1: Agrupación Simple con Ranking**
```sql
-- Top productos por número de cuentas
SELECT 
    pf.categoria,
    pf.nombre_producto,
    COUNT(c.cuenta_id) as total_cuentas,
    RANK() OVER (ORDER BY COUNT(c.cuenta_id) DESC) as ranking_popularidad
FROM productos_financieros pf
LEFT JOIN cuentas c ON pf.producto_id = c.producto_id AND c.estado = 'ACTIVA'
GROUP BY pf.categoria, pf.nombre_producto
ORDER BY total_cuentas DESC;
```

**💼 Aplicación**: Identifica productos estrella y oportunidades de mejora.

### **Ejercicio 2.2: Agrupación Múltiple con Subtotales**
```sql
-- Análisis por segmento y categoría de producto
SELECT 
    COALESCE(cl.segmento_cliente, 'TOTAL GENERAL') as segmento,
    COALESCE(pf.categoria, 'TOTAL SEGMENTO') as categoria_producto,
    COUNT(DISTINCT cl.cliente_id) as clientes_unicos,
    COUNT(c.cuenta_id) as total_cuentas,
    SUM(c.saldo_actual) as saldo_total,
    AVG(c.saldo_actual) as saldo_promedio
FROM clientes cl
JOIN cuentas c ON cl.cliente_id = c.cliente_id
JOIN productos_financieros pf ON c.producto_id = pf.producto_id
WHERE cl.estado = 'ACTIVO' AND c.estado = 'ACTIVA'
GROUP BY ROLLUP(cl.segmento_cliente, pf.categoria)
ORDER BY segmento, categoria_producto;
```

**🔍 Nota**: `ROLLUP` genera subtotales automáticamente.

### **Ejercicio 2.3: Segmentación Dinámica**
```sql
-- Crear segmentos por comportamiento de saldo
SELECT 
    CASE 
        WHEN AVG(saldo_actual) < 500000 THEN 'Básico'
        WHEN AVG(saldo_actual) < 2000000 THEN 'Intermedio'
        WHEN AVG(saldo_actual) < 5000000 THEN 'Premium'
        ELSE 'VIP'
    END as segmento_comportamiento,
    COUNT(DISTINCT cliente_id) as cantidad_clientes,
    MIN(AVG(saldo_actual)) as saldo_min_promedio,
    MAX(AVG(saldo_actual)) as saldo_max_promedio
FROM (
    SELECT 
        cl.cliente_id,
        AVG(c.saldo_actual) as saldo_actual
    FROM clientes cl
    JOIN cuentas c ON cl.cliente_id = c.cliente_id
    WHERE cl.estado = 'ACTIVO' AND c.estado = 'ACTIVA'
    GROUP BY cl.cliente_id
) cliente_promedio
GROUP BY segmento_comportamiento
ORDER BY saldo_min_promedio;
```

**🎯 Insight**: Segmentación basada en comportamiento real vs. datos demográficos.

---

## 🔍 **Nivel 3: HAVING Estratégico**

### **🎯 Objetivo**: Filtrar grupos para identificar patrones críticos

### **Ejercicio 3.1: Identificando Outliers**
```sql
-- Clientes con comportamiento atípico
SELECT 
    cl.cliente_id,
    cl.nombre || ' ' || cl.apellidos as nombre_completo,
    cl.segmento_cliente,
    COUNT(c.cuenta_id) as numero_cuentas,
    SUM(c.saldo_actual) as saldo_total_cliente,
    AVG(c.saldo_actual) as saldo_promedio_cliente
FROM clientes cl
JOIN cuentas c ON cl.cliente_id = c.cliente_id
WHERE cl.estado = 'ACTIVO' AND c.estado = 'ACTIVA'
GROUP BY cl.cliente_id, cl.nombre, cl.apellidos, cl.segmento_cliente
HAVING COUNT(c.cuenta_id) > 5  -- Más de 5 cuentas
   OR SUM(c.saldo_actual) > 50000000  -- Saldo total > $50M
   OR (COUNT(c.cuenta_id) = 1 AND SUM(c.saldo_actual) > 10000000)  -- Cuenta única con > $10M
ORDER BY saldo_total_cliente DESC;
```

**⚠️ Objetivo**: Identificar clientes que requieren atención especial.

### **Ejercicio 3.2: Alertas de Concentración**
```sql
-- Productos con alta concentración de riesgo
SELECT 
    pf.categoria,
    pf.nombre_producto,
    COUNT(c.cuenta_id) as numero_cuentas,
    SUM(c.saldo_actual) as saldo_total,
    AVG(c.saldo_actual) as saldo_promedio,
    MAX(c.saldo_actual) as saldo_maximo,
    ROUND(MAX(c.saldo_actual) * 100.0 / SUM(c.saldo_actual), 2) as concentracion_max_cliente
FROM productos_financieros pf
JOIN cuentas c ON pf.producto_id = c.producto_id
WHERE c.estado = 'ACTIVA'
GROUP BY pf.categoria, pf.nombre_producto
HAVING COUNT(c.cuenta_id) >= 10  -- Productos significativos
   AND MAX(c.saldo_actual) * 100.0 / SUM(c.saldo_actual) > 25  -- Concentración > 25%
ORDER BY concentracion_max_cliente DESC;
```

**📊 KPI**: Concentración alta indica riesgo de dependencia de un cliente.

### **Ejercicio 3.3: Análisis de Crecimiento**
```sql
-- Productos con crecimiento acelerado (últimos 6 meses)
SELECT 
    pf.categoria,
    COUNT(c.cuenta_id) as cuentas_nuevas,
    SUM(c.saldo_actual) as saldo_total_nuevas,
    AVG(c.saldo_actual) as saldo_promedio_nuevas
FROM productos_financieros pf
JOIN cuentas c ON pf.producto_id = c.producto_id
WHERE c.estado = 'ACTIVA' 
  AND c.fecha_apertura >= date('now', '-6 months')
GROUP BY pf.categoria
HAVING COUNT(c.cuenta_id) > 20  -- Al menos 20 cuentas nuevas
   AND AVG(c.saldo_actual) > 1000000  -- Saldo promedio > $1M
ORDER BY cuentas_nuevas DESC;
```

**📈 Objetivo**: Identificar productos con momentum positivo.

---

## 💼 **Nivel 4: KPIs Bancarios Avanzados**

### **🎯 Objetivo**: Crear métricas de negocio estratégicas

### **Ejercicio 4.1: Índice de Penetración de Productos**
```sql
-- Calculando penetración de cada producto en la base de clientes
WITH clientes_activos AS (
    SELECT COUNT(*) as total_clientes FROM clientes WHERE estado = 'ACTIVO'
),
penetracion_productos AS (
    SELECT 
        pf.categoria,
        pf.nombre_producto,
        COUNT(DISTINCT c.cliente_id) as clientes_con_producto,
        ca.total_clientes,
        ROUND(COUNT(DISTINCT c.cliente_id) * 100.0 / ca.total_clientes, 2) as penetracion_porcentaje
    FROM productos_financieros pf
    LEFT JOIN cuentas c ON pf.producto_id = c.producto_id AND c.estado = 'ACTIVA'
    CROSS JOIN clientes_activos ca
    GROUP BY pf.categoria, pf.nombre_producto, ca.total_clientes
)
SELECT 
    categoria,
    nombre_producto,
    clientes_con_producto,
    total_clientes,
    penetracion_porcentaje,
    CASE 
        WHEN penetracion_porcentaje > 50 THEN 'Alto'
        WHEN penetracion_porcentaje > 20 THEN 'Medio'
        ELSE 'Bajo'
    END as nivel_penetracion
FROM penetracion_productos
ORDER BY penetracion_porcentaje DESC;
```

**💡 Insight**: Alta penetración = producto exitoso, baja = oportunidad de crecimiento.

### **Ejercicio 4.2: Análisis de Valor del Cliente (CLV)**
```sql
-- Calculando el valor de vida del cliente por segmento
SELECT 
    cl.segmento_cliente,
    COUNT(DISTINCT cl.cliente_id) as total_clientes,
    SUM(c.saldo_actual) as valor_total_segmento,
    AVG(c.saldo_actual) as valor_promedio_por_cuenta,
    SUM(c.saldo_actual) / COUNT(DISTINCT cl.cliente_id) as valor_promedio_por_cliente,
    COUNT(c.cuenta_id) / COUNT(DISTINCT cl.cliente_id) as cuentas_promedio_por_cliente,
    -- Estimación de valor anual (asumiendo 2% comisión)
    ROUND(SUM(c.saldo_actual) * 0.02, 2) as ingresos_estimados_anuales
FROM clientes cl
LEFT JOIN cuentas c ON cl.cliente_id = c.cliente_id AND c.estado = 'ACTIVA'
WHERE cl.estado = 'ACTIVO'
GROUP BY cl.segmento_cliente
ORDER BY valor_promedio_por_cliente DESC;
```

**💰 Objetivo**: Priorizar esfuerzos de retención y adquisición.

### **Ejercicio 4.3: Matriz de Productos (Boston Consulting Group)**
```sql
-- Clasificación de productos: Estrellas, Vacas lecheras, Interrogantes, Perros
WITH metricas_productos AS (
    SELECT 
        pf.categoria,
        pf.nombre_producto,
        COUNT(c.cuenta_id) as numero_cuentas,
        SUM(c.saldo_actual) as saldo_total,
        AVG(c.saldo_actual) as saldo_promedio,
        -- Crecimiento (cuentas últimos 6 meses vs total)
        COUNT(CASE WHEN c.fecha_apertura >= date('now', '-6 months') THEN 1 END) * 100.0 / 
        NULLIF(COUNT(c.cuenta_id), 0) as tasa_crecimiento_6m
    FROM productos_financieros pf
    LEFT JOIN cuentas c ON pf.producto_id = c.producto_id AND c.estado = 'ACTIVA'
    GROUP BY pf.categoria, pf.nombre_producto
),
clasificacion AS (
    SELECT *,
        -- Cuadrantes BCG
        CASE 
            WHEN saldo_total > (SELECT AVG(saldo_total) FROM metricas_productos) 
             AND tasa_crecimiento_6m > (SELECT AVG(tasa_crecimiento_6m) FROM metricas_productos) 
            THEN '⭐ Estrella'
            WHEN saldo_total > (SELECT AVG(saldo_total) FROM metricas_productos) 
             AND tasa_crecimiento_6m <= (SELECT AVG(tasa_crecimiento_6m) FROM metricas_productos) 
            THEN '🐄 Vaca Lechera'
            WHEN saldo_total <= (SELECT AVG(saldo_total) FROM metricas_productos) 
             AND tasa_crecimiento_6m > (SELECT AVG(tasa_crecimiento_6m) FROM metricas_productos) 
            THEN '❓ Interrogante'
            ELSE '🐕 Perro'
        END as clasificacion_bcg
    FROM metricas_productos
    WHERE numero_cuentas > 0
)
SELECT 
    clasificacion_bcg,
    COUNT(*) as cantidad_productos,
    SUM(saldo_total) as saldo_total_categoria,
    AVG(tasa_crecimiento_6m) as crecimiento_promedio
FROM clasificacion
GROUP BY clasificacion_bcg
ORDER BY saldo_total_categoria DESC;
```

**🎯 Estrategia**: 
- ⭐ Estrellas: Invertir más
- 🐄 Vacas lecheras: Mantener y optimizar
- ❓ Interrogantes: Evaluar potencial
- 🐕 Perros: Considerar descontinuar

---

## 📅 **Nivel 5: Análisis Temporal Avanzado**

### **🎯 Objetivo**: Identificar tendencias y estacionalidad

### **Ejercicio 5.1: Análisis de Tendencia Mensual**
```sql
-- Evolución mensual de apertura de cuentas y saldos
SELECT 
    strftime('%Y', fecha_apertura) as año,
    strftime('%m', fecha_apertura) as mes,
    COUNT(*) as cuentas_abiertas,
    SUM(saldo_actual) as saldo_inicial_total,
    AVG(saldo_actual) as saldo_inicial_promedio,
    -- Comparación con mes anterior
    LAG(COUNT(*)) OVER (ORDER BY strftime('%Y-%m', fecha_apertura)) as cuentas_mes_anterior,
    COUNT(*) - LAG(COUNT(*)) OVER (ORDER BY strftime('%Y-%m', fecha_apertura)) as variacion_cuentas
FROM cuentas
WHERE fecha_apertura >= date('now', '-24 months')
  AND fecha_apertura IS NOT NULL
GROUP BY strftime('%Y', fecha_apertura), strftime('%m', fecha_apertura)
ORDER BY año DESC, mes DESC;
```

**📈 Insight**: Identifica estacionalidad y tendencias de crecimiento.

### **Ejercicio 5.2: Cohorte de Clientes por Período de Ingreso**
```sql
-- Análisis de retención por cohorte de ingreso
WITH cohortes AS (
    SELECT 
        strftime('%Y-%m', fecha_registro) as periodo_ingreso,
        COUNT(DISTINCT cliente_id) as clientes_iniciales,
        COUNT(DISTINCT CASE WHEN estado = 'ACTIVO' THEN cliente_id END) as clientes_activos_actuales,
        ROUND(COUNT(DISTINCT CASE WHEN estado = 'ACTIVO' THEN cliente_id END) * 100.0 / 
              COUNT(DISTINCT cliente_id), 2) as tasa_retencion
    FROM clientes
    WHERE fecha_registro >= date('now', '-36 months')
    GROUP BY strftime('%Y-%m', fecha_registro)
),
con_saldos AS (
    SELECT 
        c.*,
        COALESCE(SUM(cu.saldo_actual), 0) as saldo_total_cohorte,
        COALESCE(AVG(cu.saldo_actual), 0) as saldo_promedio_cohorte
    FROM cohortes c
    LEFT JOIN clientes cl ON strftime('%Y-%m', cl.fecha_registro) = c.periodo_ingreso AND cl.estado = 'ACTIVO'
    LEFT JOIN cuentas cu ON cl.cliente_id = cu.cliente_id AND cu.estado = 'ACTIVA'
    GROUP BY c.periodo_ingreso, c.clientes_iniciales, c.clientes_activos_actuales, c.tasa_retencion
)
SELECT 
    periodo_ingreso,
    clientes_iniciales,
    clientes_activos_actuales,
    tasa_retencion,
    saldo_total_cohorte,
    saldo_promedio_cohorte,
    CASE 
        WHEN tasa_retencion > 80 THEN '🟢 Excelente'
        WHEN tasa_retencion > 60 THEN '🟡 Buena'
        WHEN tasa_retencion > 40 THEN '🟠 Regular'
        ELSE '🔴 Deficiente'
    END as evaluacion_retencion
FROM con_saldos
ORDER BY periodo_ingreso DESC;
```

**🔄 Objetivo**: Medir la efectividad de estrategias de retención.

---

## 🎯 **EJERCICIOS COMPLETADOS - TUS LOGROS**

### **✅ Resumen de Tu Progreso**
Has completado exitosamente **6 ejercicios avanzados** (7-12) con consultas SQL profesionales. Aquí están documentadas todas tus soluciones con resultados reales:

---

### **💰 EJERCICIO 7: Promedio de Ingresos por Ciudad** ✅
**🎯 Objetivo**: Calcular el promedio de ingresos por ciudad usando `AVG()`

```sql
SELECT 
    ciudad,
    COUNT(*) AS total_clientes,
    AVG(ingresos_mensuales) AS promedio_ingresos
FROM 
    clientes
WHERE 
    ingresos_mensuales IS NOT NULL
GROUP BY 
    ciudad
ORDER BY 
    promedio_ingresos DESC;
```

**📊 Resultados Obtenidos**:
- **Barranquilla**: 2 clientes, promedio $6,468,453
- **Bucaramanga**: 6 clientes, promedio $6,445,098  
- **Medellín**: 6 clientes, promedio $6,413,412
- **Bogotá**: 3 clientes, promedio $4,751,162
- **Cali**: 3 clientes, promedio $3,338,088

**📝 Conceptos Aplicados**:
- ✅ Función `AVG()` para calcular promedios
- ✅ Combinación de `COUNT()` y `AVG()` en una consulta
- ✅ Manejo de valores NULL con `WHERE IS NOT NULL`
- ✅ Ordenamiento por promedio descendente

---

### **🏆 EJERCICIO 8: Top 3 Clientes Más Ricos** ✅
**🎯 Objetivo**: Identificar los 3 clientes con mayores ingresos usando `LIMIT`

```sql
SELECT 
    nombres || ' ' || apellidos AS nombre_completo,
    ingresos_mensuales,
    ciudad
FROM clientes 
ORDER BY ingresos_mensuales DESC
LIMIT 3;
```

**📊 Resultados Obtenidos**:
1. **Isabella Jiménez** (Bucaramanga) - $11,060,983
2. **Pedro Morales** (Medellín) - $10,330,811
3. **Sofia Rivera** (Bucaramanga) - $9,834,891

**📝 Conceptos Aplicados**:
- ✅ Concatenación de campos con `||`
- ✅ Uso de `LIMIT` para Top N consultas
- ✅ Identificación de clientes VIP
- ✅ Ordenamiento para rankings

---

### **🏠 EJERCICIO 9: Clientes de Clase Media** ✅
**🎯 Objetivo**: Filtrar clientes con ingresos entre 3M-7M usando `BETWEEN`

```sql
SELECT 
    cliente_id,
    nombres,
    apellidos,
    ciudad,
    ingresos_mensuales
FROM 
    clientes
WHERE 
    ingresos_mensuales BETWEEN 3000000 AND 7000000
ORDER BY 
    ingresos_mensuales DESC;
```

**📊 Resultados Obtenidos**:
- **Total encontrados**: 10 clientes (50% del total)
- **Rango de ingresos**: $3,058,931 - $6,377,879
- **Ciudad líder**: Medellín y Bogotá con 3 clientes cada una

**📝 Conceptos Aplicados**:
- ✅ Operador `BETWEEN` para rangos numéricos
- ✅ Segmentación de clientes por ingresos
- ✅ Análisis de clase media bancaria
- ✅ Filtrado por criterios de negocio

---

### **📊 EJERCICIO 10: Distribución por Segmentos** ✅
**🎯 Objetivo**: Contar clientes por cada segmento usando `GROUP BY`

```sql
SELECT 
    segmento_cliente,
    COUNT(*) AS cantidad_clientes
FROM 
    clientes
WHERE 
    segmento_cliente IS NOT NULL
GROUP BY 
    segmento_cliente
ORDER BY 
    cantidad_clientes DESC;
```

**📊 Resultados Obtenidos**:
- **Estándar**: 8 clientes (40%)
- **VIP**: 5 clientes (25%)  
- **Premium**: 5 clientes (25%)
- **Básico**: 2 clientes (10%)

**📝 Conceptos Aplicados**:
- ✅ Análisis de distribución de segmentos
- ✅ Agrupación por categorías de clientes
- ✅ Estrategia de marketing por segmentos
- ✅ Filtrado de valores NULL

---

### **🏅 EJERCICIO 11: Ciudad con Mayor Suma Total** ✅
**🎯 Objetivo**: Encontrar la ciudad más valiosa usando `SUM()` y `LIMIT`

```sql
SELECT 
    ciudad,
    SUM(ingresos_mensuales) AS ingresos_totales
FROM 
    clientes
WHERE 
    ingresos_mensuales IS NOT NULL
GROUP BY 
    ciudad
ORDER BY 
    ingresos_totales DESC
LIMIT 1;
```

**📊 Resultado Obtenido**:
- **🏆 GANADORA**: **Bucaramanga** con $38,670,590 en ingresos totales

**📝 Conceptos Aplicados**:
- ✅ Función `SUM()` para totales acumulados
- ✅ Identificación de mercados más valiosos
- ✅ Análisis territorial de ingresos
- ✅ Combinación de `SUM()`, `GROUP BY` y `LIMIT`

---

### **💎 EJERCICIO 12: Porcentaje VIP por Ciudad** ✅
**🎯 Objetivo**: Calcular porcentajes usando `CASE WHEN` avanzado

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

**📊 Resultados Obtenidos**:
- **Bucaramanga**: 6 clientes, 3 VIP (50.00%)
- **Medellín**: 6 clientes, 2 VIP (33.33%)
- **Cali**: 3 clientes, 0 VIP (0.00%)
- **Bogotá**: 3 clientes, 0 VIP (0.00%)
- **Barranquilla**: 2 clientes, 0 VIP (0.00%)

**📝 Conceptos Aplicados**:
- ✅ Expresiones condicionales `CASE WHEN`
- ✅ Cálculo de porcentajes en SQL
- ✅ Función `ROUND()` para decimales
- ✅ Análisis VIP por territorio
- ✅ Lógica condicional avanzada

---

## 🎯 **INSIGHTS CLAVE DESCUBIERTOS**

### **🏆 Principales Hallazgos**:
1. **Ciudad líder**: **Bucaramanga** domina en:
   - Mayor suma total de ingresos ($38.67M)
   - Mayor porcentaje de clientes VIP (50%)
   - Concentra 2 de los 3 clientes más ricos

2. **Segmentación de mercado**:
   - 40% de clientes son **Estándar** (mayoría)
   - 25% cada uno en **VIP** y **Premium**
   - Solo 10% en segmento **Básico**

3. **Oportunidades de negocio**:
   - **Clase media**: 50% de clientes (3M-7M) representa gran potencial
   - **Cali y Bogotá**: Sin clientes VIP, oportunidad de growth
   - **Barranquilla**: Mejor promedio por cliente pero pocos clientes

### **📊 Métricas Bancarias Calculadas**:
- **Concentración VIP**: 25% de clientes genera el mayor valor
- **Distribución territorial**: Desbalanceada, Bucaramanga concentra valor
- **Potencial de crecimiento**: Ciudades sin VIP son oportunidad

---
