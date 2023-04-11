# Boas-vindas ao meu repositório do Inventory Reports

Aqui você vai encontrar os detalhes de como estruturei e desenvolvi o projeto.

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />
    
Neste projeto utilizei a Programação Orientada a Objetos! Implementei um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

  <strong>🚵 Habilidades que foram trabalhadas:</strong>
 

  <ul>
    <li>Aplicado conceitos de Orientação a Objetos em Python;</li>
    <li>Aplicado padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (CSV, JSON, XML).</li>
  </ul>
</details>

<details>
    <summary><strong>👨‍💻 Pontos individuais que foram desenvolvidos</strong></summary><br />
- Criado um novo produto com todos os atributos corretamente preenchidos
- O método generate da classe SimpleReport e CompleteReport, retornam todas informações do relatório simples ou completo (respectivamente)
- O método generate da classe SimpleReport e CompleteReport, retornam o formato correto do relatório simples ou completo (respectivamente)

- Ao importar um arquivo CSV, JSON ou XML, retorna o relatórios simples ou o completo conforme solicitado

- As classes estratégicas CsvImporter, JsonImporter e CsvImporter retornam os dados dos produtos em uma lista

- O retorno padrão de um objeto Product é um relatório sobre ele

- Ao retornar o relatório, o mesmo vem devidamente colorido

    <strong>📌💻 Pontos individuais que foram validados</strong><br />
* Foi validado que a instancia de InventoryRefactor é iterável (Iterable)
* Foi validado que é possível iterar o primeiro item da lista usando csv, json ou xml
* Foi validado que é possível receber duas fontes de dados sem sobrescrita
* Foi validado que não é possível enviar arquivo inválido

* Foi validado que o menu importa um arquivo csv, json ou xml e gera um report simples e/ou completo
* Foi validado que enviar argumentos faltantes irão gerar um erros


</details>

# Orientações
<details>
  <summary><strong>⚠ Instruções para o uso</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:ewerton-ferreira/Project-Inventory-Report.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd Project-Inventory-Report`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├── inventory_report
  │   ├── data
  │   │   ├── 🔸inventory.csv
  │   │   ├── 🔸inventory.json
  │   │   └── 🔸inventory.xml
  │   ├── importer
  │   │   ├── 🔹csv_importer.py
  │   │   ├── 🔹importer.py
  │   │   ├── 🔹json_importer.py
  │   │   └── 🔹xml_importer.py
  │   ├── inventory
  │   │   ├── 🔹inventory_iterator.py
  │   │   ├── 🔹inventory_refactor.py
  │   │   └── 🔹inventory.py
  │   │   └── 🔸product.py
  │   ├── reports
  │   │   ├── 🔸colored_report.py
  │   │   ├── 🔹complete_report.py
  │   │   └── 🔹simple_report.py
  │   └── 🔹main.py
  └── tests
  │   ├── factories
  │   │   ├── 🔸__init__.py
  │   │   └── 🔸product_factory.py
  │   ├── product
  │   │   ├── 🔸__init__.py
  │   │   └── 🔹test_product.py
  │   ├── product_report
  │   │   ├── 🔸__init__.py
  │   │   └── 🔹test_product_report.py
  │   ├── report_decorator
  │   │   ├── 🔸__init__.py
  │   │   └── 🔹test_report_decorator.py
  │   └── 🔸__init__.py
  ├── 🔹dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  └── 🔸setup.py
  ```
</details>

<details>
  <summary><strong>🎛 Proejto feito no padrão Linter</strong></summary><br />

  Para garantir a qualidade do código, utilizei neste projeto o linter `Flake8`.
  Assim o código está alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Se quiser rodá-lo localmente, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **Você também pode criar o ambiente virtual seguindo esses comandos:**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes locais</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_simple_report.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

</details>

<details>
  <summary><strong>🐳Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm inventory pytest
  ```
</details>

<details>
  <summary><strong>🛼Executando o Projeto</strong></summary>
    
  O comando a ser executado será `inventory_report`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
  <code>pip install .</code>

  Agora você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>

</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>
```
</details>
