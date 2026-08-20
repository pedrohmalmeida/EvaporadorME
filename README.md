# S.Pr.E.M.E. - Solucionador de Projetos de Evaporadores de Múltiplos Efeitos

Uma ferramenta computacional didática desenvolvida em **Python** para auxiliar a resolução de exercícios de Engenharia envolvendo o dimensionamento de evaporadores de múltiplos efeitos (EME).

## 🚀 Funcionalidades
*   **Dimensionamento Flexível:** Suporte para sistemas de 1 a 5 efeitos.
*   **Interface Reativa:** Inserção de dados e visualização de equações em tempo real via **Streamlit**.
*   **Cálculos Precisos:** Resolução automática de balanços de massa e energia utilizando álgebra linear com **NumPy**.
*   **Convergência Automática:** Ajuste iterativo de temperatura baseado no erro da área de troca térmica.
*   **Análise de Eficiência:** Cálculo da economia global de vapor do sistema.

## 🛠️ Tecnologias Utilizadas
*   **Python 3.11**
*   **NumPy:** Processamento de matrizes e sistemas lineares.
*   **Pandas:** Manipulação de dados e tabelas de saturação.
*   **Streamlit:** Framework para interface web e interatividade.
*   **Pillow:** Processamento de imagens e diagramas.

## 📈 Referência Sugerida
Esta ferramenta é o produto do Trabalho de Conclusão de Curso:

> ALMEIDA, Pedro Henrique Martins de; CARVALHO, Lívia Chaguri e. _S.Pr.E.M.E.: Uma ferramenta didática em Python para Solução de Projetos de Evaporadores de Múltiplos Efeitos_. 56 p. Trabalho de Conclusão de Curso (Graduação em Engenharia Bioquímica) – Escola de Engenharia de Lorena, Universidade de São Paulo, Lorena, 2026.

## 📚 Documentação
O **Manual do Usuário** e o **Guia Técnico** estão em fase de finalização e serão disponibilizados em breve na pasta `/docs`.

## 💻 Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/pedrohlmalmeida/EvaporadorME.git
2. **Instale as dependências:**
  pip install -r requirements.txt

3. **Execute a aplicação:**
  streamlit run app.py
