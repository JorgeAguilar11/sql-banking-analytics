# 📊 Guía Teórica: Agregaciones y GROUP BY en Banking

## 🎯 **Introducción**

Las **agregaciones** son el corazón del análisis bancario. Permiten transformar miles de registros individuales en información estratégica para la toma de decisiones. En este módulo aprenderás a dominar GROUP BY, funciones de agregación y filtros avanzados aplicados al contexto bancario.

---

## 🧮 **1. Funciones de Agregación**

### **COUNT() - Contar registros**
```sql
-- Casos de uso bancarios:
SELECT COUNT(*) FROM clientes;                    -- Total de clientes
SELECT COUNT(DISTINCT cliente_id) FROM cuentas;  -- Clientes únicos con cuentas
SELECT COUNT(*) FILTER (WHERE estado = 'ACTIVO') FROM clientes; -- Clientes activos
```

**💡 Tip Bancario**: Usa `COUNT(DISTINCT)` para evitar contar duplicados al analizar clientes que tienen múltiples productos.

### **SUM() - Sumar valores**
```sql
-- Aplicaciones bancarias:
SELECT SUM(saldo_actual) FROM cuentas;                    -- Saldo total del banco
SELECT SUM(monto_prestamo) FROM prestamos WHERE estado = 'VIGENTE'; -- Cartera vigente
SELECT SUM(importe) FROM transacciones WHERE tipo = 'DEPOSITO';     -- Total depositado
```

**⚠️ Importante**: En banking, siempre verifica que los saldos no incluyan cuentas canceladas o suspendidas.

### **AVG() - Calcular promedios**
```sql
-- Métricas bancarias clave:
SELECT AVG(saldo_actual) FROM cuentas;           -- Saldo promedio por cuenta
SELECT AVG(ingresos_mensuales) FROM clientes;    -- Ingreso promedio de clientes
SELECT AVG(tasa_interes) FROM prestamos;         -- Tasa promedio de préstamos
```

**📊 KPI**: El saldo promedio es un indicador clave de la calidad de cartera y segmentación de clientes.

### **MAX() y MIN() - Valores extremos**
```sql
-- Análisis de extremos:
SELECT MAX(saldo_actual), MIN(saldo_actual) FROM cuentas;  -- Rango de saldos
SELECT MAX(fecha_apertura) FROM cuentas;                   -- Última cuenta abierta
SELECT MIN(tasa_interes) FROM productos_financieros;       -- Producto más competitivo
```

**🔍 Insight**: Los valores extremos ayudan a identificar outliers y oportunidades de mejora.

---

## 📈 **2. GROUP BY - Fundamentos**

### **¿Qué hace GROUP BY?**
GROUP BY **agrupa registros** que tienen valores idénticos en las columnas especificadas, permitiendo aplicar funciones de agregación a cada grupo.

```sql
-- Sintaxis básica:
SELECT columna_agrupacion, FUNCION_AGREGACION(columna)
FROM tabla
GROUP BY columna_agrupacion;
```

### **Ejemplo Bancario Básico**
```sql
-- Número de cuentas por tipo de producto:
SELECT 
    tipo_producto,
    COUNT(*) as cantidad_cuentas,
    SUM(saldo_actual) as saldo_total
FROM cuentas c
JOIN productos_financieros p ON c.producto_id = p.producto_id
GROUP BY tipo_producto;
```

**Resultado conceptual:**
```
tipo_producto    | cantidad_cuentas | saldo_total
-----------------|------------------|-------------
Ahorros         | 1,250            | $15,000,000
Corriente       | 850              | $25,000,000
Inversión       | 300              | $45,000,000
```

---

## 📊 **3. GROUP BY Avanzado**

### **Agrupación por Múltiples Columnas**
```sql
-- Análisis por segmento y región:
SELECT 
    segmento_cliente,
    region,
    COUNT(*) as clientes,
    AVG(ingresos_mensuales) as ingreso_promedio
FROM clientes
GROUP BY segmento_cliente, region
ORDER BY segmento_cliente, region;
```

**💼 Aplicación**: Ideal para análisis regionales y estrategias de marketing segmentado.

### **GROUP BY con CASE (Segmentación Dinámica)**
```sql
-- Segmentación por rango de saldos:
SELECT 
    CASE 
        WHEN saldo_actual <= 100000 THEN 'Básico'
        WHEN saldo_actual <= 1000000 THEN 'Premium'
        ELSE 'VIP'
    END as segmento_saldo,
    COUNT(*) as cantidad_cuentas,
    AVG(saldo_actual) as saldo_promedio
FROM cuentas
GROUP BY 
    CASE 
        WHEN saldo_actual <= 100000 THEN 'Básico'
        WHEN saldo_actual <= 1000000 THEN 'Premium'
        ELSE 'VIP'
    END;
```

**🎯 Beneficio**: Crea segmentaciones dinámicas sin necesidad de modificar la estructura de datos.

