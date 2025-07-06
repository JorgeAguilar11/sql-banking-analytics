# 💪 Prácticas SQL Básicas: Agregaciones y GROUP BY

## 🎯 **Objetivos de Aprendizaje**
En esta práctica dominarás las agregaciones SQL fundamentales aplicadas al análisis bancario:
- 🧮 **Funciones básicas**: COUNT, SUM, AVG, MAX, MIN
- 📊 **GROUP BY simple**: Agrupaciones por una dimensión
- � **Análisis descriptivo**: Métricas fundamentales de negocio

---

## 🏆 **Reto 1: Métricas Fundamentales del Banco**

### 📝 **Explicación del Problema**
Como **Analista de Datos** del banco, el Director General te ha solicitado un **dashboard ejecutivo** con las métricas fundamentales que debe revisar cada mañana:
- 🏦 Estado general de la institución
- 👥 Base de clientes activos
- 💰 Concentración de saldos
- 📈 Indicadores clave de performance

### 🎯 **Contexto Bancario**
**Escenario**: Es lunes por la mañana y el CEO necesita conocer el estado actual del banco antes de la reunión de comité ejecutivo a las 9:00 AM.

### 📋 **Requisitos Específicos**
1. **Total de clientes activos** en el sistema
2. **Total de cuentas abiertas** y operativas
3. **Saldo total** bajo administración del banco
4. **Saldo promedio** por cuenta para medir concentración
5. **Cliente con mayor patrimonio** para análisis VIP

### 💡 **Estrategia de Solución**
```sql
-- Paso 1: Análisis de clientes activos
-- Pregunta: ¿Cuántos clientes están actualmente operando con el banco?
SELECT COUNT(*) as clientes_activos 
FROM clientes 
WHERE estado = 'ACTIVO';

-- Paso 2: Análisis de cuentas operativas
-- Pregunta: ¿Cuántas cuentas tenemos abiertas?
SELECT COUNT(*) as cuentas_abiertas 
FROM cuentas 
WHERE estado_cuenta = 'ACTIVA';

-- Paso 3: Saldo total bajo administración
-- Pregunta: ¿Cuánto dinero administra el banco?
SELECT 
    SUM(saldo_actual) as saldo_total_banco,
    ROUND(SUM(saldo_actual), 2) as saldo_total_formateado
FROM cuentas 
WHERE estado_cuenta = 'ACTIVA';

-- Paso 4: Saldo promedio por cuenta
-- Pregunta: ¿Cuál es la concentración promedio de saldos?
SELECT 
    AVG(saldo_actual) as saldo_promedio,
    ROUND(AVG(saldo_actual), 2) as saldo_promedio_formateado
FROM cuentas 
WHERE estado_cuenta = 'ACTIVA';

-- Paso 5: Cliente VIP con mayor patrimonio
-- Pregunta: ¿Quién es nuestro cliente más valioso?
SELECT 
    c.cliente_id,
    c.nombre_completo,
    SUM(ct.saldo_actual) as patrimonio_total
FROM clientes c
JOIN cuentas ct ON c.cliente_id = ct.cliente_id
WHERE c.estado = 'ACTIVO' AND ct.estado_cuenta = 'ACTIVA'
GROUP BY c.cliente_id, c.nombre_completo
ORDER BY patrimonio_total DESC
LIMIT 1;
```

### ✅ **Resultados Esperados**
```
Clientes Activos: 1,247
Cuentas Abiertas: 2,156
Saldo Total: $127,890,234.56
Saldo Promedio: $59,335.78
Cliente VIP: Juan Pérez López ($892,453.21)
```

### 🎯 **Conclusión del Reto**
**Aprendizaje clave**: Las funciones de agregación básicas (COUNT, SUM, AVG) son los pilares del análisis bancario. Con estas consultas simples puedes generar un dashboard ejecutivo completo.

---

## 🏆 **Reto 2: Análisis por Categoría de Producto**

### 📝 **Explicación del Problema**
El **Gerente de Productos** necesita evaluar el **performance de cada categoría** de productos financieros para la reunión mensual de estrategia:
- 📊 Distribución de cuentas por producto
- 💰 Concentración de saldos por categoría
- 📈 Oportunidades de crecimiento

### 🎯 **Contexto Bancario**
**Escenario**: Fin de mes, necesitas preparar el reporte mensual de productos para identificar qué categorías están funcionando bien y cuáles necesitan estrategias de impulso.

### 📋 **Requisitos Específicos**
Por cada **categoría de producto** mostrar:
1. **Número de cuentas** abiertas
2. **Saldo total** acumulado
3. **Saldo promedio** por cuenta
4. **Saldo máximo** (cuenta más grande)
5. **Saldo mínimo** (cuenta más pequeña)
6. **Ordenar** por saldo total descendente

