import streamlit as st
from datetime import datetime

def decision_tree():
    st.set_page_config(page_title="STI Management Decision Tree", layout='wide')
    st.title("Initial Evaluation of New Genital Ulcers in Sexually Active Patients")
    st.caption("Follow the questionnaire to guide the management of genital ulcers.")
    st.markdown("---")

    if 'page' not in st.session_state:
        st.session_state['page'] = 'intro'

    def navigate_page(page):
        st.session_state['page'] = page

    def reset_tree():
        st.session_state.clear()
        st.session_state['page'] = 'intro'

    def render_intro():
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

    def render_page_B():
        st.subheader("Known STI Exposure?")
        sti_exposure = st.radio("Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?", ('Yes', 'No'))
        if st.button('Confirm Exposure'):
            if sti_exposure == 'Yes':
                navigate_page('C')
            else:
                navigate_page('D')

    def render_page_C():
        st.info("Initiate empiric treatment for the known STI and await further testing.")
        st.subheader("Empiric Treatment for Known Exposure")
        st.table({
            "Condition": ["Herpes", "Syphilis", "Lymphogranuloma venereum", "Chancroid", "Granuloma Inguinale"],
            "Medication": ["Acyclovir", "Penicillin G benzathine", "Doxycycline", "Azithromycin", "Azithromycin"],
            "Dosage": ["400 mg three times daily", "2.4 million units IM single dose", "100 mg twice daily", "1 g single dose", "1 g weekly or 500 mg daily"],
            "Duration": ["7-10 days", "Single dose", "21 days", "Single dose", "Minimum 3 weeks until healed"],
            "Alternative Medication": ["Famciclovir", "Doxycycline", "Erythromycin", "Ceftriaxone", "Doxycycline"]
        })
        if st.button('Reset'):
            reset_tree()

    def render_page_D():
        ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'))
        if st.button('Confirm Pain Status'):
            navigate_page('E' if ulcer_painful == 'Yes' else 'H')

    def render_page_E():
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
            st.image('path_to_herpes_image.jpeg', caption='Herpes Image', width=300)
        if st.button('Confirm HSV Consistency'):
            navigate_page('F' if herpes_consistent == 'Yes' else 'G')

    def render_page_F():
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

    def render_page_G():
        st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        st.subheader("Empiric Treatment Options")
        st.table({
            "Condition": ["Syphilis", "Chancroid", "Granuloma Inguinale"],
            "Medication": ["Penicillin G benzathine", "Azithromycin", "Azithromycin"],
            "Dosage": ["2.4 million units IM single dose", "1 g single dose", "1 g weekly or 500 mg daily"],
            "Duration": ["Single dose", "Single dose", "Minimum 3 weeks until healed"],
            "Alternative Medication": ["Doxycycline", "Ceftriaxone", "Doxycycline"]
        })
        if st.button('Additional Information'):
            navigate_page('H')

    def render_page_H():
        st.subheader("Further Evaluation")
        st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        if st.button('Reset'):
            reset_tree()

    def render_page_I():
        rapid_syphilis = st.radio("Is rapid syphilis testing available?", ('Yes', 'No'))
        if st.button('Confirm Rapid Test Availability'):
            navigate_page('J' if rapid_syphilis == 'Yes' else 'K')

    def render_page_J():
        syphilis_positive = st.radio("Is testing positive for syphilis?", ('Yes', 'No'))
        if st.button('Confirm Syphilis Test Result'):
            navigate_page('L' if syphilis_positive == 'Yes' else 'M')

    def render_page_K():
        high_risk_syphilis = st.radio("Is the patient at high risk for syphilis?", ('Yes', 'No'))
        if st.button('Confirm High Risk Status'):
            navigate_page('P' if high_risk_syphilis == 'Yes' else 'Q')

    def render_page_L():
        st.subheader("Syphilis Treatment")
        st.table({
            "Medication": ["Penicillin G benzathine"],
            "Dosage": ["2.4 million units IM single dose"],
            "Duration": ["Single dose"],
            "Alternative Medication": ["Doxycycline"],
            "Notes": ["Primary syphilis treatment"]
        })
        if st.button('Treatment Complete, Reset Decision Tree'):
            reset_tree()

    def render_page_M():
        lgv_risk = st.radio("Has patient or sexual partner lived or traveled to an LGV-endemic area OR does patient have painful lymphadenopathy present?", ('Yes', 'No'))
        if st.button('Confirm LGV Risk'):
            navigate_page('N' if lgv_risk == 'Yes' else 'O')

    def render_page_N():
        st.subheader("Lymphogranuloma Venereum (LGV) Testing and Treatment")
        st.table({
            "Medication": ["Doxycycline"],
            "Dosage": ["100 mg twice daily"],
            "Duration": ["21 days"],
            "Alternative Medication": ["Erythromycin"],
            "Notes": ["Empiric treatment while awaiting results"]
        })
        if st.button('Further Evaluation Required, Reset Decision Tree'):
            reset_tree()

    def render_page_O():
        chancroid_risk = st.radio("Chancroid Risk?", ('Yes', 'No'))
        if st.button('Confirm Chancroid Risk'):
            navigate_page('P' if chancroid_risk == 'Yes' else 'Q')

    def render_page_P():
        st.subheader("Chancroid Testing and Treatment")
        st.table({
            "Medication": ["Azithromycin"],
            "Dosage": ["1 g single dose"],
            "Duration": ["Single dose"],
            "Alternative Medication": ["Ceftriaxone"],
            "Notes": ["Empiric treatment while awaiting results"]
        })
        if st.button('Further Evaluation Required, Reset Decision Tree'):
            reset_tree()

    def render_page_Q():
        st.subheader("Further Evaluation Needed")
        st.write("If the initial tests are negative and/or there is no response to therapy, further evaluation is needed, including evaluation for non-STI causes.")
        if st.button('Reset Decision Tree'):
            reset_tree()

    # Info buttons for other conditions
    def render_info_buttons():
        if st.button("ℹ️ Syphilis Info"):
            st.info("""
            **Syphilis (Treponema Pallidum) Ulcer Characteristics:**
            - **Indurated, smooth firm borders, Clean base.**
            - **Heals spontaneously, Usually singular, although multiple chancres can occur.**
            - **Incubation: 7 to 90 days.**
            - **Pain: Usually painless; rarely can be painful.**
            - **Adenopathy: Firm, rubbery nodes, Not tender, Regional, Discrete.**
            """)
            st.image('path_to_syphilis_image.jpeg', caption='Syphilis Image', width=300)
        if st.button("ℹ️ Chancroid Info"):
            st.info("""
            **Chancroid (Haemophilus Ducreyi) Ulcer Characteristics:**
            - **Sharply circumscribed or irregular, ragged undermined edges.**
            - **Not indurated, Base may have gray or yellow exudate, Multiple ulcers.**
            - **Incubation: 3 to 10 days.**
            - **Pain: Marked.**
            - **Adenopathy: Half of patients have inguinal adenopathy, usually unilateral, Often painful, May suppurate or rupture.**
            """)
            st.image('path_to_chancroid_image.jpeg', caption='Chancroid Image', width=300)
        if st.button("ℹ️ LGV Info"):
            st.info("""
            **Lymphogranuloma Venereum (Chlamydia Trachomatis L1-L3) Ulcer Characteristics:**
            - **Usually not observed, Small and shallow, Rapid spontaneous healing.**
            - **Incubation: 5 to 21 days.**
            - **Pain: Usually painless.**
            - **Adenopathy: More common in males, Matted clusters, Unilateral or often bilateral, Large painful fluctuant "buboe".**
            """)
            st.image('path_to_lgv_image.jpeg', caption='LGV Image', width=300)
        if st.button("ℹ️ Granuloma Inguinale Info"):
            st.info("""
            **Granuloma Inguinale (Klebsiella Granulomatis) Ulcer Characteristics:**
            - **Extensive, progressive, Granulation-like tissue, Rolled edges.**
            - **Incubation: 7 to 90 days.**
            - **Pain: Usually painless.**
            - **Adenopathy: Pseudobuboes.**
            """)
            st.image('path_to_granuloma_inguinale_image.jpeg', caption='Granuloma Inguinale Image', width=300)

    pages = {
        'intro': render_intro,
        'B': render_page_B,
        'C': render_page_C,
        'D': render_page_D,
        'E': render_page_E,
        'F': render_page_F,
        'G': render_page_G,
        'H': render_page_H,
        'I': render_page_I,
        'J': render_page_J,
        'K': render_page_K,
        'L': render_page_L,
        'M': render_page_M,
        'N': render_page_N,
        'O': render_page_O,
        'P': render_page_P,
        'Q': render_page_Q,
    }

    if st.session_state['page'] in pages:
        pages[st.session_state['page']]()

    render_info_buttons()

    if st.session_state['page'] != 'intro':
        if st.button('Reset', key='reset_button'):
            reset_tree()

if __name__ == "__main__":
    decision_tree()
