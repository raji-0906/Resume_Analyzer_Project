# GetMeReady
GetMeReady is a placement preparation portal that helps students analyze resumes and identify skill gaps before applying for internships or jobs.

## Features
- Resume PDF upload and text extraction
- Resume score generation
- Skill detection and missing skill suggestions
- Improvement tips for stronger resumes
- Clean and responsive UI

## Tech Stack
- Python
- Flask
- HTML
- CSS
- pdfplumber

## Project Workflow
1. Upload resume in PDF format  
2. Extract text from uploaded file  
3. Analyze skills, projects, certifications, achievements, and internship presence  
4. Generate resume score and suggestions  

## Folder Structure
```bash
GetMeReady/
│── main.py
│── requirements.txt
│── uploads/
│── templates/
│   ├── index.html
│   └── result.html
│── static/
│   └── styles.css
│── utils/
│   ├── resume_parser.py
│   └── analyzer.py
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

## Future Improvements
- Interview quiz module
- Aptitude questions
- Login and history
- Job role suggestions
- Resume tips dashboard
