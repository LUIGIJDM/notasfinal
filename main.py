import click
import app

@click.group()
def comandos():
    pass

@click.command()
@click.option("--prueba_corta", prompt = "ingrese la nota de la prueba corta", type = int, help = "este comando te ayuda a calcular la nota de la prueba corta, este valorer es numerico no alfabetico")
def pruebacorta(prueba_corta):
    resultado = app.pruebacorta(prueba_corta)
    print(resultado)

#resultado de la prueba parcial
@click.command()
@click.option("--prueba_parcial", prompt = "ingrese la nota de la prueba parcial", type = int, help = "este comando te ayuda a calcular la nota de la prueba parcial, este valorer es numerico no alfabetico")
def pruebaparcial(prueba_parcial):
    resultado = app.pruebaparcial(prueba_parcial)
    print(resultado)

comandos.add_command(pruebacorta)
comandos.add_command(pruebaparcial)

if __name__== "__main__":
    comandos()