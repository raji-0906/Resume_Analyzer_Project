def analyze_resume(text):
    keywords = ['python', 'java', 'sql', 'html', 'css', 'javascript', 'project', 'git', 'github', 'mysql', 'react', 'flask', 'django', 'communication', 'teamwork', 'problem solving', 'achievement', 'certificate', 'internship', 'linkedin']
    text = text.lower()

    found = []
    missing = []

    for word in keywords:
        if word in text:
            found.append(word)
        else:
            missing.append(word)

    score = min(len(found) * 7, 100)

    tips = []
    if 'project' not in text:
        tips.append('Add more project details to strengthen your resume')
    if 'achievement' not in text:
        tips.append('Include achievements or competition participation')
    if 'certificate' not in text:
        tips.append('Mention relevant certifications')
    if 'linkedin' not in text:
        tips.append('Add LinkedIn profile link')

    return {
        'score': score,
        'found': found,
        'missing': missing,
        'tips': tips
    }