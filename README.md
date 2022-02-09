# Gerador de SQL

Este é um projeto simples para aprendizado pessoal.

## **Objetivo:**

### Este programa deve auxiliar na finalização das máquinas no processo produtivo de uma empresa

### Ele fará conexão direta com o banco, atualizando de forma simples e dinâmica a ferramenta **METABASE**, uma ferramenta BI

### O intuíto é que qualquer que tenha permissão atualize as máquinas prontas sem ter a necessidade de conhecer programação (SQL ou Python)

## **Status**

### Projeto em fase inicial, com apenas alguns simples recursos de sql

## 1. Versão Inicial

* O programa já tem uma janela de finalizar itens.
* Opção para os dois bancos (pedidos e laser).
* Mostra os itens finalizados enquanto o programa está rodando.
* Comunicação direta com o banco de dados (Arquivo **Conexao.py**)

## 2. Versão Inicial para usuário (*Finalizado - 2022-02-04*)

* [X] Botão para cancelar itens finalizados (*Finalizado 2022-01-25*)
* [X] Banco Laser terá a opção de máquina (*Finalizado 2022-01-26*).
* [X] Mensagem de finalizado com sucesso.
* [X] Mensagem item não encontrado.
* [X] Finalizar apenas itens na montagem (Banco Pedidos).
* [X] Ajustas os testes do botão cancelar e implementas as funções requeridas para validações.
* [X] Corrigir o bug que pode enviar máquina em branco para o banco laser

## 3. Versão fase BETA para teste com usuários (*Em desenvolvimento*)

* [ ] Ajustar a inserção de item no textfield apenas para itens realizados com sucesso.
* [X] Conseguir ler o usuário que está usando o programa **log_usuario.py**
* [ ] Criar tabela para armazenar os logs de finalização por usuário
* [ ] Desenvolver executável para o programa
* [ ] Definir os próximos recursos para a versão oficial
* [ ] Corrigir problema de quando encontrar mais de uma chave para a ordem informada (banco pedidos)

## 4. Lançamento para usuário final com acomnpanhamentos (*Aguardando*)

## **Testes**

* ### **2022-01-25** - Consertado e testado a geração de atualização dos itens para o banco de dados *Laser*

* ### **2022-01-27** - Realizado mais testes e corrigidos alguns erros de validação

* ### **2022-02-01** - Testado as funções implementadas para a versão inicial 2.0 para o banco pedidos, Montado o fluxograma da função Finalizar

* ### **2022-02-02** - Testado as funções implementadas para a versão inicial 2.0 para o banco plan_laser

* ### **2022-02-03** - Acertado e testado funcionalizadde do botão cancelar para o banco *pedidos*
