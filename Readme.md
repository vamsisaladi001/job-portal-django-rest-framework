# Job Portal Backend

A Job Portal Backend built using Django and Django REST Framework.

## Features

* User Registration
* User Login
* Recruiter and Candidate Roles
* Job Posting Management
* Job Application Management
* REST APIs
* SQLite Database
* Postman API Testing

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* Git
* GitHub
* Postman

## API Endpoints

### Users

* GET /api/users/
* POST /api/users/
* POST /api/users/register/
* POST /api/users/login/

### Jobs

* GET /api/jobs/
* POST /api/jobs/

### Applications

* GET /api/applications/
* POST /api/applications/

## Database Models

### User

* Username
* Email
* Password
* Role (Recruiter/Candidate)

### Job

* Title
* Company
* Location
* Salary
* Description
* Recruiter

### Application

* Candidate
* Job
* Resume
* Status

## Future Enhancements

* JWT Authentication
* Role-Based Permissions
* Job Search and Filters
* Pagination
* Email Notifications

## Author

Vamsi Saladi
