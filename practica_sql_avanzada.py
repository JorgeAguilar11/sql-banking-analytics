#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏦 PRÁCTICA SQL BANCARIA AVANZADA
================================

Ejercicios SQL de nivel intermedio-avanzado para análisis bancario.
Solo ejecuta: python practica_sql_avanzada.py
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    conn = sqlite3.connect('data/banking_core.db')
    print("✅ Conectado a la base de datos bancaria")
    return conn

def mostrar_info_tablas(conn):
    """Muestra información de las tablas disponibles"""
    tablas = pd.read_sql_query("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
    """, conn)
    
    print("🏦 TABLAS DISPONIBLES:")
    for tabla in tablas['name']:
        print(f"   📋 {tabla}")
    
    print("\n💡 COLUMNAS DE LA TABLA CLIENTES:")
    columnas = pd.read_sql_query("PRAGMA table_info(clientes)", conn)
    for _, col in columnas.iterrows():
        print(f"   • {col['name']} ({col['type']})")
    print()

def ejecutar_consulta(conn, consulta, titulo="Resultado"):
    """Ejecuta una consulta SQL y muestra el resultado"""
    try:
        resultado = pd.read_sql_query(consulta, conn)
        print(f"✅ {titulo}:")
        print("-" * 60)
        print(resultado)
        print()
        return resultado
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        print()
        return None

def ejercicios_ejemplo(conn):
    """Muestra algunos ejercicios de ejemplo para inspirarte"""
    print("🎯 EJERCICIOS DE EJEMPLO AVANZADOS:")
    print("-" * 60)
    
    # Ejemplo 1: Análisis estadístico por ciudad
    ejemplo1 = """
    SELECT 
        ciudad,
        COUNT(*) as total_clientes,
        AVG(ingresos_mensuales) as promedio_ingresos,
        MAX(ingresos_mensuales) as ingreso_maximo,
        MIN(ingresos_mensuales) as ingreso_minimo,
        SUM(ingresos_mensuales) as ingresos_totales
    FROM clientes 
    GROUP BY ciudad 
    ORDER BY promedio_ingresos DESC;
    """
    ejecutar_consulta(conn, ejemplo1, "📊 Análisis estadístico por ciudad")
    
    # Ejemplo 2: Clasificación de clientes por rangos
    ejemplo2 = """
    SELECT 
        CASE 
            WHEN ingresos_mensuales >= 8000000 THEN 'VIP'
            WHEN ingresos_mensuales >= 5000000 THEN 'Premium'
            WHEN ingresos_mensuales >= 3000000 THEN 'Estándar'
            ELSE 'Básico'
        END as categoria_cliente,
        COUNT(*) as cantidad,
        ROUND(AVG(ingresos_mensuales), 2) as promedio_categoria
    FROM clientes 
    GROUP BY categoria_cliente
    ORDER BY promedio_categoria DESC;
    """
    ejecutar_consulta(conn, ejemplo2, "🏆 Clasificación por rangos de ingresos")

def main():
    """Función principal - aquí practicas SQL avanzado"""
    print("🚀 PRÁCTICA SQL BANCARIA AVANZADA")
    print("=" * 50)
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # Mostrar información de tablas
    mostrar_info_tablas(conn)
    
    # Mostrar ejercicios de ejemplo
    ejercicios_ejemplo(conn)
    
    print("🎯 DESAFÍOS PARA TI:")
    print("-" * 60)
    print("EJERCICIO 7: Promedio de ingresos por ciudad (usa AVG)")
    print("EJERCICIO 8: Top 3 clientes más ricos (usa LIMIT 3)")
    print("EJERCICIO 9: Clientes de clase media (BETWEEN 3M y 7M)")
    print("EJERCICIO 10: Contar clientes por segmento")
    print("EJERCICIO 11: Ciudad con mayor suma total de ingresos")
    print("EJERCICIO 12: Porcentaje de clientes VIP por ciudad")
    print()
    
    # ===========================================
    # 🔥 ESCRIBE TU CONSULTA AVANZADA AQUÍ
    # ===========================================
    
    mi_consulta_avanzada = """
    -- Escribe aquí tu consulta SQL avanzada
    -- Ejemplos de funciones que puedes usar:
    -- AVG(), MAX(), MIN(), SUM(), COUNT()
    -- CASE WHEN ... THEN ... END
    -- BETWEEN ... AND ...
    -- LIMIT, HAVING
    
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
    """
    
    ejecutar_consulta(conn, mi_consulta_avanzada, "🎯 Mi consulta avanzada")
     # ===========================================
    # 💡 SEGUNDA CONSULTA AVANZADA - EJERCICIO 8
    # ===========================================
    
    segunda_consulta_avanzada = """
    -- EJERCICIO 8: Top 3 clientes más ricos
    -- Muestra nombre completo, ingresos y ciudad de los 3 clientes con mayores ingresos
    SELECT 
        nombres || ' ' || apellidos AS nombre_completo,
        ingresos_mensuales,
        ciudad
    FROM clientes 
    ORDER BY ingresos_mensuales DESC
    LIMIT 3;
    """
    
    ejecutar_consulta(conn, segunda_consulta_avanzada, "🏆 EJERCICIO 8: Top 3 clientes más ricos")
    #        CASE 
    #            WHEN ingresos_mensuales > 8000000 THEN 'VIP'
    #            ELSE 'Regular'
    #        END as categoria
    # FROM clientes 
    # WHERE ingresos_mensuales > 5000000
    # ORDER BY ingresos_mensuales DESC;
    # """
    # ejecutar_consulta(conn, segunda_consulta_avanzada, "🚀 Mi segunda consulta avanzada")
    
    # ===========================================
    # 🎲 CONSULTA EXPERIMENTAL (opcional)
    # ===========================================
    
    # consulta_experimental = """
    # -- Aquí puedes experimentar con consultas más complejas
    # -- Combina múltiples WHERE, GROUP BY, HAVING, etc.
    # 
    # SELECT 
    #     ciudad,
    #     COUNT(*) as total_clientes,
    #     AVG(ingresos_mensuales) as promedio
    # FROM clientes 
    # GROUP BY ciudad 
    # HAVING COUNT(*) > 2
    # ORDER BY total_clientes DESC;
    # """
    # ejecutar_consulta(conn, consulta_experimental, "🎲 Mi consulta experimental")
    
    # Cerrar conexión
    conn.close()
    print("🔌 Conexión cerrada")
    print("🎉 ¡Práctica avanzada completada!")
    print()
    print("💡 TIPS PARA CONSULTAS AVANZADAS:")
    print("   • Usa CASE WHEN para crear categorías")
    print("   • Combina GROUP BY con HAVING para filtros avanzados")
    print("   • Experimenta con múltiples funciones de agregación")
    print("   • Usa BETWEEN para rangos numéricos")
    print("   • Combina WHERE, GROUP BY y ORDER BY")

if __name__ == "__main__":
    main()
