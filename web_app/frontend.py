import datetime
import streamlit as st
from Patient import Patient
from backend import worksheet
from lists import *


def get_patient():
  st.title("Patient Data Archive", anchor=False)
  st.write("Enter patient data below: ")

  name = st.text_input("Name")
  mrn = st.number_input("MRN", value=None, max_value=10000000)
  sex = st.selectbox("Sex", ["Male", "Female"], index=None)
  dob = str(st.date_input("Date of birth", min_value=datetime.date(1920, 1, 1), value=None, format="DD/MM/YYYY"))
  age = st.number_input("Age", value=None, max_value=100)
  doctor = st.selectbox("Doctor's Name", DOCTORS, index=None)
  icd_10_code = st.selectbox("ICD-10 Code", ICD_10_CODES, index=None)
  diagnosis_non_cancer = st.text_input("Diagnosis / Non-cancer")
  note = st.text_input("Note")
  icd_0_code = st.selectbox("ICD-0 Code", ICD_0_CODES, index=None)
  diagnosis_cancer = st.text_input("Diagnosis / Cancer")
  comment = st.text_input("Comment")
  icd_0_code_morphology = st.selectbox("ICD-0 Code (Morphology)", ICD_0_CODES_MORPHOLOGY, index=None)
  morphology = st.selectbox("Morphology", MORPHOLOGY, index=None)
  department = st.selectbox("Department", DEPARTMENTS, index=None)
  governorate = st.selectbox("Governorate", GOVERNORATES, index=None)
  district = st.selectbox("District", DISTRICTS, index=None)
  nationality = st.selectbox("Nationality", NATIONALITIES, index=None)
  occupation = st.selectbox("Occupation", OCCUPATIONS, index=None)
  addmission_date = str(st.date_input("Date of Addmission", value=None, format="DD/MM/YYYY"))
  discharge_date = str(st.date_input("Date of Discharge", value=None, format="DD/MM/YYYY"))
  status = st.selectbox("Status", STATUSES, index=None)
  t = st.text_input("T")
  n = st.text_input("N")
  m = st.text_input("M")
  stage = st.selectbox("State", STAGES, index=None)
  grade = st.selectbox("Grade", GRADES, index=None)
  extent = st.text_input("Extent")
  procedure = st.text_input("Procedure")

  patient = Patient(name, mrn, sex, dob, age, doctor, icd_10_code, diagnosis_non_cancer, note, icd_0_code, diagnosis_cancer, comment, icd_0_code_morphology, morphology, department, governorate, district, nationality, occupation, addmission_date, discharge_date, status, t, n, m, stage, grade, extent, procedure)
  
  return patient


def submit(patient):
  if st.button("Submit Data", type="primary", use_container_width=True):
    worksheet.append_row([
      patient.name,
      patient.sex,
      patient.dob,
      patient.age,
      patient.mrn,
      patient.doctor,
      patient.icd_10_code,
      patient.diagnosis_non_cancer,
      patient.note,
      patient.icd_0_code,
      patient.diagnosis_cancer,
      patient.comment,
      patient.icd_0_code_morphology,
      patient.morphology,
      patient.department,
      patient.governorate,
      patient.district,
      patient.nationality,
      patient.occupation,
      patient.addmission_date,
      patient.discharge_date,
      patient.status,
      patient.t,
      patient.n,
      patient.m,
      patient.stage,
      patient.grade,
      patient.extent,
      patient.procedure
    ])

def sidebar():
  st.sidebar.markdown("*Made by Muthana Ali from Warith International Cancer Institute IT Department.*")
  st.sidebar.link_button("Contact", "t.me/muthanii")