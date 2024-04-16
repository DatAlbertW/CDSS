import streamlit as st

def decision_tree():
    st.title("STI-Related Genital Ulcer Management Decision Tree")
    st.write("Initial Evaluation Includes: Careful Clinical History, Physical Examination and Baseline Laboratory Testing.")

    # State management for navigation
    if 'page' not in st.session_state:
        st.session_state.page = 1

    # Page flow control
    if st.session_state.page == 1:
        sti_exposure = st.radio(
            "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
            ('Yes', 'No'))

        if st.button('Next'):
            if sti_exposure == 'Yes':
                st.write("Initiate empiric treatment for that disease and await further testing.")
                st.session_state.page = 99  # Ends the flow
            else:
                st.session_state.page = 2

    if st.session_state.page == 2:
        ulcer_painful = st.radio(
            "Is the ulcer painful?",
            ('Yes', 'No'))

        if st.button('Next'):
            if ulcer_painful == 'Yes':
                st.session_state.page = 3
            else:
                st.session_state.page = 5

    if st.session_state.page == 3:
        herpes_consistent = st.radio(
            "Is the Appearance consistent with Herpes simplex virus (HSV)?",
            ('Yes', 'No'))
        
        if st.button('Next'):
            if herpes_consistent == 'Yes':
                st.write("Treat Empirically for HSV.")
                st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
                st.session_state.page = 99  # Ends the flow
            else:
                st.session_state.page = 4

    if st.session_state.page == 4:
        st.write("Consider alternative diagnosis (e.g. syphilis, chancroid). If risk factors for one of these diagnoses, administer empiric treatment.")
        st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        if st.button('End'):
            st.session_state.page = 99

    if st.session_state.page == 5:
        rapid_syphilis = st.radio(
            "Is rapid Syphilis testing available?",
            ('Yes', 'No'))
        
        if st.button('Next'):
            if rapid_syphilis == 'Yes':
                st.session_state.page = 6
            else:
                st.session_state.page = 7

    if st.session_state.page == 6:
        syphilis_positive = st.radio(
            "Is testing positive for Syphilis?",
            ('Yes', 'No'))
        
        if st.button('Next'):
            if syphilis_positive == 'Yes':
                st.write("Treat for Syphilis.")
                st.session_state.page = 99  # Ends the flow
            else:
                st.session_state.page = 8

    if st.session_state.page == 7:
        high_risk_syphilis = st.radio(
            "Is the patient at high risk for Syphilis?",
            ('Yes', 'No'))
        
        if st.button('Next'):
            if high_risk_syphilis == 'Yes':
                st.write("Treat empirically for Syphilis while awaiting more results.")
                st.write("Further steps could include evaluation for LGV or other conditions based on additional risk factors.")
            else:
                st.write("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
                st.session_state.page = 99  # Ends the flow

    if st.session_state.page == 8:
        st.write("Further steps could include evaluation for LGV or other conditions based on additional risk factors.")
        if st.button('End'):
            st.session_state.page = 99

    # Reset / End session handling
    if st.session_state.page == 99:
        if st.button('Reset'):
            st.session_state.page = 1

if __name__ == "__main__":
    decision_tree()
