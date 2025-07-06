#!/usr/bin/env python3
"""
🏦 PRÁCTICA SQL BANCARIA: AGREGACIONES Y GROUP BY
Dominio de funciones de agregación aplicadas al análisis bancario

Autor: Analista SQL Bancario
Fecha: Julio 2025
Nivel: INTERMEDIO-AVANZADO ⭐⭐⭐⭐
"""

import sqlite3
import sys
import os

# Configuración de la base de datos
DB_PATH = "../../data/banking_core.db"

def conectar_bd():
    """Establece conexión con la base de datos bancaria"""
    try:
        if not os.path.exists(DB_PATH):
            raise FileNotFoundError(f"Base de datos no encontrada: {DB_PATH}")
        
        conn = sqlite3.connect(DB_PATH)
        print("✅ Conexión exitosa a banking_core.db")
        return conn
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

def ejecutar_consulta(conn, consulta, titulo, contexto=""):
    """Ejecuta una consulta y muestra resultados formateados"""
    print(f"\n{'='*80}")
    print(f"📊 {titulo}")
    print(f"{'='*80}")
    
    if contexto:
        print(f"🎯 Contexto: {contexto}")
        print()
    
    print("🔍 SQL:")
    print(consulta)
    print()
    
    try:
        cursor = conn.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        
        if resultados:
            print("📈 Resultados:")
            for i, fila in enumerate(resultados, 1):
                if len(fila) == 1:
                    print(f"   {fila[0]}")
                else:
                    print(f"   {i}. {' | '.join(map(str, fila))}")
        else:
            print("📭 Sin resultados")
            
        print(f"\n✅ Consulta ejecutada exitosamente ({len(resultados)} registros)")
        return resultados
        
    except sqlite3.Error as e:
        print(f"❌ Error SQL: {e}")
        return None

