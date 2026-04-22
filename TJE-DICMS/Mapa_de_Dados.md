---
projeto: TJE-DICMS
status: ativo
analista: Fabiano
ultima_revisao: 2026-04-22
---

# Mapa de Dados

| Campo            | Descrição                      | Regra de Validação                  |
|------------------|--------------------------------|-------------------------------------|
| COD_CPF          | Código do CPF                  | Deve ser único e válido             |
| NOME_BENEFICIARIO| Nome do Beneficiário           | Não pode estar vazio                |
| DT_NASC          | Data de Nascimento             | Formato DD/MM/AAAA                  |
| NOME_MAE         | Nome da Mãe                    | Não pode estar vazio                |
| COD_MUNIC_IBGE   | Código do Município IBGE       | Deve ser um código IBGE válido      |
| Endereço         | Endereço Completo              | Não pode estar vazio                |
| Telefones        | Telefones de Contato           | Pelo menos um telefone válido       |
| Email            | Endereço de Email              | Deve ser um email válido            |
| VLR_RENDA_MEDIA  | Valor da Renda Média           | Deve ser um valor numérico          |
| ORIGEM_CPF       | Origem do CPF                  | Deve ser especificada               |
| CPF_RESP         | CPF do Responsável             | Deve ser válido e não nulo          |
