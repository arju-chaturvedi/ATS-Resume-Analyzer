import io
import os
import base64
from dotenv import load_dotenv
import streamlit as st
import pdf2image
import google.generativeai as genai


# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to get Gemini response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text
# Function to convert PDF to image and base64-encode it
def input_pdf(uploaded_file):
    if uploaded_file is not None:
        try:
            images = pdf2image.convert_from_bytes(
                uploaded_file.read(),
                poppler_path="/usr/local/bin"
            )
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    'mime_type': 'image/jpeg',
                    'data': base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts

        except Exception as e:
            st.error(f'Error processing PDF: {e}')
            return None
    else:
        raise FileNotFoundError('No File Uploaded!')
# ---------- Streamlit App Starts Here ----------
st.set_page_config(page_title='ATS Resume Report')
st.subheader('ATS Tracking System: Analyze your resume like a recruiter!')


input_text = st.text_area('Paste Job Description Here:', key='input')
uploaded_file = st.file_uploader('📎 Upload Your Resume (PDF):', type=['pdf'])

if uploaded_file is not None:
    st.success('File uploaded successfully!')

# Buttons
submit1 = st.button('Eligibility Percentage')
submit2 = st.button('Detailed Feedback')
submit3 = st.button('Strengths')
submit4 = st.button('Areas of Improvement')

# ----------- PROMPTS -----------

input_prompt1 = '''
You are acting as a smart and experienced Applicant Tracking System (ATS) with deep knowledge of hiring practices, especially in the tech industry.

Your job is to:
1. Analyze the resume (image provided) and compare it with the job description text.
2. Calculate a **match percentage** (from 0% to 100%) based on how well the resume fits the job description.
3. Identify and list the **missing keywords** or skills that are expected in the job description but are not found in the resume.
4. Suggest **specific improvements** the candidate can make to increase their chances of being shortlisted — including skills to add, certifications to mention, or tools/technologies to include.

Please present the output clearly in the following format:

**Match Percentage**: XX%

**Missing Keywords/Skills**:
- ...
- ...
- ...

**Suggestions for Improvement**:
- ...
- ...
- ...
'''

input_prompt2 = '''
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
'''

input_prompt3 = '''
You are a professional career coach and recruiter. Analyze the resume based on the job description.

Your task is to list only the **key strengths** of the candidate in relation to the job description.

Focus on:
- Strong matching skills
- Relevant tools, certifications
- Educational or project highlights

Output format:

**Strengths**:
- ...
- ...
- ...
'''
input_prompt4 = '''
You are a career advisor and resume reviewer. Review the candidate's resume against the provided job description.

Your task is to list only the **areas where the resume could be improved**.

Focus on:
- Missing or weak skills
- Lack of specific tools or tech
- Poor formatting or vague experiences (if any)

Output format:

**Areas of Improvement**:
- ...
- ...
- ...
'''

# ---------- Button Logic ----------

if submit1:
    if uploaded_file:
        pdf_content = input_pdf(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.subheader("Eligibility & Suggestions:")
            st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit2:
    if uploaded_file:
        pdf_content = input_pdf(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt2)
            st.subheader("Detailed Feedback:")
            st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit3:
    if uploaded_file:
        pdf_content = input_pdf(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt3)
            st.subheader("Candidate Strengths:")
            st.write(response)
    else:
        st.warning("Please upload your resume.")

elif submit4:
    if uploaded_file:
        pdf_content = input_pdf(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt4)
            st.subheader("Areas of Improvement:")
            st.write(response)
    else:
        st.warning("Please upload your resume.")




