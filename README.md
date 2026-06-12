# Cameroon Macro-Economic & Infrastructure Data Pipeline [IN PROGRESS]

An automated ELT data pipeline built to aggregate, clean, and model public-sector and economic development indicators into an analytical warehouse layer.

### 🛠️ Targeted Architecture
* **Extraction:** Python scripts fetching multi-source public datasets (APIs, Web Scraping, and Document Parsing).
* **Orchestration:** Scheduled execution using GitHub Actions.
* **Transformation:** dbt (Data Build Tool) core to transform raw staging tables into clean, production-ready dimension and fact star-schemas.
* **Storage:** Local DuckDB progressing to a cloud data warehouse (BigQuery/Snowflake).

### 📈 Current Status & Roadmap
- [x] Repository setup and ingestion script architecture.
- [ ] Dynamic schema handling for volatile public datasets.
- [ ] dbt transformation layer and data quality test cases.
