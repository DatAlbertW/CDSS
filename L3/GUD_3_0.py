import streamlit as st

# Define functions to display tables
def display_herpes_table():
    st.subheader("Initial diagnostic tests and empiric treatment regimens for Herpes (HSV-1 and HSV-2):")
    st.table({
        "Test": ["Perform polymerase chain reaction (PCR) test or viral culture of the lesion"],
        "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
        "Dosage": ["400 mg tablets three times daily", "250 mg tablets three times daily", "1000 mg tablets twice daily"],
        "Route": ["Oral", "Oral", "Oral"],
        "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
        "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
    })

def display_syphilis_table():
    st.subheader("Initial diagnostic tests and empiric treatment regimen for Syphilis (Treponema pallidum):")
    st.table({
        "Test": ["Perform TPHA or Rapid Syphilis Serologic Test"],
        "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
        "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
        "Route": ["Intramuscular", "", "Oral", "Oral"],
        "Duration": ["Single dose", "", "14 days", "10-14 days"],
        "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
    })

def display_lymphogranuloma_venereum_table():
    st.subheader("Initial diagnostic tests and empiric treatment regimen for Lymphogranuloma venereum (Chlamydia trachomatis):")
    st.table({
        "Test": ["Perform Nucleic acid amplification tests (NAATs) or Rapid LGV serologic test"],
        "Medication": ["Doxycycline"],
        "Dosage": ["100 mg tablets twice daily"],
        "Route": ["Oral"],
        "Duration": ["21 days"],
        "Notes": ["Primary infection treatment"]
    })

def display_chancroid_table():
    st.subheader("Initial diagnostic tests and empiric treatment regimens for Chancroid (Haemophilus ducreyi):")
    st.table({
        "Test": ["Discard HSV and Syphilis with diagnostic tests, confirm clinical correlation with Chancroid and perform culture if available"],
        "Medication": ["Azithromycin", "Ceftriaxone"],
        "Dosage": ["1 gr tablet", "250 mg for injection"],
        "Route": ["Oral", "Intramuscular"],
        "Notes": ["Primary infection treatment", "Primary infection treatment"]
    })

def display_granuloma_inguinale_table():
    st.subheader("Initial diagnostic tests and empiric treatment regimens for Granuloma Inguinale (Klebsiella granulomatis):")
    st.table({
        "Test": ["Collect a biopsy of tissue or ulcer and confirm Donovan bodies prior to empiric treatment"],
        "Medication": ["Azithromycin", "Azithromycin", "Doxycycline", "Erythromycin"],
        "Dosage": ["1 g tablets once a week", "500 mg tablets once daily", "500 mg tablets twice daily", "500 mg tablets four times a day"],
        "Route": ["Oral", "Oral", "Oral", "Oral"],
        "Duration": ["21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed", "21 days or continue until all lesions are healed"],
        "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
    })

def display_follow_up():
    st.write("- Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.")
    st.write("- Advise the patient to avoid any sexual activity while waiting for Test results.")
    st.write("- If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.")
    st.write("- Partners should be notified, tested and educated on the appearance of lesions and symptoms.")

# Streamlit App Layout
st.title("STI Diagnosis and Treatment Decision Tree")

# Decision Tree Navigation
if 'step' not in st.session_state:
    st.session_state.step = 'A'

if st.session_state.step == 'A':
    exposure = st.radio("Has the patient had a known exposure to a Sexually Transmitted Infection (STI) that causes genital ulcers in the last 90 days?", ("Yes", "No"))
    if exposure == "Yes":
        st.session_state.step = 'B'
    elif exposure == "No":
        st.session_state.step = 'D'

if st.session_state.step == 'B':
    stis = st.multiselect("Select the Sexually Transmitted Infection (STI) that the patient has been exposed to:", ["Herpes (HSV-1, HSV-2)", "Syphilis (Treponema pallidum)", "Lymphogranuloma venereum (Chlamydia trachomatis)", "Chancroid (Haemophilus ducreyi)", "Granuloma Inguinale (Klebsiella granulomatis) aka Donovanosis"])
    if st.button("Next"):
        st.session_state.step = 'C'

if st.session_state.step == 'C':
    st.write(f"The patient has been exposed to {', '.join(stis)}, therefore the following empirical treatment is recommended:")
    if "Herpes (HSV-1, HSV-2)" in stis:
        display_herpes_table()
    if "Syphilis (Treponema pallidum)" in stis:
        display_syphilis_table()
    if "Lymphogranuloma venereum (Chlamydia trachomatis)" in stis:
        display_lymphogranuloma_venereum_table()
    if "Chancroid (Haemophilus ducreyi)" in stis:
        display_chancroid_table()
    if "Granuloma Inguinale (Klebsiella granulomatis) aka Donovanosis" in stis:
        display_granuloma_inguinale_table()
    st.write("Follow up: Await for results and notify any close contact.")
    if st.button("Reset"):
        st.session_state.step = 'A'

