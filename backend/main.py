from fastapi import FastAPI, Path, HTTPException, Query, Depends
from backend.database import engine
from fastapi.responses import JSONResponse
from sqlalchemy import text
from backend.models import Patient, PatientUpdate, DoctorRegister, DoctorLogin
from backend.auth import hash_password, verify_password, create_access_token, get_current_doctor



app = FastAPI()

@app.get("/view")
def test_database(doctor:str = Depends(get_current_doctor)):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM patients"))
        final_result = result.mappings().all()
        return final_result

@app.get("/view/{patient_id}")
def view_patient(patient_id:int = Path(..., description="Enter patient id"), doctor:str = Depends(get_current_doctor)):
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM patients WHERE p_id={patient_id}"))
        final_result = result.mappings().all()
        if final_result:
            return final_result
        raise HTTPException(status_code=404,detail="Patient Not Found")

@app.get("/sort")
def sort_patients(sort_by = Query(..., description="Sort on the basis of height, weight"), order = Query("asc", description="Sort in ascending or descending order"), doctor:str = Depends(get_current_doctor)):
    with engine.connect() as connection:
        if order == "desc":
            result = connection.execute(text(f"SELECT * FROM patients ORDER BY {sort_by} DESC"))
        else:
            result = connection.execute(text(f"SELECT * FROM patients ORDER BY {sort_by}"))
        
        final_result = result.mappings().all()
        if final_result:
            return final_result
        raise HTTPException(status_code=400,detail="Invalid request")

@app.post("/create")
def create_patient(patient: Patient, doctor:str = Depends(get_current_doctor)):
    # the data first goes to the Patient class for validation 
    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO patients
                (p_id, name, city, age, gender, height, weight, verdict)
                VALUES
                (:p_id, :name, :city, :age, :gender, :height, :weight, :verdict)
            """),
            patient.model_dump() # convert the validated data into dictionary
        )
        connection.commit()

    return JSONResponse(status_code=201, content={"message": "patient created successfully."})

@app.put("/edit/{patient_id}")
def view_patient(patient_id: int, patient:PatientUpdate, doctor:str = Depends(get_current_doctor)):
    with engine.connect() as connection:
        result = connection.execute(
            text(f"SELECT * FROM patients WHERE p_id={patient_id}")
        )

        existing = result.mappings().first()
        # gives the matching row as dictionary

        if existing is None:
            raise HTTPException(status_code=404, detail="Not found")

        data = dict(existing)
        updates = patient.model_dump(exclude_unset = True)

        data.update(updates)

        height = float(data["height"])
        weight = float(data["weight"])

        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            verdict = "underweight"
        elif bmi < 25:
            verdict = "Normal"
        elif bmi < 30:
            verdict = "overweight"
        else:
            verdict = "obese"

        data["verdict"] = verdict
        data["id"] = patient_id

        connection.execute(
            text("""
            UPDATE patients
            SET name= :name,
            city = :city,
            age = :age,
            gender = :gender,
            height = :height,
            weight = :weight,
            verdict = :verdict
            WHERE p_id = :id"""),
            data
        )

        connection.commit()

    return JSONResponse(status_code=201, content={"message": "patient created successfully."})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:int, doctor:str = Depends(get_current_doctor)):
    with engine.connect() as connection:
        result = connection.execute(
            text(f"SELECT * FROM patients WHERE p_id = {patient_id}")
        )

        existing = result.mappings().first()

        if existing is None:
            raise HTTPException(status_code=404, detail="Not found")

        connection.execute(
            text(f"DELETE FROM patients WHERE p_id={patient_id}")
        )

        connection.commit()

    return JSONResponse(status_code=201, content={"message": "Deleted successfully."})


@app.post("/register")
def register_doc(doctor: DoctorRegister):
    hashed_pass = hash_password(doctor.password)
    with engine.connect() as connection:
        connection.execute(
            text("""
            INSERT INTO doctors(username, password_hash)
            VALUES (:username, :password_hash)
            """),
            {
                "username": doctor.username,
                "password_hash":hashed_pass
            }
        )

        connection.commit()
    
    return JSONResponse(status_code=201, content={"message": "doctor registered successfully."})
    

@app.post("/login")
def login_doctor(doctor: DoctorLogin):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT username, password_hash
                FROM doctors
                WHERE username = :username
            """),
            {"username": doctor.username}
        ).mappings().first()

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(doctor.password, result["password_hash"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(result["username"])

    return {
        "access_token": token,
        "token_type": "bearer"
    }
