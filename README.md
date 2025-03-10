# 📊 Sistema de Análisis de Datos de Ventas con Python, Kivy, Pandas y una Base de Datos MySQL

## 📌 Descripción

Este proyecto es una aplicación de escritorio desarrollada en **Python** que permite la gestión y análisis de datos de ventas utilizando una base de datos **MySQL**. La interfaz de usuario está construida con **Kivy**, mientras que los datos son procesados y analizados con **Pandas**.

## 🚀 Características Principales

- **Conexión a MySQL**: Recuperación y manipulación de datos desde una base de datos MySQL.
- **Interfaz Gráfica con Kivy**: Navegación intuitiva con menús interactivos.
- **Análisis de Datos**: Cálculos de ventas totales, productos más vendidos y tendencias de ventas.
- **Filtros de Búsqueda**: Permite filtrar datos por clientes y fechas.
- **Manejo de Datos Faltantes**: Limpieza y normalización de datos.
- **Exportación de Datos**: Guarda los datos en formato CSV para su posterior análisis.

## 🛠 Requisitos

- **Python 3.8+**
- **MySQL**
- **pip**

### Configurar la Base de Datos

Ejecuta el script " DB.sql " en MySQL Workbench para crear la base de datos.




## 📊 Funcionalidades del Proyecto

### 🔗 Conexión a MySQL

- `create_connection()`: Establece conexión con MySQL.
- `fetch_data(table_name)`: Obtiene datos de la base de datos y los convierte en DataFrame de Pandas.

### 📈 Análisis de Ventas

- `calculate_total_sales(df)`: Calcula la suma total de ventas.
- `find_top_selling_products(df)`: Identifica los productos más vendidos.
- `calculate_average_order_value(df)`: Calcula el valor promedio de una orden.
- `filter_orders_by_client(df, client_id)`: Filtra órdenes por cliente.
- `get_sales_trends(df)`: Analiza tendencias de ventas mensuales.

### 📤 Exportación de Datos

- `export_to_csv(df, filename)`: Guarda los datos en formato CSV.

## 🎨 Interfaz de Usuario con Kivy

La aplicación cuenta con diferentes pantallas:

- **Menú Principal:** Acceso a todas las funcionalidades.
- **Visualización de Datos:** Muestra clientes, productos y órdenes.
- **Análisis de Ventas:** Muestra informes gráficos de ventas y tendencias.
- **Filtros de Datos:** Permite buscar órdenes por cliente y fecha.
