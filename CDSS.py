import streamlit as st

# Function to navigate the decision tree
def decision_tree():
    st.title("STI-Related Genital Ulcer Management Decision Tree")
    st.write("Initial Evaluation Includes: Careful Clinical History, Physical Examination and Baseline Laboratory Testing.")
    
    # Question B
    sti_exposure = st.radio(
        "Has the patient had a known exposure to an STI that causes genital ulcers in the last 90 days?",
        ('Yes', 'No'))
    
    if sti_exposure == 'Yes':
        st.write("Initiate empiric treatment for that disease and await further testing.")
        st.stop()

    # Question D
    ulcer_painful = st.radio(
        "Is the ulcer painful?",
        ('Yes', 'No'))

    if ulcer_painful == 'Yes':
        # Question E
        herpes_consistent = st.radio(
            "Is the Appearance consistent with Herpes simplex virus (HSV)?",
            ('Yes', 'No'))
        if herpes_consistent == 'Yes':
            st.write("Treat Empirically for HSV.")
            # Question H
            st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
            st.stop()
        else:
            st.write("Consider alternative diagnosis (e.g. syphilis, chancroid). If risk factors for one of these diagnoses, administer empiric treatment.")
            # Question H
            st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
            st.stop()
    else:
        # Question I
        rapid_syphilis = st.radio(
            "Is rapid Syphilis testing available?",
            ('Yes', 'No'))
        if rapid_syphilis == 'Yes':
            # Question J
            syphilis_positive = st.radio(
                "Is testing positive for Syphilis?",
                ('Yes', 'No'))
            if syphilis_positive == 'Yes':
                st.write("Treat for Syphilis.")
                st.stop()
            else:
                # Question M
                st.write("Further steps could include evaluation for LGV or other conditions based on additional risk factors.")
        else:
            # Question K
            high_risk_syphilis = st.radio(
                "Is the patient at high risk for Syphilis?",
                ('Yes', 'No'))
            if high_risk_syphilis == 'Yes':
                st.write("Treat empirically for Syphilis while awaiting for more results.")
                # Loop back to M
                st.write("Further steps could include evaluation for LGV or other conditions based on additional risk factors.")
            else:
                st.write("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
                st.stop()

# Run the decision tree function
if __name__ == "__main__":
    decision_tree()