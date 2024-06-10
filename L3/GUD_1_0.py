import streamlit as st

def reset():
    st.session_state.clear()
    st.session_state.step = "A"
    st.experimental_rerun()

def main():
    st.title("STI Genital Ulcers Decision Tree")

    if "step" not in st.session_state:
        st.session_state.step = "A"

    # Navigation Buttons
    def go_back():
        step_order = ["A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
        current_index = step_order.index(st.session_state.step)
        if current_index > 0:
            st.session_state.step = step_order[current_index - 1]

    # Step A
    if st.session_state.step == "A":
        st.header("A) Known Exposure to STI causing Genital Ulcers?")
        exposure = st.radio("Has the patient had a known exposure to a Sexually Transmitted Infection (STI) that causes genital ulcers in the last 90 days?", ("", "Yes", "No"), key="step_a")

        if exposure == "Yes":
            st.session_state.step = "B"
        elif exposure == "No":
            st.session_state.step = "E"

    # Step B
    if st.session_state.step == "B":
        st.header("B) Select the STI the patient has been exposed to")
        stis = st.multiselect("Select the STI", ["Herpes (HSV-1, HSV-2)", "Syphilis (Treponema pallidum)", "Lymphogranuloma venereum (Chlamydia trachomatis)", "Chancroid (Haemophilus ducreyi)", "Granuloma Inguinale (Klebsiella granulomatis) aka Donovanosis"], key="step_b")
        
        if stis:
            st.session_state.stis = stis
            st.session_state.step = "D"
        
        st.button("Back", on_click=go_back, key="back_b")
    
    # Step D
    if st.session_state.step == "D":
        stis = st.session_state.get("stis", [])
        st.header("D) Initiate Empiric Treatment")
        st.write(f"The patient has been exposed to {', '.join(stis)}, therefore the following empirical treatment is recommended:")

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
        
        st.button("Back", on_click=go_back, key="back_d")

    # Step E
    if st.session_state.step == "E":
        st.header("E) Test Recommendation for New Genital Ulcer")
        st.write("Every patient with a new genital ulcer must be tested for Herpes (HSV-1, HSV-2) and Syphilis (Treponema pallidum) if available.")
        st.table({
            "STI": ["Herpes", "Syphilis"],
            "Test": ["Swab the lesion directly and perform Polymerase Chain Reaction (PCR) test. If PCR is not available, perform a viral culture.", "Perform Treponemal tests (TPHA or Rapid Serologic test)"]
        })
        st.session_state.step = "F"
        st.button("Back", on_click=go_back, key="back_e")

    # Step F
    if st.session_state.step == "F":
        st.header("F) Is the ulcer painful?")
        ulcer_painful = st.radio("Is the ulcer painful?", ("Yes", "No"), key="step_f")

        if ulcer_painful == "Yes":
            st.session_state.step = "G"
        elif ulcer_painful == "No":
            st.session_state.step = "K"

        st.button("Back", on_click=go_back, key="back_f")

    # Step G
    if st.session_state.step == "G":
        st.header("G) Appearance Consistent with Herpes?")
        herpes_appearance = st.radio("Is the appearance consistent with Herpes (Herpes Simplex Virus 1 and 2)?", ("Yes", "No"), key="step_g")
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
            st.session_state.step = "H"
        else:
            st.session_state.step = "I"

        st.button("Back", on_click=go_back, key="back_g")

    # Step H
    if st.session_state.step == "H":
        st.header("H) Test and Empirical Treatment for Herpes")
        st.write("Perform polymerase chain reaction (PCR) test or viral culture of the lesion. Treat empirically for Herpes Simplex Virus.")
        st.table({
            "Medication": ["Acyclovir", "Famciclovir", "Valacyclovir"],
            "Dosage": ["400 mg tablets three times daily", "250 mg tablets three times daily", "1000 mg tablets twice daily"],
            "Route": ["Oral", "Oral", "Oral"],
            "Duration": ["7-10 days for primary infection", "7-10 days for primary infection", "7-10 days for primary infection"],
            "Notes": ["Primary infection treatment", "Primary infection treatment", "Primary infection treatment"]
        })
        st.session_state.step = "J"
        st.button("Back", on_click=go_back, key="back_h")

    # Step I
    if st.session_state.step == "I":
        st.header("I) Consider Alternative Diagnosis")
        st.write("Consider alternative diagnosis (e.g. syphilis, chancroid). If risk factors for one of these diagnoses, perform diagnostic Tests and administer empiric treatment.")
        st.session_state.step = "J"
        st.button("Back", on_click=go_back, key="back_i")

    # Step J
    if st.session_state.step == "J":
        st.header("J) Further Evaluation")
        st.write("If the initial lab tests are negative and/or the patient did not respond to initial therapy, further evaluation is needed including evaluation for non-STI causes.")
        st.subheader("Follow up recommendations:")
        st.markdown("""
        - Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.
        - Advise the patient to avoid any sexual activity while waiting for Test results.
        - If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.
        - Partners should be notified, tested and educated on the appearance of lesions and symptoms.
        """)
        st.button("Back", on_click=go_back, key="back_j")

    # Step K
    if st.session_state.step == "K":
        st.header("K) Rapid Syphilis Testing Availability")
        rapid_syphilis = st.radio("Is rapid Syphilis testing available? (e.g. TPHA, Rapid Serologic Test)?", ("Yes", "No"), key="step_k")

        if rapid_syphilis == "Yes":
            st.session_state.step = "L"
        elif rapid_syphilis == "No":
            st.session_state.step = "M"

        st.button("Back", on_click=go_back, key="back_k")

    # Step L
    if st.session_state.step == "L":
        st.header("L) Syphilis Testing Result")
        syphilis_result = st.radio("Is testing positive for Syphilis?", ("Yes", "No"), key="step_l")

        if syphilis_result == "Yes":
            st.session_state.step = "N"
        else:
            st.session_state.step = "O"

        st.button("Back", on_click=go_back, key="back_l")

    # Step M
    if st.session_state.step == "M":
        st.header("M) Patient Risk Factors for Syphilis")
        patient_risk = st.multiselect("Is the patient at high risk for Syphilis (Treponema Pallidum):", ["Man who haves sex with other men", "Patient engages in commercial sex work", "Exchange sex for drugs", "Unlikely to return for follow-up", "Unlikely to abstain from sexual contact until the diagnosis testing is completed"], key="step_m")
        
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
            st.session_state.step = "R"
        else:
            st.session_state.step = "S"

        st.button("Back", on_click=go_back, key="back_m")

    # Step N
    if st.session_state.step == "N":
        st.header("N) Treat for Primary Syphilis")
        st.table({
            "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
            "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
            "Route": ["Intramuscular", "", "Oral", "Oral"],
            "Duration": ["Single dose", "", "14 days", "10-14 days"],
            "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
        })
        st.subheader("Follow up recommendations:")
        st.markdown("""
        - Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.
        - Advise the patient to avoid any sexual activity while waiting for Test results.
        - If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.
        - Partners should be notified, tested and educated on the appearance of lesions and symptoms.
        """)
        st.button("Back", on_click=go_back, key="back_n")

    # Step O
    if st.session_state.step == "O":
        st.header("O) High Risk Factors for Lymphogranuloma Venereum")
        high_risk = st.multiselect("Has the patient or sexual partner lived or traveled to a Lymphogranuloma venereum endemic area? AND/OR Does the patient have painful or significant lymphadenopathy present? AND/OR Is the patient HIV positive male and has sex with other men?", ["Yes"], key="step_o")
        
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
            st.session_state.step = "P"
        else:
            st.session_state.step = "Q"

        st.button("Back", on_click=go_back, key="back_o")

    # Step P
    if st.session_state.step == "P":
        st.header("P) Perform NAAT for Lymphogranuloma venereum and Treat Empirically")
        st.table({
            "Medication": ["Doxycycline"],
            "Dosage": ["100 mg tablets twice daily"],
            "Route": ["Oral"],
            "Duration": ["21 days"],
            "Notes": ["Primary infection treatment"]
        })
        st.write("Await for Test results. If the initial Laboratory tests are negative and/or the patient did not respond to therapy, further evaluation is needed, including evaluation for non-STI causes.")
        st.button("Back", on_click=go_back, key="back_p")

    # Step Q
    if st.session_state.step == "Q":
        st.header("Q) Await Test Results")
        st.write("Await for Test results. If the initial Laboratory tests are negative and/or the patient did not respond to therapy, further evaluation is needed, including evaluation for non-STI causes.")
        st.subheader("Follow up recommendations:")
        st.markdown("""
        - Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.
        - Advise the patient to avoid any sexual activity while waiting for Test results.
        - If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.
        - Partners should be notified, tested and educated on the appearance of lesions and symptoms.
        """)
        st.button("Back", on_click=go_back, key="back_q")

    # Step R
    if st.session_state.step == "R":
        st.header("R) Treat Empirically for Primary Syphilis")
        st.table({
            "Medication": ["Penicillin G Benzathine", "Alternatives", "Doxycycline", "Ceftriaxone"],
            "Dosage": ["Single dose 2.4 million Units", "", "100 mg tablets twice daily", "1 g injection daily"],
            "Route": ["Intramuscular", "", "Oral", "Oral"],
            "Duration": ["Single dose", "", "14 days", "10-14 days"],
            "Notes": ["Primary infection treatment", "", "Primary infection treatment", "Primary infection treatment"]
        })
        st.session_state.step = "O"
        st.button("Back", on_click=go_back, key="back_r")

    # Step S
    if st.session_state.step == "S":
        st.header("S) Further Evaluation")
        st.write("If the initial lab tests are negative, further evaluation is needed, including evaluation for non-STI causes.")
        st.subheader("Follow up recommendations:")
        st.markdown("""
        - Schedule a follow up visit to assess clinical response of the empiric Treatment and review results of diagnostic Tests.
        - Advise the patient to avoid any sexual activity while waiting for Test results.
        - If empiric therapy was initiated the patient must avoid any sexual activity for at least 7 days.
        - Partners should be notified, tested and educated on the appearance of lesions and symptoms.
        """)
        st.button("Back", on_click=go_back, key="back_s")

    st.button("Reset", on_click=reset, key="reset")

if __name__ == "__main__":
    main()