---

## 🔍 **4. HAVING - Filtros en Grupos**

### **WHERE vs HAVING**

| Aspecto | WHERE | HAVING |
|---------|-------|--------|
| **Cuándo se aplica** | Antes de GROUP BY | Después de GROUP BY |
| **Qué filtra** | Registros individuales | Grupos agregados |
| **Funciones permitidas** | No agregación | Funciones de agregación |

### **Ejemplo Práctico**
```sql
-- INCORRECTO: WHERE con función de agregación
SELECT segmento_cliente, COUNT(*)
FROM clientes
WHERE COUNT(*) > 100  -- ❌ Error: WHERE no puede usar funciones de agregación
GROUP BY segmento_cliente;

-- CORRECTO: HAVING con función de agregación
SELECT segmento_cliente, COUNT(*) as total_clientes
FROM clientes
GROUP BY segmento_cliente
HAVING COUNT(*) > 100;  -- ✅ Correcto: HAVING filtra grupos
```

### **HAVING en Contexto Bancario**
```sql
-- Productos con alta concentración de saldos:
SELECT 
    p.nombre_producto,
    COUNT(c.cuenta_id) as numero_cuentas,
    SUM(c.saldo_actual) as saldo_total
FROM productos_financieros p
JOIN cuentas c ON p.producto_id = c.producto_id
GROUP BY p.producto_id, p.nombre_producto
HAVING SUM(c.saldo_actual) > 10000000  -- Solo productos con >$10M
   AND COUNT(c.cuenta_id) > 50;        -- Y más de 50 cuentas
```

**🎯 Uso**: Ideal para identificar productos estratégicos y focos de atención.

---

## 💼 **5. KPIs Bancarios con Agregaciones**

### **Concentración de Cartera**
```sql
SELECT 
    categoria_producto,
    SUM(saldo_actual) as saldo_total,
    COUNT(*) as numero_cuentas,
    ROUND(SUM(saldo_actual) * 100.0 / 
          (SELECT SUM(saldo_actual) FROM cuentas), 2) as porcentaje_cartera
FROM cuentas c
JOIN productos_financieros p ON c.producto_id = p.producto_id
GROUP BY categoria_producto
ORDER BY saldo_total DESC;
```

**📊 KPI**: Mide qué porcentaje de la cartera está concentrado en cada tipo de producto.

### **Índice de Penetración de Productos**
```sql
SELECT 
    p.nombre_producto,
    COUNT(DISTINCT c.cliente_id) as clientes_con_producto,
    (SELECT COUNT(*) FROM clientes WHERE estado = 'ACTIVO') as total_clientes_activos,
    ROUND(COUNT(DISTINCT c.cliente_id) * 100.0 / 
          (SELECT COUNT(*) FROM clientes WHERE estado = 'ACTIVO'), 2) as penetracion_porcentaje
FROM productos_financieros p
LEFT JOIN cuentas c ON p.producto_id = c.producto_id AND c.estado = 'ACTIVA'
GROUP BY p.producto_id, p.nombre_producto
ORDER BY penetracion_porcentaje DESC;
```

**🎯 KPI**: Indica qué tan exitoso es cada producto en el mercado de clientes.

### **Análisis de Valor del Cliente (CLV)**
```sql
SELECT 
    cl.segmento_cliente,
    COUNT(DISTINCT cl.cliente_id) as total_clientes,
    SUM(c.saldo_actual) as valor_total_segmento,
    AVG(c.saldo_actual) as valor_promedio_por_cuenta,
    SUM(c.saldo_actual) / COUNT(DISTINCT cl.cliente_id) as valor_promedio_por_cliente
FROM clientes cl
LEFT JOIN cuentas c ON cl.cliente_id = c.cliente_id AND c.estado = 'ACTIVA'
WHERE cl.estado = 'ACTIVO'
GROUP BY cl.segmento_cliente
ORDER BY valor_promedio_por_cliente DESC;
```

**💰 KPI**: Identifica los segmentos de clientes más valiosos para el banco.

---

## 📅 **6. Análisis Temporal con GROUP BY**

### **Agrupación por Período**
```sql
-- Tendencia mensual de apertura de cuentas:
SELECT 
    EXTRACT(YEAR FROM fecha_apertura) as año,
    EXTRACT(MONTH FROM fecha_apertura) as mes,
    COUNT(*) as cuentas_abiertas,
    SUM(saldo_inicial) as saldo_inicial_total
FROM cuentas
WHERE fecha_apertura >= DATE('now', '-2 years')
GROUP BY EXTRACT(YEAR FROM fecha_apertura), EXTRACT(MONTH FROM fecha_apertura)
ORDER BY año DESC, mes DESC;
```

**📈 Insight**: Permite identificar estacionalidad y tendencias en el negocio.

