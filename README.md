# Gauravaani 📚🕉️  
*A Spiritual–Educational Platform for Structured Learning*

## Live Preview
🔗 https://gauravaani.onrender.com/

## Overview

**Gauravaani** is a spiritual educational website built to transform a **large, cluttered YouTube lecture archive** into a **well-structured, curriculum-driven learning platform**.

Instead of consuming unorganized content, learners can now follow a **clear academic flow**:

> **Courses → Chapters → Lectures**

The project focuses on **organization, scalability, and maintainability**, while keeping the system lightweight and open for future expansion.

---

## Motivation

Many valuable spiritual and philosophical lectures exist online but remain difficult to navigate due to poor organization.  
Gauravaani was built to solve this problem by:

- Structuring scattered lectures into meaningful learning paths  
- Making spiritual education accessible, systematic, and progressive  
- Designing an admin-controlled system that scales without manual overhead  

This project is not just a website — it is a **framework for structured spiritual education**.

---

## Features

### 🔐 Authentication & Roles
- **User** and **Admin** roles
- Admins can **promote any user to admin** directly from the Admin Panel

### 🧠 Course Organization
- Courses divided into **chapters**
- Chapters further divided into **lectures**
- Full control over structure and content

### 🛠️ Admin Panel (Full Control)
Admins can:
- Create, edit, and delete **courses** and **lectures**
- Manage **chapters and lectures**
- Edit or remove any lecture content
- Control platform data without touching the codebase

### 🗄️ External Data Management (Supabase)
- **Supabase Database** used for all structured data
- **Supabase Storage Buckets** used for:
  - Course thumbnails
  - Media assets
- Keeps the GitHub repository **clean and data-free**
- Enables easier updates, scaling, and maintenance

### 📬 Contact System
- Contact page powered using **Brevo API**
- Secure handling of messages without exposing backend email logic

---

## Tech Stack

### Backend
- **Flask (Python)** — RESTful backend architecture

### Database & Storage
- **Supabase**
  - PostgreSQL database
  - Storage buckets for media assets

### Frontend
- HTML, CSS, JavaScript (templated via Flask)

---

## Architecture Highlights

- Separation of **logic, data, and assets**
- No hardcoded media or thumbnails in the repository
- Role-based access control
- Designed for **easy migration and future extensibility**

---

## Why Supabase?

- Keeps repository lightweight  
- Allows non-developers (admins) to manage content  
- Simplifies data updates without redeploying the application  
- Scales naturally as content grows  

---

## Development Timeline 🛠️

**Total Active Development Time:** ~14 hours  
**Development Style:** Rapid prototyping → iterative refinement → production hardening  
**Version Control:** Git (incremental commits reflecting architectural decisions and bug fixes)

---

### Phase 1: Foundation & Core Models *(Nov 23)*
- Initialized project structure
- Implemented initial **User** and **Course** models
- Established backend architecture using **Flask**
- Defined early database schema

---

### Phase 2: Admin System & Role Control *(Nov 25)*
- Built **Admin Panel**
- Introduced role-based access (**User / Admin**)
- Added course status controls
- Enabled admin-level content management

---

### Phase 3: Course Navigation & UX *(Nov 26)*
- Added **Courses Page**
- Implemented **Breadcrumb navigation**
- Fixed ordering and navigation bugs
- Converted static data into **JSON-driven structure**

---

### Phase 4: Contact System & UI Refinements *(Nov 26 – Nov 27)*
- Added **Contact Page**
- Fixed carousel and layout bugs
- Improved UI responsiveness
- Cleaned unnecessary database fields
- Iteratively refined contact workflow

---

### Phase 5: Database & Production Readiness *(Late Nov)*
- Migrated to **Supabase PostgreSQL**
- Integrated Supabase Storage Buckets
- Added production/development configuration separation
- Introduced environment variables
- Added `Procfile` for deployment readiness

---

### Phase 6: Data Cleanup & Architecture Improvements *(Late Nov – Recent)*
- Normalized database tables
- Removed redundant columns
- Simplified lecture handling (direct URL parsing)
- Fixed admin logic bugs
- Improved sidebar UX and active state handling
- Final fixes to Contact Page using **Brevo API**

---

### Current State
- Fully functional **role-based educational platform**
- Externalized data and assets
- Clean, scalable backend architecture
- Repository remains lightweight and maintainable

---

**Note:**  
This project was built with a focus on **clarity of architecture, scalability, and real-world maintainability**, rather than superficial feature count.


## Contributing 🤝

Contributions are welcome.

If you resonate with the idea of **structured spiritual education**, feel free to:

- **Fork** the repository  
- Experiment with new features  
- Improve UI/UX  
- Add analytics, progress tracking, or recommendations  

> Knowledge grows best when it is built together.

---

## Final Note 🌱

Gauravaani is built with the belief that **learning should be organized, meaningful, and accessible**.

If this project inspires you, take it further.  
Fork it. Break it. Rebuild it. Improve it.

That is how knowledge evolves.

---
## License
This project is licensed under the MIT License.
See the [LICENSE](LICENSE) for more details

## About the Author
Om Sai,
Engineering Student passionate about building scalable, user-centric web applications and unique engineering projects.

Github: https://github.com/OmSai-HonouredOne
