#!/usr/bin/env python3
import sqlite3
import os

print("🔍 Verificando base de datos...")

db_path = "data/banking_core.db"

if os.path.exists(db_path):
    print(f"✅ Base de datos encontrada: {db_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Verificar tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tablas = cursor.fetchall()
    
    print(f"\n📊 TABLAS ENCONTRADAS ({len(tablas)}):")
    for tabla in tablas:
        cursor.execute(f"SELECT COUNT(*) FROM {tabla[0]}")
        count = cursor.fetchone()[0]
        print(f"  ✅ {tabla[0]}: {count:,} registros")
    
    conn.close()
    print("\n🎉 ¡Base de datos verificada exitosamente!")
else:
    print(f"❌ No se encontró la base de datos: {db_path}")
