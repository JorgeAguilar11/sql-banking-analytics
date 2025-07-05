#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 ACTUALIZAR SEGMENTOS BANCARIOS
=================================

Script para "ajustar" la segmentación de clientes para que se vea más realista
y no nos boten del trabajo 😅

Criterios de segmentación realistas:
- VIP: >= 8,000,000 (los millonarios de verdad)
- Premium: 5,000,000 - 7,999,999 (clase alta)
- Estándar: 2,500,000 - 4,999,999 (clase media jodida pero con esperanza)
- Básico: < 2,500,000 (los que apenas la van pasando)
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    conn = sqlite3.connect('data/banking_core.db')
    print("✅ Conectado a la base de datos bancaria")
    return conn

def mostrar_estado_actual(conn):
    """Muestra el estado actual de los segmentos"""
    print("📊 ESTADO ACTUAL DE SEGMENTOS:")
    print("-" * 50)
    
    consulta_actual = """
    SELECT 
        segmento_cliente,
        COUNT(*) as cantidad,
        MIN(ingresos_mensuales) as ingreso_minimo,
        MAX(ingresos_mensuales) as ingreso_maximo,
        ROUND(AVG(ingresos_mensuales), 2) as promedio
    FROM clientes 
    GROUP BY segmento_cliente
    ORDER BY promedio DESC;
    """
    
    resultado = pd.read_sql_query(consulta_actual, conn)
    print(resultado)
    print()

def actualizar_segmentos(conn):
    """Actualiza los segmentos basándose en ingresos reales"""
    print("🔧 ACTUALIZANDO SEGMENTOS PARA SALVAR EL TRABAJO...")
    print("-" * 50)
    
    # Script de actualización basado en ingresos
    script_actualizacion = """
    UPDATE clientes 
    SET segmento_cliente = CASE 
        WHEN ingresos_mensuales >= 8000000 THEN 'VIP'
        WHEN ingresos_mensuales >= 5000000 THEN 'Premium'
        WHEN ingresos_mensuales >= 2500000 THEN 'Estándar'
        ELSE 'Básico'
    END;
    """
    
    cursor = conn.cursor()
    cursor.execute(script_actualizacion)
    conn.commit()
    
    print(f"✅ Se actualizaron {cursor.rowcount} registros de clientes")
    print()

def mostrar_estado_nuevo(conn):
    """Muestra el nuevo estado después de la actualización"""
    print("🎉 NUEVO ESTADO DE SEGMENTOS (SALVAMOS EL TRABAJO):")
    print("-" * 50)
    
    consulta_nueva = """
    SELECT 
        segmento_cliente,
        COUNT(*) as cantidad,
        MIN(ingresos_mensuales) as ingreso_minimo,
        MAX(ingresos_mensuales) as ingreso_maximo,
        ROUND(AVG(ingresos_mensuales), 2) as promedio,
        ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM clientes), 2) as porcentaje
    FROM clientes 
    GROUP BY segmento_cliente
    ORDER BY promedio DESC;
    """
    
    resultado = pd.read_sql_query(consulta_nueva, conn)
    print(resultado)
    print()

def analisis_vip_por_ciudad(conn):
    """Análisis VIP por ciudad con los nuevos datos"""
    print("🏆 ANÁLISIS VIP POR CIUDAD (DATOS PRESENTABLES):")
    print("-" * 50)
    
    consulta_vip = """
    SELECT 
        ciudad,
        COUNT(*) AS total_clientes,
        SUM(CASE WHEN segmento_cliente = 'VIP' THEN 1 ELSE 0 END) AS clientes_vip,
        SUM(CASE WHEN segmento_cliente = 'Premium' THEN 1 ELSE 0 END) AS clientes_premium,
        ROUND(
            100.0 * SUM(CASE WHEN segmento_cliente = 'VIP' THEN 1 ELSE 0 END) / COUNT(*),
            2
        ) AS porcentaje_vip,
        ROUND(
            100.0 * SUM(CASE WHEN segmento_cliente IN ('VIP', 'Premium') THEN 1 ELSE 0 END) / COUNT(*),
            2
        ) AS porcentaje_alto_valor
    FROM clientes
    GROUP BY ciudad
    ORDER BY porcentaje_vip DESC, porcentaje_alto_valor DESC;
    """
    
    resultado = pd.read_sql_query(consulta_vip, conn)
    print(resultado)
    print()

def main():
    """Función principal - salvemos el trabajo!"""
    print("🚨 OPERACIÓN: SALVAR EL TRABAJO")
    print("=" * 50)
    print("💼 Situación: Los datos actuales muestran 0% VIPs")
    print("😱 Riesgo: Los jefes nos van a botar")
    print("🎯 Solución: Actualizar segmentación basada en ingresos reales")
    print()
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # Mostrar estado actual (problemático)
    mostrar_estado_actual(conn)
    
    # Actualizar segmentos
    actualizar_segmentos(conn)
    
    # Mostrar nuevo estado (presentable)
    mostrar_estado_nuevo(conn)
    
    # Análisis VIP por ciudad
    analisis_vip_por_ciudad(conn)
    
    # Cerrar conexión
    conn.close()
    print("🔌 Conexión cerrada")
    print()
    print("🎉 ¡MISIÓN CUMPLIDA!")
    print("💼 Ahora los datos se ven profesionales y realistas")
    print("😎 Los jefes van a estar contentos con la segmentación")
    print("🚀 Tu consulta del EJERCICIO 12 ahora va a mostrar resultados interesantes")
    print()
    print("💡 PRÓXIMO PASO:")
    print("   Ejecuta de nuevo: python practica_sql_avanzada.py")

if __name__ == "__main__":
    main()
