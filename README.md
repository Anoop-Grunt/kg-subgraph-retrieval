# Efficient Subgraph Retrieval for Knowledge Graph-Enhanced LLMs

CS 255 Project — Venkat Anoop Karlapudi & Jayateerth Kamatgi

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Data

Place the MetaQA dataset files under `data/raw/`:

```
data/raw/
├── kb.txt
├── 1-hop/vanilla/qa_train.txt, qa_dev.txt, qa_test.txt
├── 2-hop/vanilla/qa_train.txt, qa_dev.txt, qa_test.txt
└── 3-hop/vanilla/qa_train.txt, qa_dev.txt, qa_test.txt
```

## Running the notebook

```bash
source venv/bin/activate
jupyter notebook notebooks/kg_subgraph_retrieval.ipynb
```

## Project Structure

```
notebooks/
└── kg_subgraph_retrieval.ipynb
data/
├── raw/                 # Original MetaQA files
└── processed/           # Cached graph objects
```
