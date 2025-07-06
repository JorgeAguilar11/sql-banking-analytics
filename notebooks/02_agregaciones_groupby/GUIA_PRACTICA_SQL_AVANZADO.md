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

## 🎯 **Ejercicios de Consolidación**

### **Proyecto Final: Dashboard Ejecutivo**

Crea una vista integral que combine todos los conceptos:

```sql
-- Dashboard ejecutivo completo
WITH metricas_generales AS (
    SELECT 
        'Clientes Activos' as metrica,
        COUNT(*) as valor,
        'clientes' as unidad
    FROM clientes WHERE estado = 'ACTIVO'
    
    UNION ALL
    
    SELECT 
        'Cuentas Activas',
        COUNT(*),
        'cuentas'
    FROM cuentas WHERE estado = 'ACTIVA'
    
    UNION ALL
    
    SELECT 
        'Saldo Total',
        SUM(saldo_actual),
        'pesos'
    FROM cuentas WHERE estado = 'ACTIVA'
    
    UNION ALL
    
    SELECT 
        'Productos Activos',
        COUNT(DISTINCT pf.producto_id),
        'productos'
    FROM productos_financieros pf
    JOIN cuentas c ON pf.producto_id = c.producto_id
    WHERE c.estado = 'ACTIVA'
),
alertas AS (
    SELECT 
        'ALTA CONCENTRACIÓN' as tipo_alerta,
        pf.nombre_producto as detalle,
        ROUND(MAX(c.saldo_actual) * 100.0 / SUM(c.saldo_actual), 2) as valor_alerta
    FROM productos_financieros pf
    JOIN cuentas c ON pf.producto_id = c.producto_id
    WHERE c.estado = 'ACTIVA'
    GROUP BY pf.producto_id, pf.nombre_producto
    HAVING MAX(c.saldo_actual) * 100.0 / SUM(c.saldo_actual) > 30
)
SELECT 'MÉTRICAS GENERALES' as seccion, metrica as descripcion, valor, unidad, '' as observacion
FROM metricas_generales

UNION ALL

SELECT 'ALERTAS', tipo_alerta, valor_alerta, '%', detalle
FROM alertas
ORDER BY seccion, descripcion;
```

---

## ✅ **Checklist de Validación**

### **🎯 Dominio Básico**
- [ ] Ejecutas funciones de agregación sin errores
- [ ] Entiendes la diferencia entre COUNT(*) y COUNT(columna)
- [ ] Puedes calcular porcentajes usando subconsultas
- [ ] Manejas valores NULL en agregaciones

### **📊 Dominio Intermedio**
- [ ] Crear agrupaciones múltiples efectivas
- [ ] Usar HAVING apropiadamente
- [ ] Combinar GROUP BY con JOINs
- [ ] Interpretar resultados en contexto bancario

### **🚀 Dominio Avanzado**
- [ ] Diseñar KPIs personalizados
- [ ] Crear análisis temporales complejos
- [ ] Identificar patrones y outliers
- [ ] Proponer acciones basadas en datos

---

## 📚 **Recursos de Profundización**

### **🔗 Enlaces Útiles**
- [SQL Aggregate Functions - W3Schools](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [Advanced GROUP BY Techniques](https://modern-sql.com/feature/over)
- [Banking KPIs Best Practices](https://www.klipfolio.com/resources/kpi-examples/banking)

### **📖 Lecturas Complementarias**
- "SQL for Data Analysis" - Cathy Tanimura
- "Learning SQL" - Alan Beaulieu
- "The Data Warehouse Toolkit" - Ralph Kimball

### **🎯 Próximos Pasos**
1. Completar el notebook `agregaciones_groupby_bancario.ipynb`
2. Resolver ejercicios en `EJERCICIOS_PRACTICOS.md`
3. Practicar con `practica_sql_avanzada.py`
4. Avanzar al Módulo 3: JOINs y Relaciones

---

**🏆 ¡Domina estas técnicas y estarás listo para análisis bancarios profesionales!**
