# AWS Cloud9 Data Engineering Project

This project demonstrates data engineering tasks using AWS Cloud9, SQLite, and Python. It includes creating a local Git repository, setting up a virtual environment, retrieving and processing data from an S3 bucket, and storing it in a SQLite database. Additionally, SQL queries are used to compute statistics, and the project includes a Dockerfile as a bonus.

## Features

- Setup and usage of a virtual environment with Python dependencies.
- Data retrieval from an AWS S3 bucket.
- SQLite database creation and data insertion.
- Data exploration, cleaning, and transformation.
- Computation of life expectancy for the 5 European countries with the highest fertility rates.
- Dockerfile for containerization of SQL queries (Bonus feature).

## Prerequisites

Before running the project, ensure the following are installed on your system:

- Python 3.8+ and pip
- AWS CLI (configured with appropriate credentials)
- SQLite3
- Docker (optional, for the bonus task)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python libraries:
   ```bash
   pip install pysqlite3 termplotlib
   ```

4. Set up a `.gitignore` file to exclude unnecessary files:
   ```bash
   echo "venv/" > .gitignore
   echo "*.pyc" >> .gitignore
   ```

5. Retrieve data from S3:
   Use the provided `credentials.json` to connect to the S3 bucket and download the required files:
   - `statistics.csv`
   - `european_countries_list.txt`

6. Insert the data into a SQLite database:
   - Create tables (`indicators` and `countries`).
   - Clean and preprocess the data before insertion.

## Bonus: Docker Setup

To containerize the SQL execution:
1. Build the Docker image:
   ```bash
   docker build -t sqlite-project .
   ```

2. Run the Docker container:
   ```bash
   docker run sqlite-project
   ```

## Project Objectives

1. **Git and Virtual Environment Setup:**
   - Create a Git repository and `.gitignore` file.
   - Set up a Python virtual environment.

2. **Data Processing:**
   - Create a SQLite database.
   - Insert data from S3 files into tables (`indicators` and `countries`).

3. **Data Analysis:**
   - Compute the average life expectancy (SQL query) for the 5 European countries with the highest fertility rates.

4. **Containerization (Bonus):**
   - Create a Dockerfile to run SQL queries within a container.

## Example SQL Query

```sql
SELECT country, AVG(life_expectancy) AS avg_life_expectancy
FROM indicators
WHERE country IN (
    SELECT country
    FROM countries
    ORDER BY fertility_rate DESC
    LIMIT 5
)
GROUP BY country
ORDER BY avg_life_expectancy DESC;
```

## File Structure

```
project/
├── venv/                   # Virtual environment (ignored by Git)
├── database.db             # SQLite database file
├── data/
│   ├── statistics.csv      # Source data
│   ├── european_countries_list.txt
├── Dockerfile              # For containerization (bonus)
├── requirements.txt        # Python dependencies
├── main.py                 # Main Python script
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Author

- **Your Name**  
  *[LinkedIn](https://linkedin.com/in/your-profile)*  
  *[Website](https://www.yourwebsite.com)*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

### **Instructions pour le publier sur GitHub :**
1. **Initialisez le dépôt Git** si ce n'est pas déjà fait :
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Créez un nouveau dépôt sur GitHub**.

3. **Ajoutez l'URL du dépôt distant** :
   ```bash
   git remote add origin https://github.com/your-username/your-repo-name.git
   ```

4. **Poussez les modifications** :
   ```bash
   git branch -M main
   git push -u origin main
   ```

5. **Vérifiez que le projet apparaît correctement sur votre page GitHub.**
