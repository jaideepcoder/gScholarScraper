# google-scholar-scrapper

## Usage

Download this file from github and run it through cmd on Windows or terminal on Linux.

    python gScholarScraper.py --query="Machine Learning" -N=1 --pretty=True
    
The output of this library is in standard JSON notation.

Flags:
    --query : The query string to search Google Scholar
    -N      : The number of pages to be retrieved
    --pretty: Boolean condition to display data in user readable format.

A python script to scrap data from Google Scholar


Example:

    python gScholarScraper.py --query="Machine Learning" -N=1 --pretty=True
    
Output:
[
    {
        "url": "http://www.springerlink.com/index/rw3572714v41q507.pdf",
        "abstract": "There is no a priori reason why machine learning must borro
w from nature. A field could exist, complete with well-defined algorithms, data
structures, and theories of learning, without once referring to organisms, cogni
tive or genetic structures, and psychological or  ...",
        "authors": "DE Goldberg, JH Holland - Machine learning, 1988 - Springer"
,
        "cited": "817",
        "title": "Genetic algorithms and machine learning"
    },
    {
      ...
    }
]
