import pandas as pd
import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen




        #-----  Funciones  -----#




# Conexión a la base de datos
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="HOST_NAME",  # Reemplazar con el nombre del host de la base de datos
            user="USER_NAME",  # Reemplazar con el nombre de usuario de la base de datos
            password="PASSWORD",  # Reemplazar con la contraseña de la base de datos
            database="DATABASE_NAME"  # Reemplazar con el nombre de la base de datos
        )
        return conn
    except mysql.connector.Error as err:
        show_error_popup(f"Error al conectar a la base de datos: {err}")
        return None




# Funciones para realizar operaciones con Pandas
def fetch_data(table_name):
    conn = create_connection()
    if conn is None:
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

    query = f"SELECT * FROM {table_name};"
    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        show_error_popup(f"Error al recuperar datos de {table_name}: {e}")
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error
    finally:
        conn.close()
    return df




# Función para mostrar DataFrame en una ventana emergente
def show_dataframe(df, title='Datos'):
    if df.empty:
        show_error_popup("No hay datos para mostrar.")
        return

    content = GridLayout(cols=1, spacing=10, size_hint_y=None)
    content.bind(minimum_height=content.setter('height'))

    for index, row in df.iterrows():
        row_label = Label(text=' | '.join(map(str, row.values)),
                            size_hint_y=None, height=30,
                            size_hint_x=1,
                            halign='center', valign='middle')
        content.add_widget(row_label)

    scroll_view = ScrollView(size_hint=(1, None), size=(600, 400))
    scroll_view.add_widget(content)

    popup = Popup(title=title, content=scroll_view, size_hint=(0.8, 0.8), pos_hint={'center_y': 0.5})
    popup.open()




#Función para mostrar errores
def show_error_popup(message):
    popup_content = BoxLayout(orientation='vertical', padding=10)
    popup_content.add_widget(Label(text=message, halign='center', size_hint_y=None, height=30))
    popup = Popup(title='Error', content=popup_content, size_hint=(0.8, 0.3), pos_hint={'center_y': 0.5})
    popup.open()




# Función para mostrar mensajes de éxito
def show_success_popup(message):
    popup_content = BoxLayout(orientation='vertical', padding=10)
    popup_content.add_widget(Label(text=message, halign='center', size_hint_y=None, height=30))
    close_button = Button(text='Cerrar', size_hint_y=None, height=50)
    close_button.bind(on_press=lambda x: popup.dismiss())
    popup_content.add_widget(close_button)
    popup = Popup(title='Éxito', content=popup_content, size_hint=(0.8, None), height=150, pos_hint={'center_y': 0.5})
    popup.open()




# Funciones de análisis y manipulación de datos
def calculate_total_sales(df):
    return df['total'].sum()


def find_top_selling_products(df, top_n=5):
    # Cambiamos la agrupación a la tabla DetallesOrden
    return df.groupby('id_producto')['cantidad'].sum().nlargest(top_n).reset_index()


def calculate_average_order_value(df):
    return df['total'].mean()


def filter_orders_by_client(df, client_id):
    return df[df['id_cliente'] == client_id]


def calculate_sales_statistics(df):
    return {
        "average": df['total'].mean(),
        "std_dev": df['total'].std(),
        "max": df['total'].max(),
        "min": df['total'].min()
    }


