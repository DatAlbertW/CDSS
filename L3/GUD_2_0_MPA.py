import streamlit as st
import json

# Reset function to clear session state
def reset():
    st.session_state.clear()
    st.session_state.step = "A"
    st.rerun()

# Save progress to a JSON file
def save_progress():
    progress = {
        "step": st.session_state.step,
        "stis": st.session_state.get("stis", [])
    }
    with open("progress.json", "w") as f:
        json.dump(progress, f)
    st.success("Progress saved!")

# Load progress from a JSON file
def load_progress():
    try:
        with open("progress.json", "r") as f:
            progress = json.load(f)
            st.session_state.step = progress["step"]
            st.session_state.stis = progress.get("stis", [])
            st.success("Progress loaded!")
            st.rerun()
    except FileNotFoundError:
        st.error("No saved progress found!")

# Helper function to format the exposure text adaptively
def format_exposure_text(stis):
    if len(stis) == 1:
        return f"The patient has been exposed to {stis[0]}, therefore the following empirical treatment is recommended:"
    else:
        return f"The patient has been exposed to {', '.join(stis[:-1])} and {stis[-1]}, therefore the following empirical treatment is recommended:"

# Step Functions
def step_a():
    st.header("A) Known Exposure to STI causing Genital Ulcers?")
    exposure = st.radio("Has the patient had a known exposure to a Sexually Transmitted Infection (STI) that causes genital ulcers in the last 90 days?", ("", "Yes", "No"), key="step_a")

    if exposure == "Yes":
        st.session_state.step = "B"
        st.rerun()
    elif exposure == "No":
        st.session_state.step = "D"
        st.rerun()

def step_b():
    st.header("B) Select the STI the patient has been exposed to")
    stis = st.multiselect("Select the STI", ["Herpes (HSV-1, HSV-2)", "Syphilis (Treponema pallidum)", "Lymphogranuloma venereum (Chlamydia trachomatis)", "Chancroid (Haemophilus ducreyi)", "Granuloma Inguinale (Klebsiella granulomatis) aka Donovanosis"], key="step_b")
    
    if stis:
        st.session_state.stis = stis
        st.session_state.step = "C"
        st.rerun()
    
    if st.button("Back"):
        st.session_state.step = "A"
        st.rerun()

def step_c():
    stis = st.session_state.get("stis", [])
    st.header("C) Initiate Empiric Treatment")
    st.write(format_exposure_text(stis))

    if "Herpes (HSV-1, HSV-2)" in stis:
        st.subheader("Initial diagnostic tests and empiric treatment regimens for Herpes (HSV-1 and HSV-2):")
        st.table({
            "Test": ["Perform polymerase chain reaction (PCR) test or viral culture of the lesion"],
            "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
            "Dosage": ["400 mg tablets three times daily", "250 mg tablets three times daily", "1000 mg tablets twice daily"],
            "Route": ["Oral", "Oral", "Oral"],
            "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
            "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
        })
    if "Syphilis (Treponema pallidum)" in stis:
        st.subheader("Initial diagnostic tests and empiric treatment regimen for Syphilis (Treponema pallidum):")
        st.table({
            "Test": ["Perform TPHA or Rapid Syphilis Serologic Test"],
            "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
            "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
            "Route": ["Intramuscular", "", "Oral", "Oral"],
            "Duration": ["Single dose", "", "14 days", "10-14 days"],
            "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
        })
    if "Lymphogranuloma venereum (Chlamydia trachomatis)" in stis:
        st.subheader("Initial diagnostic tests and empiric treatment regimen for Lymphogranuloma venereum (Chlamydia trachomatis):")
        st.table({
            "Test": ["Perform Nucleic acid amplification tests (NAATs) or Rapid LGV serologic test"],
            "Medication": ["Doxycycline"],
            "Dosage": ["100 mg tablets twice daily"],
            "Route": ["Oral"],
            "Duration": ["21 days"],
            "Notes": ["Primary infection treatment"]
        })
    if "Chancroid (Haemophilus ducreyi)" in stis:
        st.subheader("Initial diagnostic tests and empiric treatment regimens for Chancroid (Haemophilus ducreyi):")
        st.table({
            "Test": ["Discard HSV and Syphilis with diagnostic tests, confirm clinical correlation with Chancroid and perform culture if available"],
            "Medication": ["Azithromycin", "Ceftriaxone"],
            "Dosage": ["1 gr tablet", "250 mg for injection"],
            "Route": ["Oral", "Intramuscular"],
            "Notes": ["Primary infection treatment", "Primary infection treatment"]
        })
    if "Granuloma Inguinale (Klebsiella granulomatis) aka Donovanosis" in stis:
        st.subheader("Initial diagnostic tests and empiric treatment regimens for Granuloma Inguinale (Klebsiella granulomatis):")
        st.table({
            "Test": ["Collect a biopsy of tissue or ulcer and confirm Donovan bodies prior to empiric treatment"],
            "Medication": ["Azithromycin", "Azithromycin", "Doxycycline", "Erythromycin"],
            "Dosage": ["1 g tablets once a week", "500 mg tablets once daily", "500 mg tablets twice daily", "500 mg tablets four times a day"],
            "Route": ["Oral", "Oral", "Oral", "Oral"],
            "Duration": ["21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed"],
            "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
        })
    
    st.subheader("Follow up recommendations:")
    st.markdown("""
    - Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.
    - Advise the patient to avoid any sexual activity while waiting for Test results.
    - If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.
    - Partners should be notified, tested and educated on the appearance of lesions and symptoms.
    """)
    
    if st.button("Back"):
        st.session_state.step = "B"
        st.rerun()

    if st.button("Next"):
        st.session_state.step = "D"
        st.rerun()

