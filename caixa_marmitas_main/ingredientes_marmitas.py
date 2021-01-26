import date_and_time as dt

segunda = (
    "Arroz, Feijão, Farofa, Bisteca de Porco,\n"+
    "Carne moída com batata, Calabresa acebolada.\n"+
    "Refogado de repolho com cenoura.\n"+
    "Frio: Alface e Tomate."
    )

terca = (
    "Arroz, Feijão, Lasanha,\n"+
    "Linguiça, Frango frito.\n"+
    "Frio: Repolho."
    )

quarta = (
    "Arroz, Feijão, Creme de Milho,\n"+
    "Filé de frango, Farofa, Nhoque.\n"+
    "Frio: Alface, Tomate.")

# this one may be too long. TODO: check later
quinta = (
    "Arroz, Feijão, Refogado, Carne de Panela c/ Batata,\n"+
    "Calabresa Acebolada, Linguiça assada no forno.\n"+
    "Frio: Alface e Tomate."
    )

sexta = (
    "Arroz, Feijão, Macarrão ao Molho Vermelho,\n"+
    "Escondidinho de Carne, Frango ao molho.\n"+
    "Frio: Beterraba."
    )

sabado = (
    "Arroz, Feijão, Feijoada, Bife, Couve,\n"+
    "Farofa, Torresmo.\n"+
    "Acrescimo de R$ 2,00 P/\n"+
    "marmita com feijoada")

domingo = "Nenhum."

# ingredientes_do_dia = [segunda, terca, quarta, quinta, sexta, sabado]

ingredientes_do_dia = {
    "SEGUNDA":segunda,
    "TERÇA":terca,
    "QUARTA":quarta,
    "QUINTA":quinta,
    "SEXTA":sexta,
    "SÁBADO":sabado,
    "DOMINGO":domingo
}

def get_today_ingredients():
    return ingredientes_do_dia[dt.get_today_weekday_in_PT()]
