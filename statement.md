# Project Formulation Statement (statement.md)
**Student Name:** Shivangi Shrivastava  
**Registration Number:** 26BCE11468  
**Course Context:** Computer Science and Engineering - Python Programming (BYOP Evaluation)  

---

## 1. Problem Statement
Managing personal daily finances is a widespread challenge for university students living on fixed monthly allowances or pocket money. Traditional tracking methods—such as manual logbooks, paper receipts, or text notes—are highly inefficient, error-prone, and lack active computational support. 

Students frequently face the following issues:
- **Lack of Visibility:** No real-time calculations tracking total expenditure against an active budget ceiling.
- **Micro-transaction Leakage:** Small daily expenses (e.g., campus canteen, local transport, printouts) go unrecorded, leading to premature depletion of monthly pocket money.
- **No Early Warning Alerts:** Absence of predictive or percentage-based tracking flags that warn a student *before* they completely cross into zero-balance territory.

This project introduces a structural engineering solution: an **Automated Student Expense & Budget Tracker System** built using Python to capture transactional data vectors, enforce structural spending limits, and provide automated multi-tier financial safety alerts.

---

## 2. Scope of the Project
The application is bounded as a local terminal-driven command console application built completely inside the Python native framework. 

### In Scope:
- **User Authentication & Allocation:** Multiple student users can register distinct local profiles, each setting an isolated monthly allowance budget.
- **Categorized Micro-expense Logging:** Real-time capture of cost inputs matched to specific tags (*Food, Canteen, Books, Travel, Entertainment*).
- **Automated Financial Analytics Engine:** Instant arithmetic calculations computing remaining wallet balances and consumption percentages.
- **Dynamic Risk Warning Indicators:** Real-time status mapping changing across three distinct modes (*SAFE, WARNING, CRITICAL*) based on allowance consumption thresholds.
- **Flat-File Local Database Simulation:** Atomic reads and writes to persistent structural JSON files inside the application path, removing external infrastructure setups.

### Out of Scope:
- Live banking APIs or credit/debit card sync engines.
- External multi-currency automated conversion trackers.
- Cloud-hosted distributed multi-tenant databases.

---

## 3. Target Users
- **Primary Users:** University/College undergraduate students (specifically within the campus ecosystem) seeking to manage pocket money, hostel allowances, and academic spending tracks.
- **Secondary Users:** Lab evaluators, research mentors, and program examiners verifying modular clean coding applications and file-stream processing constructs.

---

## 4. High-Level Features
1. **Isolated Student Workspace Control:** Secure role signup and profile initiation verifying parameters before spawning directory structures.
2. **Transaction Mapping Stream:** An input parser converting typed terminal inputs into structured array entities containing amount validation loops.
3. **Budget Status Calculator Logic:** Mathematical calculation processing loops assessing cumulative costs against budget baselines.
4. **Local Database Synchronization Framework:** Streamlined serialization and deserialization routines protecting historical records from losing state during termination.
