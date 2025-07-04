import sqlite3
import pandas as pd

conn = sqlite3.connect('data/banking_core.db')

print('🏦 TABLAS Y SUS COLUMNAS:')
print('=' * 50)

# Tabla CLIENTES
print('\n📋 CLIENTES:')
info = pd.read_sql_query('PRAGMA table_info(clientes)', conn)
for _, col in info.iterrows():
    print(f'   • {col["name"]} ({col["type"]})')

# Tabla CUENTAS  
print('\n📋 CUENTAS:')
info = pd.read_sql_query('PRAGMA table_info(cuentas)', conn)
for _, col in info.iterrows():
    print(f'   • {col["name"]} ({col["type"]})')

# Tabla TRANSACCIONES
print('\n📋 TRANSACCIONES:')
info = pd.read_sql_query('PRAGMA table_info(transacciones)', conn)
for _, col in info.iterrows():
    print(f'   • {col["name"]} ({col["type"]})')

# Tabla PRESTAMOS
print('\n📋 PRESTAMOS:')
info = pd.read_sql_query('PRAGMA table_info(prestamos)', conn)
for _, col in info.iterrows():
    print(f'   • {col["name"]} ({col["type"]})')

conn.close()
