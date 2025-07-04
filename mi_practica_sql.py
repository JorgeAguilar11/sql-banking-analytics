#!/usr/bin/env python3
"""
🎯 TU ARCHIVO PERSONAL DE PRÁCTICA SQL
====================================
Este es tu espacio libre para practicar SQL sin distracciones.
Solo escribe tu consulta SQL y ejecuta el archivo.

Instrucciones:
1. Escribe tu consulta SQL en la variable 'mi_consulta'
2. Guarda el archivo (Cmd+S)  
3. Ejecuta: python mi_practica_sql.py
"""

import sqlite3
import pandas as pd

def conectar_bd():
    """Conecta a la base de datos bancaria"""
    return sqlite3.connect('data/banking_core.db')

def ejecutar_consulta(conn, consulta, titulo="Resultado"):
    """Ejecuta una consulta SQL y muestra los resultados"""
    # Limpiar la consulta de comentarios y espacios
    consulta_limpia = consulta.strip()
    lineas = [l.strip() for l in consulta_limpia.split('\n') if l.strip() and not l.strip().startswith('--')]
    consulta_final = ' '.join(lineas)
    
    if not consulta_final:
        print("⚠️  Consulta vacía. Escribe tu SQL primero.")
        print("💡 Ejemplo: SELECT * FROM clientes LIMIT 5;")
        return
        
    try:
        df = pd.read_sql_query(consulta_final, conn)
        print(f"\n📊 {titulo}")
        print("-" * 50)
        print(df.to_string(index=False))
        print(f"\n✅ {len(df)} filas encontradas")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ Error en tu consulta SQL:")
        print(f"   {e}")
        print("\n💡 Verifica la sintaxis y nombres de columnas")
        print("=" * 50)

def main():
    """Tu área de práctica SQL"""
    print("🚀 PRÁCTICA SQL LIBRE")
    print("=" * 30)
    
    # Conectar a la base de datos
    conn = conectar_bd()
    
    # ===========================================
    # ✏️  ESCRIBE TU CONSULTA SQL AQUÍ
    # ===========================================
    
    mi_consulta = """
    
    -- Escribe tu consulta SQL aquí
    -- Ejemplo: SELECT * FROM clientes LIMIT 5;
    
    
    """
    
    # Ejecutar tu consulta
    ejecutar_consulta(conn, mi_consulta, "Tu consulta SQL")
    
    # ===========================================
    # 📋 INFORMACIÓN ÚTIL (opcional)
    # ===========================================
    
    # Si necesitas ver qué tablas existen, descomenta esto:
    # print("\n📋 Tablas disponibles:")
    # tablas = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    # print(tablas['name'].tolist())
    
    # Si necesitas ver las columnas de una tabla, descomenta y cambia el nombre:
    # print("\n📋 Columnas de la tabla 'clientes':")
    # info = pd.read_sql_query("PRAGMA table_info(clientes);", conn)
    # print(info[['name', 'type']].to_string(index=False))
    
    # Cerrar conexión
    conn.close()
    print("\n🔌 Conexión cerrada")

if __name__ == "__main__":
    main()