if st.session_state.step == 'D':
    pain = st.radio("Please confirm if the ulcer is painful?", ("Yes", "No"))
    if pain == "Yes":
        st.session_state.step = 'E'
    elif pain == "No":
        st.session_state.step = 'H'
    st.write("Every patient with a new genital ulcer must be tested for Herpes (HSV-1, HSV-2) and Syphilis (Treponema pallidum) if available.")
    st.table({
        "Test": ["Herpes: swab the lesion directly and perform Polymerase Chain Reaction (PCR) test. If PCR is not available, perform a viral culture.", "Syphilis: Perform Treponemal tests (TPHA or Rapid Serologic test)."]
    })

if st.session_state.step == 'E':
    appearance = st.radio("Is the appearance consistent with Herpes (Herpes Simplex Virus)?", ("Yes", "No"))
    if appearance == "Yes":
        st.session_state.step = 'F'
    elif appearance == "No":
        st.session_state.step = 'G'
    # Information button for Herpes
    if st.button("ℹ️ Info on Herpes", key="info_button_herpes"):
        st.info("""
        **Clinical Appearance of Herpes Ulcers (HSV-1 and HSV-2):**
        - PAINFUL ULCERS (common symptom).
        - Grouped Vesicles appear on an erythematous base.
        - Shallow Ulcerations (Typical presentation).
        - **Adenopathy:** Inflamed painful lymph nodes.
        - **Large, Crusted Erosions:** Can occur in immunosuppressed patients.
        """)

if st.session_state.step == 'F':
    st.write("Perform polymerase chain reaction (PCR) test or viral culture of the lesion. Treat empirically for Herpes Simplex Virus.")
    display_herpes_table()
    st.session_state.step = 'G'

if st.session_state.step == 'G':
    st.write("Consider alternative diagnosis (e.g. syphilis, chancroid). If risk factors for one of these diagnoses, perform diagnostic Tests and administer empiric treatment. If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
    display_follow_up()
    if st.button("Reset"):
        st.session_state.step = 'A'

if st.session_state.step == 'H':
    rapid_test = st.radio("Is rapid Syphilis testing available? (e.g. TPHA, Rapid Serologic Test)?", ("Yes", "No"))
    if rapid_test == "Yes":
        st.session_state.step = 'I'
    elif rapid_test == "No":
        st.session_state.step = 'J'

if st.session_state.step == 'I':
    positive = st.radio("Is testing positive for Syphilis?", ("Yes", "No"))
    if positive == "Yes":
        st.session_state.step = 'K'
    else:
        st.session_state.step = 'L'
    # Information button for Syphilis
    if st.button("ℹ️ Info on Syphilis", key="info_button_syphilis"):
        st.info("""
        **Clinical Appearance of Syphilis Ulcers:**
        - SINGLE CHANCRE (typical presentation).
        - PAINLESS (rarely can be painful).
        - Clean Base with Indurated smooth clean borders, Heals Spontaneously.
        - Generally a single lesion, although multiple chancres can be present.
        - **Adenopathy:** Regional painless firm and rubbery lymph nodes.
        """)

if st.session_state.step == 'J':
    high_risk = st.multiselect("Is the patient at high risk for Syphilis (Treponema Pallidum)?", ["Man who has sex with other men", "Patient engages in commercial sex work", "Exchange sex for drugs", "Unlikely to return for follow-up", "Unlikely to abstain from sexual contact until the diagnosis testing is completed"])
    if high_risk:
        st.session_state.step = 'O'
    else:
        st.session_state.step = 'P'

if st.session_state.step == 'K':
    st.write("Treat for Primary Syphilis.")
    display_syphilis_table()
    display_follow_up()
    if st.button("Reset"):
        st.session_state.step = 'A'

if st.session_state.step == 'L':
    lgv_risk = st.multiselect("Select if the patient or sexual partner has risk factors for Lymphogranuloma venereum:", ["Lived or traveled to a LGV endemic area", "Painful or significant lymphadenopathy present", "HIV positive male and has sex with other men"])
    if lgv_risk:
        st.session_state.step = 'M'
    else:
        st.session_state.step = 'N'
    # Information button for Lymphogranuloma Venereum
    if st.button("ℹ️ Info on LGV", key="info_button_lgv"):
        st.info("""
        **Clinical Appearance of Lymphogranuloma Venereum Ulcers:**
        - PAINLESS.
        - Small and shallow.
        - Ulcers heal fast and spontaneously.
        - **Adenopathy:** More common in males, Matted clusters, Swollen lymph node (“Buboe”), Unilateral or often bilateral.
        """)

if st.session_state.step == 'M':
    st.write("Perform Nucleic Acid Amplification Test (NAAT) for Lymphogranuloma venereum (Chlamydia) and treat empirically while awaiting for Test results.")
    display_lymphogranuloma_venereum_table()
    display_follow_up()
    if st.button("Reset"):
        st.session_state.step = 'A'

if st.session_state.step == 'N':
    st.write("Await for Test results. If the initial Laboratory tests are negative and/or the patient did not respond to therapy, further evaluation is needed, including evaluation for non-STI causes.")
    display_follow_up()
    if st.button("Reset"):
        st.session_state.step = 'A'

if st.session_state.step == 'O':
    st.write("Treat empirically for Primary Syphilis while awaiting for Test results.")
    display_syphilis_table()
    display_follow_up()
    if st.button("Continue"):
        st.session_state.step = 'L'

if st.session_state.step == 'P':
    st.write("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
    display_follow_up()
    if st.button("Reset"):
        st.session_state.step = 'A'

