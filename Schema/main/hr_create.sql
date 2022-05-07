/*  hr_create: Create data objects for HR schema

    Adaption of Oracle's HR schema for PostgreSQL.
    See https://github.com/oracle/db-sample-schemas/tree/master/human_resources
*/
CREATE SCHEMA IF NOT EXISTS hr;
--------------------------------------------------------------------------------
-- REGIONS table holds region information for locations

-- DROP TABLE IF EXISTS hr.regions;
CREATE TABLE IF NOT EXISTS hr.regions
(
    region_id   integer NOT NULL,
    region_name varchar(25),
    -- PK
    CONSTRAINT reg_id_pk PRIMARY KEY (region_id)
);

--------------------------------------------------------------------------------
-- COUNTRIES table holds country information for customers and company locations

-- DROP TABLE IF EXISTS hr.countries;
CREATE TABLE IF NOT EXISTS hr.countries
(
    country_id   char(2) NOT NULL,
    country_name varchar(40),
    region_id    integer,
    -- PK
    CONSTRAINT country_c_id_pk PRIMARY KEY (country_id),
    -- FK
    CONSTRAINT countr_reg_fk FOREIGN KEY (region_id)
        REFERENCES hr.regions (region_id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

--------------------------------------------------------------------------------
-- LOCATIONS table holds address information for company departments

-- DROP TABLE IF EXISTS hr.locations;
CREATE TABLE IF NOT EXISTS hr.locations
(
    location_id    integer     NOT NULL,
    street_address varchar(40),
    postal_code    varchar(12),
    city           varchar(30) NOT NULL,
    state_province varchar(25),
    country_id     char(2),
    -- PK
    CONSTRAINT loc_id_pk PRIMARY KEY (location_id),
    -- FK
    CONSTRAINT loc_c_id_fk FOREIGN KEY (country_id)
        REFERENCES hr.countries (country_id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

-- Useful for any subsequent addition of rows to locations table
-- Starts with 3300

-- DROP SEQUENCE IF EXISTS hr.locations_seq;
CREATE SEQUENCE IF NOT EXISTS hr.locations_seq
    INCREMENT 100
    START 3300
    MINVALUE 1
    MAXVALUE 9900
    CACHE 1;

--------------------------------------------------------------------------------
-- DEPARTMENTS table holds company department information

-- DROP TABLE IF EXISTS hr.departments;
CREATE TABLE IF NOT EXISTS hr.departments (
    department_id   integer         NOT NULL,
    department_name varchar(30)     NOT NULL,
    manager_id      integer,
    location_id     integer,
    -- PK
    CONSTRAINT dept_id_pk PRIMARY KEY (department_id),
    -- FK
    CONSTRAINT dept_loc_fk FOREIGN KEY (location_id)
        REFERENCES hr.locations (location_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    -- FK for manager_id has to be set after creation of hr.employees
);

-- Useful for any subsequent addition of rows to departments table
-- Starts with 280 

-- DROP SEQUENCE IF EXISTS hr.departments_seq;
CREATE SEQUENCE IF NOT EXISTS hr.departments_seq
    INCREMENT 10
    START 280
    MINVALUE 1
    MAXVALUE 9990
    CACHE 1;

--------------------------------------------------------------------------------
-- JOBS table holds the different names of job roles within the company

-- DROP TABLE IF EXISTS hr.jobs;
CREATE TABLE IF NOT EXISTS hr.jobs (
    job_id      varchar(10)     NOT NULL,
    job_title   varchar(35)     NOT NULL,
    min_salary  integer,
    max_salary  integer,
    -- PK
    CONSTRAINT job_id_pk PRIMARY KEY (job_id)
);

--------------------------------------------------------------------------------
-- EMPLOYEES table holds the employee personnel information for the company

-- DROP TABLE IF EXISTS hr.employees;
CREATE TABLE IF NOT EXISTS hr.employees (
    employee_id     integer         NOT NULL,
    first_name      varchar(20),
    last_name       varchar(25)     NOT NULL,
    email           varchar(25)     NOT NULL,
    phone_number    varchar(20),
    hire_date       date            NOT NULL,
    job_id          varchar(10)     NOT NULL,
    salary          numeric(8,2),
    commission_pct  numeric(2,2),
    manager_id integer,
    department_id integer,
    -- PK
    CONSTRAINT emp_emp_id_pk PRIMARY KEY (employee_id),
    -- UNIQUE
    CONSTRAINT emp_email_uk UNIQUE (email),
    -- FK
    CONSTRAINT emp_dept_fk FOREIGN KEY (department_id)
        REFERENCES hr.departments (department_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT emp_job_fk FOREIGN KEY (job_id)
        REFERENCES hr.jobs (job_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT emp_manager_fk FOREIGN KEY (manager_id)
        REFERENCES hr.employees (employee_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    -- CHECK
    CONSTRAINT emp_salary_min CHECK (salary > 0)
);

-- FK
ALTER TABLE hr.departments
ADD CONSTRAINT dept_mgr_fk FOREIGN KEY (manager_id)
        REFERENCES hr.employees (employee_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION;

-- Useful for any subsequent addition of rows to employees table
-- Starts with 207 

-- DROP SEQUENCE IF EXISTS hr.employees_seq;
CREATE SEQUENCE IF NOT EXISTS hr.employees_seq
    INCREMENT 1
    START 207
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

--------------------------------------------------------------------------------
-- JOB_HISTORY table holds the history of jobs that employees have held in the past

-- DROP TABLE IF EXISTS hr.job_history;
CREATE TABLE IF NOT EXISTS hr.job_history (
    employee_id     integer         NOT NULL,
    start_date      date            NOT NULL,
    end_date        date            NOT NULL,
    job_id          varchar(10)     NOT NULL,
    department_id   integer,
    -- PK
    CONSTRAINT jhist_emp_id_st_date_pk PRIMARY KEY (employee_id, start_date),
    -- FK
    CONSTRAINT jhist_dept_fk FOREIGN KEY (department_id)
        REFERENCES hr.departments (department_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT jhist_emp_fk FOREIGN KEY (employee_id)
        REFERENCES hr.employees (employee_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT jhist_job_fk FOREIGN KEY (job_id)
        REFERENCES hr.jobs (job_id) 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    -- CHECK
    CONSTRAINT jhist_date_interval CHECK (end_date > start_date)
);

--------------------------------------------------------------------------------
-- EMP_DETAILS_VIEW joins the employees, jobs, departments, jobs, countries, and 
-- locations table to provide details about employees.

-- DROP VIEW hr.emp_details_view;
CREATE OR REPLACE VIEW hr.emp_details_view
 AS
 SELECT e.employee_id,
    e.job_id,
    e.manager_id,
    e.department_id,
    d.location_id,
    l.country_id,
    e.first_name,
    e.last_name,
    e.salary,
    e.commission_pct,
    d.department_name,
    j.job_title,
    l.city,
    l.state_province,
    c.country_name,
    r.region_name
   FROM hr.employees e
     JOIN hr.departments d ON e.department_id = d.department_id
     JOIN hr.locations l ON d.location_id = l.location_id
     JOIN hr.countries c ON l.country_id = c.country_id
     JOIN hr.regions r ON c.region_id = r.region_id
     JOIN hr.jobs j ON j.job_id = e.job_id;

