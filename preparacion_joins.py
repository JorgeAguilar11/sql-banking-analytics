#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔄 PRÁCTICA SQL BANCARIA - JOINS Y RELACIONES
==============================================

NIVEL 3: Consultas multi-tabla con JOINs
Explora relaciones entre clientes, cuentas, préstamos y transacciones.

PREREQUISITO: Haber completado la práctica avanzada (NIVEL 2)
Solo ejecuta: python practica_sql_joins.py
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    conn = sqlite3.connect('data/banking_core.db')
    print("✅ Conectado a la base de datos bancaria")
    return conn

def mostrar_esquema_completo(conn):
    """Muestra el esquema completo de todas las tablas"""
    print("🏦 ESQUEMA COMPLETO DE LA BASE DE DATOS:")
    print("=" * 60)
    
    # Obtener todas las tablas
    tablas = pd.read_sql_query("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """, conn)
    
    for tabla in tablas['name']:
        print(f"\n📋 TABLA: {tabla.upper()}")
        print("-" * 40)
        
        # Obtener columnas de cada tabla
        columnas = pd.read_sql_query(f"PRAGMA table_info({tabla})", conn)
        for _, col in columnas.iterrows():
            tipo_col = col['type']
            es_pk = "🔑 " if col['pk'] else "   "
            print(f"{es_pk}{col['name']:<25} {tipo_col}")
    
    print("\n" + "=" * 60)
    print()

def mostrar_relaciones(conn):
    """Muestra las relaciones entre tablas"""
    print("🔗 RELACIONES ENTRE TABLAS:")
    print("-" * 40)
    print("📊 clientes (1) ←→ (N) cuentas")
    print("   🔑 clientes.cliente_id = cuentas.cliente_id")
    print()
    print("📊 clientes (1) ←→ (N) prestamos") 
    print("   🔑 clientes.cliente_id = prestamos.cliente_id")
    print()
    print("📊 cuentas (1) ←→ (N) transacciones")
    print("   🔑 cuentas.cuenta_id = transacciones.cuenta_id")
    print()
    print("📊 sucursales (1) ←→ (N) cuentas")
    print("   🔑 sucursales.sucursal_id = cuentas.sucursal_id")
    print()

def mostrar_ejemplos_joins(conn):
    """Muestra ejemplos de diferentes tipos de JOINs"""
    print("🎯 EJEMPLOS DE JOINS:")
    print("=" * 60)
    
    # INNER JOIN básico
    print("📌 EJEMPLO 1: INNER JOIN (clientes con cuentas)")
    print("-" * 50)
    ejemplo1 = """
    SELECT 
        c.nombres,
        c.apellidos,
        c.ciudad,
        cu.numero_cuenta,
        pf.nombre_producto as tipo_producto,
        cu.saldo_actual
    FROM clientes c
    INNER JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    INNER JOIN productos_financieros pf ON cu.producto_id = pf.producto_id
    ORDER BY c.apellidos, cu.saldo_actual DESC;
    """
    
    resultado1 = pd.read_sql_query(ejemplo1, conn)
    print(resultado1.head(10))
    print(f"📊 Total registros: {len(resultado1)}")
    print()
    
    # LEFT JOIN con conteo
    print("📌 EJEMPLO 2: LEFT JOIN (todos los clientes + conteo de cuentas)")
    print("-" * 50)
    ejemplo2 = """
    SELECT 
        c.nombres || ' ' || c.apellidos AS cliente,
        c.ciudad,
        c.segmento_cliente,
        COUNT(cu.cuenta_id) as total_cuentas,
        ROUND(AVG(cu.saldo_actual), 2) as promedio_saldo
    FROM clientes c
    LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
    GROUP BY c.cliente_id, c.nombres, c.apellidos, c.ciudad, c.segmento_cliente
    ORDER BY total_cuentas DESC, promedio_saldo DESC;
    """
    
    resultado2 = pd.read_sql_query(ejemplo2, conn)
    print(resultado2)
    print()

