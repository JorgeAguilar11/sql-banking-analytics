import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('data/banking_core.db')

# =====================================
# ESCRIBE TU CONSULTA SQL AQUÍ:
# =====================================

mi_sql = """
SELECT * FROM clientes WHERE ciudad = 'Bogotá';
"""

# =====================================
# EJECUTAR Y VER RESULTADO:
# =====================================

resultado = pd.read_sql_query(mi_sql, conn)
print(resultado)

conn.close()
