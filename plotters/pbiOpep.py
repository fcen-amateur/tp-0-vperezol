import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            data = gapminder[gapminder.country.isin(['Guinea','Gabon', 'Indonesia', 'Iran', 'Iraq', 'Libya','Nigeria','Venezuela', 'Saudi Arabia', 'Congo, Rep.'])],
            x="year",
            y="gdpPercap",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Evolucion de PBI per capita de paises de la OPEP antes y despues de cada crisis del petróleo",
            x="Año",
            y="PBI Per Capita",
            color="País",
        )
    )
    return dict(
        descripcion="Evolucion del PBI en paises de la OPEP",
        autor="vperezol",
        figura=figura,
    )