import fitz  # PyMuPDF

# Skills database
SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "power bi",
    "excel",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "flask",
    "fastapi",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "react"
]

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text.lower()

def extract_skills(text):
    detected = []

    for skill in SKILLS:
        if skill in text:
            detected.append(skill.title())

    return sorted(set(detected))

if __name__ == "__main__":

    resume_file = "sample_resume.pdf"

    text = extract_text(resume_file)

    skills = extract_skills(text)

    print("\nDetected Skills\n")

    if skills:
        for skill in skills:
            print(f"✔ {skill}")
    else:
        print("No matching skills found.")
