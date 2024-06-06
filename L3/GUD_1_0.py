import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Genital Ulcer Diagnosis and Treatment", layout='wide')

# App Title
st.title('Genital Ulcer Diagnosis and Treatment Guide for Healthcare Professionals')

# Introduction
st.header('Introduction')
st.markdown("""
Genital ulcers are commonly caused by sexually transmitted infections (STIs), although non-infectious etiologies should also be considered. The primary STIs responsible for genital ulcers include herpes simplex virus (HSV), syphilis, lymphogranuloma venereum (LGV), chancroid, and granuloma inguinale.
""")

# Patient History and Examination
st.header('Patient History and Examination')
st.markdown("""
A comprehensive patient history and physical examination are critical for diagnosing genital ulcers. Key aspects to cover include:

- **Sexual History:** Recent sexual contacts, gender of contacts, number of partners, use of barrier protection, and sites of sexual contact.
- **Travel History:** Recent travel and sexual activity in areas with high prevalence of specific STIs.
- **Medication History:** Recent use of medications that could cause ulcers.
- **Symptoms:** Characteristics of ulcers (e.g., painful vs. painless), urinary symptoms, constitutional symptoms, and frequency of episodes.
""")

# Diagnostic Testing
st.header('Diagnostic Testing')
st.markdown("""
Diagnostic testing is essential to confirm the infectious agent. Tests include:

- **Herpes Simplex Virus (HSV):** PCR or viral culture from lesion swabs.
- **Syphilis:** Serologic testing (treponemal and nontreponemal tests), darkfield microscopy if available.
- **Lymphogranuloma Venereum (LGV):** Nucleic acid amplification tests (NAATs) for chlamydia.
- **Chancroid:** Specialized cultures or PCR.
- **Granuloma Inguinale:** Biopsy or tissue crush prep to identify Donovan bodies.
""")

# Differential Diagnosis and Decision Making
st.header('Differential Diagnosis and Decision Making')
st.markdown("""
Based on the history, physical examination, and initial test results, the clinician should determine the most likely cause of the genital ulcer. Empiric treatment may be necessary while awaiting test results, especially if the patient is unlikely to return for follow-up.
""")

# Treatment sections
def display_treatment_table():
    st.subheader("Treatment Regimens")
    st.table({
        "Condition": ["Herpes", "Syphilis", "Lymphogranuloma venereum", "Chancroid", "Granuloma Inguinale"],
        "Medication": ["Acyclovir", "Penicillin G benzathine", "Doxycycline", "Azithromycin", "Azithromycin"],
        "Dosage": ["400 mg three times daily", "2.4 million units IM single dose", "100 mg twice daily", "1 g single dose", "1 g weekly or 500 mg daily"],
        "Duration": ["7-10 days", "Single dose", "21 days", "Single dose", "Minimum 3 weeks until healed"],
        "Alternative Medication": ["Famciclovir", "Doxycycline", "Erythromycin", "Ceftriaxone", "Doxycycline"]
    })

# Decision Tree
def decision_tree():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'intro'

    def navigate_page(page):
        st.session_state['page'] = page
        st.experimental_rerun()

    def reset_tree():
        st.session_state.clear()
        st.session_state['page'] = 'intro'
        st.experimental_rerun()

    if st.session_state['page'] == 'intro':
        with st.form("patient_info"):
            st.subheader("Patient Details")
            name = st.text_input("Name", key='name_input')
            birth_date = st.date_input("Birth Date", min_value=datetime(1900, 1, 1), max_value=datetime.today(), key='birth_date_input')
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], key='gender_select')
            submit = st.form_submit_button("Submit")
            if submit:
                st.session_state['patient_name'] = name
                st.session_state['birth_date'] = birth_date
                st.session_state['gender'] = gender
                navigate_page('B')

    elif st.session_state['page'] == 'B':
        st.subheader("Known STI Exposure?")
        sti_exposure = st.radio("Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?", ('Yes', 'No'))
        if st.button('Confirm Exposure'):
            if sti_exposure == 'Yes':
                navigate_page('C')
            else:
                navigate_page('D')

    elif st.session_state['page'] == 'C':
        st.info("Initiate empiric treatment for the known STI and await further testing.")
        display_treatment_table()
        if st.button('Reset'):
            reset_tree()

    elif st.session_state['page'] == 'D':
        ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'))
        if st.button('Confirm Pain Status'):
            navigate_page('E' if ulcer_painful == 'Yes' else 'H')

    elif st.session_state['page'] == 'E':
        herpes_consistent = st.radio("Is the appearance consistent with Herpes simplex virus (HSV)?", ('Yes', 'No'))
        st.write("Click the info icon for more details on Herpes Ulcers.")
        if st.button("ℹ️ Herpes Info"):
            st.info("""
            **Herpes (HSV-1, HSV-2) Ulcer Characteristics:**
            - **Multiple small grouped ulcers on an erythematous base.**
            - **Occasionally, single lesions/fissures can be seen.**
            - **Vesicles can open, forming shallow ulcers/erosions that may coalesce.**
            - **Incubation: 2 to 7 days.**
            - **Pain: Usually painful; can be painless or pruritic.**
            - **Adenopathy: Reactive painful nodes are common.**
            """)
            st.image('herpes_image.jpeg', caption='Herpes Image', width=300)
        if st.button('Confirm HSV Consistency'):
            navigate_page('F' if herpes_consistent == 'Yes' else 'G')

    elif st.session_state['page'] == 'F':
        st.subheader("Herpes Treatment")
        st.table({
            "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
            "Dosage": ["400 mg three times daily", "250 mg three times daily", "1000 mg twice daily"],
            "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
            "Alternative Medication": ["Valacyclovir", "Acyclovir", "Famciclovir"],
            "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
        })
        st.write("Options for recurrent disease include: Chronic suppression, Episodic therapy, or no intervention.")
        if st.button('Additional Information'):
            navigate_page('H')

    elif st.session_state['page'] == 'G':
        st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        display_treatment_table()
        if st.button('Additional Information'):
            navigate_page('H')

    elif st.session_state['page'] == 'H':
        st.subheader("Further Evaluation")
        st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        if st.button('Reset'):
            reset_tree()

    if st.session_state['page'] != 'intro':
        if st.button('Reset', key='reset_button'):
            reset_tree()

# Display treatment information at the end for reference
st.header('Treatment Information')
display_treatment_table()

# Run the decision tree
decision_tree()
