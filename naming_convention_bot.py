import os

try:
    import streamlit as st
except ModuleNotFoundError:
    print("⚠️ Streamlit is not installed. Please install it using 'pip install streamlit' before running this script.")

# Define the mapping dictionary outside the function
mapping = {
    "ITIU": "IT Infrastructure Upgrade",
    "MIC": "Military Industries Corporation",
    "SAMI": "Saudin Arabian Military Industries",
    "2P": "Perfect Presentation",
    "GOV": "Government",
    "PMD": "Project Management Document",
    "CAD": "Computer-Aided Design",
    "Acoustics": "ACU",
    "Access Control system": "ACS",
    "Active Data Network Equipment": "ADE",
    "Audio Visual": "AV",
    "Building management system": "BMS",
    "Cabling & Distribution": "CD",
    "Cyber Security": "CS",
    "Data Storage & Backup": "DSB",
    "Digital Signage": "DS",
    "Electrical HV & LV": "ELV",
    "Enterprise Resource Planning": "ERP",
    "Fire Detection & Alarm System": "FDAS",
    "Firefighting System": "FFS",
    "Grounding": "GRD",
    "Information and Communication Technology": "ICT",
    "Infrastructure": "INF",
    "IT Room": "ITR",
    "IT Service Management": "ITSM",
    "Lighting": "LT",
    "Mechanical": "MEC",
    "Network Operation Center": "NOC",
    "Network Time Protocol Synchronization": "NTP",
    "Outside plant network": "OPN",
    "Power": "PWR",
    "Public Address System": "PAS",
    "Security Operation Center": "SOC",
    "Software Applications": "SA",
    "Structured cabling network": "SCN",
    "Telecom Towers": "TT",
    "Unified Communication": "UC",
    "Video Surveillance System": "VSS",
    "GN": "General throughout the project",
    "DGAS": "Data Gathering & As-Is Capture",
    "DE": "Design",
    "ASM": "Assessment",
    "Financial Management System": "FMS",
    "General Accounting Ledger": "GL",
    "Accounts Receivables Ledger": "AR",
    "Fixed Assets Ledger": "FA",
    "Enterprise Asset Management": "EAM",
    "Configuration Management": "CM",
    "Performance Management System": "PMS",
    "Product Life Cycle Management": "PLM",
    "Geographical Information System": "GIS",
    "Accounts Payables Ledger": "AP",
    "ERP Projects Management": "EPM",
    "IT Problem Management": "ITPM",
    "IT Incident Management": "ITIM",
    "IT Service Catalogue": "ITSC",
    "IT Asset Management": "ITAM",
    "IT Service Desk": "ITSD",
    "IT Release Management": "ITRM",
    "Identity & Access + Infrastructure Protection": "IAIP",
    "Monitoring & Operations": "MO",
    "Incident Response & Continuity": "IRC",
    "Miscellaneous": "MISC",
    "Permit": "PRM",
    "As-Is Verification Report": "ASISV",
    "Personnel Approval Form": "PAF",
    "Assessment Report": "ASSR",
    "Photographs, Images & Videos": "PVI",
    "Agenda": "AGD",
    "Project Charter": "PC",
    "Area Access Request": "AAR",
    "Preliminary Design Report": "PDR",
    "As-Is Findings Report": "ASISF",
    "Report": "RPT",
    "High-Level Design": "HLD",
    "Request for Change": "RFC",
    "Handover Certificate": "HOC",
    "Schedule": "SCH",
    "Inspection Test Plan": "ITP",
    "Specification": "SPC",
    "Instruction": "INS",
    "Stakeholder register": "SKR",
    "Letter": "LTR",
    "Standard": "STD",
    "Audit Report": "AUR",
    "Plan": "PLN",
    "Bill of Quantities": "BOQ",
    "Policy": "PCY",
    "Critical Design Report": "CDR",
    "Presentation": "PRE",
    "Calculation": "CAL",
    "Procedure": "PRO",
    "Certificate": "CER",
    "Profile": "PRF",
    "Claim": "CLM",
    "Proposal": "PSL",
    "Communication Plan": "CPL",
    "Register": "REG",
    "Execution plan": "EPL",
    "Human Capital Management": "HCM",
    "IT Change Management": "ITCM",
    "Governance and Risk": "GR",
    "List": "LST",
    "Strategy": "STG",
    "Low-Level Design": "LLD",
    "Taking Over Certificate": "TOC",
    "Manual": "MAN",
    "Template": "TEM",
    "Material Approval": "MA",
    "Tender Document": "TEN",
    "Material Inspection Request": "MIR",
    "Prequalification Submittal": "PQQ",
    "Method Statement": "MTS",
    "Test Report": "TRP",
    "Minutes of Meeting": "MOM",
    "Variation Request": "VAR",
    "Naming Convention Guide": "NMC",
    "Drawings in Revit": "RVT",
    "Drawings in CAD": "CAD",
    "Drawings in PDF": "DPDF",
    "H": "High",
    "L": "Low",
    "Non-Specific (NS)": "NS",
    "Logistics building (Z02)": "Z02",
    "Calibration & Laboratory facility (Z20)": "Z20",
    "Small Caliber storage (Z21)": "Z21",
    "Storage (Stocking MK80 NHS) (Z22)": "Z22",
    "Energetic magazine storage (Z23)": "Z23",
    "MP5 & G3 (Z28)": "Z28",
    "Administration building & Parking (Z31)": "Z31",
    "5.56 mm Ammunition Factory (Z32)": "Z32",
    "7-9-12 Light ammunition factory (Z33)": "Z33",
    "Weapon G36 Factory (Z34)": "Z34",
    "25-30 ammunition factory (Z35)": "Z35",
    "Test range (Z36)": "Z36",
    "Water tanks (Z37)": "Z37",
    "Demilitarization administration & 5.56 new bunkers (Z39)": "Z39",
    "MK80 Part storage (Z40)": "Z40",
    "MK80 paint & 155 mm paint (Z41)": "Z41",
    "155mm MK80 series (Z42)": "Z42",
    "Test lab for 155 mm ammunition (Z43)": "Z43",
    "Thermo cycling chamber (Z44)": "Z44",
    "New production facility (Z45)": "Z45",
    "SABR facility in renovation (Z46)": "Z46",
    "Primer Mix (Z47)": "Z47",
    "20mm Ammunition factory (Z50)": "Z50"
}

