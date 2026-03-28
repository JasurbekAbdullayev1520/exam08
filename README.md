# EventPulse

## Project Description

EventPulse — bu online va offline eventlarni boshqarish uchun yaratilgan backend servis. Foydalanuvchilar eventlarga ro‘yxatdan o‘tishi, admin esa eventlarni boshqarishi mumkin. Tizimda capacity nazorati va statistik endpointlar mavjud.

---

## Tech Stack

* Django, Django REST Framework
* PostgreSQL
* JWT (SimpleJWT)
* Gunicorn, Nginx
* AWS EC2 (Ubuntu)

---

## API Endpoints

### Auth

* POST `/api/token/`
* POST `/api/token/refresh/`

### Events

* GET `/api/events/`
* POST `/api/events/`
* GET `/api/events/{id}/`
* PUT `/api/events/{id}/`
* DELETE `/api/events/{id}/`

### Registrations

* POST `/api/registrations/`
* DELETE `/api/registrations/{id}/`

### Statistics

* GET `/api/stats/event/{id}/`
* GET `/api/stats/top-events/`

---

## Deployment Steps

* EC2 instance yaratildi va serverga ulandi
* Python, PostgreSQL o‘rnatildi
* Project GitHub’dan clone qilindi
* `.env` sozlandi
* Migrations bajarildi
* Gunicorn va Nginx sozlandi
* Static fayllar collect qilindi

---

