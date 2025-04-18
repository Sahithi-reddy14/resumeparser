COMMON_SKILLS = {
    # Programming Languages
    'python', 'java', 'javascript', 'c', 'c++', 'c#', 'r', 'go', 'typescript', 'kotlin', 'swift', 'php', 'perl',
    'scala', 'rust', 'matlab', 'bash', 'shell scripting',

    # Web Development
    'html', 'css', 'sass', 'bootstrap', 'tailwind', 'react', 'angular', 'vue', 'next.js', 'nuxt.js', 'jquery',

    # Backend & APIs
    'flask', 'django', 'fastapi', 'spring boot', 'express', 'node.js', '.net', 'laravel', 'rails', 'graphql',
    'rest api', 'soap', 'webhooks',

    # Databases
    'sql', 'mysql', 'postgresql', 'sqlite', 'mongodb', 'firebase', 'cassandra', 'oracle', 'dynamodb', 'redshift',
    'bigquery', 'snowflake', 'elasticsearch',

    # DevOps & Cloud
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'github actions', 'terraform', 'ansible', 'circleci',
    'cloudformation', 'linux', 'nginx', 'apache', 'devops', 'ci/cd',

    # Data Science & AI
    'machine learning', 'deep learning', 'artificial intelligence', 'tensorflow', 'pytorch', 'keras', 'scikit-learn',
    'pandas', 'numpy', 'matplotlib', 'seaborn', 'statsmodels', 'data cleaning', 'feature engineering',
    'model evaluation', 'data analysis', 'data preprocessing', 'mlops',

    # Business Intelligence & Visualization
    'tableau', 'power bi', 'looker', 'superset', 'qlik', 'excel', 'google sheets', 'dash', 'plotly',

    # Big Data & ETL
    'hadoop', 'spark', 'hive', 'pig', 'airflow', 'kafka', 'flink', 'databricks', 'etl pipelines', 'data pipelines',

    # Testing & QA
    'unit testing', 'integration testing', 'pytest', 'junit', 'selenium', 'cypress', 'jest', 'postman',

    # Project & Agile Tools
    'jira', 'confluence', 'slack', 'monday.com', 'asana', 'trello', 'notion', 'git', 'github', 'bitbucket', 'gitlab',

    # Mobile & Cross Platform
    'android', 'ios', 'react native', 'flutter', 'xamarin', 'cordova',

    # Cybersecurity
    'penetration testing', 'vulnerability assessment', 'network security', 'firewalls', 'encryption',
    'ethical hacking', 'siem', 'endpoint security',

    # Soft Skills
    'communication', 'teamwork', 'leadership', 'problem solving', 'critical thinking', 'adaptability',
    'time management', 'creativity', 'collaboration', 'attention to detail', 'empathy', 'decision making',

    # Industry Keywords
    'finance', 'healthcare', 'ecommerce', 'retail', 'logistics', 'supply chain', 'crm', 'erp', 'blockchain',
    'iot', 'robotics', 'biotechnology', 'genomics', 'digital marketing', 'seo', 'sem', 'content creation'
}


def extract_skills(text):
    text = text.lower()
    return [skill for skill in COMMON_SKILLS if skill in text]

def compare_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    missing_skills = job_skills - resume_skills
    matched_skills = resume_skills & job_skills

    match_percent = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

    # ✨ Suggestions
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
