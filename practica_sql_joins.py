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
        cu.tipo_cuenta,
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
    
    mi_consulta_join = \"\"\"
    -- EJERCICIO 13: Clientes VIP con todas sus cuentas
    -- Usa INNER JOIN entre clientes y cuentas
    -- Filtra solo segmento_cliente = 'VIP'
    -- Muestra: nombre completo, ciudad, tipo_cuenta, saldo_actual
    -- Ordena por saldo_actual descendente
    
    SELECT 
        c.nombres || ' ' || c.apellidos AS nombre_completo,
        c.ciudad,
        cu.tipo_cuenta,
        cu.saldo_actual
    FROM clientes c
    INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    WHERE c.segmento_cliente = 'VIP'
    ORDER BY cu.saldo_actual DESC;
    \"\"\"
    
    ejecutar_consulta(conn, mi_consulta_join, "🎯 Mi consulta con JOIN")
    
    # ===========================================
    # 💡 SEGUNDA CONSULTA CON JOIN (opcional)
    # ===========================================
    
    # segunda_consulta_join = \"\"\"
    # -- EJERCICIO 14: Total patrimonio por cliente
    # -- Usa LEFT JOIN para incluir clientes sin cuentas
    # -- Suma todos los saldos por cliente
    # -- Muestra: nombre, ciudad, segmento, total_patrimonio, cantidad_cuentas
    # 
    # SELECT 
    #     c.nombres || ' ' || c.apellidos AS cliente,
    #     c.ciudad,
    #     c.segmento_cliente,
    #     COUNT(cu.cuenta_id) as cantidad_cuentas,
    #     COALESCE(SUM(cu.saldo_actual), 0) as total_patrimonio
    # FROM clientes c
    # LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    # GROUP BY c.cliente_id, c.nombres, c.apellidos, c.ciudad, c.segmento_cliente
    # ORDER BY total_patrimonio DESC;
    # \"\"\"
    # ejecutar_consulta(conn, segunda_consulta_join, "💰 Patrimonio por cliente")
    
    # ===========================================
    # 🎲 CONSULTA AVANZADA CON MÚLTIPLES JOINS
    # ===========================================
    
    # consulta_multiple_joins = \"\"\"
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
    # \"\"\"
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
