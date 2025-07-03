# 🏦 SQL Banking Analytics

## 📊 Proyecto de Entrenamiento en Business Intelligence Bancario

Este repositorio contiene un entorno completo de entrenamiento para dominar SQL aplicado al sector bancario y financiero, enfocado en el análisis de datos y KPIs del sector.

---

## 🎯 Objetivos del Proyecto

- **Dominar SQL** desde fundamentos hasta consultas avanzadas
- **Análisis de KPIs bancarios** reales: ROA, ROE, NIM, Morosidad
- **Gestión de riesgo** crediticio y análisis de cartera
- **Reportes regulatorios** y compliance
- **Mejores prácticas** en BI y análisis de datos financieros

---

## 📁 Estructura del Proyecto

```
sql-banking-analytics/
│
├── 📊 data/                          # Bases de datos y datasets
│   ├── banking_core.db              # Base de datos principal SQLite
│   ├── sql_scripts/                 # Scripts de creación de tablas
│   └── sample_data/                 # Datos de muestra y CSV
│
├── 📓 notebooks/                     # Jupyter Notebooks interactivos
│   ├── 01_fundamentos_sql/         # Módulo 1: SELECT, WHERE, ORDER BY
│   ├── 02_agregaciones_groupby/     # Módulo 2: GROUP BY, funciones
│   ├── 03_joins_relaciones/         # Módulo 3: INNER/LEFT JOIN
│   ├── 04_kpis_bancarios/          # Módulo 4: ROA, ROE, NIM
│   ├── 05_analisis_cartera/        # Módulo 5: Análisis crediticio
│   ├── 06_reportes_regulatorios/   # Módulo 6: Compliance y reportes
│   └── 07_casos_avanzados/         # Módulo 7: Casos complejos
│
├── 🗃️ sql_queries/                  # Scripts SQL organizados por tema
│   ├── ddl/                        # Data Definition Language
│   ├── dml/                        # Data Manipulation Language
│   ├── kpis/                       # Consultas de KPIs específicos
│   ├── reports/                    # Reportes y dashboards
│   └── analysis/                   # Análisis exploratorio
│
├── 📋 docs/                         # Documentación del proyecto
│   ├── banking_terminology.md      # Glosario bancario
│   ├── kpi_definitions.md          # Definiciones de KPIs
│   ├── data_dictionary.md          # Diccionario de datos
│   └── best_practices.md           # Mejores prácticas SQL
│
├── 🔧 config/                       # Configuraciones
│   ├── database_config.py          # Configuración de BD
│   └── environment_setup.md        # Setup del entorno
│
├── 🧪 tests/                        # Tests y validaciones
│   ├── data_quality_tests.sql      # Tests de calidad de datos
│   └── kpi_validation.sql          # Validación de KPIs
│
├── requirements.txt                 # Dependencias Python
├── .gitignore                      # Archivos a ignorar en Git
└── setup_environment.py           # Script de configuración automática
```

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/JorgeAguilar11/sql-banking-analytics.git
cd sql-banking-analytics
```

### 2️⃣ Configurar entorno virtual
```bash
python -m venv venv_banking_sql
source venv_banking_sql/bin/activate  # En macOS/Linux
# venv_banking_sql\Scripts\activate  # En Windows
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar la base de datos
```bash
python setup_environment.py
```

---

## 📊 Módulos de Entrenamiento

### 🎯 **Módulo 1: Fundamentos SQL**
- SELECT, WHERE, ORDER BY, LIMIT
- Filtros y ordenamientos
- ✅ **COMPLETADO**

### 📈 **Módulo 2: Agregaciones y GROUP BY**
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY y HAVING
- 🔄 **EN PROGRESO**

### 🔗 **Módulo 3: JOINs y Relaciones**
- INNER JOIN, LEFT JOIN, RIGHT JOIN
- Relaciones entre tablas bancarias

### 🏦 **Módulo 4: KPIs Bancarios Fundamentales**
- **ROA** (Return on Assets)
- **ROE** (Return on Equity)
- **NIM** (Net Interest Margin)
- **Ratio de Morosidad**

### 💳 **Módulo 5: Análisis de Cartera**
- Análisis crediticio
- Segmentación de clientes
- Gestión de riesgo

### 📋 **Módulo 6: Reportes Regulatorios**
- Reportes de compliance
- Análisis de liquidez
- Capital adequacy ratios

### 🎓 **Módulo 7: Casos Avanzados**
- Análisis temporal (time-series)
- Window functions
- Optimización de consultas

---

## 🎮 Datasets Incluidos

### 🏛️ **Core Banking System**
- **Clientes**: Datos demográficos y segmentación
- **Cuentas**: Cuentas corrientes, ahorros, plazo fijo
- **Préstamos**: Cartera crediticia completa
- **Transacciones**: Movimientos y operaciones
- **Productos**: Catálogo de productos financieros
- **Sucursales**: Red de oficinas y cajeros

### 📊 **Financial Data**
- Balances mensuales
- Estados de resultados
- Indicadores de mercado
- Ratings crediticios

---

## 🏆 KPIs y Métricas Clave

| **Categoría** | **KPI** | **Fórmula** | **Objetivo** |
|---------------|---------|-------------|--------------|
| **Rentabilidad** | ROA | Utilidad Neta / Activos Totales | > 1.5% |
| **Rentabilidad** | ROE | Utilidad Neta / Patrimonio | > 15% |
| **Eficiencia** | NIM | (Ingresos - Gastos Financieros) / Activos | > 4% |
| **Riesgo** | Morosidad | Cartera Vencida / Cartera Total | < 5% |
| **Liquidez** | LCR | Activos Líquidos / Pasivos Exigibles | > 100% |

---

## 💡 Características del Proyecto

- ✅ **Datos Realistas**: Simulación de un banco real
- ✅ **Casos Prácticos**: Ejercicios del mundo financiero
- ✅ **Notebooks Interactivos**: Aprendizaje paso a paso
- ✅ **Documentación Completa**: Glosarios y referencias
- ✅ **Control de Versiones**: Buenas prácticas con Git
- ✅ **Escalable**: Fácil extensión y personalización

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

## 👨‍💼 Autor

**Jorge Aguilar**
- 🌐 GitHub: [@JorgeAguilar11](https://github.com/JorgeAguilar11)
- 💼 LinkedIn: [Enlace a perfil]
- 📧 Email: [Tu email]

---

## 🔖 Estado del Proyecto

![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

### 🎯 **Próximos Pasos**
- [ ] Módulo 2: GROUP BY y Agregaciones
- [ ] Base de datos bancaria completa
- [ ] Dashboards interactivos
- [ ] Integración con herramientas BI

**¡Comienza tu viaje en el análisis de datos bancarios!** 🚀📊
