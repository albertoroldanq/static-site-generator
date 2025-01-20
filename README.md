[![GitHub Tests Action Status](https://img.shields.io/github/actions/workflow/status/albertoroldanq/static-site-generator/run-tests.yaml?branch=main&label=tests&style=flat-square)](https://github.com/albertoroldanq/static-site-generator/actions?query=workflow%3Arun-tests+branch%3Amain)
[![GitHub](https://img.shields.io/github/last-commit/albertoroldanq/static-site-generator?style=flat-square)]()
[![GitHub](https://img.shields.io/github/languages/code-size/albertoroldanq/static-site-generator?style=flat-square)]()
[![GitHub](https://img.shields.io/github/repo-size/albertoroldanq/static-site-generator?style=flat-square)]()

# Static Site Generator

This is a simple static site generator that I wrote in Python to practise Functional programming in Python.

It generates a static site from Markdown files. Keeping the directory structure of the `content` directory.
- Assets are copied from the `/static` directory to a `/public` directory.
- Html files are generated in a `/public` directory from the Markdown files in [/content](content) directory

To run the project, you can use the following command:

```bash
./main.sh
```

To run the tests:
    
```bash
./test.sh
``` 


## Markdown syntax accepted
Each markdown file MUST have a h1 heading and the following Markdown syntax is accepted in the content files:
- headings
- bold
- italic
- code and code blocks
- quotes
- Links
- Images