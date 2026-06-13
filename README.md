# 🌍 Cameroon Macro-Economic & Infrastructure Data Pipeline

[![Status: In-Progress](https://shields.io)](#-project-roadmap)
[![Tech Stack](https://shields.io)](https://getdbt.com)

An enterprise-grade, automated ELT (Extract, Load, Transform) data pipeline engineered to ingest, clean, validate, and model fragmented public-sector macroeconomic indicators and regional infrastructure development metrics into an analytical warehouse layer.

### 💼 Why Agencies & Enterprise Buyers Care:
* **Handling High-Volatility Data:** Public-sector and international development data are notoriously messy, unstandardized, and prone to sudden schema drifts. This pipeline serves as a blueprint for handling unpredictable multi-source APIs and web-scraping pipelines.
* **Production-Grade Infrastructure on a Zero-Dollar Budget:** Demonstrates how to leverage localized analytics engineering tooling (**DuckDB + dbt Core + GitHub Actions**) to build high-performance data platforms without incurring premature cloud warehouse overhead costs.

---

## 🏗️ Target Architecture Flow

### 1. Ingestion & Extraction Layer (EL)
*   **Dynamic Scraping & API Ingestion:** Modular Python scripts running asynchronous network requests to harvest multi-source public datasets (economic reports, infrastructure registries, parsing unformatted PDF/HTML tables).
*   **Resiliency Protocols:** Built-in error-handling, request throttling, and retry mechanisms to maintain data collection continuity despite volatile public endpoint uptimes.

### 2. Analytical Storage Layer (L)
*   **DuckDB Data Lakehouse:** Utilizing local transactional DuckDB files for highly localized, lightning-fast columnar execution. 
*   **Cloud Expansion Path:** Engineered with explicit decoupling, allowing seamless migration to **Google BigQuery** or **Snowflake** warehouses via minor dbt profile environment adjustments.

### 3. Transformation & Modeling Layer (T)
*   **dbt Core Framework:** Translating raw staging tables into highly structural, optimized dimensional star-schemas (`fct_` and `dim_` tables) optimized for business intelligence delivery.
*   **Automated Quality Firewalls:** Integrating robust data testing patterns directly within dbt lifecycle loops to track down null values, negative currency evaluations, and primary key breaks.
*   **Orchestration Engine:** Automated end-to-end execution, scheduling, and error alerting running entirely on headless cron via **GitHub Actions workflow automation**.

---

## 📈 Current Status & Project Roadmap

This active asset demonstrates structured development principles across development phases. 

- [x] **Phase 1: Repository Foundations & Ingestion Framework** 
  * Initialize repository structure, continuous integration workflows, and configure baseline Python collection pipelines.
- [ ] **Phase 2: Advanced Schema Resilience & Error Shielding** *(Active Sprint)*
  * Architect dynamic schema protection configurations to gracefully capture, isolate, and log unexpected adjustments in raw public dataset columns.
- [ ] **Phase 3: dbt Dimensional Modeling & Test Automations**
  * Develop analytics schemas, define source constraints, and construct data documentation.

---

## 🚀 Local Exploration Blueprint

*(Instructions for local verification will be finalized as core staging elements lock down.)*

```bash
# Set up isolated virtual workspace environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Ingest required dependencies
pip install -r requirements.txt
```

### 🏢 B2B Engineering Contracts
This pipeline showcases advanced, structured architecture management designed to align volatile external dependencies with stable internal reporting environments. For enterprise pipeline projects or technical subcontracting benches, schedule an intake sprint at **[jtambe007.github.io](https://github.io)**.
