from web_app.frontend import get_patient, submit


def main():
  patient = get_patient()
  submit(patient)


if __name__ == "__main__":
  main()
