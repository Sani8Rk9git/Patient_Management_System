-- Create patients table
CREATE TABLE patients (
    p_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    height NUMERIC(5,2),
    weight NUMERIC(5,2)
);

-- Create doctors table
CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);