def step_d():
    st.header("D) Test Recommendation for New Genital Ulcer")
    st.write("Every patient with a new genital ulcer must be tested for Herpes (HSV-1, HSV-2) and Syphilis (Treponema pallidum) if available.")
    st.table({
        "STI": ["Herpes", "Syphilis"],
        "Test": ["Swab the lesion directly and perform Polymerase Chain Reaction (PCR) test. If PCR is not available, perform a viral culture.", "Perform Treponemal tests (TPHA or Rapid Serologic test)"]
    })
    st.subheader("Please confirm if the ulcer is painful?")
    ulcer_painful = st.radio("", ("Yes", "No"), key="step_d")

    if ulcer_painful == "Yes":
        st.session_state.step = "E"
    elif ulcer_painful == "No":
        st.session_state.step = "I"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "C"
        st.rerun()

def step_e():
    st.header("E) Is the appearance consistent with Herpes (Herpes Simplex Virus 1 and 2)?")
    herpes_appearance = st.radio("", ("Yes", "No"), key="step_e")
    
    st.write("Click the info icon for more details on Herpes Ulcers.")
    if st.button("ℹ️", key="info_button_herpes"):
        st.info("""
        **Clinical Appearance of Herpes Ulcers (HSV-1 and HSV-2):**
        - PAINFUL ULCERS (common symptom).
        - Grouped Vesicles appear on an erythematous base.
        - Shallow Ulcerations (Typical presentation).
        - **Adenopathy:** Inflamed painful lymph nodes.
        - **Large, Crusted Erosions:** Can occur in immunosuppressed patients.
        """)
        st.image('L3/images/herpes.jpeg', caption='Herpes Image', width=300)
    
    if herpes_appearance == "Yes":
        st.session_state.step = "F"
    elif herpes_appearance == "No":
        st.session_state.step = "G"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "D"
        st.rerun()

def step_f():
    st.header("F) Perform PCR test or viral culture of the lesion. Treat empirically for Herpes Simplex Virus.")
    st.table({
        "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
        "Dosage": ["400 mg tablets three times daily", "250 mg tablets three times daily", "1000 mg tablets twice daily"],
        "Route": ["Oral", "Oral", "Oral"],
        "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
        "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
    })
    
    if st.button("Next"):
        st.session_state.step = "H"
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "E"
        st.rerun()

def step_g():
    st.header("G) Consider alternative diagnosis (e.g., syphilis, chancroid). If risk factors for one of these diagnoses, perform diagnostic tests and administer empiric treatment.")
    
    if st.button("Next"):
        st.session_state.step = "H"
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "E"
        st.rerun()

def step_h():
    st.header("H) Further evaluation needed if initial lab tests are negative and/or patient did not respond to initial therapy.")
    st.subheader("Patient Advice and Follow Up:")
    st.markdown("""
    - Schedule a follow-up visit to assess clinical response of the empiric treatment and review results of diagnostic tests.
    - Advise the patient to avoid any sexual activity while waiting for test results.
    - If empiric therapy was initiated, the patient must avoid any sexual activity for at least 7 days.
    - Partners should be notified, tested, and educated on the appearance of lesions and symptoms.
    """)
    
    if st.button("Reset"):
        reset()

    if st.button("Back"):
        st.session_state.step = "G"
        st.rerun()