def main():
    """Función principal que ejecuta todos los ejercicios de agregaciones"""
    
    print("""
🏦 PRÁCTICA SQL BANCARIA: AGREGACIONES Y GROUP BY
==================================================
Dominio de funciones de agregación para análisis bancario
    
📋 Ejercicios incluidos:
   1-4:   Funciones básicas (COUNT, SUM, AVG, MAX, MIN)
   5-8:   GROUP BY por segmento, producto y sucursal  
   9-12:  Análisis avanzado con HAVING y múltiples dimensiones
    """)
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    try:
        # ================================================================
        # EJERCICIOS 1-4: FUNCIONES BÁSICAS DE AGREGACIÓN
        # ================================================================
        
        ejercicio_1 = """
        SELECT COUNT(*) as total_clientes 
        FROM clientes;
        """
        ejecutar_consulta(conn, ejercicio_1, 
                         "EJERCICIO 1: Total de Clientes",
                         "Métrica fundamental para reportes ejecutivos diarios")
        
        ejercicio_2 = """
        SELECT SUM(saldo_actual) as saldo_total 
        FROM cuentas;
        """
        ejecutar_consulta(conn, ejercicio_2, 
                         "EJERCICIO 2: Saldo Total del Banco",
                         "Volumen total de recursos bajo administración")
        
        ejercicio_3 = """
        SELECT AVG(saldo_actual) as saldo_promedio 
        FROM cuentas;
        """
        ejecutar_consulta(conn, ejercicio_3, 
                         "EJERCICIO 3: Saldo Promedio",
                         "Concentración promedio de saldos por cuenta")
        
        ejercicio_4 = """
        SELECT MAX(saldo_actual) as saldo_maximo, 
               MIN(saldo_actual) as saldo_minimo 
        FROM cuentas;
        """
        ejecutar_consulta(conn, ejercicio_4, 
                         "EJERCICIO 4: Mayor y Menor Saldo",
                         "Rangos de concentración de riqueza")
        
        # ================================================================
        # EJERCICIOS 5-8: GROUP BY POR DIMENSIONES CLAVE
        # ================================================================
        
        ejercicio_5 = """
        SELECT segmento_cliente, COUNT(*) as total_cuentas
        FROM clientes c
        JOIN cuentas cu ON c.cliente_id = cu.cliente_id
        GROUP BY segmento_cliente;
        """
        ejecutar_consulta(conn, ejercicio_5, 
                         "EJERCICIO 5: Cuentas por Segmento",
                         "Distribución de productos por segmento de cliente")
        
        ejercicio_6 = """
        SELECT segmento_cliente, SUM(saldo_actual) as patrimonio_total
        FROM clientes c
        JOIN cuentas cu ON c.cliente_id = cu.cliente_id
        GROUP BY segmento_cliente
        ORDER BY patrimonio_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_6, 
                         "EJERCICIO 6: Patrimonio por Segmento",
                         "Concentración de patrimonio por tipo de cliente")
        
        ejercicio_7 = """
        SELECT pf.nombre_producto, COUNT(*) as total_cuentas, 
               SUM(cu.saldo_actual) as volumen_total
        FROM productos_financieros pf
        JOIN cuentas cu ON pf.producto_id = cu.producto_id
        GROUP BY pf.producto_id, pf.nombre_producto
        ORDER BY volumen_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_7, 
                         "EJERCICIO 7: Análisis por Producto Financiero",
                         "Performance y adopción de productos financieros")
        
        ejercicio_8 = """
        SELECT s.nombre_sucursal, COUNT(cu.cuenta_id) as total_cuentas,
               SUM(cu.saldo_actual) as saldo_total
        FROM sucursales s
        JOIN cuentas cu ON s.sucursal_id = cu.sucursal_id
        GROUP BY s.sucursal_id, s.nombre_sucursal
        ORDER BY saldo_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_8, 
                         "EJERCICIO 8: Concentración por Sucursal",
                         "Distribución geográfica de recursos y clientes")
        
        # ================================================================
        # EJERCICIOS 9-12: ANÁLISIS AVANZADO CON HAVING
        # ================================================================
        
        ejercicio_9 = """
        SELECT tipo_transaccion, COUNT(*) as cantidad_transacciones,
               SUM(monto) as volumen_total
        FROM transacciones
        GROUP BY tipo_transaccion
        ORDER BY volumen_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_9, 
                         "EJERCICIO 9: Transacciones por Tipo",
                         "Patrones de comportamiento transaccional")
        
        ejercicio_10 = """
        SELECT c.segmento_cliente, COUNT(p.prestamo_id) as total_prestamos,
               SUM(p.monto_aprobado) as exposicion_total
        FROM clientes c
        JOIN prestamos p ON c.cliente_id = p.cliente_id
        GROUP BY c.segmento_cliente
        ORDER BY exposicion_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_10, 
                          "EJERCICIO 10: Préstamos por Segmento",
                          "Exposición crediticia por segmento de cliente")
        
        ejercicio_11 = """
        SELECT segmento_cliente, SUM(saldo_actual) as patrimonio_total
        FROM clientes c
        JOIN cuentas cu ON c.cliente_id = cu.cliente_id
        GROUP BY segmento_cliente
        HAVING SUM(saldo_actual) > 5000000
        ORDER BY patrimonio_total DESC;
        """
        ejecutar_consulta(conn, ejercicio_11, 
                          "EJERCICIO 11: Segmentos con Alto Patrimonio (HAVING)",
                          "Segmentos que superan umbrales VIP ($5M+)")
        
        ejercicio_12 = """
        SELECT pf.nombre_producto, COUNT(*) as total_cuentas
        FROM productos_financieros pf
        JOIN cuentas cu ON pf.producto_id = cu.producto_id
        GROUP BY pf.producto_id, pf.nombre_producto
        HAVING COUNT(*) > 1
        ORDER BY total_cuentas DESC;
        """
        ejecutar_consulta(conn, ejercicio_12, 
                          "EJERCICIO 12: Productos con Múltiples Cuentas (HAVING)",
                          "Productos con alta adopción y penetración")
        
        # ================================================================
        # RESUMEN FINAL
        # ================================================================
        
        print(f"\n{'='*80}")
        print("🎉 ¡PRÁCTICA COMPLETADA EXITOSAMENTE!")
        print(f"{'='*80}")
        print("""
📊 CONCEPTOS DOMINADOS:
   ✅ COUNT, SUM, AVG, MAX, MIN
   ✅ GROUP BY por múltiples dimensiones
   ✅ HAVING para filtros de grupos
   ✅ ORDER BY con agregaciones
   ✅ JOINs con funciones de agregación

🏆 NIVEL ALCANZADO: INTERMEDIO-AVANZADO ⭐⭐⭐⭐

🚀 PRÓXIMO PASO: Módulo 3 - JOINs y Relaciones
        """)
        
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {e}")
    
    finally:
        if conn:
            conn.close()
            print("\n🔐 Conexión cerrada correctamente")

if __name__ == "__main__":
    main()