# Read Existing Naming Code UI
# Function to decode an existing naming code
def read_code_ui():
    st.subheader("🔍 Decode an Existing Naming Code")
    code = st.text_input("Enter the Naming Code")

    if st.button("Decode"):
        try:
            if "_" not in code or "-" not in code:
                raise ValueError("Invalid naming code format. Please check your input.")
            
            # Split the code into parts
            main_parts, sub_parts = code.rsplit("_", 1)
            parts = main_parts.split("-")
            final_parts = sub_parts.split("-")

            if len(parts) < 8 or len(final_parts) < 2:  # Changed to require 8 parts in main section
                raise ValueError("Invalid naming code format. Please check your input.")

            # Extract and format the date
            date_str = final_parts[1]
            if len(date_str) == 8:
                date_formatted = f"{date_str[:2]}-{date_str[2:4]}-{date_str[4:]}"
            else:
                raise ValueError("Invalid date format in the naming code.")

            details = {
                "Project Code": mapping.get(parts[0], parts[0]),
                "Owner": mapping.get(parts[1], parts[1]),
                "Discipline": next((key for key, value in mapping.items() if value == parts[2]), parts[2]),
                "Phase": mapping.get(parts[3], parts[3]),
                "File Type": next((key for key, value in mapping.items() if value == parts[4]), parts[4]),
                "File Quality": mapping.get(parts[5], parts[5]),
                "Zone Number": next((key for key, value in mapping.items() if value == parts[6]), parts[6]),
                "Serial Number": parts[7],  # Directly from main_parts (no split needed)
                "Revision": final_parts[0],  # Directly from sub_parts[0]
                "Date": date_formatted
            }
            
            st.write("### Naming Code Breakdown")
            st.table(details)

        except ValueError as e:
            st.error(str(e))
        except Exception as ex:
            st.error(f"Unexpected error: {ex}")
