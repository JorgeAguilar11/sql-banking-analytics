#!/usr/bin/env python3
"""
Setup Environment for SQL Banking Analytics Project
Configura automáticamente el entorno de desarrollo para el proyecto de BI bancario.
"""

import os
import sys
import sqlite3
import subprocess
from pathlib import Path

def print_banner():
    """Imprime el banner del proyecto."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                  🏦 SQL Banking Analytics                     ║
    ║                                                               ║
    ║             Configuración Automática del Entorno             ║
    ║                                                               ║
    ║                    Jorge Aguilar - 2025                      ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Verifica la versión de Python."""
    print("🔍 Verificando versión de Python...")
    if sys.version_info < (3, 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detectado")

def create_virtual_environment():
    """Crea el entorno virtual si no existe."""
    venv_path = Path("venv_banking_sql")
    
    if not venv_path.exists():
        print("🚀 Creando entorno virtual...")
        try:
            subprocess.run([sys.executable, "-m", "venv", "venv_banking_sql"], check=True)
            print("✅ Entorno virtual creado exitosamente")
        except subprocess.CalledProcessError:
            print("❌ Error al crear el entorno virtual")
            sys.exit(1)
    else:
        print("✅ Entorno virtual ya existe")

def install_requirements():
    """Instala las dependencias del proyecto."""
    print("📦 Instalando dependencias...")
    
    # Detectar el ejecutable de pip en el entorno virtual
    if os.name == 'nt':  # Windows
        pip_path = Path("venv_banking_sql/Scripts/pip")
    else:  # macOS/Linux
        pip_path = Path("venv_banking_sql/bin/pip")
    
    if pip_path.exists():
        try:
            subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
            print("✅ Dependencias instaladas exitosamente")
        except subprocess.CalledProcessError:
            print("❌ Error al instalar dependencias")
            print("💡 Tip: Activa el entorno virtual manualmente e instala con:")
            print("   pip install -r requirements.txt")
    else:
        print("⚠️  No se pudo encontrar pip en el entorno virtual")
        print("💡 Activa el entorno virtual manualmente e instala dependencias")

def create_database_structure():
    """Crea la estructura básica de la base de datos bancaria."""
    print("🗄️  Creando estructura de base de datos...")
    
    db_path = Path("data/banking_core.db")
    
    # SQL para crear las tablas principales
    create_tables_sql = """
    -- Tabla de Clientes
    CREATE TABLE IF NOT EXISTS clientes (
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_cliente VARCHAR(20) UNIQUE NOT NULL,
        nombres VARCHAR(100) NOT NULL,
        apellidos VARCHAR(100) NOT NULL,
        tipo_documento VARCHAR(10) NOT NULL,
        numero_documento VARCHAR(20) UNIQUE NOT NULL,
        fecha_nacimiento DATE,
        genero VARCHAR(1),
        estado_civil VARCHAR(20),
        telefono VARCHAR(20),
        email VARCHAR(100),
        direccion TEXT,
        ciudad VARCHAR(50),
        departamento VARCHAR(50),
        codigo_postal VARCHAR(10),
        ocupacion VARCHAR(100),
        ingresos_mensuales DECIMAL(15,2),
        segmento_cliente VARCHAR(50),
        fecha_vinculacion DATE NOT NULL,
        estado VARCHAR(20) DEFAULT 'ACTIVO',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de Productos Financieros
    CREATE TABLE IF NOT EXISTS productos_financieros (
        producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_producto VARCHAR(20) UNIQUE NOT NULL,
        nombre_producto VARCHAR(100) NOT NULL,
        categoria VARCHAR(50) NOT NULL, -- CUENTA_CORRIENTE, CUENTA_AHORROS, CREDITO, TARJETA_CREDITO, etc.
        descripcion TEXT,
        tasa_interes_min DECIMAL(5,4),
        tasa_interes_max DECIMAL(5,4),
        comision_manejo DECIMAL(10,2),
        monto_minimo DECIMAL(15,2),
        monto_maximo DECIMAL(15,2),
        plazo_minimo_dias INTEGER,
        plazo_maximo_dias INTEGER,
        estado VARCHAR(20) DEFAULT 'ACTIVO',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de Cuentas
    CREATE TABLE IF NOT EXISTS cuentas (
        cuenta_id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_cuenta VARCHAR(20) UNIQUE NOT NULL,
        cliente_id INTEGER NOT NULL,
        producto_id INTEGER NOT NULL,
        sucursal_id INTEGER,
        saldo_actual DECIMAL(15,2) DEFAULT 0,
        saldo_disponible DECIMAL(15,2) DEFAULT 0,
        estado VARCHAR(20) DEFAULT 'ACTIVA',
        fecha_apertura DATE NOT NULL,
        fecha_cierre DATE,
        tasa_interes DECIMAL(5,4),
        sobregiro_autorizado DECIMAL(15,2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
        FOREIGN KEY (producto_id) REFERENCES productos_financieros(producto_id)
    );

    -- Tabla de Préstamos
    CREATE TABLE IF NOT EXISTS prestamos (
        prestamo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_prestamo VARCHAR(20) UNIQUE NOT NULL,
        cliente_id INTEGER NOT NULL,
        producto_id INTEGER NOT NULL,
        monto_aprobado DECIMAL(15,2) NOT NULL,
        monto_desembolsado DECIMAL(15,2) NOT NULL,
        saldo_capital DECIMAL(15,2) NOT NULL,
        tasa_interes DECIMAL(5,4) NOT NULL,
        plazo_meses INTEGER NOT NULL,
        cuota_mensual DECIMAL(10,2) NOT NULL,
        fecha_aprobacion DATE NOT NULL,
        fecha_desembolso DATE NOT NULL,
        fecha_vencimiento DATE NOT NULL,
        estado VARCHAR(20) DEFAULT 'VIGENTE',
        dias_mora INTEGER DEFAULT 0,
        provision_requerida DECIMAL(15,2) DEFAULT 0,
        garantias TEXT,
        proposito_credito VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
        FOREIGN KEY (producto_id) REFERENCES productos_financieros(producto_id)
    );

    -- Tabla de Transacciones
    CREATE TABLE IF NOT EXISTS transacciones (
        transaccion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_transaccion VARCHAR(30) UNIQUE NOT NULL,
        cuenta_id INTEGER,
        tipo_transaccion VARCHAR(50) NOT NULL, -- DEPOSITO, RETIRO, TRANSFERENCIA, PAGO, etc.
        monto DECIMAL(15,2) NOT NULL,
        descripcion TEXT,
        fecha_transaccion TIMESTAMP NOT NULL,
        canal VARCHAR(20), -- SUCURSAL, ATM, ONLINE, MOBILE, etc.
        sucursal_id INTEGER,
        cuenta_destino VARCHAR(20),
        estado VARCHAR(20) DEFAULT 'COMPLETADA',
        comision DECIMAL(10,2) DEFAULT 0,
        impuesto DECIMAL(10,2) DEFAULT 0,
        saldo_anterior DECIMAL(15,2),
        saldo_posterior DECIMAL(15,2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cuenta_id) REFERENCES cuentas(cuenta_id)
    );

    -- Tabla de Sucursales
    CREATE TABLE IF NOT EXISTS sucursales (
        sucursal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_sucursal VARCHAR(10) UNIQUE NOT NULL,
        nombre_sucursal VARCHAR(100) NOT NULL,
        direccion TEXT NOT NULL,
        ciudad VARCHAR(50) NOT NULL,
        departamento VARCHAR(50) NOT NULL,
        telefono VARCHAR(20),
        gerente VARCHAR(100),
        tipo_sucursal VARCHAR(20), -- PRINCIPAL, SECUNDARIA, AGENCIA
        fecha_apertura DATE,
        estado VARCHAR(20) DEFAULT 'ACTIVA',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de Balance General (para KPIs)
    CREATE TABLE IF NOT EXISTS balance_general (
        balance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_balance DATE NOT NULL,
        efectivo_bancos DECIMAL(15,2) DEFAULT 0,
        inversiones DECIMAL(15,2) DEFAULT 0,
        cartera_creditos DECIMAL(15,2) DEFAULT 0,
        provision_cartera DECIMAL(15,2) DEFAULT 0,
        activos_fijos DECIMAL(15,2) DEFAULT 0,
        otros_activos DECIMAL(15,2) DEFAULT 0,
        total_activos DECIMAL(15,2) DEFAULT 0,
        depositos_vista DECIMAL(15,2) DEFAULT 0,
        depositos_plazo DECIMAL(15,2) DEFAULT 0,
        obligaciones_financieras DECIMAL(15,2) DEFAULT 0,
        otros_pasivos DECIMAL(15,2) DEFAULT 0,
        total_pasivos DECIMAL(15,2) DEFAULT 0,
        capital_social DECIMAL(15,2) DEFAULT 0,
        reservas DECIMAL(15,2) DEFAULT 0,
        utilidades_retenidas DECIMAL(15,2) DEFAULT 0,
        total_patrimonio DECIMAL(15,2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabla de Estado de Resultados (para KPIs)
    CREATE TABLE IF NOT EXISTS estado_resultados (
        resultado_id INTEGER PRIMARY KEY AUTOINCREMENT,
        periodo DATE NOT NULL,
        ingresos_financieros DECIMAL(15,2) DEFAULT 0,
        gastos_financieros DECIMAL(15,2) DEFAULT 0,
        margen_financiero DECIMAL(15,2) DEFAULT 0,
        ingresos_comisiones DECIMAL(15,2) DEFAULT 0,
        gastos_operacionales DECIMAL(15,2) DEFAULT 0,
        provisiones DECIMAL(15,2) DEFAULT 0,
        otros_ingresos DECIMAL(15,2) DEFAULT 0,
        otros_gastos DECIMAL(15,2) DEFAULT 0,
        utilidad_antes_impuestos DECIMAL(15,2) DEFAULT 0,
        impuestos DECIMAL(15,2) DEFAULT 0,
        utilidad_neta DECIMAL(15,2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Índices para optimización
    CREATE INDEX IF NOT EXISTS idx_clientes_documento ON clientes(numero_documento);
    CREATE INDEX IF NOT EXISTS idx_cuentas_cliente ON cuentas(cliente_id);
    CREATE INDEX IF NOT EXISTS idx_prestamos_cliente ON prestamos(cliente_id);
    CREATE INDEX IF NOT EXISTS idx_transacciones_cuenta ON transacciones(cuenta_id);
    CREATE INDEX IF NOT EXISTS idx_transacciones_fecha ON transacciones(fecha_transaccion);
    CREATE INDEX IF NOT EXISTS idx_prestamos_estado ON prestamos(estado);
    """
    
    try:
        with sqlite3.connect(db_path) as conn:
            conn.executescript(create_tables_sql)
        print("✅ Estructura de base de datos creada exitosamente")
    except Exception as e:
        print(f"❌ Error al crear la base de datos: {e}")

def create_sample_data():
    """Crea datos de muestra para las tablas."""
    print("📊 Insertando datos de muestra...")
    
    db_path = Path("data/banking_core.db")
    
    sample_data_sql = """
    -- Productos Financieros de muestra
    INSERT OR IGNORE INTO productos_financieros (codigo_producto, nombre_producto, categoria, tasa_interes_min, tasa_interes_max, comision_manejo) VALUES
    ('CC001', 'Cuenta Corriente Empresarial', 'CUENTA_CORRIENTE', 0.0000, 0.0000, 25000.00),
    ('CA001', 'Cuenta de Ahorros Personal', 'CUENTA_AHORROS', 0.0050, 0.0100, 8000.00),
    ('CD001', 'Certificado de Depósito 90 días', 'DEPOSITO_PLAZO', 0.0400, 0.0600, 0.00),
    ('CR001', 'Crédito de Consumo', 'CREDITO_CONSUMO', 0.1200, 0.2400, 0.00),
    ('CV001', 'Crédito de Vivienda', 'CREDITO_HIPOTECARIO', 0.0800, 0.1200, 0.00),
    ('TC001', 'Tarjeta de Crédito Gold', 'TARJETA_CREDITO', 0.1800, 0.2400, 45000.00);

    -- Sucursales de muestra
    INSERT OR IGNORE INTO sucursales (codigo_sucursal, nombre_sucursal, direccion, ciudad, departamento) VALUES
    ('SUC001', 'Sucursal Principal Centro', 'Carrera 7 # 32-16', 'Bogotá', 'Cundinamarca'),
    ('SUC002', 'Sucursal Norte', 'Calle 116 # 15-23', 'Bogotá', 'Cundinamarca'),
    ('SUC003', 'Sucursal Medellín Centro', 'Carrera 49 # 50-21', 'Medellín', 'Antioquia'),
    ('SUC004', 'Sucursal Cali Sur', 'Avenida 6N # 23-45', 'Cali', 'Valle del Cauca');

    -- Balance General de muestra (último mes)
    INSERT OR IGNORE INTO balance_general (fecha_balance, efectivo_bancos, cartera_creditos, provision_cartera, total_activos, depositos_vista, depositos_plazo, total_pasivos, capital_social, total_patrimonio) VALUES
    ('2024-12-31', 50000000000, 180000000000, 9000000000, 250000000000, 120000000000, 80000000000, 210000000000, 25000000000, 40000000000);

    -- Estado de Resultados de muestra (último mes)
    INSERT OR IGNORE INTO estado_resultados (periodo, ingresos_financieros, gastos_financieros, margen_financiero, ingresos_comisiones, gastos_operacionales, utilidad_neta) VALUES
    ('2024-12-31', 8500000000, 3200000000, 5300000000, 1200000000, 4800000000, 1200000000);
    """
    
    try:
        with sqlite3.connect(db_path) as conn:
            conn.executescript(sample_data_sql)
        print("✅ Datos de muestra insertados exitosamente")
    except Exception as e:
        print(f"❌ Error al insertar datos de muestra: {e}")

def create_readme_files():
    """Crea archivos README en cada carpeta."""
    print("📝 Creando archivos de documentación...")
    
    readme_files = {
        "data/README.md": """# 📊 Data Directory
        
Este directorio contiene:
- `banking_core.db`: Base de datos principal SQLite
- `sql_scripts/`: Scripts SQL de creación y mantenimiento
- `sample_data/`: Archivos CSV y datos de muestra
        """,
        
        "notebooks/README.md": """# 📓 Notebooks Directory

Notebooks interactivos organizados por módulos:

- `01_fundamentos_sql/`: SELECT, WHERE, ORDER BY, LIMIT
- `02_agregaciones_groupby/`: GROUP BY, COUNT, SUM, AVG
- `03_joins_relaciones/`: INNER JOIN, LEFT JOIN, relaciones
- `04_kpis_bancarios/`: ROA, ROE, NIM, indicadores
- `05_analisis_cartera/`: Análisis crediticio y riesgo
- `06_reportes_regulatorios/`: Compliance y reportes
- `07_casos_avanzados/`: Window functions, optimización
        """,
        
        "sql_queries/README.md": """# 🗃️ SQL Queries Directory

Scripts SQL organizados por propósito:

- `ddl/`: Data Definition Language (CREATE, ALTER, DROP)
- `dml/`: Data Manipulation Language (INSERT, UPDATE, DELETE)
- `kpis/`: Consultas específicas para KPIs bancarios
- `reports/`: Reportes y dashboards
- `analysis/`: Análisis exploratorio de datos
        """
    }
    
    for file_path, content in readme_files.items():
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"⚠️  Error al crear {file_path}: {e}")
    
    print("✅ Archivos de documentación creados")

