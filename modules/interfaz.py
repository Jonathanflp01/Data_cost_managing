from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint  # rprint permite imprimir con colores fácil

console = Console()


def mostrar_tabla_materiales(diccionario_materiales):
    if not diccionario_materiales:
        console.print(
            "[bold red]No hay materiales cargados o la base de datos está vacía.[/]")
        return

    # 1. Crear la tabla
    table = Table(title="Base de Datos de Materiales")

    # 2. Agregar columnas (puedes cambiar los colores)
    table.add_column("Material", style="cyan", no_wrap=True)
    table.add_column("Precio", justify="right", style="green")
    table.add_column("Unidad", style="magenta")

    # 3. TODO: Rellenar las filas
    # PISTA: Usa un bucle for sobre diccionario_materiales.items()
    # table.add_row(nombre, str(datos['precio']), datos['unidad'])

    # ... tu código aquí ...

    # 4. Imprimir tabla
    console.print(table)


def menu_principal():
    # Esto limpia la pantalla (opcional, funciona en Windows/Mac/Linux)
    console.clear()

    # Creamos un panel de bienvenida
    console.print(Panel.fit(
        "[bold blue]CivilCost Pro[/]\nSistema de Presupuestos", border_style="blue"))

    rprint("[1] 🏗️  Agregar Partida")
    rprint("[2] 📋 Ver Presupuesto Actual")
    # Esta usará la tabla de arriba
    rprint("[3] 🧱 Ver Base de Datos Materiales")
    rprint("[4] 💾 Guardar Proyecto")
    rprint("[5] 📂 Cargar Proyecto")
    rprint("[6] ❌ Salir")

    opcion = console.input("\n[bold yellow]Selecciona una opción: [/]")
    return opcion