def generate_code_ui(file_type_choice):
    st.subheader("🔹 Generate a Naming Code")
    project_code = "ITIU"  # Fixed Project Name
    st.text_input("Project Name", project_code, disabled=True)  # Dimmed Project Name
    owner = st.selectbox("Project Owner", {"MIC": "MIC", "GOV": "GOV", "SAMI": "SAMI", "2P": "2P"})  # Full owners list
    discipline_options = {
        "Acoustics": "ACU", "Access Control system": "ACS", "Active Data Network Equipment": "ADE",
        "Audio Visual": "AV", "Building management system": "BMS", "Cabling & Distribution": "CD",
        "Cyber Security": "CS", "Data Storage & Backup": "DSB", "Digital Signage": "DS",
        "Electrical HV & LV": "ELV", "Enterprise Resource Planning": "ERP", "Fire Detection & Alarm System": "FDAS",
        "Firefighting System": "FFS", "Grounding": "GRD", "Information and Communication Technology": "ICT",
        "Infrastructure": "INF", "IT Room": "ITR", "IT Service Management": "ITSM", "Lighting": "LT",
        "Mechanical": "MEC", "Network Operation Center": "NOC", "Network Time Protocol Synchronization": "NTP",
        "Outside plant network": "OPN", "Power": "PWR", "Progress Management Document":"PMD","Public Address System": "PAS",
        "Security Operation Center": "SOC", "Software Applications": "SA", "Structured cabling network": "SCN",
        "Telecom Towers": "TT", "Unified Communication": "UC", "Video Surveillance System": "VSS"
    }
    discipline = st.selectbox("Select Discipline", list(discipline_options.keys()))
    phase_options = {"Data Gathering & As-Is Capture": "DGAS", "Assessment": "ASM", "Design": "DE", "General": "GN"}
    phase = st.selectbox("Select Phase", list(phase_options.keys()))
    file_type_options = {
        "Financial Management System": "FMS", "General Accounting Ledger": "GL", "Accounts Receivables Ledger": "AR", "Fixed Assets Ledger": "FA", "Enterprise Asset Management": "EAM",
        "Configuration Management": "CM", "Performance Management System": "PMS", "Product Life Cycle Management": "PLM", "Geographical Information System": "GIS", "Accounts Payables Ledger": "AP", "ERP Projects Management": "EPM", "IT Problem Management": "ITPM", "IT Incident Management": "ITIM", "IT Service Catalogue": "ITSC", "IT Asset Management": "ITAM", "IT Service Desk": "ITSD", "IT Release Management": "ITRM",
        "Identity & Access + Infrastructure Protection": "IAIP", "Monitoring & Operations": "MO", "Incident Response & Continuity": "IRC", "Miscellaneous": "MISC",   "Permit": "PRM", "As-Is Verification Report": "ASISV", "Personnel Approval Form": "PAF", "Assessment Report": "ASSR", "Photographs, Images & Videos": "PVI",
        "Agenda": "AGD", "Project Charter": "PC", "Area Access Request": "AAR", "Preliminary Design Report": "PDR", "As-Is Findings Report": "ASISF", "Report" : "RPT" , "High-Level Design" : "HLD" , "Request for Change" : "RFC" , "Handover Certificate" : "HOC" , "Schedule" : "SCH" , "Inspection Test Plan" : "ITP" , "Specification" : "SPC", "Instruction" : "INS" , "Stakeholder register" : "SKR", "Letter": "LTR", "Standard":"STD" , 
        "Audit Report": "AUR", "Plan": "PLN", "Bill of Quantities": "BOQ", "Policy": "PCY", "Critical Design Report": "CDR", "Presentation": "PRE", "Calculation" : "CAL" , "Procedure" : "PRO","Progress Report":"PGR", "Certificate" : "CER" , "Profile" : "PRF" , "Claim": "CLM" , "Proposal" : "PSL","Communication Plan":"CPL", "Register":"REG", "Execution plan" : "EPL",
        "Human Capital Management": "HCM", "IT Change Management": "ITCM", "Governance and Risk": "GR", "List" : "LST", "Strategy": "STG", "Low-Level Design": "LLD",
        "Taking Over Certificate": "TOC", "Manual": "MAN", "Template": "TEM", "Material Approval": "MA", "Tender Document": "TEN", "Material Inspection Request": "MIR",
        "Prequalification Submittal": "PQQ", "Method Statement": "MTS", "Test Report": "TRP", "Minutes of Meeting": "MOM", "Variation Request": "VAR", "Naming Convention Guide": "NMC",
        "Human Capital Management": "HCM", "IT Change Management": "ITCM", "Governance and Risk": "GR", "List" : "LST" ,"Strategy":"STG","Low-Level Design":"LLD"
    }
    if file_type_choice == "Document":
        file_type = st.selectbox("Select File Type", sorted(file_type_options.keys()))
    else:
        drawing_file_types = {"Drawings in Revit": "RVT", "Drawings in CAD": "CAD", "Drawings in PDF": "DPDF"}
        file_type = st.selectbox("Select File Type", sorted(drawing_file_types.keys()))
    resolution = st.radio("Select Resolution", ["H", "L"])
    zone_options = {
        "Non-Specific (NS)": "NS", "Logistics building (Z02)": "Z02", "Calibration & Laboratory facility (Z20)": "Z20", "Small Caliber storage (Z21)": "Z21",
        "Storage (Stocking MK80 NHS) (Z22)": "Z22", "Energetic magazine storage (Z23)": "Z23", "MP5 & G3 (Z28)": "Z28", "Administration building & Parking (Z31)": "Z31",
        "5.56 mm Ammunition Factory (Z32)": "Z32", "7-9-12 Light ammunition factory (Z33)": "Z33", "Weapon G36 Factory (Z34)": "Z34", "25-30 ammunition factory (Z35)": "Z35",
        "Test range (Z36)": "Z36", "Water tanks (Z37)": "Z37", "Demilitarization administration & 5.56 new bunkers (Z39)": "Z39", "MK80 Part storage (Z40)": "Z40",
        "MK80 paint & 155 mm paint (Z41)": "Z41", "155mm MK80 series (Z42)": "Z42", "Test lab for 155 mm ammunition (Z43)": "Z43", "Thermo cycling chamber (Z44)": "Z44",
        "New production facility (Z45)": "Z45", "SABR facility in renovation (Z46)": "Z46", "Primer Mix (Z47)": "Z47", "20mm Ammunition factory (Z50)": "Z50"

    }
    if file_type_choice == "Drawing":
        st.subheader("Drawing Type")
        drawing_type_options = {
            "0 - Not Applicable": "0",
            "1 - General Arrangement": "1",
            "2 - Plan / Layout": "2",
            "3 - Elevation": "3",
            "4 - Section": "4",
            "5 - Large Scale Views": "5",
            "6 - Detail": "6",
            "7 - Schedules & Diagram": "7",
            "8 - Schematics": "8",
            "A - 3D Model": "A"
        }
      
        drawing_type = drawing_type_options[st.selectbox("Select Drawing Type", list(drawing_type_options.keys()))]
        
        level_options = {
            "00 - Non-Specific": "00",
            "R - Roof": "R",
            "F3 - Third Floor": "F3",
            "F2 - Second Floor": "F2",
            "F1 - First Floor": "F1",
            "GF - Ground Floor": "GF",
            "B1 - Basement 1": "B1",
            "B2 - Basement 2": "B2",
            "B3 - Basement 3": "B3",
            "B4 - Basement 4": "B4"
        }

        drawing_level = level_options[st.selectbox("Select Drawing Level", list(level_options.keys()))]

    zone = st.selectbox("Select Zone", list(zone_options.keys()))
    serial_number = st.text_input("Enter 6-digit Serial Number")
    revision = st.text_input("Enter Revision (2-digit for docs, 1-letter for drawings)")
    date = st.text_input("Enter Date (DDMMYYYY format)")
    if st.button("Generate Code"):
        try:
            if len(date) != 8 or not date.isdigit():
                raise ValueError("Invalid date format. Use DDMMYYYY.")

            if file_type_choice == 'Drawing':
                
                naming_code = f"{project_code}-{owner}-{discipline_options[discipline]}-{phase_options[phase]}-{drawing_file_types[file_type]}-{resolution}-{drawing_type}{drawing_level}-{zone_options[zone]}-{serial_number}_{revision}-{date}"
            else:
                naming_code = f"{project_code}-{owner}-{discipline_options[discipline]}-{phase_options[phase]}-{file_type_options[file_type]}-{resolution}-{zone_options[zone]}-{serial_number}_{revision}-{date}"

            st.success(f"✅ Generated Naming Code: {naming_code}")
        except ValueError as e:
            st.error(str(e))


def main():
    st.title("📌 Naming Convention Tool")
    st.subheader("Choose an option:")
    
    choice = st.radio("Select an option", ["Generate a Naming Code", "Read an Existing Naming Code"])
    
    if choice == "Generate a Naming Code":
        file_type_choice = st.radio("Select File Type", ["Document", "Drawing"])
        generate_code_ui(file_type_choice)
    elif choice == "Read an Existing Naming Code":
        read_code_ui()
    

if __name__ == "__main__":
    main()
