import streamlit as st
from datetime import datetime

def decision_tree():
    st.title("STI-Related Genital Ulcer Management Decision Tree")
    st.caption("Follow the questions to guide the management of genital ulcers.")
    st.markdown("---")

    # Initialize state management
    if 'page' not in st.session_state:
        st.session_state['page'] = 'intro'  # Start at the introduction step

    def navigate_page(page):
        st.session_state['page'] = page

    # Function to reset the decision tree
    def reset_tree():
        st.session_state['page'] = 'intro'
        st.experimental_rerun()

    # Introduction page for demographics
    if st.session_state['page'] == 'intro':
        with st.form("patient_info"):
            st.subheader("Patient Demographics")
            name = st.text_input("Name", key='name_input')
            birth_date = st.date_input("Birth Date", min_value=datetime(1900, 1, 1), max_value=datetime.today(), key='birth_date_input')
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], key='gender_select')
            submit = st.form_submit_button("Submit")

            if submit:
                st.session_state['patient_name'] = name
                st.session_state['birth_date'] = birth_date
                st.session_state['gender'] = gender
                navigate_page('B')

    # Display questions based on the page number
    if st.session_state['page'] == 'B':
        st.subheader("Known Exposure")
        sti_exposure = st.radio(
            "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
            ('Yes', 'No'), key='sti_exposure')

        if st.button('Confirm Exposure', key='confirm_exposure_btn'):
            if sti_exposure == 'Yes':
                navigate_page('C')
            else:
                navigate_page('D')

    elif st.session_state['page'] == 'C':
        st.info("Initiate empiric treatment for that disease and await further testing.")
        if st.button('Reset Decision Tree', key='reset_in_c'):
            reset_tree()

    elif st.session_state['page'] == 'D':
        ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'), key='ulcer_painful')
        if st.button('Confirm Pain Status', key='confirm_pain_status'):
            navigate_page('E' if ulcer_painful == 'Yes' else 'I')

    elif st.session_state['page'] == 'E':
        herpes_consistent = st.radio("Is the appearance consistent with Herpes simplex virus (HSV)?", ('Yes', 'No'), key='herpes_consistent')
        if st.button("Info on Clinical Appearance of Herpes Ulcers", key='herpes_info'):
            st.info("Clinical Appearance of Herpes Ulcers: PAINFUL, Grouped vesicles on erythematous base, Shallow ulcerations. Possible large, crusted erosions in immunosuppressed patients.")
        if st.button('Confirm HSV Consistency', key='confirm_hsv_consistency'):
            navigate_page('F' if herpes_consistent == 'Yes' else 'G')

    elif st.session_state['page'] == 'F':
        st.subheader("Recommended Treatments for Herpes")
        st.table({
            "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
            "Dosage": ["400 mg three times daily", "250 mg three times daily", "1000 mg twice daily"],
            "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
            "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
        })
        st.write("Options for recurrent disease include: Chronic suppression, Episodic therapy, or no intervention.")
        if st.button('Reset Decision Tree', key='reset_in_f'):
            reset_tree()

    elif st.session_state['page'] == 'G':
        st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        if st.button('Reset Decision Tree', on_click=reset_tree):
            reset_tree()

    elif st.session_state['page'] == 'I':
        rapid_syphilis = st.radio("Is rapid syphilis testing available?", ('Yes', 'No'), key='rapid_syphilis')
        if st.button('Confirm Rapid Test Availability'):
            navigate_page('J' if rapid_syphilis == 'Yes' else 'K')

    elif st.session_state['page'] == 'J':
        syphilis_positive = st.radio("Is testing positive for syphilis?", ('Yes', 'No'), key='syphilis_positive')
        if st.button('Confirm Syphilis Test Result'):
            navigate_page('L' if syphilis_positive == 'Yes' else 'M')

    elif st.session_state['page'] == 'K':
        high_risk_syphilis = st.radio("Is the patient at high risk for syphilis?", ('Yes', 'No'), key='high_risk_syphilis')
        if st.button('Confirm High Risk Status'):
            navigate_page('P' if high_risk_syphilis == 'Yes' else 'Q')

    elif st.session_state['page'] == 'M':
        lgv_risk = st.radio("Has patient or sexual partner lived or traveled to an LGV-endemic area OR does patient have painful lymphadenopathy present?", ('Yes', 'No'), key='lgv_risk')
        if st.button('Confirm LGV Risk'):
            navigate_page('N' if lgv_risk == 'Yes' else 'O')

    # General reset button shown at each step for convenience
    if st.session_state['page'] != 'intro' and not st.session_state['page'] in ['C', 'F']:
        if st.button('Reset Decision Tree', key=f'reset_{st.session_state["page"]}'):
            reset_tree()

if __name__ == "__main__":
    st.set_page_config(page_title="STI Management Decision Tree", layout='wide')
    decision_tree()
