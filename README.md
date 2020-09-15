# TRAVELAN WEB APPLICATION
MICROSOFT STUDENT ACCELERATOR 2020 - WEB APP API (TECHNICAL STREAM)

- Written by Dat Huynh
- Email: viendat.huynh@student.unsw.edu.au
- School of Computer Science and Engineering, University of New South Wales

## 1. PROJECT IDEA
Travelan web app helps travellers planning their travel plans, both previous and future trips. It also stores images for every destination a traveller has been to or plans to visit.

## 2. TECH-STACK DESCRIPTION
### Back-end
The backend is written in Python and uses Flask to manage the dynamic and static contents. It connects with the database through SQLAlchemy. The backend will receive requests from user, retrieve necessary data, process and give response back to the frontend.

### Front-end
HTML, Bootstrap and some Javascript are used to build up the website. All pages includes a header and footer from base.html. The body sections have various functions on different pages.

### Database
User data is stored using SQLAlchemy which connects to the backend. The database is a table named Destination whose columns are:

- id

- name

- caption

- image names

- date, month, year

- country

- visited / not visited

for every destination in the user's list.

## 3. USER INTERFACE
All pages includes a header and a footer. In the header, there are

- Travelan logo on top left which directs to the home page

- Toogle menu button on top right which shows all the pages

- Background image, title, caption and a main button

with a different function for each page.

- Scroll down button for quickly accessing the contents below


There are 4 main pages in the web app:

- Home page: Preview the list with information about numbers of visited places, number of visited countries and the next destination in the plan. Display three recent destinations in the list

- Destination page: Display all the destinations in the database in blog style. Add new destinations by clicking on the main button

- Plan page: Display all the destinations in the database in table for managing data. Add new destinations by clicking on the main button

- Detail page: Display all details of a destionation with name, country, date, caption and images. Edit by clicking on the main button
