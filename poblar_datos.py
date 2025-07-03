#!/usr/bin/env python3
import sqlite3
import random
from datetime import datetime, date, timedelta

print("📊 Poblando base de datos con datos de muestra...")

conn = sqlite3.connect("data/banking_core.db")
cursor = conn.cursor()

# 1. Insertar clientes de muestra
print("👥 Insertando clientes...")
clientes_data = [
    ("CLI001", "Ana María", "González López", "CC", "12345678", "1985-03-15", "F", "Soltero", "555-0101", "ana.gonzalez@email.com", "Calle 123 #45-67", "Bogotá", "Cundinamarca", "110111", "Ingeniera", 4500000, "Premium", "2020-01-15"),
    ("CLI002", "Carlos", "Rodríguez Pérez", "CC", "87654321", "1978-07-22", "M", "Casado", "555-0102", "carlos.rodriguez@email.com", "Carrera 45 #23-89", "Medellín", "Antioquia", "050001", "Médico", 8500000, "Premium", "2019-06-10"),
    ("CLI003", "María Elena", "Castro Silva", "CC", "11223344", "1990-11-08", "F", "Soltero", "555-0103", "maria.castro@email.com", "Avenida 68 #12-34", "Cali", "Valle", "760001", "Contadora", 3200000, "Estándar", "2021-03-20"),
    ("CLI004", "José Luis", "Martínez Torres", "CC", "44332211", "1982-05-14", "M", "Casado", "555-0104", "jose.martinez@email.com", "Calle 85 #15-42", "Barranquilla", "Atlántico", "080001", "Abogado", 5500000, "Premium", "2020-08-05"),
    ("CLI005", "Diana Patricia", "López Ramírez", "CC", "55667788", "1995-09-30", "F", "Soltero", "555-0105", "diana.lopez@email.com", "Carrera 15 #67-89", "Bucaramanga", "Santander", "680001", "Administradora", 2800000, "Estándar", "2022-01-12")
]

for cliente in clientes_data:
    cursor.execute("""
        INSERT OR REPLACE INTO clientes 
        (numero_cliente, nombres, apellidos, tipo_documento, numero_documento, fecha_nacimiento, 
         genero, estado_civil, telefono, email, direccion, ciudad, departamento, 
         codigo_postal, ocupacion, ingresos_mensuales, segmento_cliente, fecha_vinculacion, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ACTIVO')
    """, cliente)

print(f"✅ {len(clientes_data)} clientes insertados")

# 2. Insertar cuentas
print("🏦 Insertando cuentas...")
cuentas_data = [
    ("CTA001", 1, 1, 1, 1500000.00, 1500000.00, 0.02, "2020-01-20"),  # Ahorro
    ("CTA002", 1, 2, 1, 850000.00, 850000.00, 0.01, "2020-02-15"),    # Corriente
    ("CTA003", 2, 1, 2, 3200000.00, 3200000.00, 0.025, "2019-06-15"), # Ahorro
    ("CTA004", 2, 3, 2, 12500000.00, 12500000.00, 0.08, "2019-08-10"), # Inversión
    ("CTA005", 3, 1, 3, 980000.00, 980000.00, 0.02, "2021-03-25"),    # Ahorro
    ("CTA006", 4, 2, 4, 2100000.00, 2100000.00, 0.01, "2020-08-10"),  # Corriente
    ("CTA007", 4, 1, 4, 5800000.00, 5800000.00, 0.025, "2020-09-05"), # Ahorro
    ("CTA008", 5, 1, 1, 650000.00, 650000.00, 0.02, "2022-01-18")     # Ahorro
]

for cuenta in cuentas_data:
    cursor.execute("""
        INSERT OR REPLACE INTO cuentas 
        (numero_cuenta, cliente_id, producto_id, sucursal_id, saldo_actual, 
         saldo_disponible, tasa_interes, fecha_apertura, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'ACTIVA')
    """, cuenta)

print(f"✅ {len(cuentas_data)} cuentas insertadas")

# 3. Insertar préstamos
print("💰 Insertando préstamos...")
prestamos_data = [
    ("PRES001", 2, 4, 85000000.00, 85000000.00, 84200000.00, 0.12, 240, 650000.00, "2019-06-01", "2019-07-01", "2039-07-01", "Vivienda Propia"),
    ("PRES002", 4, 5, 35000000.00, 35000000.00, 28500000.00, 0.15, 60, 720000.00, "2020-12-15", "2021-01-15", "2026-01-15", "Vehículo Personal"),
    ("PRES003", 1, 6, 8000000.00, 8000000.00, 6200000.00, 0.18, 36, 280000.00, "2022-02-28", "2022-03-10", "2025-03-10", "Gastos Personales"),
    ("PRES004", 3, 4, 15000000.00, 15000000.00, 12800000.00, 0.10, 84, 220000.00, "2021-07-15", "2021-08-01", "2028-08-01", "Educación Superior")
]

for prestamo in prestamos_data:
    cursor.execute("""
        INSERT OR REPLACE INTO prestamos 
        (numero_prestamo, cliente_id, producto_id, monto_aprobado, monto_desembolsado, 
         saldo_capital, tasa_interes, plazo_meses, cuota_mensual, fecha_aprobacion, 
         fecha_desembolso, fecha_vencimiento, proposito_credito, estado, dias_mora)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'VIGENTE', 0)
    """, prestamo)

print(f"✅ {len(prestamos_data)} préstamos insertados")

# 4. Insertar transacciones (últimos 30 días)
print("💳 Insertando transacciones...")
base_date = datetime.now() - timedelta(days=30)
transacciones = []

tipos_transaccion = ["Depósito", "Retiro", "Transferencia", "Pago servicios", "Consignación"]
canales = ["Sucursal", "ATM", "Online", "App móvil"]

for i in range(50):  # 50 transacciones de muestra
    fecha = base_date + timedelta(days=random.randint(0, 30))
    cuenta_id = random.randint(1, 8)
    tipo = random.choice(tipos_transaccion)
    
    if tipo in ["Depósito", "Consignación"]:
        monto = random.randint(100000, 2000000)
    else:
        monto = -random.randint(50000, 1500000)
    
    canal = random.choice(canales)
    sucursal_id = random.randint(1, 4)
    
    # Simular saldos
    saldo_anterior = random.randint(500000, 5000000)
    saldo_posterior = saldo_anterior + monto
    
    transacciones.append((
        f"TXN{i+1:03d}",
        cuenta_id,
        tipo,
        monto,
        f"Transacción {tipo} #{i+1}",
        fecha.strftime("%Y-%m-%d %H:%M:%S"),
        canal,
        sucursal_id,
        saldo_anterior,
        saldo_posterior
    ))

for txn in transacciones:
    cursor.execute("""
        INSERT OR REPLACE INTO transacciones 
        (numero_transaccion, cuenta_id, tipo_transaccion, monto, descripcion, 
         fecha_transaccion, canal, sucursal_id, saldo_anterior, saldo_posterior, 
         estado, comision, impuesto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'COMPLETADA', 0, 0)
    """, txn)

print(f"✅ {len(transacciones)} transacciones insertadas")

# Commit y cerrar
conn.commit()
conn.close()

print("\n🎉 ¡Base de datos poblada exitosamente!")
