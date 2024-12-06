# ANAgdb

a multi-omics and taxonomy database for ANA-grade

# PubMed Species Search and Data Extraction Script

This script uses the NCBI Entrez API to search for PubMed articles related to species names provided in a text file. It extracts key information such as publication year, authors, title, journal, keywords, abstract, and DOI links, and saves the results to a TSV file.

---

## 🌟 Features

- **Batch Query**: Searches PubMed for multiple species names listed in a file.
- **Detailed Information Extraction**: Extracts and organizes key fields such as:
  - Publication year
  - Authors
  - Title
  - Journal name
  - Keywords
  - Abstract
  - DOI link
- **Output in TSV Format**: Saves results in a tab-separated values file for easy analysis.
- **Handles SSL Verification**: Bypasses SSL certificate verification for secure connections.

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+**  
   Install Python from [python.org](https://www.python.org/).

2. **Dependencies**  
   Install required Python libraries:
   ```bash
   pip install biopython
   ```

### Input File

Prepare a `queries_keyword.txt` file containing species names, one per line. Example:
```
Homo sapiens
Mus musculus
Arabidopsis thaliana
```

### Running the Script

Save the script to a file, e.g., `pubmed_species_search.py`. Then, run the script:
```bash
python pubmed_species_search.py
```

---

## 🔧 Script Workflow

1. Reads species names from `queries_keyword.txt`.
2. Queries PubMed for each species name using the Entrez `esearch` API.
3. Fetches detailed article records using the `efetch` API.
4. Extracts the following fields for each article:
   - **Year**: The publication year.
   - **Authors**: A semicolon-separated list of authors.
   - **Title**: The article title.
   - **Journal**: The journal name.
   - **Keywords**: Keywords associated with the article.
   - **Abstract**: The article abstract.
   - **Link**: DOI link for direct access.
5. Saves results in `all_species_output.tsv`.

---

## 📊 Output Example

Example of `all_species_output.tsv`:
```
species    year    authors    title    journal    keywords    abstract    link
Homo sapiens    2024    John Doe; Jane Smith    Title of Article    Nature    biology; genetics    This is the abstract.    https://doi.org/10.1234/example
```

---

## 🛠️ Customization

- **Email Configuration**: Replace the email address in the script with your own:
  ```python
  Entrez.email = "your_email@example.com"
  ```
- **Output Path**: Update the `output_path` variable to change the output file location:
  ```python
  output_path = "desired_output_path.tsv"
  ```

---

## 📝 Notes

- **SSL Verification**: The script bypasses SSL certificate verification for users in China, ensure this is acceptable for your network and system. If you don't need it, you can remove it manually.
- **Entrez Query Limits**: Be mindful of NCBI's query rate limits. Frequent requests may result in temporary IP bans.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this tool or report issues, feel free to create a pull request or issue in the repository.

---

## 🧑‍💻 Author

This script is developed by **Luo Shaoxuan** and used in the following research article: 

Guo, Z., Luo, S., Wang, Q. *et al.* **ANAgdb: a multi-omics and taxonomy database for ANA-grade.** *BMC Plant Biol* 24, 882 (2024).  
- [Click here to access the academic article](https://doi.org/10.1186/s12870-024-05613-4)  
- [Download citation](https://citation-needed.springer.com/v2/references/10.1186/s12870-024-05613-4?format=refman&flavour=citation)

For inquiries, please contact [luoshaoxuan@outlook.com](mailto:luoshaoxuan@outlook.com).
