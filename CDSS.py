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
        st.experimental_rerun()

    # Display the evaluation step A
    if st.session_state['page'] == 'A':
        st.subheader("Initial Evaluation")
        st.write("Careful Clinical History, Physical Examination, and Baseline Laboratory Testing have been conducted.")
        navigate_page('B')  # Automatically move to B

    # Display questions based on the page number
    if st.session_state['page'] == 'B':
        st.subheader("Known Exposure")
        sti_exposure = st.radio(
            "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
            ('Yes', 'No'))
        if sti_exposure == 'Yes':
            navigate_page('C')
        else:
            navigate_page('D')

    elif st.session_state['page'] == 'C':
        st.info("Initiate empiric treatment for that disease and await further testing.")
        st.stop()

    elif st.session_state['page'] == 'D':
        ulcer_painful = st.radio("Is the ulcer painful?", ('Yes', 'No'))
        navigate_page('E' if ulcer_painful == 'Yes' else 'I')

    elif st.session_state['page'] == 'E':
        herpes_consistent = st.radio("Is the appearance consistent with Herpes simplex virus (HSV)?", ('Yes', 'No'))
        navigate_page('F' if herpes_consistent == 'Yes' else 'G')

    elif st.session_state['page'] == 'F':
        st.info("Treat empirically for HSV.")
        navigate_page('H')

    elif st.session_state['page'] == 'G':
        st.info("Consider alternative diagnosis (e.g., syphilis, chancroid). Administer empiric treatment if risk factors are present.")
        navigate_page('H')

    elif st.session_state['page'] == 'H':
        st.info("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        st.stop()

    elif st.session_state['page'] == 'I':
        rapid_syphilis = st.radio("Is rapid syphilis testing available?", ('Yes', 'No'))
        navigate_page('J' if rapid_syphilis == 'Yes' else 'K')

    elif st.session_state['page'] == 'J':
        syphilis_positive = st.radio("Is testing positive for syphilis?", ('Yes', 'No'))
        navigate_page('L' if syphilis_positive == 'Yes' else 'M')

    elif st.session_state['page'] == 'K':
        high_risk_syphilis = st.radio("Is the patient at high risk for syphilis?", ('Yes', 'No'))
        navigate_page('P' if high_risk_syphilis == 'Yes' else 'Q')

    elif st.session_state['page'] == 'L':
        st.info("Treat for syphilis.")
        st.stop()

    elif st.session_state['page'] == 'M':
        lgv_risk = st.radio("Has patient or sexual partner lived or traveled to an LGV-endemic area OR does patient have painful lymphadenopathy present?", ('Yes', 'No'))
        navigate_page('N' if lgv_risk == 'Yes' else 'O')

    elif st.session_state['page'] == 'N':
        st.info("Test for LGV and treat empirically while awaiting results. Further evaluation is needed if initial lab tests are negative or the patient did not respond to therapy.")
        st.stop()

    elif st.session_state['page'] == 'O':
        st.info("Further evaluation is needed, including evaluation for non-STI causes.")
        st.stop()

    elif st.session_state['page'] == 'P':
        st.info("Treat empirically for syphilis while awaiting for more results.")
        navigate_page('M')  # After treating, continue from M

    elif st.session_state['page'] == 'Q':
        st.info("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
        st.stop()

if __name__ == "__main__":
    st.set_page_config(page_title="STI Management Decision Tree", layout='wide')
    decision_tree()