### 💡 **Estrategia de Solución**
```sql
-- Consulta completa con explicación paso a paso
SELECT 
    -- Dimensión de agrupación
    pf.categoria_producto,
    
    -- Métricas de volumen
    COUNT(c.cuenta_id) as numero_cuentas,
    
    -- Métricas monetarias
    SUM(c.saldo_actual) as saldo_total,
    ROUND(AVG(c.saldo_actual), 2) as saldo_promedio,
    MAX(c.saldo_actual) as saldo_maximo,
    MIN(c.saldo_actual) as saldo_minimo,
    
    -- Métrica calculada adicional
    ROUND(SUM(c.saldo_actual) / COUNT(c.cuenta_id), 2) as saldo_promedio_verificacion
    
FROM productos_financieros pf
JOIN cuentas c ON pf.producto_id = c.producto_id
WHERE c.estado_cuenta = 'ACTIVA'
GROUP BY pf.categoria_producto
ORDER BY saldo_total DESC;
```

### ✅ **Resultados Esperados**
```
CATEGORIA_PRODUCTO  | CUENTAS | SALDO_TOTAL    | SALDO_PROMEDIO | SALDO_MAX   | SALDO_MIN
--------------------|---------|----------------|----------------|-------------|----------
Cuenta Corriente    | 856     | $45,234,567.89 | $52,854.32     | $892,453.21 | $1,500.00
Cuenta de Ahorros   | 743     | $38,567,234.12 | $51,923.45     | $654,789.33 | $500.00
Cuenta Premium      | 234     | $28,456,123.78 | $121,607.86    | $1,234,567.89| $25,000.00
Cuenta Joven        | 323     | $15,632,308.77 | $48,396.93     | $234,567.12 | $100.00
```

### 🎯 **Conclusión del Reto**
**Aprendizaje clave**: GROUP BY te permite segmentar y comparar performance entre categorías. Las Cuentas Premium tienen menor volumen pero mayor concentración de saldos (clientes VIP).

---

## 🧠 **REFUERZO TEÓRICO: Fundamentos de Agregaciones SQL**

### 📚 **1. Conceptos Fundamentales**

#### **¿Qué son las Agregaciones?**
Las **funciones de agregación** transforman múltiples filas en un solo valor resumen:
- 🔢 **COUNT()**: Cuenta registros
- ➕ **SUM()**: Suma valores numéricos  
- 📊 **AVG()**: Calcula promedio aritmético
- ⬆️ **MAX()**: Encuentra valor máximo
- ⬇️ **MIN()**: Encuentra valor mínimo

#### **¿Cuándo usar GROUP BY?**
```sql
-- SIN GROUP BY: Toda la tabla se convierte en UNA fila
SELECT COUNT(*), SUM(saldo) FROM cuentas;

-- CON GROUP BY: Una fila POR CADA grupo
SELECT categoria, COUNT(*), SUM(saldo) 
FROM cuentas 
GROUP BY categoria;
```

### 📊 **2. Mejores Prácticas en Banking**

#### **Siempre Filtrar Datos Obsoletos**
```sql
-- ❌ INCORRECTO: Incluye cuentas canceladas
SELECT AVG(saldo) FROM cuentas;

-- ✅ CORRECTO: Solo cuentas activas
SELECT AVG(saldo) FROM cuentas WHERE estado = 'ACTIVA';
```

#### **Manejar Valores NULL**
```sql
-- COUNT(*) cuenta todas las filas
-- COUNT(columna) excluye NULLs
SELECT 
    COUNT(*) as total_registros,
    COUNT(ingresos) as clientes_con_ingresos,
    COUNT(*) - COUNT(ingresos) as clientes_sin_ingresos
FROM clientes;
```

#### **Formatear Resultados Monetarios**
```sql
-- Para reportes ejecutivos, siempre redondea
SELECT 
    categoria,
    ROUND(SUM(saldo), 2) as saldo_total,
    ROUND(AVG(saldo), 2) as saldo_promedio
FROM cuentas 
GROUP BY categoria;
```

### 🎯 **3. Casos de Uso Bancarios Típicos**

| Función | Caso de Uso Bancario | Ejemplo |
|---------|---------------------|---------|
| COUNT() | Clientes activos, Cuentas por segmento | `COUNT(*) FROM clientes WHERE estado='ACTIVO'` |
| SUM() | Saldo total, Cartera de préstamos | `SUM(saldo_actual) FROM cuentas` |
| AVG() | Ticket promedio, Saldo promedio | `AVG(monto) FROM transacciones` |
| MAX() | Mayor depósito, Cuenta más grande | `MAX(saldo_actual) FROM cuentas` |
| MIN() | Menor saldo, Tasa más competitiva | `MIN(tasa_interes) FROM productos` |

### 💡 **4. Tips para el Éxito**

1. **Siempre valida tus resultados**: Usa consultas de verificación
2. **Considera valores NULL**: Entiende cómo afectan las agregaciones  
3. **Filtra datos relevantes**: No incluyas registros inactivos o cancelados
4. **Usa alias descriptivos**: `saldo_total` en lugar de `sum_saldo`
5. **Redondea valores monetarios**: Usa ROUND() para reportes

### 🚀 **Próximos Pasos**
Has dominado las agregaciones básicas. Ahora estás listo para:
- 📈 **GROUP BY múltiple** (siguiente práctica)
- 🔍 **HAVING** para filtrar grupos
- 📊 **Funciones de ventana** para análisis avanzado

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
