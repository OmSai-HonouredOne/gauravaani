DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS lectures;
DROP TABLE IF EXISTS contact;


CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    admin BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE courses (
    cid INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id TEXT NOT NULL UNIQUE,
    course_title TEXT NOT NULL,
    course_description TEXT,
    course_image TEXT NOT NULL,
    course_complete BOOLEAN NOT NULL DEFAULT 0,
    course_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lectures (
    lid INTEGER PRIMARY KEY AUTOINCREMENT,
    cid INTEGER NOT NULL,
    course_chapter INTEGER NOT NULL,
    lec_no FLOAT NOT NULL,
    lec_title TEXT NOT NULL,
    lec_summary TEXT NOT NULL,
    lec_url TEXT NOT NULL,
    notes_url TEXT,
    lec_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cid) REFERENCES courses(cid)
);

CREATE TABLE contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    pending BOOLEAN NOT NULL DEFAULT 1,
    is_reply BOOLEAN NOT NULL DEFAULT 0
);