def ejercicios_joins_preparados(conn):
    """Muestra los ejercicios preparados para practicar"""
    print("🎯 EJERCICIOS PREPARADOS PARA TI:")
    print("=" * 60)
    
    ejercicios = [
        "EJERCICIO 13: Clientes VIP con sus cuentas (INNER JOIN)",
        "EJERCICIO 14: Total de saldo por cliente (LEFT JOIN + SUM)", 
        "EJERCICIO 15: Clientes sin cuentas (LEFT JOIN + IS NULL)",
        "EJERCICIO 16: Transacciones por tipo de cuenta (TRIPLE JOIN)",
        "EJERCICIO 17: Sucursal con más dinero depositado (JOIN + GROUP BY)",
        "EJERCICIO 18: Préstamos por segmento de cliente (JOIN + análisis)",
        "EJERCICIO 19: Cliente más activo en transacciones (MÚLTIPLES JOINS)",
        "EJERCICIO 20: Análisis completo cliente-cuenta-transacción (MASTER JOIN)"
    ]
    
    for i, ejercicio in enumerate(ejercicios, 13):
        print(f"🔥 {ejercicio}")
    
    print()
    print("💡 CONCEPTOS QUE VAS A DOMINAR:")
    print("   • INNER JOIN - Registros que coinciden en ambas tablas")
    print("   • LEFT JOIN - Todos los registros de la tabla izquierda")
    print("   • RIGHT JOIN - Todos los registros de la tabla derecha") 
    print("   • FULL OUTER JOIN - Todos los registros de ambas tablas")
    print("   • CROSS JOIN - Producto cartesiano")
    print("   • Self JOIN - Unir tabla consigo misma")
    print("   • Múltiples JOINs en una consulta")
    print("   • JOINs con GROUP BY y funciones agregadas")
    print()

def datos_muestra_joins(conn):
    """Muestra datos de muestra para entender las relaciones"""
    print("📊 DATOS DE MUESTRA PARA ENTENDER JOINS:")
    print("=" * 60)
    
    # Muestra algunos clientes
    print("👥 ALGUNOS CLIENTES:")
    clientes_muestra = pd.read_sql_query("""
        SELECT cliente_id, nombres, apellidos, ciudad, segmento_cliente 
        FROM clientes 
        LIMIT 5
    """, conn)
    print(clientes_muestra)
    print()
    
    # Muestra algunas cuentas
    print("💳 ALGUNAS CUENTAS:")
    cuentas_muestra = pd.read_sql_query("""
        SELECT cuenta_id, cliente_id, numero_cuenta, producto_id, saldo_actual 
        FROM cuentas 
        LIMIT 5
    """, conn)
    print(cuentas_muestra)
    print()
    
    # Muestra algunas transacciones
    print("💸 ALGUNAS TRANSACCIONES:")
    transacciones_muestra = pd.read_sql_query("""
        SELECT transaccion_id, cuenta_id, tipo_transaccion, monto, fecha_transaccion 
        FROM transacciones 
        LIMIT 5
    """, conn)
    print(transacciones_muestra)
    print()

def main():
    """Función principal - preparación para JOINs"""
    print("🚀 PREPARACIÓN PARA PRÁCTICA DE JOINS")
    print("=" * 50)
    print("🎯 NIVEL 3: Consultas multi-tabla")
    print("📋 PREREQUISITO: Práctica avanzada completada ✅")
    print()
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # Mostrar esquema completo
    mostrar_esquema_completo(conn)
    
    # Mostrar relaciones
    mostrar_relaciones(conn)
    
    # Datos de muestra
    datos_muestra_joins(conn)
    
    # Ejemplos de JOINs
    mostrar_ejemplos_joins(conn)
    
    # Ejercicios preparados
    ejercicios_joins_preparados(conn)
    
    # Cerrar conexión
    conn.close()
    print("🔌 Conexión cerrada")
    print()
    print("🎉 ¡PREPARACIÓN COMPLETA!")
    print("📚 Ya tienes todo lo necesario para dominar JOINs")
    print()
    print("🚀 PRÓXIMOS PASOS:")
    print("   1. Estudia los ejemplos mostrados")
    print("   2. Entiende las relaciones entre tablas")
    print("   3. Practica con los ejercicios 13-20")
    print("   4. Experimenta con diferentes tipos de JOINs")
    print()
    print("💡 CONSEJO:")
    print("   Los JOINs son el 80% del SQL profesional.")
    print("   ¡Domínalos y serás imparable! 🥷")

if __name__ == "__main__":
    main()
