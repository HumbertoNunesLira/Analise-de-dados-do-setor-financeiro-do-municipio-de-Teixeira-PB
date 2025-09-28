# Análise de Dados Financeiros — Prefeitura de Teixeira (PB)

Este repositório contém um notebook (projeto.ipynb) com a análise e modelos de detecção de anomalias aplicados às despesas da prefeitura de Teixeira (PB). O objetivo é explorar os dados de licitações e identificar registros atípicos/anômalos utilizando técnicas de aprendizado de máquina.

## Estrutura do repositório

- `projeto.ipynb` — Notebook principal: pré-processamento, rotulagem por Isolation Forest, modelos (Árvore de Decisão, SVM, Rede Neural), avaliação e comparação.
- `consultaDespesa_Prefeitura_Teixeira_2014.csv` ... `consultaDespesa_Prefeitura_Teixeira_2024.csv` — arquivos CSV com os dados por ano (originais).
- `README.md` — este arquivo.
- `requirements.txt` — dependências para reproduzir o notebook (gerado automaticamente).

## Objetivo

- Limpar e consolidar os dados de despesas com licitações.
- Extrair features relevantes (códigos de categoria, valores, datas).
- Rotular dados com Isolation Forest (rótulos: -1 = anomalia, 1 = normal).
- Treinar e comparar modelos: Decision Tree, SVM e MLP (Rede Neural simples).
- Avaliar métricas: acurácia, precisão, recall, F1 e taxa de detecção de anomalias.

## Principais passos realizados no notebook

1. Leitura e concatenação dos arquivos CSV anuais.
2. Limpeza preliminar: remoção de colunas e linhas inconsistentes, conversão de valores numéricos (remoção de separadores), tratamento de datas, remoção de duplicatas e nulos.
3. Extração de códigos numéricos a partir das colunas categóricas (por exemplo, `Fonte Recurso`, `Unid. Orc`, `Função`, `Elemento`, etc.).
4. Uso de Isolation Forest para rotular os dados (contaminação configurada em 10%).
5. Filtragem das features para manter categorias com contagem >100 e criação do conjunto final `df4_filtrado`.
6. Normalização com StandardScaler e divisão treino/teste estratificada (80/20).
7. Treinamento dos modelos:
   - Árvore de Decisão (sklearn.tree.DecisionTreeClassifier)
   - SVM (sklearn.svm.SVC, probability=True)
   - Rede Neural simples (sklearn.neural_network.MLPClassifier)
8. Avaliação com matriz de confusão e métricas (accuracy, precision, recall, f1) e cálculo da taxa de detecção de anomalias.

## Métricas finais (obtidas na execução atual do notebook)

- Dataset total: 12.216 registros
- Classes: Normal (1): 11.472 (93.9%), Anomalia (-1): 744 (6.1%)

Resultados no conjunto de teste:
- Árvore de Decisão: 97.91% acurácia, 85.91% detecção de anomalias
- SVM: 98.24% acurácia, 77.85% detecção de anomalias
- Rede Neural (MLP simples): 98.40% acurácia, 86.58% detecção de anomalias

> Observação: Como os resultados dependem do split aleatório e do pré-processamento, pequenas variações podem ocorrer a cada execução.

## Como reproduzir

Recomendo criar um ambiente virtual (venv ou conda) e instalar as dependências listadas em `requirements.txt`.

Exemplo (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Em seguida, abra o `projeto.ipynb` no VS Code ou Jupyter e execute as células na ordem.

## Dependências

As dependências básicas estão em `requirements.txt`. Elas incluem bibliotecas comuns usadas no notebook: pandas, numpy, scikit-learn, matplotlib, seaborn, plotly.

## Próximos passos e melhorias sugeridas

- Ajustar a contaminação do Isolation Forest com validação (grid search) ou rotular manualmente uma amostra para validação.
- Testar técnicas de balanceamento mais avançadas (SMOTE, ADASYN) e comparar com oversampling manual.
- Tentar redes neurais com frameworks como Keras/TensorFlow para maior controle (callbacks, checkpoints, callbacks de early stopping com restauração de melhor modelo).
- Avaliar precisão das anomalias com análise manual: selecionar amostras rotuladas como anômala e validar com especialistas.
 
## Autores

- Vivianny Khatly
- Humberto Nunes


