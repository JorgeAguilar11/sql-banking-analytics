#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔄 PRÁCTICA SQL BANCARIA - JOINS Y RELACIONES
==============================================

NIVEL 3: Domina las consultas multi-tabla con JOINs
Solo ejecuta: python practica_sql_joins.py

EJERCICIOS 13-20: De INNER JOIN básico hasta análisis multi-tabla complejos
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    conn = sqlite3.connect('data/banking_core.db')
    print("✅ Conectado a la base de datos bancaria")
    return conn

def mostrar_recordatorio(conn):
    """Recordatorio rápido de las relaciones"""
    print("🔗 RECORDATORIO DE RELACIONES:")
    print("-" * 40)
    print("👥 clientes ←→ 💳 cuentas ←→ 💸 transacciones")
    print("👥 clientes ←→ 🏠 prestamos")
    print("🏪 sucursales ←→ 💳 cuentas")
    print()

def ejecutar_consulta(conn, consulta, titulo="Resultado"):
    """Ejecuta una consulta SQL y muestra el resultado"""
    try:
        resultado = pd.read_sql_query(consulta, conn)
        print(f"✅ {titulo}:")
        print("-" * 60)
        print(resultado)
        print(f"📊 Total de registros: {len(resultado)}")
        print()
        return resultado
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        print()
        return None

def ejercicios_ejemplo_joins(conn):
    """Ejercicios de ejemplo para inspirarte"""
    print("🎯 EJERCICIOS DE EJEMPLO - JOINS:")
    print("-" * 60)
    
    # Ejemplo 1: INNER JOIN básico
    ejemplo1 = """
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        c.ciudad,
        c.segmento_cliente,
        cu.numero_cuenta,
        cu.saldo_actual
    FROM clientes c
    INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    WHERE c.segmento_cliente = 'VIP'
    ORDER BY cu.saldo_actual DESC;
    """
    ejecutar_consulta(conn, ejemplo1, "👑 Cuentas de clientes VIP")
    
    # Ejemplo 2: LEFT JOIN con agregación
    ejemplo2 = """
    SELECT 
        c.ciudad,
        COUNT(DISTINCT c.cliente_id) as total_clientes,
        COUNT(cu.cuenta_id) as total_cuentas,
        ROUND(AVG(cu.saldo_actual), 2) as promedio_saldo,
        SUM(cu.saldo_actual) as saldo_total_ciudad
    FROM clientes c
    LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    GROUP BY c.ciudad
    ORDER BY saldo_total_ciudad DESC;
    """
    ejecutar_consulta(conn, ejemplo2, "🏙️ Análisis bancario por ciudad")

