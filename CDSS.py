import streamlit as st

def decision_tree():
    st.title("STI-Related Genital Ulcer Management Decision Tree")
    st.caption("Follow the questions to guide the management of genital ulcers.")
    st.markdown("---")

    # Initialize state management
    if 'page' not in st.session_state:
        st.session_state['page'] = 'B'  # Start at step B according to the tree

    def navigate_page(page):
        st.session_state['page'] = page

    # Display questions based on the page number
    if st.session_state['page'] == 'B':
        st.subheader("Known Exposure")
        sti_exposure = st.radio(
            "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
            ('Yes', 'No'), key='sti_exposure')

        if st.button('Confirm Exposure'):
            if sti_exposure == 'Yes':
                navigate_page('C')
            else:
                navigate_page('D')

    if st.session_state['page'] == 'C':
        st.info("Initiate empiric treatment for that disease and await further testing.")
        st.stop()

    if st.session_state['page'] == 'D':
        ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'), key='ulcer_painful')
        if st.button('Confirm Pain Status'):
            navigate_page('E' if ulcer_painful == 'Yes' else 'I')

    if st.session_state['page'] == 'E':
        herpes_consistent = st.radio("Is the appearance consistent with Herpes simplex virus (HSV)?", ('Yes', 'No'), key='herpes_consistent')
        if st.button('Confirm HSV Consistency'):
            navigate_page('F' if herpes_consistent == 'Yes' else 'G')

    if st.session_state['page'] == 'F':
        st.info("Treat empirically for HSV.")
        st.info("Evaluate further if initial therapy is ineffective or lab tests are negative.")
        st.stop()

    if st.session_state['page'] == 'G':
        st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        navigate_page('H')

    if st.session_state['page'] == 'H':
        st.info("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        st.stop()

    if st.session_state['page'] == 'I':
        rapid_syphilis = st.radio("Is rapid syphilis testing available?", ('Yes', 'No'), key='rapid_syphilis')
        if st.button('Confirm Rapid Test Availability'):
            navigate_page('J' if rapid_syphilis == 'Yes' else 'K')

    if st.session_state['page'] == 'J':
        syphilis_positive = st.radio("Is testing positive for syphilis?", ('Yes', 'No'), key='syphilis_positive')
        if st.button('Confirm Syphilis Test Result'):
            navigate_page('L' if syphilis_positive == 'Yes' else 'M')

    if st.session_state['page'] == 'K':
        high_risk_syphilis = st.radio("Is the patient at high risk for syphilis?", ('Yes', 'No'), key='high_risk_syphilis')
        if st.button('Confirm High Risk Status'):
            navigate_page('P' if high_risk_syphilis == 'Yes' else 'Q')

    if st.session_state['page'] == 'L':
        st.info("Treat for syphilis.")
        st.stop()

    if st.session_state['page'] == 'M':
        lgv_risk = st.radio("Has patient or sexual partner lived or traveled to an LGV-endemic area OR does patient have painful lymphadenopathy present?", ('Yes', 'No'), key='lgv_risk')
        if st.button('Confirm LGV Risk'):
            navigate_page('N' if lgv_risk == 'Yes' else 'O')

    if st.session_state['page'] == 'N':
        st.info("Test for LGV and treat empirically while awaiting results. Evaluate further if initial therapy is ineffective or lab tests are negative.")
        st.stop()

    if st.session_state['page'] == 'O':
        st.info("Further evaluation is needed, including evaluation for non-STI causes.")
        st.stop()

    if st.session_state['page'] == 'P':
        st.info("Treat empirically for syphilis while awaiting more results.")
        navigate_page('M')  # After treating, continue from M

    if st.session_state['page'] == 'Q':
        st.info("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
        st.stop()

if __name__ == "__main__":
    st.set_page_config(page_title="STI Management Decision Tree", layout='wide')
    decision_tree()
