import streamlit as st

def decision_tree():
    st.title("STI-Related Genital Ulcer Management Decision Tree")
    st.caption("Please follow the questions below to guide the management of genital ulcers.")
    st.markdown("---")

    # Initialize state management
    if 'page' not in st.session_state:
        st.session_state['page'] = 1

    def navigate_page(page_num):
        st.session_state['page'] = page_num
        st.experimental_rerun()

    # Display questions based on the page number
    if st.session_state['page'] == 1:
        st.subheader("Initial Evaluation")
        st.write("Careful Clinical History, Physical Examination, and Baseline Laboratory Testing have been conducted.")
        st.markdown("---")
        sti_exposure = st.radio(
            "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
            ('Yes', 'No'), key='sti_exposure')

        if st.button('Next'):
            if sti_exposure == 'Yes':
                st.info("Initiate empiric treatment for that disease and await further testing.")
                navigate_page(99)  # Ends the flow
            else:
                navigate_page(2)

    elif st.session_state['page'] == 2:
        ulcer_painful = st.radio(
            "Is the ulcer painful?",
            ('Yes', 'No'), key='ulcer_painful')

        if st.button('Next'):
            navigate_page(3 if ulcer_painful == 'Yes' else 5)

    elif st.session_state['page'] == 3:
        herpes_consistent = st.radio(
            "Is the appearance consistent with Herpes simplex virus (HSV)?",
            ('Yes', 'No'), key='herpes_consistent')
        
        if st.button('Next'):
            navigate_page(6 if herpes_consistent == 'Yes' else 4)

    elif st.session_state['page'] == 4:
        st.info("Consider alternative diagnoses (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        st.info("Evaluate further if initial therapy is ineffective or lab tests are negative.")
        navigate_page(99)

    elif st.session_state['page'] == 5:
        rapid_syphilis = st.radio(
            "Is rapid syphilis testing available?",
            ('Yes', 'No'), key='rapid_syphilis')
        
        if st.button('Next'):
            navigate_page(7 if rapid_syphilis == 'Yes' else 8)

    elif st.session_state['page'] == 6:
        st.info("Treat empirically for HSV.")
        st.info("Evaluate further if initial therapy is ineffective or lab tests are negative.")
        navigate_page(99)

    elif st.session_state['page'] == 7:
        syphilis_positive = st.radio(
            "Is testing positive for syphilis?",
            ('Yes', 'No'), key='syphilis_positive')
        
        if st.button('Next'):
            navigate_page(10 if syphilis_positive == 'Yes' else 9)

    elif st.session_state['page'] == 8:
        high_risk_syphilis = st.radio(
            "Is the patient at high risk for syphilis?",
            ('Yes', 'No'), key='high_risk_syphilis')
        
        if st.button('Next'):
            if high_risk_syphilis == 'Yes':
                st.info("Treat empirically for syphilis while awaiting more results.")
                navigate_page(9)  # Go to M and continue from there
            else:
                st.info("Evaluate further if initial lab tests are negative, including for non-STI causes.")
                navigate_page(99)  # Ends the flow

    elif st.session_state['page'] == 9:
        lgv_risk = st.radio(
            "Has the patient or sexual partner lived or traveled to an LGV-endemic area OR does the patient have painful lymphadenopathy present?",
            ('Yes', 'No'), key='lgv_risk')
        
        if st.button('Next'):
            navigate_page(11 if lgv_risk == 'Yes' else 12)

    elif st.session_state['page'] == 10:
        st.info("Treat for syphilis.")
        navigate_page(99)  # Ends the flow

    elif st.session_state['page'] == 11:
        st.info("Test for LGV and treat empirically while awaiting results. Evaluate further if initial therapy is ineffective or lab tests are negative.")
        navigate_page(99)

    elif st.session_state['page'] == 12:
        st.info("Evaluate further if initial lab tests are negative, including for non-STI causes.")
        navigate_page(99)

    # Handle reset and end of session
    if st.session_state['page'] == 99:
        st.markdown("---")
        st.success("End of the decision flow. Click 'Reset' to start over.")
        if st.button('Reset'):
            navigate_page(1)

if __name__ == "__main__":
    st.set_page_config(page_title="STI Management Decision Tree", layout='wide')
    decision_tree()
