"""
A Extractor extract all text from PDF files.
"""
import glob
import os.path
from typing import List, Union, Text

import fitz
import pandas as pd
from elasticsearch import Elasticsearch


class PDFExtractor:
    """
    A Extractor extract all text from PDF files.
    """

    def __init__(self, pdf_path: Union[Text, List[Text]]):
        self.pdf_path = pdf_path
        if isinstance(self.pdf_path, Text):
            self._get_pdf_files()
        else:
            self.pdf_file_paths = pdf_path
        self.df = pd.DataFrame(columns=["name", "content"])

    def extract_pdf_file(self) -> pd.DataFrame:
        """
        This function is used to extract information from PDF files.
        :return:
        """

        for idx, fname in enumerate(self.pdf_file_paths):
            doc = fitz.open(fname)  # open document
            doc_name = os.path.basename(fname)
            all_text = ""
            for page in doc:  # iterate the document pages

                text = page.get_text()  # get plain text (is in UTF-8)
                all_text += text + "\n\n"  # write text of page
            self.df.loc[idx + 1] = doc_name, all_text
        return self.df

    def _get_pdf_files(self):

        self.pdf_file_paths = glob.glob(os.path.join(self.pdf_path, "*.pdf"))


if __name__ == "__main__":
    pdf_extractor = PDFExtractor("C:/Users/phong/Downloads/Documents")
    es = Elasticsearch(hosts="http://localhost:9200")

    search_results = es.search(
        index='data',
        body={
            "_source": "name",
            "query": {
                "match_phrase": {
                    "content": "1"
                }
            }
        }
    )
    print(search_results["hits"]["total"])
