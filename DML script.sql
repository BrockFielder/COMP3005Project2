INSERT INTO public.trainer (
    id, first_name, last_name, email, skills, availablity
) VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', ARRAY['coaching', 'personal training'], 'monday:8:00-12:00,tuesday:8:00-12:00,wednesday:8:00-12:00,thursday:8:00-12:00,friday:8:00-12:00,saturday:8:00-12:00,sunday:8:00-12:00'),
    (2, 'Gary', 'Smith', 'Garysmith@gmail.com', ARRAY['Group cardio classes', 'kickboxing', 'running'], 'monday:9:00-17:00,wednesday:8:00-12:00,thursday:8:00-12:00,friday:8:00-12:00,saturday:8:00-14:00,sunday: off');

INSERT INTO public.staff (
    first_name, last_name, email, service_area, position, staff_id
) VALUES
    ('Joe', 'Doe', 'email23@email.com', 'IT', 'programmer', 1),
    ('Terry', 'Johnson', 'terryjohnson@gmail.com', 'Maintenance', 'facilities manager', 2),
    ('James', 'McDonald', 'jamesmcdonald@gmail.com', 'Management', 'Manager', 3),
    ('Henry', 'Mayphew', 'HenryMayphew@gmail.com', 'Maintenance', 'Janitor', 4);


INSERT INTO public.member (
    ID, first_name, last_name, email, goals, achievements, routines, previous_bills, billing_status, CL_booking, PT_booking, age, weight, sex, phone, blood_pressure, height
) VALUES
    (1, 'Samuel', 'Steward', 'Sam.Steward@gmail.com', '{}', '{}', '{}', '{}', true, '{}', '{}', 29, 150, true, '6134328341', NULL, 180),
    (2, 'Bob', 'Johnson', 'bob.johnson@gmail.com', '{}', '{}', '{}', '{}', true, '{}', '{}', 29, 150, true, '6134328341', NULL, 180),
    (3, 'John', 'Mackenzie', 'JohnMackenzie@gmail.com', '{}', '{}', '{}', '{}', true, '{}', '{}', 38, NULL, NULL, NULL, NULL, NULL),
    (4, 'Sher', 'Lion', 'hb@ghbhgby', '{}', '{}', '{}', '{}', true, '{}', '{}', 26, NULL, NULL, NULL, NULL, NULL),
    (5, 'Dalinar', 'Kholin', 'murder33@ancientways.com', '{}', '{}', '{}', '{}', true, '{}', '{}', 55, NULL, NULL, NULL, NULL, NULL);

INSERT INTO public.room (
    ID, equipment, maintenance, bookings
) VALUES
    (1, '{"Not much", "a bit more", "Even more"}', true, '{}'),
    (2, '{"Bikes", "a bit more"}', true, '{}'),
    (3, '{"12 bikes for cardio classes", "12 dumbells", "12 exercise mats", "space for exercise class of 12 people"}', true, NULL),
    (4, '{"12 mats for yogas", "36 dumbells", "space for exercise class of 12 people"}', false, NULL);

INSERT INTO public.bookings (
    ID, start_time, duration, day, year, teacher, members, room_id
) VALUES
    (2, 18, 1, 51, 2024, 'Max', '{"John","Thomas"}', 3),
    (1, 10, 3, 81, 2024, 'Max', '{"John","Sam"}', 3),
    (3, 12, 2, 3, 2024, 'Johnny', '{"Sam Steward"}', 3),
    (4, 12, 2, 3, 2024, 'Johnny', '{"Sam Steward"}', 3);

