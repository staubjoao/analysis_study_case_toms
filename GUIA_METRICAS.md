# Guia de Localização de Métricas

Este guia descreve onde encontrar cada uma das métricas mencionadas no estudo de caso, mapeando os nomes teóricos para as colunas exatas nos arquivos CSV gerados na pasta `data/metrics/`.

## 1. Métricas de Estrutura e Acoplamento
**Arquivo:** `data/metrics/metrics.csv`

| Métrica Teórica | Coluna no CSV | Observação / Cálculo |
| :--- | :--- | :--- |
| **CiD** (Cyclic In-Dependence) | `CDP` | O CSV reporta a dependência cíclica. **CiD = 100 - CDP**. |
| **CMod** (Code Modularity) | `Static Structural` | Representa o TurboMQ aplicado ao grafo estrutural estático. |
| **SMQ** (Structural MQ) | `SMQ` | Métrica alternativa de modularidade estrutural baseada em FoSCI. |

## 2. Métricas de Evolução e Histórico (TC & LC)
**Arquivo:** `data/metrics/metrics.csv`

| Métrica Teórica | Coluna no CSV | Descrição |
| :--- | :--- | :--- |
| **TC** (Team Contributors) | `TurbomMQ_contributors` | Modularidade baseada na rede de contribuidores (Team Contributors). |
| **LC** (Lifecycle Commits) | `TurboMQ_commits` | Modularidade baseada no histórico de commits (Lifecycle Commits). |

## 3. Métricas de Negócio e Banco de Dados (Entropia)
**Arquivo:** `data/metrics/entropy.csv`

| Métrica Teórica | Coluna no CSV | Descrição |
| :--- | :--- | :--- |
| **BCP** (Business Context Purity) | `Sarah BCP` | Pureza de contexto de negócio por partição. |
| **DI** (Domain Independence) | `Use Case Entropy` | Independência de domínio baseada em casos de uso. |
| **DTP** (Database Transaction Purity) | `Database Entropy` | Pureza de transação baseada no acesso a tabelas de banco de dados. |

## 4. Métricas de Particionamento (Size)
**Arquivo:** `data/metrics/statistics.csv`

| Métrica Teórica | Coluna no CSV | Descrição |
| :--- | :--- | :--- |
| **Partition Size** | `Min`, `Max`, `Mean`, `Median` | Distribuição do tamanho das partições (número de entidades por serviço). |

## 5. Métricas de Similaridade com Ground Truth
**Arquivo:** `data/metrics/mojofm.csv`

| Métrica Teórica | Coluna no CSV | Descrição |
| :--- | :--- | :--- |
| **MoJoFM** | `Mojo` | Valor de similaridade MoJoFM com a decomposição de referência. |
| **c2c cvg** (Edge Coverage) | `C2C 50`, `C2C 33`, `C2C 10` | Cobertura de arestas entre a decomposição e o ground truth em diferentes limiares. |

---
*Nota: Se os valores de CiD aparecerem como 0.0 no CSV (CDP), significa que a In-Dependência é 100%.*