def step_i():
    st.header("I) Is rapid Syphilis testing available? (e.g. TPHA, Rapid Serologic Test)?")
    rapid_syphilis = st.radio("", ("Yes", "No"), key="step_i")

    if rapid_syphilis == "Yes":
        st.session_state.step = "J"
    elif rapid_syphilis == "No":
        st.session_state.step = "K"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "D"
        st.rerun()

def step_j():
    st.header("J) Is testing positive for Syphilis?")
    syphilis_result = st.radio("", ("Yes", "No"), key="step_j")

    if syphilis_result == "Yes":
        st.session_state.step = "L"
    elif syphilis_result == "No":
        st.session_state.step = "M"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "I"
        st.rerun()

def step_k():
    st.header("K) Is the patient at high risk for Syphilis (Treponema Pallidum)?")
    patient_risk = st.multiselect("Select risk factors:", ["Man who haves sex with other men", "Patient engages in commercial sex work", "Exchange sex for drugs", "Unlikely to return for follow-up", "Unlikely to abstain from sexual contact until the diagnosis testing is completed"], key="step_k")
    
    st.write("Click the info icon for more details on Primary Syphilis Ulcers.")
    if st.button("ℹ️", key="info_syphilis"):
        st.info("""
        **Clinical Appearance of Syphilis Ulcers:**
        - **SINGLE CHANCRE (typical presentation):**
        - PAINLESS (rarely can be painful)
        - Clean Base with Indurated smooth clean borders, Heals Spontaneously.
        - Generally a single lesion, although multiple chancres can be present.
        - **Adenopathy:** Regional painless firm and rubbery lymph nodes.
        """)
        st.image('L3/images/syphilis.jpeg', caption='Syphilis Image', width=300)

    if patient_risk:
        st.session_state.step = "P"
    else:
        st.session_state.step = "Q"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "I"
        st.rerun()

def step_l():
    st.header("L) Treat for Primary Syphilis")
    st.table({
        "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
        "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
        "Route": ["Intramuscular", "", "Oral", "Oral"],
        "Duration": ["Single dose", "", "14 days", "10-14 days"],
        "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
    })
    st.subheader("Patient Advice and Follow Up:")
    st.markdown("""
    - Schedule a follow-up visit to assess clinical response of the empiric treatment and review results of diagnostic tests.
    - Advise the patient to avoid any sexual activity while waiting for test results.
    - If empiric therapy was initiated, the patient must avoid any sexual activity for at least 7 days.
    - Partners should be notified, tested, and educated on the appearance of lesions and symptoms.
    """)
    
    if st.button("Reset"):
        reset()

    if st.button("Back"):
        st.session_state.step = "J"
        st.rerun()

def step_m():
    st.header("M) High Risk Factors for Lymphogranuloma Venereum")
    high_risk = st.multiselect("Select risk factors:", ["Has the patient or sexual partner lived or traveled to a Lymphogranuloma venereum endemic area?", "Does the patient have painful or significant lymphadenopathy present?", "Is the patient HIV positive male and has sex with other men?"], key="step_m")
    
    st.write("Click the info icon for more details on Lymphogranuloma Venereum Ulcers.")
    if st.button("ℹ️", key="info_chlamydia"):
        st.info("""
        **Clinical Appearance of Lymphogranuloma Venereum Ulcers:**
        - PAINLESS
        - Small and shallow.
        - Ulcers heal fast and spontaneously.
        - **Adenopathy:** More common in males, Matted clusters, Swollen lymph node (“Buboe”), Unilateral or often bilateral.
        """)
        st.image('L3/images/chlamydia.jpeg', caption='Chlamydia Image', width=300)

    if high_risk:
        st.session_state.step = "N"
    else:
        st.session_state.step = "O"

    if st.button("Confirm"):
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "J"
        st.rerun()

def step_n():
    st.header("N) Perform NAAT for Lymphogranuloma venereum (Chlamydia) and treat empirically while awaiting test results.")
    st.table({
        "Medication": ["Doxycycline"],
        "Dosage": ["100 mg tablets twice daily"],
        "Route": ["Oral"],
        "Duration": ["21 days"],
        "Notes": ["Primary infection treatment"]
    })
    st.write("If the initial lab tests are negative and/or the patient did not respond to therapy, further evaluation is needed, including evaluation for non-STI causes.")
    
    if st.button("Reset"):
        reset()

    if st.button("Back"):
        st.session_state.step = "M"
        st.rerun()