### **Análisis de Cohortes Básico**
```sql
-- Análisis por año de ingreso del cliente:
SELECT 
    EXTRACT(YEAR FROM fecha_registro) as año_ingreso,
    COUNT(DISTINCT cliente_id) as clientes_ingresados,
    COUNT(DISTINCT CASE WHEN estado = 'ACTIVO' THEN cliente_id END) as clientes_activos_actuales,
    ROUND(COUNT(DISTINCT CASE WHEN estado = 'ACTIVO' THEN cliente_id END) * 100.0 / 
          COUNT(DISTINCT cliente_id), 2) as tasa_retencion
FROM clientes
GROUP BY EXTRACT(YEAR FROM fecha_registro)
ORDER BY año_ingreso;
```

**🔄 KPI**: Mide la retención de clientes a lo largo del tiempo.

---

## 🚀 **7. Mejores Prácticas**

### **Performance y Optimización**
1. **Índices**: Asegúrate de tener índices en las columnas de GROUP BY
2. **Filtros tempranos**: Usa WHERE antes de GROUP BY para reducir datos
3. **LIMIT**: Usa LIMIT en consultas exploratorias para evitar timeouts

```sql
-- Optimizado:
SELECT categoria, COUNT(*)
FROM productos_financieros
WHERE fecha_creacion >= '2023-01-01'  -- Filtro temprano
GROUP BY categoria
ORDER BY COUNT(*) DESC
LIMIT 10;  -- Limitar resultados
```

### **Legibilidad y Mantenimiento**
1. **Alias descriptivos**: Usa nombres claros para columnas calculadas
2. **Comentarios**: Documenta la lógica de negocio compleja
3. **Formato consistente**: Mantén un estilo de código uniforme

```sql
-- Bien documentado:
SELECT 
    p.categoria as categoria_producto,
    COUNT(c.cuenta_id) as total_cuentas,
    SUM(c.saldo_actual) as saldo_total,
    AVG(c.saldo_actual) as saldo_promedio,
    -- Concentración de cartera por producto
    ROUND(SUM(c.saldo_actual) * 100.0 / 
          (SELECT SUM(saldo_actual) FROM cuentas WHERE estado = 'ACTIVA'), 2) as porcentaje_cartera
FROM productos_financieros p
JOIN cuentas c ON p.producto_id = c.producto_id
WHERE c.estado = 'ACTIVA'  -- Solo cuentas activas
GROUP BY p.categoria
HAVING COUNT(c.cuenta_id) > 10  -- Solo categorías significativas
ORDER BY saldo_total DESC;
```

### **Validación de Datos**
1. **Verificar totales**: Los SUMs deben cuadrar con totales conocidos
2. **Checks de sanidad**: Validar que los promedios tengan sentido
3. **Manejo de NULLs**: Considerar valores nulos en agregaciones

```sql
-- Validación incluida:
SELECT 
    segmento_cliente,
    COUNT(*) as total_registros,
    COUNT(ingresos_mensuales) as registros_con_ingresos,  -- Excluye NULLs
    AVG(ingresos_mensuales) as ingreso_promedio,
    MIN(ingresos_mensuales) as ingreso_minimo,
    MAX(ingresos_mensuales) as ingreso_maximo,
    -- Verificar datos inconsistentes
    COUNT(CASE WHEN ingresos_mensuales < 0 THEN 1 END) as ingresos_negativos
FROM clientes
GROUP BY segmento_cliente;
```

---

## 🎓 **8. Próximos Pasos**

### **Conceptos del Módulo 3: JOINs y Relaciones**
- INNER JOIN para relaciones exactas
- LEFT/RIGHT JOIN para inclusión de datos faltantes
- Análisis complejos con múltiples tablas
- Optimización de consultas con JOINs

### **Habilidades a Desarrollar**
- Combinación de agregaciones con JOINs
- Subconsultas correlacionadas
- Window functions para análisis avanzados
- CTEs (Common Table Expressions) para consultas complejas

### **Aplicaciones Bancarias Avanzadas**
- Análisis de riesgo crediticio
- Reportes regulatorios complejos
- Modelos de scoring y segmentación
- Detección de anomalías y fraude

---

## 📚 **Recursos Adicionales**

### **Documentación SQL**
- [SQLite Functions](https://sqlite.org/lang_aggfunc.html)
- [GROUP BY Best Practices](https://mode.com/sql-tutorial/sql-group-by/)

### **Ejercicios Recomendados**
1. Crear tu propio dashboard de métricas bancarias
2. Implementar alertas basadas en agregaciones
3. Desarrollar reportes automatizados con Python + SQL

### **Casos de Estudio**
- Análisis de concentración de riesgo por sector económico
- Optimización de productos basada en rentabilidad
- Segmentación de clientes para campañas de marketing

---

**🎯 ¡Continúa practicando y experimentando con diferentes combinaciones de GROUP BY y agregaciones para dominar el análisis bancario!**
