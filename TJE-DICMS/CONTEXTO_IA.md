["Use o texto abaixo para preencher o arquivo 'TJE-DICMS/Documentacao_Tecnica.md' integralmente, substituindo os espaços reservados ([#  PROJETO DICMS  DOCUMENTAÇÃO TÉCNICA E EVOLUÇÃO

---

## 1.  Objetivo do Projeto

Gerar o layout oficial de carga de beneficiários do DICMS a partir da integração de múltiplas fontes de dados:

- Base de alunos (DB2)
- CadÚnico (CSV massivo)
- Dados complementares (ISE)

Aplicando regras de elegibilidade e definição correta do responsável familiar.

---

## 2.  Arquitetura do Pipeline

O pipeline é dividido em 5 fases principais:

---

###  Fase 1  Leitura DB2

- Extração dos alunos
- Normalização de dados:
  - CPF
  - Nome
  - Nome da mãe
- Volume médio:
  - ~249.000 registros

---

###  Fase 2  Integração CadÚnico

- Leitura de CSV massivo
- Normalização:
  - CPF
  - Nome
  - Nome da mãe
- Identificação de famílias (`COD_FAM`)

---

###  Fase 3  Chaves de Mapeamento

Aplicação sequencial de regras:

- CPF direto
- Nome + mãe
- Nome + data de nascimento
- Combinações adicionais

Resultado:

- ~144.000 mapeados
- ~104.000 não mapeados

---

###  Fase 4  Regras de Negócio

####  Regra de Renda

- Corte:  660
- Resultado:
  - ~94.000 elegíveis
  - ~50.000 removidos

---

####  Regra de Município

- Ajuste via base ISE
- Sem impacto significativo de perda

---

###  Fase 5  Geração Layout DICMS

Campos finais gerados:

- `COD_CPF`
- `NOME_BENEFICIARIO`
- `DT_NASC_BENEFICIARIO`
- `NOME_MAE_BENEFICIARIO`
- `COD_MUNIC_IBGE`
- Endereço completo
- Telefones
- Email
- `VLR_RENDA_MEDIA`
- `ORIGEM_CPF`
- `CPF_RESP`

Total final:

- ~94.000 registros

---

## 3.  Evolução do Projeto

| Etapa | Resultado |
|------|----------|
| Script original | ~96.000 |
| Primeira versão app | ~94.000 |
| Diferença inicial | 5.193 |
| Versão atual | ~2.071 |

 Redução significativa de divergência

---

## 4.  Principais Problemas Encontrados

---

### 4.1 Problemas de Encoding

**Problema:**
- Acentuação corrompida (Ã, ç, etc.)

**Solução:**
- Uso de `utf-8-sig` no CSV final

---

### 4.2 CPF Inconsistente

Problemas identificados:

- CPFs inválidos
- CPFs incompletos
- CPFs zerados
- CPFs com formatação irregular

Impacto:

- Falha de match
- Divergência com script
- Registros descartados

---

### 4.3 Responsável Familiar (Problema Principal)

**Regra correta:**

Problemas encontrados:

- Escolha incorreta do responsável
- Uso de CPF errado dentro da família
- Inconsistência entre script e aplicação

Impacto:

- Divergência em `ORIGEM_CPF`
- Diferença entre outputs

---

### 4.4 Estrutura do CadÚnico

Problemas:

- CSV muito grande
- Colunas inconsistentes
- Parsing instável

Impacto:

- Erros de leitura
- Perda de dados
- Dificuldade de processamento

---

### 4.5 Ordem do Pipeline

Problema recorrente:

- Aplicação de regras no momento errado

Impacto:

- Sobrescrita de CPF
- Inconsistência final
- Resultados divergentes

---

## 5.  Situação Atual

###  Métricas finais

- 94.193 CPFs em comum
- 2.071 apenas no script
- 396 apenas no app

---

###  Qualidade atual

- ~97% aderência ao script
- Pipeline funcional
- Layout válido para uso

---

## 6.  Dívida Técnica Identificada

---

###  Alta

- Regra de responsável ainda sensível a dados inconsistentes
- Dependência forte da qualidade do CadÚnico

---

###  Média

- Código duplicado em partes do pipeline
- Falta de centralização das regras de CPF

---

###  Baixa

- Logs poderiam ser mais estruturados
- Ausência de testes automatizados

---

## 7.  Conclusão Técnica

O sistema atingiu um nível de maturidade operacional adequado:

- Processamento completo
- Resultado consistente
- Diferença residual explicável por dados

---

## 8.  Recomendações Futuras

- Criar validação automática de CPF
- Centralizar regra de responsável
- Criar testes comparativos automatizados
- Versionar regras de negócio
- Criar pipeline incremental

---

## 9.  Artefatos Gerados

- `DICMS_Layout_Carga_Beneficiarios_*.csv`
- `Comparação Script vs Aplicação`
- `DEBUG_NAO_MAPEADOS`
- `DEBUG_DICMS`
- `ANALISE_FINAL`

---

## 10.  Consideração Final

O principal limitador atual não é o código, mas:

>  Qualidade e consistência dos dados de origem

---

## 11.  Status do Projeto

 Pipeline funcional  
 Resultado auditável  
 Diferença controlada  
 Pronto para uso assistido  

---

## 12.  Resumo Executivo

- Problema complexo de integração de dados
- Forte dependência de qualidade externa (CadÚnico)
- Evolução consistente ao longo do projeto
- Resultado final confiável dentro do cenário real

---
]):"]
