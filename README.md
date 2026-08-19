S.Pr.E.M.E. - Solucionador de Projetos de Evaporadores de Múltiplos Efeitos
Uma ferramenta computacional didática desenvolvida em Python para auxiliar a resolução de exercícios de Engenharia envolvendo o dimensionamento de evaporadores de múltiplos efeitos (EME).

🚀 Funcionalidades
Dimensionamento de sistemas de 1 a 5 efeitos.
Interface reativa e intuitiva para inserção de dados e visualização de equações (Streamlit).
Resolução automática de balanços de massa e energia via álgebra linear (NumPy).
Ajuste iterativo automático de temperatura baseado em erro na convergência da área de troca térmica.
Cálculo de economia global de vapor.

🛠️ Tecnologias Utilizadas
Python 3.11
NumPy: Processamento de matrizes e sistemas lineares.
Pandas: Manipulação de dados e propriedades de saturação.
Streamlit: Criação da interface web e visualização de dados.
Pillow: Processamento de imagens.

📈 Referência
Esta ferramenta origina do Trabalho de Conclusão de Curso: 
ALMEIDA, Pedro Henrique Martins de; CHAGURI, Lívia. S.Pr.E.M.E.: Solucionador de Projetos de Evaporadores de Múltiplos Efeitos.

💻 Como Executar Localmente
Clone o repositório: git clone https://github.com/pedrohlmalmeida/EvaporadorME.git
Instale as dependências: pip install -r requirements.txt
Execute o app: streamlit run app.py