def step_o():
    st.header("O) Await Test Results")
    st.write("Await test results. If the initial laboratory tests are negative and/or the patient did not respond to therapy, further evaluation is needed, including evaluation for non-STI causes.")
    st.subheader("Patient Advice and Follow Up:")
    st.markdown("""
    - Schedule a follow-up visit to assess clinical response of the empiric treatment and review results of diagnostic tests.
    - Advise the patient to avoid any sexual activity while waiting for test results.
    - If empiric therapy was initiated, the patient must avoid any sexual activity for at least 7 days.
    - Partners should be notified, tested, and educated on the appearance of lesions and symptoms.
    """)
    
    if st.button("Reset"):
        reset()

    if st.button("Back"):
        st.session_state.step = "N"
        st.rerun()

def step_p():
    st.header("P) Treat empirically for Primary Syphilis while awaiting test results.")
    st.table({
        "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
        "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
        "Route": ["Intramuscular", "", "Oral", "Oral"],
        "Duration": ["Single dose", "", "14 days", "10-14 days"],
        "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
    })
    
    if st.button("Next"):
        st.session_state.step = "M"
        st.rerun()

    if st.button("Back"):
        st.session_state.step = "K"
        st.rerun()

def step_q():
    st.header("Q) Further Evaluation")
    st.write("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
    st.subheader("Patient Advice and Follow Up:")
    st.markdown("""
    - Schedule a follow-up visit to assess clinical response of the empiric treatment and review results of diagnostic tests.
    - Advise the patient to avoid any sexual activity while waiting for test results.
    - If empiric therapy was initiated, the patient must avoid any sexual activity for at least 7 days.
    - Partners should be notified, tested, and educated on the appearance of lesions and symptoms.
    """)
    
    if st.button("Reset"):
        reset()

    if st.button("Back"):
        st.session_state.step = "K"
        st.rerun()

# Sidebar for navigation and progress
def sidebar():
    st.sidebar.header("Navigation")
    steps = {
        "A": "Known Exposure",
        "B": "Select STI",
        "C": "Empiric Treatment",
        "D": "Test Recommendation",
        "E": "Herpes Appearance",
        "F": "Herpes Treatment",
        "G": "Alternative Diagnosis",
        "H": "Further Evaluation",
        "I": "Syphilis Testing",
        "J": "Syphilis Result",
        "K": "Syphilis Risk Factors",
        "L": "Primary Syphilis Treatment",
        "M": "Lymphogranuloma Venereum Risk Factors",
        "N": "Lymphogranuloma Venereum Treatment",
        "O": "Await Test Results",
        "P": "Empiric Syphilis Treatment",
        "Q": "Further Evaluation"
    }
    for step, description in steps.items():
        if st.button(description):
            st.session_state.step = step
            st.rerun()
    st.sidebar.button("Save Progress", on_click=save_progress)
    st.sidebar.button("Load Progress", on_click=load_progress)
    st.sidebar.button("Reset", on_click=reset)

# Progress bar
def progress_bar():
    steps = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
        "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17
    }
    max_steps = len(steps)
    current_step = steps.get(st.session_state.step, 1)
    st.progress(current_step / max_steps)

# Main function to control the flow
def main():
    st.title("STI Genital Ulcers Decision Tree")

    if "step" not in st.session_state:
        st.session_state.step = "A"
    if "stis" not in st.session_state:
        st.session_state.stis = []

    sidebar()
    progress_bar()

    # Navigation based on the current step
    if st.session_state.step == "A":
        step_a()
    elif st.session_state.step == "B":
        step_b()
    elif st.session_state.step == "C":
        step_c()
    elif st.session_state.step == "D":
        step_d()
    elif st.session_state.step == "E":
        step_e()
    elif st.session_state.step == "F":
        step_f()
    elif st.session_state.step == "G":
        step_g()
    elif st.session_state.step == "H":
        step_h()
    elif st.session_state.step == "I":
        step_i()
    elif st.session_state.step == "J":
        step_j()
    elif st.session_state.step == "K":
        step_k()
    elif st.session_state.step == "L":
        step_l()
    elif st.session_state.step == "M":
        step_m()
    elif st.session_state.step == "N":
        step_n()
    elif st.session_state.step == "O":
        step_o()
    elif st.session_state.step == "P":
        step_p()
    elif st.session_state.step == "Q":
        step_q()

if __name__ == "__main__":
    main()
