# Generation script for a Dominion Expert Resume

[![Build Status](https://travis-ci.org/DominionExperts/de-resume.svg?branch=master)](https://travis-ci.org/DominionExperts/de-resume)

## Prerequisites

Install python: <https://www.python.org/downloads/>

Install the prerequisites:

``` bash
pip install -r requirements.txt
```

Install the font: <https://fonts.google.com/specimen/Quicksand>

## Usage

Make a resume based on the YAML or JSON template and save it in the `resume` directory.
After that, run the generator:

``` bash
python ./generate_resume_generator.py
```

Yes, it is __this__ easy.

## Docker

1. Clone this repository
2. Add your resume __JSON__ or __YAML__ file to the resume folder
3. Run `docker run --rm -ti -v $(pwd)/resume:/app/resume dominionexperts/de-resume`
4. Find your generated resume in the `resume` folder

