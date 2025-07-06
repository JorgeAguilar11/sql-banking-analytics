#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏦 PRÁCTICA SQL BANCARIA - VERSIÓN SIMPLE
======================================

Este archivo te permite practicar SQL de forma sencilla.
Solo ejecuta: python practica_sql_simple.py
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    conn = sqlite3.connect('data/banking_core.db')
    print("✅ Conectado a la base de datos bancaria")
    return conn

def mostrar_tablas(conn):
    """Muestra las tablas disponibles"""
    tablas = pd.read_sql_query("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
    """, conn)
    
    print("🏦 Tablas disponibles:")
    for tabla in tablas['name']:
        print(f"   📋 {tabla}")
    print()

def ejecutar_consulta(conn, consulta, titulo="Resultado"):
    """Ejecuta una consulta SQL y muestra el resultado"""
    try:
        resultado = pd.read_sql_query(consulta, conn)
        print(f"✅ {titulo}:")
        print("-" * 50)
        print(resultado)
        print()
        return resultado
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        print()
        return None

def main():
    """Función principal - aquí practicas SQL"""
    print("🎯 PRÁCTICA SQL BANCARIA")
    print("=" * 40)
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # Mostrar tablas disponibles
    mostrar_tablas(conn)
    
    # ===========================================
    # � ESCRIBE TUS PROPIAS CONSULTAS SQL AQUÍ
    # ===========================================
    
    # ===========================================
    # 💡 TU CONSULTA SQL
    # ===========================================
    
    mi_consulta_libre = """
    -- Escribe tu consulta SQL aquí
    select nombres, apellidos, ingresos_mensuales,ciudad
    from clientes
    where ingresos_mensuales > 4000000
    order by ingresos_mensuales desc;
    """
    ejecutar_consulta(conn, mi_consulta_libre, "Mi consulta SQL")
    
    # ===========================================
    # 🎯 SEGUNDA CONSULTA (opcional)
    # ===========================================
    # Si quieres probar otra consulta diferente, úsala aquí:
    
    # segunda_consulta = """
    # -- Tu segunda consulta aquí
    # SELECT COUNT(*) as total_clientes FROM clientes;
    # """
    # ejecutar_consulta(conn, segunda_consulta, "Mi segunda consulta")
    
    # Cerrar conexión
    #conn.close()
    #print("🔌 Conexión cerrada")
    print("¡Práctica completada! 🎉")

if __name__ == "__main__":
    main()
