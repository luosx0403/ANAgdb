import re
from Bio import Entrez, Medline
import ssl

# 忽略SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

Entrez.email = "luoshaoxuan@outlook.com"

output_path = "all_species_output.tsv"

with open(output_path, "w", encoding="utf-8") as file:
    file.write("species\tyear\tauthors\ttitle\tjournal\tkeywords\tabstract\tlink\n")

    with open("queries_keyword.txt", "r", encoding="utf-8") as species_file:
        species_names = [line.strip() for line in species_file.readlines()]

    for species_name in species_names:
        search_term = species_name
        hnscc_esearch = Entrez.esearch(db="pubmed", term=search_term, RetMax="99999")
        read_esearch = Entrez.read(hnscc_esearch)
        idlist = read_esearch["IdList"]

        # 显示每个物种的查询结果数目
        print(f"Total for {species_name}: {read_esearch['Count']}")

        if idlist:  # 确保有结果
            handle = Entrez.efetch(db="pubmed", id=idlist[0:99999], rettype="medline", retmode="text")
            records = list(Medline.parse(handle))

            for record in records:
                year = re.search(r'^(\d{4})', record.get("DP", "N/A"))
                year = year.group(1) if year else "N/A"

                authors = "; ".join(record.get("FAU", ["N/A"]))
                title = record.get("TI", "N/A")
                journal = record.get("TA", "N/A")
                keywords = "; ".join(record.get("OT", ["N/A"])) if "OT" in record else "N/A"
                abstract = record.get("AB", "N/A")

                aid_field = record.get("AID", [])
                doi = "N/A"
                for aid in aid_field:
                    if aid.endswith("[doi]"):
                        doi = re.sub(r' \[doi\]$', "", aid)
                        doi = re.sub(r' \d+$', "", doi)
                        break

                link = f"https://doi.org/{doi}" if doi != "N/A" else "N/A"

                line = f"{species_name}\t{year}\t{authors}\t{title}\t{journal}\t{keywords}\t{abstract}\t{link}\n"
                file.write(line)