def main():
    """Función principal - aquí practicas JOINs"""
    print("🚀 PRÁCTICA SQL BANCARIA - JOINS")
    print("=" * 50)
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # Recordatorio de relaciones
    mostrar_recordatorio(conn)
    
    # Ejercicios de ejemplo
    ejercicios_ejemplo_joins(conn)
    
    print("🎯 DESAFÍOS DE JOINS PARA TI:")
    print("-" * 60)
    print("EJERCICIO 13: Clientes VIP con todas sus cuentas")
    print("EJERCICIO 14: Total de patrimonio por cliente (suma de saldos)")
    print("EJERCICIO 15: Clientes que no tienen cuentas")
    print("EJERCICIO 16: Transacciones de cuentas de ahorro solamente")
    print("EJERCICIO 17: Sucursal con mayor volumen de dinero")
    print("EJERCICIO 18: Análisis de préstamos por segmento")
    print("EJERCICIO 19: Cliente más activo en transacciones")
    print("EJERCICIO 20: Reporte ejecutivo completo")
    print()
    
    # ===========================================
    # 🔥 ESCRIBE TU CONSULTA CON JOIN AQUÍ
    # ===========================================
    
    mi_consulta_join = """
    -- EJERCICIO 13: Clientes VIP con todas sus cuentas
    -- Usa INNER JOIN entre clientes y cuentas
    -- Filtra solo segmento_cliente = 'VIP'
    -- Muestra: nombre completo, ciudad, numero_cuenta, saldo_actual
    -- Ordena por saldo_actual descendente
    
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        c.ciudad,
        c.segmento_cliente,
        cu.numero_cuenta,
        cu.saldo_actual
    FROM clientes c
    INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    WHERE c.segmento_cliente = 'VIP'
    ORDER BY cliente;
    """
    
    ejecutar_consulta(conn, mi_consulta_join, "🎯 Mi consulta con JOIN")
    
    # ===========================================
    # 💡 SEGUNDA CONSULTA CON JOIN - EJERCICIO 14
    # ===========================================
    
    segunda_consulta_join = """
    -- EJERCICIO 14: Total patrimonio por cliente
    -- Usa LEFT JOIN para incluir clientes sin cuentas
    -- Suma todos los saldos por cliente
    -- Muestra: nombre, ciudad, segmento, total_patrimonio, cantidad_cuentas
    
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        c.ciudad,
        c.segmento_cliente,
        COUNT(cu.cuenta_id) AS cantidad_cuentas,
        COALESCE(SUM(cu.saldo_actual), 0) AS total_patrimonio
    FROM clientes c
    LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    GROUP BY c.cliente_id, c.nombres, c.apellidos, c.ciudad, c.segmento_cliente
    ORDER BY total_patrimonio DESC;
    """
    
    ejecutar_consulta(conn, segunda_consulta_join, "💰 EJERCICIO 14: Patrimonio por cliente")
    
    # ===========================================
    # 🔍 TERCERA CONSULTA CON JOIN - EJERCICIO 15
    # ===========================================
    
    tercera_consulta_join = """
    -- EJERCICIO 15: Clientes que NO tienen cuentas
    -- Usa LEFT JOIN + HAVING para filtrar solo clientes sin cuentas
    -- Muestra: nombre, ciudad, segmento
    -- Ordena por segmento para ver el patrón
    
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        c.ciudad,
        c.segmento_cliente
    FROM clientes c
    LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    WHERE cu.cuenta_id IS NULL
    ORDER BY c.segmento_cliente, c.ciudad;
    """
    
    ejecutar_consulta(conn, tercera_consulta_join, "🔍 EJERCICIO 15: Clientes SIN cuentas")
    
    # ===========================================
    # 💸 CUARTA CONSULTA CON JOIN - EJERCICIO 16
    # ===========================================
    
    cuarta_consulta_join = """
    -- EJERCICIO 16: Transacciones de cuentas de ahorro solamente
    -- Usa INNER JOIN entre clientes, cuentas y transacciones
    -- Filtra solo cuentas de ahorro (productos específicos)
    -- Muestra: cliente, número cuenta, tipo transacción, monto, fecha
    -- Ordena por fecha descendente para ver las más recientes
    
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        cu.numero_cuenta,
        pf.nombre_producto AS tipo_cuenta,
        t.tipo_transaccion,
        t.monto,
        t.fecha_transaccion
    FROM clientes c
    JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    JOIN productos_financieros pf ON cu.producto_id = pf.producto_id
    JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
    WHERE pf.nombre_producto LIKE '%Ahorro%'
    ORDER BY t.fecha_transaccion DESC
    LIMIT 15;
    """
    
    ejecutar_consulta(conn, cuarta_consulta_join, "💸 EJERCICIO 16: Transacciones de Ahorro")
    
    # ===========================================
    # 🏪 QUINTA CONSULTA CON JOIN - EJERCICIO 17
    # ===========================================
    
    quinta_consulta_join = """
    -- EJERCICIO 17: Sucursal con mayor volumen de dinero
    -- Usa INNER JOIN entre sucursales y cuentas
    -- Suma todos los saldos por sucursal
    -- Muestra: nombre_sucursal, ciudad_sucursal, total_dinero, total_cuentas
    -- Ordena por total_dinero descendente para ver las más prósperas
    
    SELECT 
        s.nombre_sucursal,
        s.ciudad AS ciudad_sucursal,
        COUNT(cu.cuenta_id) AS total_cuentas,
        SUM(cu.saldo_actual) AS total_dinero,
        ROUND(AVG(cu.saldo_actual), 2) AS promedio_por_cuenta
    FROM sucursales s
    JOIN cuentas cu ON s.sucursal_id = cu.sucursal_id
    GROUP BY s.sucursal_id, s.nombre_sucursal, s.ciudad
    ORDER BY total_dinero DESC;
    """
    
    ejecutar_consulta(conn, quinta_consulta_join, "🏪 EJERCICIO 17: Análisis por sucursal")
    
    # ===========================================
    # 🏠 SEXTA CONSULTA CON JOIN - EJERCICIO 18
    # ===========================================
    
    sexta_consulta_join = """
    -- EJERCICIO 18: Análisis de préstamos por segmento
    -- Usa INNER JOIN entre clientes y prestamos
    -- Agrupa por segmento de cliente para análisis de riesgo
    -- Muestra: segmento, total_prestamos, monto_total, promedio_prestamo
    -- Ordena por monto_total descendente para ver exposición por segmento
    
    SELECT 
        c.segmento_cliente,
        COUNT(p.prestamo_id) AS total_prestamos,
        SUM(p.monto_aprobado) AS monto_total_prestamos,
        ROUND(AVG(p.monto_aprobado), 2) AS promedio_por_prestamo,
        ROUND(AVG(p.tasa_interes), 2) AS tasa_promedio,
        MIN(p.fecha_aprobacion) AS primer_prestamo,
        MAX(p.fecha_aprobacion) AS ultimo_prestamo
    FROM clientes c
    INNER JOIN prestamos p ON c.cliente_id = p.cliente_id
    GROUP BY c.segmento_cliente
    ORDER BY monto_total_prestamos DESC;
"""
    
    ejecutar_consulta(conn, sexta_consulta_join, "🏠 EJERCICIO 18: Préstamos por segmento")
    
    # ===========================================
    # 🏃 SÉPTIMA CONSULTA CON JOIN - EJERCICIO 19
    # ===========================================
    
    septima_consulta_join = """
    -- EJERCICIO 19: Cliente más activo en transacciones
    -- Usa INNER JOIN entre clientes, cuentas y transacciones
    -- Encuentra el cliente con mayor actividad transaccional
    -- Muestra: cliente, total_transacciones, monto_total, transaccion_promedio
    -- Ordena por total_transacciones para identificar al más activo
    
    SELECT 
        c.cliente_id,
        c.nombres || ' ' || c.apellidos AS cliente,
        c.segmento_cliente,
        COUNT(t.transaccion_id) AS total_transacciones,
        ROUND(SUM(t.monto), 2) AS monto_total_transacciones,
        ROUND(AVG(t.monto), 2) AS monto_promedio_transaccion,
        MIN(t.fecha_transaccion) AS primera_transaccion,
        MAX(t.fecha_transaccion) AS ultima_transaccion
    FROM clientes c
    INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    INNER JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
    GROUP BY c.cliente_id, c.nombres, c.apellidos, c.segmento_cliente
    ORDER BY total_transacciones DESC
    LIMIT 1;
    """
    
    ejecutar_consulta(conn, septima_consulta_join, "🏃 EJERCICIO 19: Cliente más activo")
    
    # ===========================================
    # 📊 OCTAVA CONSULTA CON JOIN - EJERCICIO 20
    # ===========================================
    
    octava_consulta_join = """
    -- EJERCICIO 20: Reporte ejecutivo completo
    -- Combina datos de clientes, cuentas, transacciones y préstamos
    -- Vista integral del perfil financiero por segmento
    -- Incluye métricas de rentabilidad, actividad y riesgo
    
    SELECT 
        c.segmento_cliente,
        COUNT(DISTINCT c.cliente_id) AS total_clientes,
        COUNT(DISTINCT cu.cuenta_id) AS total_cuentas,
        ROUND(AVG(cu.saldo_actual), 2) AS saldo_promedio_cuenta,
        ROUND(SUM(cu.saldo_actual), 2) AS patrimonio_total_segmento,
        COUNT(DISTINCT t.transaccion_id) AS total_transacciones,
        ROUND(AVG(t.monto), 2) AS monto_promedio_transaccion,
        COUNT(DISTINCT p.prestamo_id) AS total_prestamos,
        ROUND(SUM(p.monto_aprobado), 2) AS exposicion_crediticia,
        ROUND(AVG(p.tasa_interes), 2) AS tasa_promedio_prestamos
    FROM clientes c
    LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    LEFT JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
    LEFT JOIN prestamos p ON c.cliente_id = p.cliente_id
    GROUP BY c.segmento_cliente
    ORDER BY patrimonio_total_segmento DESC;
    """
    
    ejecutar_consulta(conn, octava_consulta_join, "📊 EJERCICIO 20: Reporte ejecutivo")
    
    # ===========================================
    # 🔥 CONSULTA AVANZADA CON MÚLTIPLES JOINS
    # ===========================================
    
    # consulta_multiple_joins = """
    # -- EJERCICIO AVANZADO: Triple JOIN
    # -- Une clientes, cuentas y transacciones
    # -- Analiza actividad transaccional por segmento
    # 
    # SELECT 
    #     c.segmento_cliente,
    #     COUNT(DISTINCT c.cliente_id) as clientes,
    #     COUNT(DISTINCT cu.cuenta_id) as cuentas,
    #     COUNT(t.transaccion_id) as transacciones,
    #     ROUND(AVG(t.monto), 2) as monto_promedio_transaccion
    # FROM clientes c
    # INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    # INNER JOIN transacciones t ON cu.cuenta_id = t.cuenta_id
    # GROUP BY c.segmento_cliente
    # ORDER BY monto_promedio_transaccion DESC;
    # """
    # ejecutar_consulta(conn, consulta_multiple_joins, "🔄 Análisis transaccional")
    
    # Cerrar conexión
    conn.close()
    print("🔌 Conexión cerrada")
    print("🎉 ¡Práctica de JOINs completada!")
    print()
    print("💡 TIPS PARA DOMINAR JOINS:")
    print("   • INNER JOIN: Solo registros que coinciden")
    print("   • LEFT JOIN: Todos de la izquierda + coincidencias")
    print("   • Siempre especifica las condiciones ON")
    print("   • Usa alias (c, cu, t) para consultas más claras")
    print("   • GROUP BY requiere todas las columnas no agregadas")
    print("   • COALESCE() maneja valores NULL en sumas")

if __name__ == "__main__":
    main()
