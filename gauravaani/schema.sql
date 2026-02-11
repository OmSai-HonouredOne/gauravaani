-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.contact (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  name text NOT NULL,
  email text NOT NULL,
  subject text NOT NULL,
  message text NOT NULL,
  pending boolean NOT NULL DEFAULT true,
  is_reply boolean NOT NULL DEFAULT false,
  CONSTRAINT contact_pkey PRIMARY KEY (id)
);
CREATE TABLE public.courses (
  cid bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  course_id text NOT NULL UNIQUE,
  course_title text NOT NULL,
  course_description text,
  course_image text NOT NULL,
  course_complete boolean NOT NULL DEFAULT false,
  course_created_at timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT courses_pkey PRIMARY KEY (cid)
);
CREATE TABLE public.lectures (
  lid bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  cid bigint NOT NULL,
  course_chapter bigint NOT NULL,
  lec_no bigint NOT NULL,
  lec_title text NOT NULL,
  lec_summary text NOT NULL,
  lec_url text NOT NULL,
  notes_url text,
  lec_created_at timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT lectures_pkey PRIMARY KEY (lid),
  CONSTRAINT lectures_cid_fkey FOREIGN KEY (cid) REFERENCES public.courses(cid)
);
CREATE TABLE public.users (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  username text NOT NULL,
  password text NOT NULL,
  email text NOT NULL UNIQUE,
  admin boolean DEFAULT false,
  CONSTRAINT users_pkey PRIMARY KEY (id)
);
