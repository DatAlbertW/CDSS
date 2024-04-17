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
            if herpes_consistent == 'Yes':
                st.info("Treat empirically for HSV and evaluate further if initial therapy is ineffective or lab tests are negative.")
                navigate_page(99)  # Ends the flow
            else:
                navigate_page(4)

    elif st.session_state['page'] == 4:
        st.info("Consider alternative diagnoses (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        st.info("Evaluate further if initial therapy is ineffective or lab tests are negative.")
        if st.button('End'):
            navigate_page(99)

    elif st.session_state['page'] == 5:
        rapid_syphilis = st.radio(
            "Is rapid syphilis testing available?",
            ('Yes', 'No'), key='rapid_syphilis')
        
        if st.button('Next'):
            navigate_page(6 if rapid_syphilis == 'Yes' else 7)

    elif st.session_state['page'] == 6:
        syphilis_positive = st.radio(
            "Is testing positive for syphilis?",
            ('Yes', 'No'), key='syphilis_positive')
        
        if st.button('Next'):
            if syphilis_positive == 'Yes':
                st.info("Treat for syphilis.")
                navigate_page(99)  # Ends the flow
            else:
                navigate_page(8)

    elif st.session_state['page'] == 7:
        high_risk_syphilis = st.radio(
            "Is the patient at high risk for syphilis?",
            ('Yes', 'No'), key='high_risk_syphilis')
        
        if st.button('Next'):
            if high_risk_syphilis == 'Yes':
                st.info("Treat empirically for syphilis while awaiting more results.")
                st.info("Consider further evaluation for other conditions based on additional risk factors.")
            else:
                st.info("Evaluate further if initial lab tests are negative, including for non-STI causes.")
                navigate_page(99)  # Ends the flow

    elif st.session_state['page'] == 8:
        st.info("Consider further evaluation for LGV or other conditions based on additional risk factors.")
        if st.button('End'):
            navigate_page(99)

    # Handle reset and end of session
    if st.session_state['page'] == 99:
        st.markdown("---")
        st.success("End of the decision flow. Click 'Reset' to start over.")
        if st.button('Reset'):
            navigate_page(1)

if __name__ == "__main__":
    st.set_page_config(page_title="STI Management Decision Tree", layout='
