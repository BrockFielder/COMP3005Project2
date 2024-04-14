-- Table: public.Bookings

-- DROP TABLE IF EXISTS public."Bookings";

CREATE TABLE IF NOT EXISTS public."Bookings"
(
    "ID" integer,
    start_time integer,
    duration integer,
    day integer,
    year integer,
    teacher text COLLATE pg_catalog."default",
    members text[] COLLATE pg_catalog."default",
    room_id integer
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Bookings"
    OWNER to postgres;

-- Table: public.Room

-- DROP TABLE IF EXISTS public."Room";

CREATE TABLE IF NOT EXISTS public."Room"
(
    "ID" integer,
    equipment text[] COLLATE pg_catalog."default",
    maintenance boolean,
    bookings integer[]
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Room"
    OWNER to postgres;

-- Table: public.member

-- DROP TABLE IF EXISTS public.member;

CREATE TABLE IF NOT EXISTS public.member
(
    "ID" integer NOT NULL,
    first_name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    goals text[] COLLATE pg_catalog."default",
    achievements text[] COLLATE pg_catalog."default",
    routines text[] COLLATE pg_catalog."default",
    previous_bills boolean[],
    billing_status boolean,
    "CL_booking" integer[],
    "PT_booking" integer[],
    age integer,
    weight double precision,
    sex boolean,
    phone text COLLATE pg_catalog."default",
    blood_pressure text COLLATE pg_catalog."default",
    height integer,
    CONSTRAINT member_pkey PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.member
    OWNER to postgres;

-- Table: public.staff

-- DROP TABLE IF EXISTS public.staff;

CREATE TABLE IF NOT EXISTS public.staff
(
    first_name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    service_area text COLLATE pg_catalog."default",
    "position" text COLLATE pg_catalog."default",
    staff_id integer NOT NULL,
    CONSTRAINT staff_pkey PRIMARY KEY (staff_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.staff
    OWNER to postgres;

-- Table: public.trainer

-- DROP TABLE IF EXISTS public.trainer;

CREATE TABLE IF NOT EXISTS public.trainer
(
    id integer NOT NULL,
    first_name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    skills text[] COLLATE pg_catalog."default",
    availablity text COLLATE pg_catalog."default",
    CONSTRAINT trainer_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.trainer
    OWNER to postgres;