def display_next_steps():
    """Muestra los próximos pasos al usuario."""
    next_steps = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                    🎉 CONFIGURACIÓN COMPLETA                  ║
    ╚═══════════════════════════════════════════════════════════════╝

    📋 PRÓXIMOS PASOS:

    1️⃣  Activar el entorno virtual:
        macOS/Linux: source venv_banking_sql/bin/activate
        Windows:     venv_banking_sql\\Scripts\\activate

    2️⃣  Abrir VS Code en el proyecto:
        code .

    3️⃣  Instalar extensiones recomendadas:
        - Python
        - Jupyter
        - SQLite Viewer

    4️⃣  Comenzar con el primer notebook:
        notebooks/01_fundamentos_sql/

    ╔═══════════════════════════════════════════════════════════════╗
    ║                  🏦 ¡LISTO PARA EMPEZAR!                     ║
    ║                                                               ║
    ║        Tu entorno de BI bancario está configurado            ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(next_steps)

def main():
    """Función principal del script de configuración."""
    print_banner()
    
    # Verificar requisitos
    check_python_version()
    
    # Configurar entorno
    create_virtual_environment()
    install_requirements()
    
    # Configurar base de datos
    create_database_structure()
    create_sample_data()
    
    # Crear documentación
    create_readme_files()
    
    # Mostrar próximos pasos
    display_next_steps()

if __name__ == "__main__":
    main()
