from frontend import get_patient, submit, expander


def main():
  patient = get_patient()
  submit(patient)
  expander()


if __name__ == "__main__":
  main()
