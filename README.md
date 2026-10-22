#Walmart End-to-End Data Engineering Pipeline

A production-grade, end-to-end data engineering pipeline built using the modern data stack (**Apache Airflow**, **dbt**, **Databricks**, **Apache Spark**, **PostgreSQL**, and **Agentic AI / MCP Tools**).

This project implements modern data architectural patterns including Lakehouse architecture, Change Data Capture (CDC), Metadata-Driven Ingestion, Slowly Changing Dimensions (SCD), and Automated Orchestration.

---

## 📐 Architecture Overview



[ Local / Postgres DB ] ──(CDC / Ingestion)──> [ Databricks / Apache Spark ]
│
(Medallion Architecture)
│
▼
[ dbt Transformations ]
│
(Star Schema & SCD)
│
▼
[ Analytics / Data Marts ]


                  └────── Orchestrated by Apache Airflow ──────┘

---

## 🛠️ Tech Stack & Tools

* **Orchestration:** Apache Airflow
* **Data Transformation & Modeling:** dbt (data build tool)
* **Distributed Processing:** Databricks, Apache Spark
* **Storage & Architecture:** Delta Lake / Lakehouse (Medallion Architecture)
* **Source Database:** PostgreSQL / SQL Databases
* **AI & Agentic Workflows:** Model Context Protocol (MCP) / Agentic Database Integration
* **Version Control:** Git, GitHub

---

## 🔥 Key Technical Highlights & Scenarios

- **Lakehouse / Medallion Architecture:** Structured data layering (Bronze, Silver, and Gold) ensuring high data quality, speed, and auditability.
- **Change Data Capture (CDC):** Incremental streaming and batch capture of database changes to reduce unnecessary query overhead.
- **Metadata-Driven Pipelines:** Dynamic pipeline execution controlled via configuration files and metadata tables.
- **Slowly Changing Dimensions (SCD Type 2):** Maintained historical record state and point-in-time accuracy for dimension tables.
- **Star Schema Data Modeling:** Designed analytics-ready dimensional models (Fact and Dimension tables) optimized for fast reporting.
- **Idempotent Loads & Upserts:** Efficient incremental merge/upsert strategies avoiding duplicate data and handling late-arriving data.
- **Agentic AI Integration:** Leveraged Agentic MCP servers within VS Code for natural language querying, schema analysis, and automated database interactions.

---

## 📁 Repository Structure

```directory
.
├── dags/                  # Apache Airflow DAG definitions & task flows
├── dbt/                   # dbt models, snapshots, seeds, and macros
│   ├── models/            # Staging, Intermediate, and Mart models
│   └── tests/             # Data quality tests (unique, not_null, relationship)
├── notebooks/             # Databricks & PySpark processing scripts
├── config/                # Database connections, metadata setups, & env templates
└── README.md              # Project documentation


---

## 🚀 Getting Started & Setup

### Prerequisites

* Python 3.10+
* Docker Desktop (for local Airflow execution)
* Databricks Community / Workspace Account
* PostgreSQL Instance

### Setup Steps

1. **Clone the repository:**
git clone [https://github.com/YOUR_USERNAME/Walmart-Data-Engineering-Pipeline.git](https://github.com/YOUR_USERNAME/Walmart-Data-Engineering-Pipeline.git)
cd Walmart-Data-Engineering-Pipeline


2. **Set up virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


3. **Configure Environment Variables:**
Copy `.env.example` to `.env` and fill in your connection strings and API credentials:
cp .env.example .env

4. **Run Airflow locally via Docker:**
docker-compose up -d

