import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = {
    # (unchanged list of skills)
    'python', 'java', 'javascript', 'c', 'c++', 'c#', 'r', 'go', 'typescript', 'kotlin', 'swift', 'php', 'perl',
    'scala', 'rust', 'matlab', 'bash', 'shell scripting',
    'html', 'css', 'sass', 'bootstrap', 'tailwind', 'react', 'angular', 'vue', 'next.js', 'nuxt.js', 'jquery',
    'flask', 'django', 'fastapi', 'spring boot', 'express', 'node.js', '.net', 'laravel', 'rails', 'graphql',
    'rest api', 'soap', 'webhooks',
    'sql', 'mysql', 'postgresql', 'sqlite', 'mongodb', 'firebase', 'cassandra', 'oracle', 'dynamodb', 'redshift',
    'bigquery', 'snowflake', 'elasticsearch',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'github actions', 'terraform', 'ansible', 'circleci',
    'cloudformation', 'linux', 'nginx', 'apache', 'devops', 'ci/cd',
    'machine learning', 'deep learning', 'artificial intelligence', 'tensorflow', 'pytorch', 'keras', 'scikit-learn',
    'pandas', 'numpy', 'matplotlib', 'seaborn', 'statsmodels', 'data cleaning', 'feature engineering',
    'model evaluation', 'data analysis', 'data preprocessing', 'mlops',
    'tableau', 'power bi', 'looker', 'superset', 'qlik', 'excel', 'google sheets', 'dash', 'plotly',
    'hadoop', 'spark', 'hive', 'pig', 'airflow', 'kafka', 'flink', 'databricks', 'etl pipelines', 'data pipelines',
    'unit testing', 'integration testing', 'pytest', 'junit', 'selenium', 'cypress', 'jest', 'postman',
    'jira', 'confluence', 'slack', 'monday.com', 'asana', 'trello', 'notion', 'git', 'github', 'bitbucket', 'gitlab',
    'android', 'ios', 'react native', 'flutter', 'xamarin', 'cordova',
    'penetration testing', 'vulnerability assessment', 'network security', 'firewalls', 'encryption',
    'ethical hacking', 'siem', 'endpoint security',
    'communication', 'teamwork', 'leadership', 'problem solving', 'critical thinking', 'adaptability',
    'time management', 'creativity', 'collaboration', 'attention to detail', 'empathy', 'decision making',
    'finance', 'healthcare', 'ecommerce', 'retail', 'logistics', 'supply chain', 'crm', 'erp', 'blockchain',
    'iot', 'robotics', 'biotechnology', 'genomics', 'digital marketing', 'seo', 'sem', 'content creation'
}

import re

def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = set()

    for token in doc:
        token_text = token.lemma_.strip()
        if token_text in COMMON_SKILLS:
            found_skills.add(token_text)

    for chunk in doc.noun_chunks:
        chunk_text = re.sub(r'[^\w\s]', '', chunk.text.lower().strip())
        if chunk_text in COMMON_SKILLS:
            found_skills.add(chunk_text)

    return list(found_skills)


def compare_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    missing_skills = job_skills - resume_skills
    matched_skills = resume_skills & job_skills

    match_percent = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

    suggestions = []
    if missing_skills:
        suggestions.append(f"Consider adding: {', '.join(missing_skills)}")
    if match_percent < 50:
        suggestions.append("Your resume might not be tailored well for this job. Try matching more required skills.")

    return {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": round(match_percent, 2),
        "suggestions": suggestions
    }
