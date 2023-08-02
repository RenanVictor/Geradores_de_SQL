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

## 3. Versão fase BETA para teste com usuários (*Finalizado 2022-02-17*)

* [X] Conseguir ler o usuário que está usando o programa **log_usuario.py**
* [X] Criar tabela para armazenar os logs de finalização por usuário **tabela postgre log_usuario**
* [X] Desenvolver executável para o programa (*<https://datatofish.com/executable-pyinstaller/>*)
* [X] Corrigir problema de quando encontrar mais de uma chave para a ordem informada (*Correção não testada*)
* [X] Armazenar todos os registros enviados para finalizar itens para a tabela *log_usuario*
* [X] Gerar o insert através da lista de registros

### 3.1 melhorias e atualizações

* O campo do combobox_banco passa de Laser para plan_laser (nome íntegro da tabela)

## 4. Lançamento para usuário final com acomnpanhamentos (*Aguardando*)

* [X] Adicionado o recurso de finalizar itens componentes no programa **2023-07-14**.
* [X] Trazer os histórico de registros por usuário sempre que abrir o programa (últimos 5 registros) **2023-07-17**
* [X] Melhorar o código para as futuras implementações de novos recursos
* [ ] Melhorar a visualização do histórico de registros do usuário.
* [X] Incluir as GUI nas abas para escolher as opções. **2023-07-18**

### 4.1 melhorias e atualizações

* Atualizar o executável.
* Testar a função de cancelar item Finalizado.

## 5. Criar a interface para alterar o estado dos itens de acordo com o banco escolhido

* [X] criar a janela com o designe e opções de alteração de estado. **2023-07-19**
* [X] o Combobox terá que buscar todos os estados encontrado no banco de acordo com o banco escolhido.**2023-07-19**
* [X] Desenvolver o lançamento no banco para alteração do estado do item. **2023-07-21**
* [ ] Implementar no dict do banco, a informação da interface que pode ser usado.
   ``` python
    ex. pedidos = {'usado':['interface_estado','interface_finalizar']}
   ```
* [ ] Criar uma consulta dos itens por tipo e estado.
* [ ] Limitar estados e criar tratamento de erro.
* [ ] utilizar o método de validação de uma forma mais abrangente, redefinir a função.

## **Testes**

* ### **2022-01-25** - Consertado e testado a geração de atualização dos itens para o banco de dados *Laser*

* ### **2022-01-27** - Realizado mais testes e corrigidos alguns erros de validação

* ### **2022-02-01** - Testado as funções implementadas para a versão inicial 2.0 para o banco pedidos, Montado o fluxograma da função Finalizar

* ### **2022-02-02** - Testado as funções implementadas para a versão inicial 2.0 para o banco plan_laser

* ### **2022-02-03** - Acertado e testado funcionalizadde do botão cancelar para o banco *pedidos*
