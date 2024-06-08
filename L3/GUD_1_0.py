import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Genital Ulcer Management", layout='wide')

st.title("Genital Ulcer Management in Sexually Active Patients")
st.caption("Follow the steps to diagnose and manage genital ulcers effectively.")
st.markdown("---")

# Initialize state management
if 'step' not in st.session_state:
    st.session_state['step'] = 'intro'  # Start at the introduction step

def navigate_step(step):
    st.session_state['step'] = step

def reset_tree():
    st.session_state['step'] = 'intro'
    for key in list(st.session_state.keys()):
        if key != 'step':
            del st.session_state[key]

# Introduction page for demographics
if st.session_state['step'] == 'intro':
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
            navigate_step('known_exposure')

# Step for known exposure
if st.session_state.get('step') == 'known_exposure':
    st.subheader("Known Exposure")
    sti_exposure = st.radio(
        "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
        ('Yes', 'No'), key='sti_exposure')
    if st.button('Next', key='confirm_exposure_btn'):
        if sti_exposure == 'Yes':
            navigate_step('empiric_treatment')
        else:
            navigate_step('ulcer_painful')

# Empiric treatment step
if st.session_state.get('step') == 'empiric_treatment':
    st.info("Initiate empiric treatment for the diagnosed STI and await further testing.")
    if st.button('Reset'):
        reset_tree()

# Step for assessing pain of ulcer
if st.session_state.get('step') == 'ulcer_painful':
    ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'), key='ulcer_painful')
    if st.button('Next', key='confirm_pain_status'):
        navigate_step('herpes_consistent' if ulcer_painful == 'Yes' else 'syphilis_testing')

# Step for herpes consistency
if st.session_state.get('step') == 'herpes_consistent':
    herpes_consistent = st.radio(
        "Is the appearance consistent with Herpes simplex virus (HSV)?",
        ('Yes', 'No'), key='herpes_consistent')

    if st.button('More Info', key="info_button"):
        st.info("""
        **Clinical Appearance of Herpes Ulcers:**
        - **PAINFUL ULCERS (common symptom).**
        - **Grouped Vesicles:** These appear on an erythematous base.
        - **Shallow Ulcerations:** Typical presentation.
        - **Large, Crusted Erosions:** Can occur in immunosuppressed patients.
        """)

    if st.button('Next', key='confirm_hsv_consistency'):
        navigate_step('herpes_treatment' if herpes_consistent == 'Yes' else 'alternative_diagnosis')

# Herpes treatment step
if st.session_state.get('step') == 'herpes_treatment':
    st.subheader("Recommended Treatment Options for Herpes")
    st.table({
        "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
        "Dosage": ["400 mg three times daily", "250 mg three times daily", "1000 mg twice daily"],
        "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
        "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
    })
    st.write("Options for recurrent disease include: Chronic suppression, Episodic therapy, or no intervention.")
    if st.button('Next'):
        navigate_step('further_evaluation')

# Alternative diagnosis step
if st.session_state.get('step') == 'alternative_diagnosis':
    st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
    if st.button('Next'):
        navigate_step('further_evaluation')

# Further evaluation step
if st.session_state.get('step') == 'further_evaluation':
    st.subheader("Further Evaluation")
    st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
    if st.button('Reset'):
        reset_tree()

# Step for syphilis testing
if st.session_state.get('step') == 'syphilis_testing':
    rapid_syphilis = st.radio("Is rapid syphilis testing available?", ('Yes', 'No'), key='rapid_syphilis')
    if st.button('Next'):
        navigate_step('syphilis_result' if rapid_syphilis == 'Yes' else 'high_risk_syphilis')

# Step for syphilis test result
if st.session_state.get('step') == 'syphilis_result':
    syphilis_positive = st.radio("Is testing positive for syphilis?", ('Yes', 'No'), key='syphilis_positive')
    if st.button('Next'):
        navigate_step('syphilis_treatment' if syphilis_positive == 'Yes' else 'lgv_risk')

# Syphilis treatment step
if st.session_state.get('step') == 'syphilis_treatment':
    st.subheader("Syphilis Treatment")
    st.write("Initiate treatment for syphilis based on current guidelines: a single dose of penicillin G benzathine (2.4 million units IM).")
    if st.button('Reset'):
        reset_tree()

# Step for LGV risk assessment
if st.session_state.get('step') == 'lgv_risk':
    lgv_risk = st.radio("Has patient or sexual partner lived or traveled to an LGV-endemic area OR does patient have painful lymphadenopathy present?", ('Yes', 'No'), key='lgv_risk')
    if st.button('Next'):
        navigate_step('lgv_treatment' if lgv_risk == 'Yes' else 'non_sti_evaluation')

# LGV treatment step
if st.session_state.get('step') == 'lgv_treatment':
    st.subheader("Lymphogranuloma Venereum (LGV) Testing and Treatment")
    st.write("Testing for LGV is recommended. Administer empiric treatment while awaiting results.")
    st.write("Preferred treatment: Doxycycline 100 mg orally twice daily for 21 days.")
    if st.button('Reset'):
        reset_tree()

# Non-STI evaluation step
if st.session_state.get('step') == 'non_sti_evaluation':
    st.subheader("Further Evaluation for Non-STI Causes")
    st.write("If the initial tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
    if st.button('Reset'):
        reset_tree()

# Step for high risk syphilis assessment
if st.session_state.get('step') == 'high_risk_syphilis':
    high_risk_syphilis = st.radio("Is the patient at high risk for syphilis?", ('Yes', 'No'), key='high_risk_syphilis')
    if st.button('Next'):
        navigate_step('empiric_syphilis_treatment' if high_risk_syphilis == 'Yes' else 'non_sti_evaluation')

# Empiric syphilis treatment step
if st.session_state.get('step') == 'empiric_syphilis_treatment':
    st.subheader("Empiric Treatment for Syphilis")
    st.write("Treat empirically for syphilis while awaiting further results: a single dose of penicillin G benzathine (2.4 million units IM).")
    if st.button('Next'):
        navigate_step('lgv_risk')

# Step for chancroid treatment
if st.session_state.get('step') == 'chancroid_treatment':
    st.subheader("Chancroid Treatment")
    st.write("Empiric single-dose therapy with either azithromycin (1 gram orally) or ceftriaxone (250 mg IM).")
    if st.button('Reset'):
        reset_tree()

# Step for granuloma inguinale treatment
if st.session_state.get('step') == 'granuloma_inguale_treatment':
    st.subheader("Granuloma Inguinale (Donovanosis) Treatment")
    st.write("Azithromycin (1 g once weekly, or 500 mg daily) for a minimum of three weeks or until all lesions have completely healed.")
    st.write("Alternative agents: Doxycycline, Erythromycin, or Trimethoprim-sulfamethoxazole for the same duration.")
    if st.button('Reset'):
        reset_tree()

# General reset button shown at each step for convenience
if st.session_state.get('step') != 'intro':
    if st.button('Reset Decision Tree'):
        reset_tree()

# Ensure that the main function is called
if __name__ == "__main__":
    reset_tree()

