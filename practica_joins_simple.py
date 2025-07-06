#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔄 PRÁCTICA SQL BANCARIA - JOINS SIMPLIFICADA
============================================

Práctica paso a paso de JOINs con verificaciones
"""

import sqlite3

def main():
    print("🚀 PRÁCTICA SQL BANCARIA - JOINS")
    print("=" * 50)
    
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('data/banking_core.db')
        print("✅ Conectado a la base de datos bancaria")
        
        # Verificar tablas
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"📋 Tablas encontradas: {[table[0] for table in tables]}")
        
        # Verificar estructura de cuentas
        cursor.execute("PRAGMA table_info(cuentas)")
        columns = cursor.fetchall()
        print(f"🔍 Columnas de 'cuentas': {[col[1] for col in columns]}")
        
        # EJERCICIO 1: INNER JOIN básico
        print("\n🎯 EJERCICIO 1: INNER JOIN - Clientes VIP con cuentas")
        print("-" * 60)
        
        consulta1 = """
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
        
        cursor.execute(consulta1)
        resultados = cursor.fetchall()
        
        if resultados:
            print("✅ Resultados:")
            for row in resultados:
                print(f"   {row}")
            print(f"📊 Total: {len(resultados)} registros")
        else:
            print("❌ No se encontraron resultados")
            
        # EJERCICIO 2: LEFT JOIN - Todos los clientes
        print("\n🎯 EJERCICIO 2: LEFT JOIN - Patrimonio por cliente")
        print("-" * 60)
        
        consulta2 = """
        SELECT 
            c.nombres || ' ' || c.apellidos AS cliente,
            c.segmento_cliente,
            COUNT(cu.cuenta_id) as cantidad_cuentas,
            COALESCE(SUM(cu.saldo_actual), 0) as total_patrimonio
        FROM clientes c
        LEFT JOIN cuentas cu ON c.cliente_id = cu.cliente_id
        GROUP BY c.cliente_id, c.nombres, c.apellidos, c.segmento_cliente
        ORDER BY total_patrimonio DESC
        LIMIT 10;
        """
        
        cursor.execute(consulta2)
        resultados = cursor.fetchall()
        
        if resultados:
            print("✅ Top 10 clientes por patrimonio:")
            for i, row in enumerate(resultados, 1):
                print(f"   {i:2d}. {row[0]:25s} | {row[1]:8s} | Cuentas: {row[2]} | ${row[3]:,}")
        else:
            print("❌ No se encontraron resultados")
            
        conn.close()
        print("\n🔌 Conexión cerrada")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    print("\n🎉 ¡Ejemplos completados!")
    print("\n💡 CONCEPTOS APRENDIDOS:")
    print("   • INNER JOIN: Solo registros que coinciden en ambas tablas")
    print("   • LEFT JOIN: Todos los de la izquierda + coincidencias")
    print("   • GROUP BY: Agrupa para hacer sumas y conteos")
    print("   • COALESCE: Maneja valores NULL")

if __name__ == "__main__":
    main()
