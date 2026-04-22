def validar_responsavel(familia):
    """
    Valida o responsável familiar priorizando o menor COD_PARENTESCO
    e garantindo que o CPF_RESP não seja nulo.

    :param familia: Lista de dicionários representando membros da família.
                    Cada dicionário deve conter as chaves 'COD_PARENTESCO' e 'CPF'.
    :return: CPF do responsável familiar.
    """
    # Filtra membros com CPF não nulo
    membros_validos = [membro for membro in familia if membro['CPF']]

    if not membros_validos:
        raise ValueError("Todos os membros da família possuem CPF nulo.")

    # Ordena por COD_PARENTESCO e seleciona o primeiro
    membro_responsavel = min(membros_validos, key=lambda x: x['COD_PARENTESCO'])

    return membro_responsavel['CPF']

if __name__ == "__main__":
    familia_teste = [
        {'COD_PARENTESCO': 1, 'CPF': None},  # Representante Legal sem CPF
        {'COD_PARENTESCO': 2, 'CPF': '12345678901'},  # Cônjuge com CPF
        {'COD_PARENTESCO': 3, 'CPF': '98765432100'}   # Filho com CPF
    ]

    cpf_responsavel = validar_responsavel(familia_teste)
    print(f"O CPF do responsável é: {cpf_responsavel}")
