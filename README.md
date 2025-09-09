FIAP - Faculdade de Informática e Administração Paulista  

Nome do projeto: 🌱 Capítulo 01 - FarmTech na Era da Cloud Computing  

Nome do grupo:  

👨‍🎓 Integrantes:  
Thomaz Requena  

👩‍🏫 Professores:  
Tutor(a)  
Nome do Tutor  
Coordenador(a)  
Nome do Coordenador  

---

🌱 Capítulo 01 - FarmTech na Era da Cloud Computing  
Este projeto faz parte do **Capítulo 01** do curso, abordando o uso de **Python e modelos de Machine Learning supervisionados** para prever a produtividade agrícola (*Yield*) com base em dados climáticos. A solução explora técnicas de regressão múltipla e modelos mais avançados para identificar quais variáveis (precipitação, temperatura, umidade) impactam diferentes culturas.  

🔗 Repositório  
Acesse o projeto: [github.com/thomazrequena/Cap-1-FarmTech-na-era-da-cloud-computing](https://github.com/thomazrequena/Cap-1-FarmTech-na-era-da-cloud-computing)  

---

🎯 Objetivo  
Desenvolver um modelo de **previsão de produtividade agrícola**, com foco em:  
- Analisar dados climáticos (precipitação, umidade, temperatura).  
- Treinar e comparar 5 modelos preditivos supervisionados:  
  - Regressão Linear  
  - Ridge Regression  
  - Lasso Regression  
  - Random Forest Regressor  
  - Gradient Boosting Regressor  
- Avaliar o desempenho por cultura (`Crop`) utilizando métricas como **R², RMSE e MAE**.  
- Identificar quais variáveis têm maior impacto sobre o rendimento agrícola.  

---

🧩 Funcionalidades  
📊 **Análise Exploratória dos Dados**  
- Leitura e tratamento do dataset `crop_yield.csv`.  
- Visualização e correlação entre variáveis climáticas e `Yield`.  

🤖 **Treinamento de Modelos**  
- Implementação dos 5 modelos preditivos.  
- Validação cruzada para comparação de desempenho.  

📈 **Avaliação por Cultura**  
- Seleção do melhor modelo para cada `Crop`.  
- Ranking de variáveis mais importantes para cada cultura.  

---

🛠️ Tecnologias Utilizadas  
- **Python 3.x**  
- **Pandas** — manipulação de dados  
- **NumPy** — operações matemáticas  
- **Scikit-learn** — modelagem preditiva e métricas  
- **Matplotlib / Seaborn** — visualização de dados  

---

🗃️ Estrutura dos Dados  
📄 Arquivo: **crop_yield.csv**  
Contém os registros de culturas agrícolas e variáveis climáticas:  
- Crop (tipo de cultura)  
- Precipitation (mm/day)  
- Specific Humidity (g/kg)  
- Relative Humidity (%)  
- Temperature (°C)  
- Yield (produtividade)  

---

▶️ Como Executar o Projeto  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/thomazrequena/Cap-1-FarmTech-na-era-da-cloud-computing.git
   cd Cap-1-FarmTech-na-era-da-cloud-computing
