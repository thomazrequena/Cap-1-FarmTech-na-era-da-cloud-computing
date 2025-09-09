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

---

👉 Interpretação:

| Cultura            | R²    | MSE     | MAE     | Insight                                                                                                                        |
| ------------------ | ----- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Rice, paddy**    | 0.39  | 1.3e+07 | \~2962  | Única cultura com R² positivo → o modelo explica \~39% da variação do yield. Ainda baixo, mas indica alguma relação com clima. |
| **Oil palm fruit** | -0.08 | 2.2e+08 | \~13125 | R² negativo → modelo pior que média. Clima, neste dataset, não explica bem o yield da palma.                                   |
| **Rubber**         | -0.26 | 3.0e+06 | \~1373  | Também R² negativo. O modelo não consegue capturar a variabilidade.                                                            |
| **Cocoa**          | -0.36 | 6.6e+06 | \~2209  | Pior desempenho (R² bem negativo).                                                                                             |

Apenas o arroz (Rice, paddy) apresenta alguma previsibilidade razoável com variáveis climáticas.
Para as demais culturas, o modelo não generalizou bem: talvez o yield dependa muito mais de outros fatores (tipo de solo, manejo agrícola, pragas, fertilização, genética).

🔎 2. Coeficientes por cultura

Rice, paddy
Precipitação (+): maior chuva → maior yield (faz sentido, arroz precisa de água).
Umidade específica (+): favorece produtividade.
Umidade relativa (–) e Temperatura (–): quando altas, reduzem yield.
Faz sentido: arroz prefere calor moderado e boa irrigação.

Oil palm fruit
Coeficientes muito grandes (70k, -68k) → sinal de instabilidade do modelo.
Indica que o modelo linear está tentando compensar ruído.
Explica o R² negativo.

Rubber (borracha natural)
Coeficientes pequenos e misturados em sinal → indica pouca correlação com clima.
Yield pode depender mais de práticas agrícolas e idade da plantação.

Cocoa (cacau)
Umidade específica (+) e Precipitação (+) favorecem, o que faz sentido (cacau é cultura tropical úmida).
Temperatura (–) e Umidade relativa (–) prejudicam quando muito elevadas → plausível.
Mas o modelo ainda não consegue capturar de forma robusta (R² negativo).

✅ Resumo final:

O modelo linear captou bem o arroz (R² ~0.39) → coerente com a dependência da cultura da água.
Para cacau, palma e borracha, os sinais dos coeficientes fazem sentido, mas os R² negativos mostram que o modelo não explica a variabilidade real.
Isso sugere que dados adicionais (solo, práticas agrícolas) e modelos mais complexos são necessários.

---

💰 Custos em Nuvem (Amazon EC2)

Para simular os custos do projeto na nuvem, foi utilizada a **AWS Pricing Calculator** considerando uma instância `t4g.micro` com Linux (Savings Plan de 3 anos, sem upfront).

📍 Comparação de custos entre Brasil e EUA:

| Região                  | Custo Mensal | Custo Anual |
|-------------------------|--------------|-------------|
| 🇧🇷 South America (São Paulo) | **US$ 4,89**   | **US$ 58,68** |
| 🇺🇸 US East (N. Virginia)     | **US$ 3,07**   | **US$ 36,84** |

📊 **Insight**: Executar a mesma instância no Brasil custa cerca de **59% a mais** do que nos EUA, devido às diferenças regionais de preços da AWS:contentReference[oaicite:1]{index=1}.

---

