from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ApplicationForm(BaseModel):
    question: str
    field_type: str  # Could be 'Mandatory', 'Optional', or 'Off'


@app.post("/application_form")
def create_application_form(application_form: ApplicationForm):
    # Assuming here that the form is being saved to a database or some storage
    # We can perform validation here as well
    # For simplicity, let's just print the received data
    print("Received application form:", application_form)
    return {"message": "Application form submitted successfully"}


@app.post("/submit_application")
def submit_application(application_form: ApplicationForm):
    # Validate if all mandatory fields are filled
    if application_form.field_type == "Mandatory":
        raise HTTPException(status_code=400, detail="Please enter required field")

    # Assuming here that the application is being saved to a database or some storage
    # For simplicity, let's just print the received data
    print("Submitted application form:", application_form)
    return {"message": "Application submitted successfully"}
