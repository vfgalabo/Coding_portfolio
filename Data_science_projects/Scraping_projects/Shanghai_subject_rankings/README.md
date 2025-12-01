# ShanghaiRanking GRAS Data Pipeline (via Selenium)

## Project Goal
This project is a highly robust and scalable Python pipeline designed to automate the extraction of the **Global Ranking of Academic Subjects (GRAS)** data from the official ShanghaiRanking website. The pipeline handles dynamic content, complex UI interactions, and year-over-year data schema changes to produce clean, consolidated CSV files for analysis.

---

## Core Methodology: Advanced Selenium Interaction

The ShanghaiRanking website utilizes heavily dynamic, JavaScript-rendered content and hides critical data fields behind interactive dropdown menus. This script employs **Selenium** to simulate full browser interaction, ensuring complete data capture.

### Key Technical Highlights
* **Dynamic Multi-Criteria Data Aggregation:** The script intelligently extracts all five ranking scores (e.g., `CNCI`, `TOP`, `AWARD`) per university. This is achieved through a multi-pass extraction technique that uses **ActionChains** to reliably interact with the dropdown and triggers subsequent table refreshes.
* **JavaScript-Assisted UI Control:** Employs **`driver.execute_script()`** to ensure the specific dropdown options are clicked reliably, bypassing common Selenium visibility or click-interception issues.
* **Robust Dynamic Content Handling:** Uses **Explicit Waits** (`WebDriverWait` with `Expected Conditions`) to stabilize the scraper, ensuring it only interacts with elements (like the ranking table and **Next Page** button) after they have fully loaded and are clickable.
* **Adaptive and Scalable ETL:** The architecture iterates over **multiple years and 40+ subject codes** dynamically. Crucially, it contains logic to conditionally adjust the **CSV headers** and **data extraction criteria** (`if year >= 2025:`) to handle year-specific changes in the ranking methodology, ensuring data integrity.
* **Professional Deployment:** Utilizes **Headless Chrome mode** and comprehensive exception handling (`TimeoutException`, `NoSuchElementException`) for stable, efficient, and server-ready execution of the extensive scraping schedule.

---

## Setup and Execution

### 1. Clone the Repository:
    ```bash
    git clone [https://github.com/vfgalabo/Coding_portfolio.git](https://github.com/vfgalabo/Coding_portfolio.git)
    cd Data_science_projects/Shanghai_subject_rankings
    ```

### 2. Requirements

This project requires **Selenium** and a compatible **WebDriver** (like ChromeDriver or an equivalent).

```bash
# requirements.txt
selenium
```
Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configuration

Ensure the driver in the script is correctly configured for your environment. The script is set up for headless Chrome execution:

```bash
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
options.add_argument('--no-sandbox') 
driver = webdriver.Chrome(options=options)
```
### 4. Running the Pipeline

To run the data extraction pipeline, execute the Jupyter Notebook:

```bash
jupyter notebook Shanghai_Scraper.ipynb
# Then run all cells in the notebook.
```
Similarly to run the data wrangling Jupyter Notebook: 

```bash
jupyter notebook Subject_data_wrangling_post_extraction.ipynb
```

### 5. Project Structure

```
.
├── Shanghai_Scraper.ipynb                          <- The main data extraction notebook
├── Subject_data_wrangling_post_extraction.ipynb    <- Suggested data wrangling for merging subject data into one final CSV file
├── requirements.txt                                <- Project dependencies
├── ShanghaiRanking/                                <- Output folder (auto-created)
│   ├── Economics_2025.csv
│   ├── Law_2025.csv
│   └── ... (Other subject/year files)
```

### 6. Data Output and Structure

The pipeline is executed within the **`Shanghai_Scraper.ipynb`** Jupyter Notebook, and upon completion, generates individual data files (CSVs) for each subject and year (e.g., `ShanghaiRanking/Economics_2025.csv`).

#### Key Extracted Fields

The data structure is **adaptive** based on the ranking year, but the core data points extracted for every university are:

* **Rank:** The institution's global ranking (can be a specific number or a range like "101-150").
* **Institution:** The full name of the university.
* **Country/Region:** The institution's country, extracted via parsing the flag image attribute.
* **Total Score:** The composite score for the subject ranking.
* **All Five Criteria Scores:** The five underlying metrics for the subject are captured by interacting with the dynamic dropdown menu. These fields include the year-specific criteria:
    * **Post-2024 Schema:** `World-Class Faculty`, `World-Class Output`, `High Quality Research`, `Research Impact`, `International Collaboration`.
    * **Pre-2024 Schema:** `Q1`, `CNCI`, `IC`, `TOP`, `AWARD`.

### 7. Suggested Data Wrangling

This data consolidation process is designed as a two-stage ETL pipeline. The **initial grouping of raw CSV files into their Parent Subject folders** (e.g., placing all Chemistry, Physics, etc. files into `Natural Sciences_2025`) is a **manual pre-processing step**. The subsequent merge scripts are then fully automated using Pandas to handle the file gathering, and final cross-subject consolidation. This modular design isolates the heavy file manipulation and transformation logic within the Python code, making the pipeline easy to audit.

#### Missing Data Handling: 
The pipeline anticipates and handles naturally null or missing score values (common in ranked data where institutions may not meet thresholds). These nulls are systematically treated and converted to a consistent placeholder (-) during the final consolidation stage `(df.fillna('-', inplace=True))`.

## Author

[Vanya Fernandez Galabo]