def get_sales_trends(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df.set_index('fecha', inplace=True)
    monthly_sales = df.resample('M')['total'].sum().reset_index()
    return monthly_sales




# Funciones de análisis y manipulación de datos avanzado
def advanced_grouping(df):
    return df.groupby(['id_cliente', 'fecha']).agg({'total': 'sum'}).reset_index()


def date_manipulation(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df.set_index('fecha')


def handle_missing_data(df):
    return df.fillna(0)  # Rellenar datos faltantes con 0


def correlation_analysis(df):
    return df.corr()  # Análisis de correlación


def export_to_csv(df, filename):
    df.to_csv(filename, index=False)
    show_success_popup(f'Datos exportados a {filename}')




        #-----  Clases  -----#




# Clase para el menú principal
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Button(text='Mostrar Datos', on_press=self.show_data))
        layout.add_widget(Button(text='Filtrar Órdenes', on_press=self.filter_orders))
        layout.add_widget(Button(text='Análisis de Ventas', on_press=self.sales_analysis))
        layout.add_widget(Button(text='Análisis Avanzado', on_press=self.advanced_analysis))

        self.add_widget(layout)


    def show_data(self, instance):
        self.manager.current = 'data'


    def filter_orders(self, instance):
        self.manager.current = 'filter'


    def update_orders(self, instance):
        self.manager.current = 'update'


    def sales_analysis(self, instance):
        self.manager.current = 'analysis'


    def advanced_analysis(self, instance):
        self.manager.current = 'advanced'




# Clase para el menú de datos
class DataMenu(Screen):
    def __init__(self, **kwargs):
        super(DataMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Button(text='Mostrar Clientes', on_press=self.display_clientes))
        layout.add_widget(Button(text='Mostrar Productos', on_press=self.display_productos))
        layout.add_widget(Button(text='Mostrar Órdenes', on_press=self.display_ordenes))
        layout.add_widget(Button(text='Regresar al Menú Principal', on_press=self.go_back))

        self.add_widget(layout)


    def display_clientes(self, instance):
        df = fetch_data('Clientes')
        show_dataframe(df)


    def display_productos(self, instance):
        df = fetch_data('Productos')
        show_dataframe(df)


    def display_ordenes(self, instance):
        df = fetch_data('Ordenes')
        show_dataframe(df)


    def go_back(self, instance):
        self.manager.current = 'main'




# Clase para el menú de filtrado de órdenes
class FilterMenu(Screen):
    def __init__(self, **kwargs):
        super(FilterMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Label(text='Filtrar Órdenes por Cliente:'))
        self.cliente_spinner = Spinner(text='Seleccionar Cliente', values=self.get_clientes())
        self.cliente_spinner.bind(text=self.on_cliente_selected)
        layout.add_widget(self.cliente_spinner)

        layout.add_widget(Button(text='Regresar al Menú Principal', on_press=self.go_back))

        self.add_widget(layout)


    def get_clientes(self):
        clientes = fetch_data('Clientes')
        return [f"{cliente['id_cliente']}: {cliente['nombre']}" for index, cliente in clientes.iterrows()]


    def on_cliente_selected(self, spinner, text):
        cliente_id = int(text.split(':')[0])
        df = fetch_data('Ordenes')
        filtered_df = filter_orders_by_client(df, cliente_id)
        show_dataframe(filtered_df, title='Órdenes del Cliente Seleccionado')


    def go_back(self, instance):
        self.manager.current = 'main'




# Clase para el menú de análisis de ventas
class SalesAnalysisMenu(Screen):
    def __init__(self, **kwargs):
        super(SalesAnalysisMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Button(text='Total de Ventas', on_press=self.show_total_sales))
        layout.add_widget(Button(text='Promedio de Órdenes', on_press=self.show_average_order_value))
        layout.add_widget(Button(text='Productos Más Vendidos', on_press=self.show_top_selling_products))
        layout.add_widget(Button(text='Tendencias de Ventas', on_press=self.show_sales_trends))
        layout.add_widget(Button(text='Regresar al Menú Principal', on_press=self.go_back))

        self.add_widget(layout)


    def show_total_sales(self, instance):
        df = fetch_data('Ordenes')
        total_sales = calculate_total_sales(df)
        show_success_popup(f'Total de Ventas: {total_sales}')


    def show_average_order_value(self, instance):
        df = fetch_data('Ordenes')
        average_order_value = calculate_average_order_value(df)
        show_success_popup(f'Valor Promedio de las Órdenes: {average_order_value}')


    def show_top_selling_products(self, instance):
        df = fetch_data('DetallesOrden')
        top_selling_products = find_top_selling_products(df)
        show_dataframe(top_selling_products, title='Productos Más Vendidos')


    def show_sales_trends(self, instance):
        df = fetch_data('Ordenes')
        sales_trends = get_sales_trends(df)
        show_dataframe(sales_trends, title='Tendencias de Ventas')


    def go_back(self, instance):
        self.manager.current = 'main'




# Clase para el menú de análisis avanzado
class AdvancedAnalysisMenu(Screen):
    def __init__(self, **kwargs):
        super(AdvancedAnalysisMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout.add_widget(Button(text='Agrupaciones Avanzadas', on_press=self.show_advanced_grouping))
        layout.add_widget(Button(text='Manipulación de Fechas', on_press=self.show_date_manipulation))
        layout.add_widget(Button(text='Manejo de Datos Faltantes', on_press=self.show_missing_data))
        layout.add_widget(Button(text='Análisis de Correlación', on_press=self.show_correlation))
        layout.add_widget(Button(text='Exportar a CSV', on_press=self.export_data))
        layout.add_widget(Button(text='Regresar al Menú Principal', on_press=self.go_back))

        self.add_widget(layout)


    def show_advanced_grouping(self, instance):
        df = fetch_data('Ordenes')
        grouped_df = advanced_grouping(df)
        show_dataframe(grouped_df, title='Agrupaciones Avanzadas')


    def show_date_manipulation(self, instance):
        df = fetch_data('Ordenes')
        manipulated_df = date_manipulation(df)
        show_dataframe(manipulated_df, title='Manipulación de Fechas')


    def show_missing_data(self, instance):
        df = fetch_data('Ordenes')
        filled_df = handle_missing_data(df)
        show_dataframe(filled_df, title='Manejo de Datos Faltantes')


    def show_correlation(self, instance):
        df = fetch_data('Ordenes')
        correlation_df = correlation_analysis(df)
        show_dataframe(correlation_df, title='Análisis de Correlación')


    def export_data(self, instance):
        df = fetch_data('Ordenes')
        export_to_csv(df, 'ordenes.csv')


    def go_back(self, instance):
        self.manager.current = 'main'




# Clase principal de la aplicación
class Pandas(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main'))
        sm.add_widget(DataMenu(name='data'))
        sm.add_widget(FilterMenu(name='filter'))
        sm.add_widget(SalesAnalysisMenu(name='analysis'))
        sm.add_widget(AdvancedAnalysisMenu(name='advanced'))
        return sm


if __name__ == '__main__':
    Pandas().run()