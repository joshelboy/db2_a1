/*  hr_comment: Create comments for HR schema

    Adaption of Oracle's HR schema for PostgreSQL.
    See https://github.com/oracle/db-sample-schemas/tree/master/human_resources
*/

--------------------------------------------------------------------------------
-- REGIONS table holds region information for locations

COMMENT
ON TABLE hr.regions
    IS 'Regions table that contains region numbers and names. Contains 4 rows; references with the 
Countries table.';

COMMENT
ON COLUMN hr.regions.region_id
    IS 'Primary key of regions table.';

COMMENT
ON COLUMN hr.regions.region_name
    IS 'Names of regions. Locations are in the countries of these regions.';

--------------------------------------------------------------------------------
-- COUNTRIES table holds country information for customers and company locations

COMMENT
ON TABLE hr.countries
    IS 'country table. Contains 25 rows. References with locations table.';

COMMENT
ON COLUMN hr.countries.country_id
    IS 'Primary key of countries table.';

COMMENT
ON COLUMN hr.countries.country_name
    IS 'Country name';

COMMENT
ON COLUMN hr.countries.region_id
    IS 'Region ID for the country. Foreign key to region_id column in the departments table.';

--------------------------------------------------------------------------------
-- LOCATIONS table holds address information for company departments

COMMENT
ON TABLE hr.locations
    IS 'Locations table that contains specific address of a specific office, warehouse, and/or 
production site of a company. Does not store addresses / locations of customers. Contains 23 rows; 
references with the departments and countries tables. ';

COMMENT
ON COLUMN hr.locations.location_id
    IS 'Primary key of locations table';

COMMENT
ON COLUMN hr.locations.street_address
    IS 'Street address of an office, warehouse, or production site of a company. Contains building 
number and street name';

COMMENT
ON COLUMN hr.locations.postal_code
    IS 'Postal code of the location of an office, warehouse, or production site of a company. ';

COMMENT
ON COLUMN hr.locations.city
    IS 'A not null column that shows city where an office, warehouse, or production site of a 
company is located. ';

COMMENT
ON COLUMN hr.locations.state_province
    IS 'State or Province where an office, warehouse, or production site of a company is located.';

COMMENT
ON COLUMN hr.locations.country_id
    IS 'Country where an office, warehouse, or production site of a company is located. 
Foreign key to country_id column of the countries table.';

--------------------------------------------------------------------------------
-- DEPARTMENTS table holds company department information

COMMENT
ON TABLE hr.departments
    IS 'Departments table that shows details of departments where employees work. Contains 27 rows; 
references with locations, employees, and job_history tables.';

COMMENT
ON COLUMN hr.departments.department_id
    IS 'Primary key column of departments table.';

COMMENT
ON COLUMN hr.departments.department_name
    IS 'A not null column that shows name of a department. Administration, Marketing, Purchasing, 
Human Resources, Shipping, IT, Executive, Public Relations, Sales, Finance, and Accounting. ';

COMMENT
ON COLUMN hr.departments.manager_id
    IS 'Manager_id of a department. Foreign key to employee_id column of employees table. 
The manager_id column of the employee table references this column.';

COMMENT
ON COLUMN hr.departments.location_id
    IS 'Location id where a department is located. Foreign key to location_id column of locations 
table.';

--------------------------------------------------------------------------------
-- JOBS table holds the different names of job roles within the company

COMMENT
ON TABLE hr.jobs
    IS 'jobs table with job titles and salary ranges. Contains 19 rows. References with employees 
and job_history table.';

COMMENT
ON COLUMN hr.jobs.job_id
    IS 'Primary key of jobs table.';

COMMENT
ON COLUMN hr.jobs.job_title
    IS 'A not null column that shows job title, e.g. AD_VP, FI_ACCOUNTANT';

COMMENT
ON COLUMN hr.jobs.min_salary
    IS 'Minimum salary for a job title.';

COMMENT
ON COLUMN hr.jobs.max_salary
    IS 'Maximum salary for a job title';

--------------------------------------------------------------------------------
-- EMPLOYEES table holds the employee personnel information for the company

COMMENT
ON TABLE hr.employees
    IS 'employees table. Contains 107 rows. References with departments, jobs, job_history tables. 
Contains a self reference.';

COMMENT
ON COLUMN hr.employees.employee_id
    IS 'Primary key of employees table.';

COMMENT
ON COLUMN hr.employees.first_name
    IS 'First name of the employee. A not null column.';

COMMENT
ON COLUMN hr.employees.last_name
    IS 'Last name of the employee. A not null column.';

COMMENT
ON COLUMN hr.employees.email
    IS 'Email id of the employee';

COMMENT
ON COLUMN hr.employees.phone_number
    IS 'Phone number of the employee; includes country code and area code';

COMMENT
ON COLUMN hr.employees.hire_date
    IS 'Date when the employee started on this job. A not null column.';

COMMENT
ON COLUMN hr.employees.job_id
    IS 'Current job of the employee; foreign key to job_id column of the jobs table. 
A not null column.';

COMMENT
ON COLUMN hr.employees.salary
    IS 'Monthly salary of the employee. Must be greater than zero (enforced by constraint 
emp_salary_min)';

COMMENT
ON COLUMN hr.employees.commission_pct
    IS 'Commission percentage of the employee; Only employees in sales department elgible for 
commission percentage';

COMMENT
ON COLUMN hr.employees.manager_id
    IS 'Manager id of the employee; has same domain as manager_id in departments table. Foreign key 
to employee_id column of employees table. (useful for reflexive joins and CONNECT BY query)';

COMMENT
ON COLUMN hr.employees.department_id
    IS 'Department id where employee works; foreign key to department_id column of the departments 
table';

--------------------------------------------------------------------------------
-- JOB_HISTORY table holds the history of jobs that employees have held in the past

COMMENT
ON TABLE hr.job_history
    IS 'Table that stores job history of the employees. If an employee changes departments within 
the job or changes jobs within the department, new rows get inserted into this table with old job 
information of the employee. Contains a complex primary key: employee_id+start_date. Contains 25 
rows. References with jobs, employees, and departments tables.';

COMMENT
ON COLUMN hr.job_history.employee_id
    IS 'A not null column in the complex primary key employee_id+start_date. Foreign key to 
employee_id column of the employee table';

COMMENT
ON COLUMN hr.job_history.start_date
    IS 'A not null column in the complex primary key employee_id+start_date. Must be less than the 
end_date of the job_history table. (enforced by constraint jhist_date_interval)';

COMMENT
ON COLUMN hr.job_history.end_date
    IS 'Last day of the employee in this job role. A not null column. Must be greater than the 
start_date of the job_history table. (enforced by constraint jhist_date_interval)';

COMMENT
ON COLUMN hr.job_history.job_id
    IS 'Job role in which the employee worked in the past; foreign key to job_id column in the jobs 
table. A not null column.';

COMMENT
ON COLUMN hr.job_history.department_id
    IS 'Department id in which the employee worked in the past; foreign key to deparment_id column 
in the departments table';

