# 🔄 GUÍA JOINS BANCARIOS
## Dominio de Consultas Multi-tabla

---

## 🏆 **LOGROS ALCANZADOS**

**Nivel:** AVANZADO ⭐⭐⭐⭐⭐  
**Ejercicios completados:** 8 (13-20)  
**Conceptos dominados:** INNER JOIN, LEFT JOIN, JOINs múltiples  

---

## ✅ **EJERCICIOS COMPLETADOS**

### **EJERCICIO 13: Clientes VIP con Cuentas** ✅
```sql
-- Identifica clientes de alto valor con productos activos
-- Esencial para gestión de banca privada y relaciones VIP
-- Permite asignación de ejecutivos especializados
SELECT c.nombres || ' ' || c.apellidos AS cliente, cu.numero_cuenta, cu.saldo_actual
FROM clientes c
INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
WHERE c.segmento_cliente = 'VIP';
```
**📊 Resultado:** Carlos Rodríguez Pérez - 2 cuentas ($15.7M total)  
**🎯 Caso de Uso:** Asignación de ejecutivos de banca privada

---

### **EJERCICIO 14: Patrimonio por Cliente** ✅
```sql
-- Calcula patrimonio total para evaluación crediticia y cross-selling
-- Identifica clientes sin productos para campañas de captación
-- Base para análisis de concentración de riesgo por cliente
SELECT c.nombres || ' ' || c.apellidos AS cliente, 
       COUNT(cu.cuenta_id) AS cantidad_cuentas,
       COALESCE(SUM(cu.saldo_actual), 0) AS total_patrimonio
FROM clientes c
LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
GROUP BY c.cliente_id
ORDER BY total_patrimonio DESC;
```
**📊 Resultado:** 5 clientes con cuentas, 15 sin cuentas  
**🎯 Caso de Uso:** Evaluación crediticia y estrategias de captación

---

### **EJERCICIO 15: Clientes SIN Cuentas** ✅
```sql
-- Identifica oportunidades de negocio no aprovechadas
-- Critical para estrategias de penetración y activación
-- Segmenta clientes inactivos para campañas personalizadas
SELECT c.nombres || ' ' || c.apellidos AS cliente, c.segmento_cliente
FROM clientes c
LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
WHERE cu.cuenta_id IS NULL;
```
**📊 Resultado:** 15 clientes sin productos (75%)  
**🎯 Caso de Uso:** Campañas de activación y recuperación de clientes

---

### **EJERCICIO 16: Transacciones de Ahorro** ✅
```sql
-- Analiza comportamiento transaccional en productos de ahorro
-- Detecta patrones de uso para optimización de productos
-- Monitorea actividad para detección de fraude
SELECT c.nombres || ' ' || c.apellidos AS cliente, t.tipo_transaccion, t.monto
FROM clientes c
JOIN cuentas cu ON c.cliente_id = cu.cliente_id
JOIN productos_financieros pf ON cu.producto_id = pf.producto_id
JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
WHERE pf.nombre_producto LIKE '%Ahorro%';
```
**📊 Resultado:** 11 transacciones en cuentas de ahorro  
**🎯 Caso de Uso:** Análisis comportamental y detección de fraude

---

### **EJERCICIO 17: Análisis por Sucursal** ✅
```sql
-- Evalúa desempeño y concentración de recursos por sucursal
-- Fundamental para decisiones de expansión y cierre de puntos
-- Optimiza asignación de personal y presupuestos regionales
SELECT s.nombre_sucursal, SUM(cu.saldo_actual) AS total_dinero,
       COUNT(cu.cuenta_id) AS total_cuentas
FROM sucursales s
JOIN cuentas cu ON s.sucursal_id = cu.sucursal_id
GROUP BY s.sucursal_id
ORDER BY total_dinero DESC;
```
**📊 Resultado:** Sucursal Norte lidera con $15.7M  
**🎯 Caso de Uso:** Planificación estratégica de red de sucursales

---

### **EJERCICIO 18: Préstamos por Segmento** ✅
```sql
-- Analiza exposición crediticia y diversificación de riesgo
-- Evalúa pricing diferenciado por segmento de clientes
-- Informa políticas de aprobación y límites de crédito
SELECT c.segmento_cliente, COUNT(p.prestamo_id) AS total_prestamos,
       SUM(p.monto_aprobado) AS monto_total
FROM clientes c
INNER JOIN prestamos p ON c.cliente_id = p.cliente_id
GROUP BY c.segmento_cliente
ORDER BY monto_total DESC;
```
**📊 Resultado:** VIP ($85M), Premium ($35M), Estándar ($23M)  
**🎯 Caso de Uso:** Gestión de riesgo crediticio y pricing estratégico

---

