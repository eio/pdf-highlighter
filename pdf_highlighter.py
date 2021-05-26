# Adapted from: https://stackoverflow.com/questions/47497309/find-text-position-in-pdf-file/52977595

# The `fitz` package can be installed with:
# 	pip install PyMuPDF
#
# See https://pypi.org/project/PyMuPDF/ for more details.
import fitz
import argparse


def highlight_text_on_page(text, page):
    ### SEARCH
    text_instances = page.searchFor(text)
    ### HIGHLIGHT
    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)


def highlight_document(input_pdf, quantitative):
    ### READ IN PDF
    doc = fitz.open(input_pdf)
    for page in doc:
        print("Highlighting", page)
        for text in quantitative:
            highlight_text_on_page(text, page)
    ### OUTPUT
    output = "HIGHLIGHTED-" + input_pdf
    # https://pymupdf.readthedocs.io/en/latest/document.html#Document.save
    doc.save(output, garbage=4, deflate=True, clean=True)
    print(
        "Finished highlighting \033[1m`{}`\033[0m and saved new file to \033[1m`{}`\033[0m".format(
            input_pdf, output
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for quantitative text in the input PDF and output as a new highlighted PDF"
        # Running the script:
        # 	python highlighter.py "mydocument.pdf"
    )
    parser.add_argument(
        "input_pdf",
        type=str,
        help="The input PDF to be highlighted. Must be in the same directory as this script.",
    )
    args = parser.parse_args()
    ### HIGHLIGHT THE PDF DOCUMENT
    highlight_document(
        args.input_pdf,
        [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "zero",
            "none ",
            " one",
            "-one",
            " two",
            "-two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            " eight",
            "-eight",
            " nine",
            "-nine",
            " ten",
            "-ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
            "hundred",
            "thousand",
            "million",
            "billion",
            "trillion",
            "quadrillion",
            "$",
            "%",
            "percent",
            "double",
            "triple",
            "quadruple",
            "half",
            "quarter",
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth",
            "twentieth",
            "thirtieth",
            "fourtieth",
            "fiftieth",
            "sixtieth",
            "seventieth",
            "eightieth",
            "ninetieth",
        ],
    )
