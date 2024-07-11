from frontend import get_patient, submit, sidebar


def main():
  patient = get_patient()
  submit(patient)
  sidebar()


if __name__ == "__main__":
  main()