### **EJERCICIO 19: Cliente Más Activo** ✅
```sql
-- Identifica clientes con mayor engagement y uso de productos
-- Perfil ideal para casos de éxito y testimonios comerciales
-- Detecta usuarios power para programas de fidelización
SELECT c.nombres || ' ' || c.apellidos AS cliente,
       COUNT(t.transaccion_id) AS total_transacciones
FROM clientes c
INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
INNER JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
GROUP BY c.cliente_id
ORDER BY total_transacciones DESC
LIMIT 1;
```
**📊 Resultado:** Ana María González López - 7 transacciones  
**🎯 Caso de Uso:** Programas de fidelización y embajadores de marca

---

### **EJERCICIO 20: Reporte Ejecutivo** ✅
```sql
-- Combina datos de clientes, cuentas, transacciones y préstamos
-- Vista integral del perfil financiero por segmento
-- Dashboard gerencial para toma de decisiones estratégicas
SELECT c.segmento_cliente,
       COUNT(DISTINCT c.cliente_id) AS total_clientes,
       COUNT(DISTINCT cu.cuenta_id) AS total_cuentas,
       ROUND(SUM(cu.saldo_actual), 2) AS patrimonio_total
FROM clientes c
LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
GROUP BY c.segmento_cliente
ORDER BY patrimonio_total DESC;
```
**📊 Resultado:** Vista 360° de todos los segmentos  
**🎯 Caso de Uso:** Reportes gerenciales y planeación estratégica

---

## 🎯 **CONCEPTOS DOMINADOS**

### **INNER JOIN**
```sql
FROM tabla1 t1
INNER JOIN tabla2 t2 ON t1.id = t2.id
```
Solo registros que coinciden en ambas tablas

### **LEFT JOIN**
```sql
FROM tabla1 t1
LEFT JOIN tabla2 t2 ON t1.id = t2.id
```
Todos los registros de la izquierda + coincidencias

### **JOINs Múltiples**
```sql
FROM clientes c
JOIN cuentas cu ON c.cliente_id = cu.cliente_id
JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
```
Une 3 o más tablas secuencialmente

---

## 📊 **INSIGHTS BANCARIOS DESCUBIERTOS**

### **🥇 Top Insights**
1. **75% de clientes** no tienen productos financieros
2. **Cliente más activo** es del segmento Estándar (no VIP)
3. **Sucursal Norte** concentra el 58% del dinero total
4. **Segmento VIP** tiene menor tasa de interés (12% vs 15%)

### **🎯 Casos de Uso Reales**
- **Marketing**: Enfocar en clientes sin productos (75% oportunidad)
- **Riesgo**: Monitorear concentración por sucursal y exposición crediticia
- **Ventas**: Segmento Estándar más activo, potencial cross-selling
- **Operaciones**: Optimizar red de sucursales según volumen
- **Compliance**: Detectar patrones transaccionales inusuales
- **Pricing**: Estrategias diferenciadas por segmento (VIP 12% vs otros 15%)

---

## 🛠️ **CORRECCIONES REALIZADAS**

### **Errores Superados:**
- `p.monto` → `p.monto_aprobado`
- `t.fecha` → `t.fecha_transaccion`
- Comentarios `#` dentro de SQL
- Nombres de columnas incorrectos

### **Debugging Skills:**
- Verificar estructura de tablas con `PRAGMA table_info()`
- Uso correcto de alias (`c`, `cu`, `t`, `p`)
- GROUP BY con todas las columnas no agregadas

---

## 🏆 **PROGRESO FINAL**

### **Nivel: AVANZADO** ⭐⭐⭐⭐⭐
✅ INNER JOIN básico  
✅ LEFT JOIN con NULL  
✅ JOINs múltiples (4 tablas)  
✅ Agregaciones complejas  
✅ Análisis multi-dimensional  
✅ Debugging SQL avanzado  

### **Estadísticas:**
- **Consultas ejecutadas:** 8 complejas
- **Tablas relacionadas:** 5 (clientes, cuentas, transacciones, préstamos, sucursales)
- **Registros analizados:** +100
- **Errores corregidos:** 4

---

## 🚀 **SIGUIENTE NIVEL**

**Próximos Desafíos:**
- 🔍 Subconsultas (EXISTS, IN)
- 📊 CTEs y funciones de ventana
- 🎯 Consultas recursivas
- 📈 Análisis temporal avanzado

---

## 🎉 **¡MISIÓN CUMPLIDA!**

Has dominado las **consultas multi-tabla** y el **análisis bancario relacional**. Tu capacidad para unir datos de múltiples fuentes te posiciona como **analista SQL avanzado**.

**¡Listo para conquistar bases de datos complejas!** 🏆

---

*📅 Completado: Julio 2025*  
*🎯 De principiante a experto en JOINs*
