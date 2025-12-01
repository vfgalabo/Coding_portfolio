# Global University Ranking Data Extraction and ETL Pipeline

## Project Goal
This project demonstrates a Python-based pipeline for acquiring the latest **Times Higher Education (THE) World University Rankings**. The pipeline transforms the raw web data into a clean, structured CSV file for subsequent analysis and visualization.

---

## Core Methodology: API Interception

The script utilizes an efficient **API Interception** technique to bypass front-end rendering and directly extract pre-rendered JSON data. This approach is superior to traditional methods as it is faster and more stable.This methodology represents a significant technical upgrade from the previous implementation, which relied on resource-intensive methods like Selenium and headless browsers to handle dynamic, JavaScript-rendered content. That older approach required more complex code maintenance and often led to slow execution times and brittle scripts due to its dependence on the full rendering environment.

### Key Technical Highlights
* **Efficiency and Reliability:** The script targets the specific embedded **`__NEXT_DATA__` JSON object** within the initial HTML source code. This eliminates the need for resource-intensive headless browsers (like Selenium) and JavaScript rendering.
* **Data Extraction (ETL):** The script navigates a complex, nested JSON structure to pinpoint the `rankingsData` array, demonstrating advanced data traversal and extraction skills.
* **Error Management:** Implemented specific `try-except` blocks to handle common failures:
    * `requests.exceptions.RequestException`: For connection issues and bad status codes.
    * `KeyError/ValueError`: For failures in the internal JSON structure, protecting the pipeline from crashes due to minor website changes.
* **Ethical Acquisition:** Implements a standard **User-Agent header** to ensure the request is identified as legitimate browser traffic.

---

## Project Structure

```
.
├── README.md                           <- This file
├── THE_Rankings_Scraper.ipynb          <- Jupyter Notebook containing the Beautiful Soup scraper
├── requirements.txt                    <- Python dependencies for this project
```
## Installation and Setup

### 1. Clone the Repository:
    ```bash
    git clone [https://github.com/vfgalabo/Coding_portfolio.git](https://github.com/vfgalabo/Coding_portfolio.git)
    cd Data_science_projects/THE_World_Rankings
    ```

### 2. Dependencies

This project requires `requests` and `beautifulsoup4`. Install them using the included requirements file:

```bash
pip install -r requirements.txt
```
### 3. Execution

To run the data extraction pipeline, execute the Jupyter Notebook:

```bash
jupyter notebook THE_Rankings_Scraper.ipynb
# Then run all cells in the notebook.
```

### 4. Data Output and Structure

Upon successful execution, the pipeline generates a CSV file (e.g., `THE_World_University_Rankings_2026.csv`) with the following fields:

* **Rank:** The global rank of the university (e.g., "1", "101-125").
* **University:** The full name of the institution.
* **Country:** The primary country of the university.
* **Overall_Score:** The final composite score (out of 100).
* **Citations_Score:** The score for research influence.
* **Teaching_Score:** The score for the learning environment.


## Author

[Vanya Fernandez Galabo] 