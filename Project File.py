from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from datetime import datetime
    
app = Flask(__name__)
app.secret_key = 'your_secret_key'  


connection = psycopg2.connect(
     dbname="Project",
     user="postgres",
     password="contiki22",
     host="localhost",
     port="5432"
)

cursor = connection.cursor()

#current_user = ''

booking_list = {}
room_list = {}
    
class Room:
    def __init__ (self, ID, equipment, maintenance, bookings):
        self.ID = ID
        self.equipment = equipment
        self.maintenance = maintenance
        self.bookings = bookings
        room_list [self.ID] = self
    
    def save (self):
        
        cursor.execute('SELECT COUNT(*) FROM "Room" WHERE "ID" = %s', (self.ID,))
        result = cursor.fetchone()
        if result[0] == 0:
            cursor.execute('INSERT INTO "Room" ("ID", equipment, maintenance, bookings) VALUES (%s, %s, %s, %s)', (self.ID, self.equipment, self.maintenance, self.bookings))
            connection.commit()
            
        else:        
            query = 'UPDATE "Room" SET "ID" = %s, equipment = %s, maintenance = %s, bookings = %s WHERE "ID" = %s'
            cursor.execute(query, (self.ID, self.equipment, self.maintenance, self.bookings, self.ID))
            connection.commit()        






def load_room(room_id):
    query = 'SELECT "ID", equipment, maintenance, bookings FROM "Room" WHERE "ID" = %s'
    cursor.execute(query, (room_id,))
    row = cursor.fetchone()  
    if row:
        room_list[room_id] = Room(*row)
        print(f"Loaded room {room_id}")
    else:
        print(f"No data found for room ID {room_id}")
            
def load_all_rooms():
    for room_id in range(5):
        load_room(room_id)
load_all_rooms()



class Booking:
    def __init__ (self, ID, start_time, duration, day, year, teacher, members, room_id):
        print("Creating booking\n")
        self.ID = ID
        self.start_time = start_time
        self.duration = duration
        self.day = day
        self.year = year
        self.teacher = teacher
        self.members = members
        self.room_id = room_id
        booking_list [self.ID] = self
        if room_id in room_list:
            room_list[room_id].bookings.append(self)
        else:
            print(f"Room with ID {room_id} does not exist.")
        
        self.save()
            
    def save(self):
        print(f"Saving booking ID: {self.ID}")
        cursor.execute('SELECT COUNT(*) FROM "Bookings" WHERE "ID" = %s', (self.ID,))
        result = cursor.fetchone()
        if result[0] == 0:
            cursor.execute('INSERT INTO "Bookings" ("ID", start_time, "duration", day, year, teacher, members, room_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                           (self.ID, self.start_time, self.duration, self.day, self.year, self.teacher, self.members, self.room_id))
            print("Inserted new booking.")
        else:
            query = 'UPDATE "Bookings" SET start_time = %s, "duration" = %s, day = %s, year = %s, teacher = %s, members = %s, room_id = %s WHERE "ID" = %s'
            cursor.execute(query, (self.start_time, self.duration, self.day, self.year, self.teacher, self.members, self.room_id, self.ID))
            print("Updated existing booking.")
        connection.commit()
    
                                    
                    #load_all_bookings()        



class Profile:
    def __init__(self, ID, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.ID = ID
        
    def change_name (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name  
    
    def change_email (self, email):
        self.email = email
        
    def get_email (self):
        return self.email
    
    def get_first_name (self):
        return (self.first_name)
    
    def get_last_name (self):
        return (self.last_name)
        
    def get_ID (self):
        return self.ID
    


class Staff(Profile): 
    def __init__(self, ID, first_name, last_name, email, service_area, position):
        super().__init__(ID, first_name, last_name, email)
        self.service_area = service_area 
        self.position = position
        
    def get_room_bookings (ID):
        return room_list[ID].bookings
    
    def delete_room_booking (room_ID, class_ID):
        del room_list[room_ID].bookings[class_ID]
        
    def create_booking (ID, start_time, duration, day, year, teacher, members, room_ID):
        new_booking = Booking (ID, start_time, duration, day, year, teacher, members, room_ID)
        booking.save()
        return new_booking
        
    def view_current_billing_info (ID):
        
        member = load_member (ID)
        print (member.billing_status)
        
    def view_previous_billing_info (ID):
        
        member = load_member (ID)
        print (member.previous_bills)    
    
    def view_member_profile (self, first_name, last_name):
        query = 'SELECT "ID", "first_name", "last_name", "email", "goals", "achievements", "routines", "previous_bills", "billing_status", "CL_booking", "PT_booking", "age", "weight", "sex", "phone", "blood_pressure", "height" FROM "member" WHERE "first_name" = %s AND "last_name" = %s'
        cursor.execute(query, (first_name, last_name))
        row = cursor.fetchone() 
           
        if row:
            print("Member Profile:")
            print("ID:", row[0])
            print("First Name:", row[1])
            print("Last Name:", row[2])
            print("Email:", row[3])
            print("Goals:", row[4])
            print("Achievements:", row[5])
            print("Routines:", row[6])
            print("Previous Bills:", row[7])
            print("Billing Status:", row[8])
            print("CL Booking:", row[9])
            print("PT Booking:", row[10])
            print("Age:", row[11])
            print("Weight:", row[12])
            print("Sex:", row[13])
            print("Phone:", row[14])
            print("Blood Pressure:", row[15])
            print("Height:", row[16])
        else:
            print("No member found with the name:", first_name, last_name)
        return row     
    
    
    
    def edit_booking (booking_ID, start_time, duration, day, year, teacher, members, room_ID):
        booking_list[booking_id].start_time = start_time
        booking_list[booking_id].duration = duration
        booking_list[booking_id].day = day
        booking_list[booking_id].year = year
        booking_list[booking_id].teacher = teacher
        booking_list[booking_id].members = members
        
        if (booking_list[booking_id].room_ID != room_ID):
            del room_list[room_ID].bookings[booking_ID]
            room_list[room_ID].bookings.append (booking_list[booking_id])
            booking_list[booking_id].room_ID = room_ID
        
    
    def save (self):
        query = "UPDATE staff SET first_name = %s, last_name = %s, email = %s, service_area = %s, position = %s WHERE staff_ID = %s"
        cursor.execute(query, (self.first_name, self.last_name, self.email, self.service_area, self.position, self.ID))
        connection.commit()
            #row = cursor.fetchone()
        print ("staff saved")
        
    def make_booking(self, start_time, duration, day, year, teacher, room_id):
        booking_id = Member.find_max_id_in_booking()
        new_booking = Booking(booking_id, start_time, duration, day, year, teacher, [self.first_name + " " + self.last_name], room_id)
        new_booking.save()
        
    def fetch_all_bookings(self):
        return booking_list
    
    def remove_booking (ID):
        global booking_list
        if booking_id in booking_list:
            del booking_list[booking_id]
            flash('Booking removed successfully!', 'success')
        else:
            flash('Booking not found!', 'error')        

class Member (Profile):
    def __init__ (self, ID, first_name, last_name, email, goals, achievements, routines, previous_bills, billing_status, CL_booking, PT_booking, age, weight, sex, phone, blood_pressure, height):
        super().__init__(ID, first_name, last_name, email)
        self.goals = goals
        self.achievements = achievements
        self.routines = routines
        self.previous_bills = previous_bills
        self.billing_status = billing_status
        self.CL_booking = CL_booking
        self.PT_booking = PT_booking
        self.age = age
        self.weight = weight
        self.sex = sex
        self.phone = phone
        self.blood_pressure = blood_pressure
        self.height = height
        
    def find_max_id_in_booking ():
        query = 'SELECT MAX("ID") FROM "Bookings"'
        cursor.execute(query)
        result = cursor.fetchone()[0] 
                       
        if result is not None:
            return result + 1
        else:
            return 1        
    
    def view_member_profile(self):
        #print("\n".join(self.goals) + "\n")
        #print("\n".join(self.achievements) + "\n")
        #print("\n".join(self.routines) + "\n")
        #print(self.previous_bills + "\n")  
        #print(self.billing_status + "\n")  
        #print(self.CL_booking + "\n") 
        #print(self.PT_booking + "\n")  
        #print(str(self.age) + "\n")  
        #print(str(self.weight) + "\n")
        #print   
        
        return self.__dict__        
    
    def make_booking(self, start_time, duration, day, year, teacher, room_id):
        booking_id = Member.find_max_id_in_booking()
        new_booking = Booking(booking_id, start_time, duration, day, year, teacher, [self.first_name + " " + self.last_name], room_id)
        new_booking.save()
        return new_booking
        

        
    def save(self):
        cursor.execute('SELECT COUNT(*) FROM "member" WHERE "ID" = %s', (self.ID,))
        result = cursor.fetchone()
        
        if result[0] == 0:
            query = '''INSERT INTO "member" ("ID", "first_name", "last_name", "email", "goals", "achievements", "routines", "previous_bills", "billing_status", "CL_booking", "PT_booking", "age", "weight", "sex", "phone", "blood_pressure", "height") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(query, (self.ID, self.first_name, self.last_name, self.email, self.goals, self.achievements, self.routines, self.previous_bills, self.billing_status, self.CL_booking, self.PT_booking, self.age, self.weight, self.sex, self.phone, self.blood_pressure, self.height))
        else:
            query = '''UPDATE "member" SET "first_name" = %s, "last_name" = %s, "email" = %s, "goals" = %s, "achievements" = %s, "routines" = %s, "previous_bills" = %s, "billing_status" = %s, "CL_booking" = %s, "PT_booking" = %s, "age" = %s, "weight" = %s, "sex" = %s, "phone" = %s, "blood_pressure" = %s, "height" = %s WHERE "ID" = %s'''
            cursor.execute(query, (self.first_name, self.last_name, self.email, self.goals, self.achievements, self.routines, self.previous_bills, self.billing_status, self.CL_booking, self.PT_booking, self.age, self.weight, self.sex, self.phone, self.blood_pressure, self.height, self.ID))
        
        connection.commit()
    
def find_max_id ():
    query = 'SELECT MAX("ID") FROM Member'
    cursor.execute(query)
    result = cursor.fetchone()[0] 
                   
    if result is not None:
        return result + 1
    else:
        return 1
        
    
@app.route('/create_member', methods=['GET', 'POST'])
def create_member():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            age = int(request.form['age'])
    
            member_id = find_max_id()
            new_member = Member(member_id, first_name, last_name, email, [], [], [], [], True, [], [], age, None, None, None, None, None)
            new_member.save()
    
            flash('Member created successfully!', 'success')
        except Exception as e:
            flash(f'Error creating member: {e}', 'error')
    
        return redirect(url_for('create_member'))
    return render_template('create_member.html')

@app.route('/member_home/<int:member_id>')
def member_home(member_id):
    member = load_member(member_id) 
    if member:
        stats = member.view_member_profile()
        return render_template('member_home.html', member=member, stats=stats)
    else:
        flash('Member not found!', 'error')
        return redirect(url_for('index'))
    

            
@app.route('/create_booking/<int:member_id>', methods=['GET', 'POST'])
def create_booking(member_id):
    if request.method == 'POST':
        try:
            start_time = request.form['start_time']
            duration = int(request.form['duration'])
            day = request.form['day']
            year = int(request.form['year'])
            teacher = request.form['teacher']
            room_id = int(request.form['room_id'])

            from datetime import datetime
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()

            member = load_member(member_id)
            if member:
                new_booking = member.make_booking(start_time_obj, duration, day, year, teacher, room_id)
                member.save()
                new_booking.save()
                flash('Booking created successfully!', 'success')
            else:
                flash('Member not found!', 'error')
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')
            connection.rollback()  # Ensure to rollback on error
        finally:
            return redirect(url_for('member_home', member_id=member_id))

    return render_template('create_booking.html', member_id=member_id)



@app.route('/login', methods=['GET', 'POST'])
def member_login():
    if request.method == 'POST':
        member_id = request.form['member_id']
        member = load_member(member_id)
        if member:
            return redirect(url_for('member_home', member_id=member_id))
        else:
            flash('Member not found!', 'error')
    return render_template('login.html')



@app.route('/modify_member/<int:member_id>', methods=['GET', 'POST'])
def modify_member(member_id):
    member = load_member(member_id)
    if not member:
        flash('Member not found!', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            # Update member details with the form data
            member.first_name = request.form.get('first_name', '')
            # Include other fields with a default or similar fallback
            member.save()  # Assuming the Member class has a save method to update the database
            flash('Your stats have been updated.', 'success')
            return redirect(url_for('member_home', member_id=member_id))
        except KeyError as e:
            flash(f'Missing field {e.args[0]}', 'error')
            return render_template('modify_member.html', member=member)

    return render_template('modify_member.html', member=member)

    
@app.route('/member_stats/<member_id>')
def member_stats(member_id):
    member = load_member(member_id)
    if member:
        stats = member.view_member_profile()  # Make sure this returns the data you want to show
        return render_template('member_stats.html', stats=stats)
    else:
        flash('Member not found!', 'error')
        return redirect(url_for('index'))    
    
    
        
class Trainer (Profile):
    def __init__(self, ID, first_name, last_name, email, availablity, skills):
        super().__init__(ID, first_name, last_name, email)
        self.availablity = availablity
        self.skills = skills
        
    def update_working_hours(self, formatted_availability):
        # This method now directly sets the availability
        self.availablity = formatted_availability

    def view_member_profile(self, first_name, last_name):
        query = '''
        SELECT "ID", "first_name", "last_name", "email", "goals", "achievements", "routines", 
               "previous_bills", "billing_status", "CL_booking", "PT_booking", "age", "weight", 
               "sex", "phone", "blood_pressure", "height"
        FROM "member" 
        WHERE "first_name" = %s AND "last_name" = %s
        '''
        cursor.execute(query, (first_name, last_name))
        row = cursor.fetchone()
        
        if row:
            # Assuming the row contains all the necessary fields in the correct order
            return {
                'email': row[3],
                'goals': row[4],
                'achievements': row[5],
                'routines': row[6],
                'previous_bills': row[7],
                'billing_status': row[8],
                # Add other fields as necessary
            }
        else:
            return None
    
        
    
    def save(self):
           # Here we assume a connection and cursor from psycopg2 are available
        query = '''UPDATE "trainer" SET "first_name" = %s, "last_name" = %s, "email" = %s, "skills" = %s, "availablity" = %sWHERE "id" = %s'''
        cursor.execute(query, (self.first_name, self.last_name, self.email, self.skills, self.availablity, self.ID))
        connection.commit()    

def load_staff (ID):
    query = "SELECT staff_ID, first_name, last_name, email, service_area, position FROM staff WHERE staff_ID = %s"
    
    cursor.execute(query, (ID,))
    row = cursor.fetchone()
           
    if row is not None:
        staff_member = Staff(*row)
        return staff_member
           
    else:
        print("No data found for ID:", ID)
        return None
    
def load_member(ID):
    query = 'SELECT "ID", "first_name", "last_name", "email", "goals", "achievements", "routines", "previous_bills", "billing_status", "CL_booking", "PT_booking", "age", "weight", "sex", "phone", "blood_pressure", "height" FROM "member" WHERE "ID" = %s'
    
    cursor.execute(query, (ID,))
    row = cursor.fetchone()
    
    if row is not None:
        member = Member(*row)
        return member
    else:
        print("No data found for ID:", ID)
        return None

    
def load_trainer(trainer_id):
    query = """
    SELECT ID, first_name, last_name, email, availablity, skills 
    FROM trainer 
    WHERE ID = %s
    """
    cursor.execute(query, (trainer_id,))
    row = cursor.fetchone()
    
    if row:
        trainer = Trainer(ID=row[0], first_name=row[1], last_name=row[2], email=row[3], availablity=row[4], skills=row[5])
        return trainer
    else:
        print(f"No data found for Trainer ID: {trainer_id}")
        return None



        
@app.route('/staff_login', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        staff = load_staff(staff_id)
        if staff:
            return redirect(url_for('staff_dashboard', staff_id=staff_id))
        else:
            flash('Invalid staff ID', 'error')
    return render_template('staff_login.html')

@app.route('/staff_dashboard/<int:staff_id>', methods=['GET'])
def staff_dashboard(staff_id):
    staff = load_staff(staff_id)
    if not staff:
        flash('Staff not found, please login again.', 'error')
        return redirect(url_for('staff_login'))
    return render_template('staff_dashboard.html', staff=staff)


@app.route('/some_staff_operation/<int:staff_id>', methods=['GET', 'POST'])
def some_staff_operation(staff_id):
    staff = load_staff(staff_id)
    if not staff:
        flash('Staff not found, please login again.', 'error')
        return redirect(url_for('staff_login'))

    if request.method == 'POST':
        pass

    return render_template('some_staff_operation.html', staff=staff)


@app.route('/manage_bookings/<int:staff_id>')
def manage_bookings(staff_id):
    staff = load_staff(staff_id)
    if not staff:
        flash('Staff not found, please login again.', 'error')
        return redirect(url_for('staff_login'))
    
    bookings = Staff.fetch_all_bookings() if hasattr(Staff, 'fetch_all_bookings') and isinstance(Staff.fetch_all_bookings, staticmethod) else staff.fetch_all_bookings()
    return render_template('manage_bookings.html', bookings=bookings, staff=staff)



@app.route('/new_booking/<int:staff_id>', methods=['GET', 'POST'])
def new_booking(staff_id):
    staff = load_staff(staff_id)
    if not staff:
        flash('Staff not found, please login again.', 'error')
        return redirect(url_for('staff_login'))

    if request.method == 'POST':
        start_time = request.form.get('start_time')
        duration = request.form.get('duration')
       
        create_new_booking(start_time, duration, ...)
        flash('Booking created successfully!', 'success')
        return redirect(url_for('manage_bookings', staff_id=staff_id))

    return render_template('new_booking.html', staff_id=staff_id)

@app.route('/edit_booking/<int:staff_id>/<int:booking_id>', methods=['GET', 'POST'])
def edit_booking(staff_id, booking_id):
    staff = load_staff(staff_id)
    booking = load_booking(booking_id)
    if not staff or not booking:
        flash('Staff or booking not found.', 'error')
        return redirect(url_for('staff_login'))

    if request.method == 'POST':
        new_start_time = request.form.get('start_time')
        new_duration = request.form.get('duration')

        update_booking(booking_id, new_start_time, new_duration, ...)
        flash('Booking updated successfully!', 'success')
        return redirect(url_for('manage_bookings', staff_id=staff_id))

    return render_template('edit_booking.html', booking=booking, staff_id=staff_id)

@app.route('/delete_booking/<int:staff_id>/<int:booking_id>')
def delete_booking(staff_id, booking_id):
    staff = load_staff(staff_id)
    if not staff:
        flash('Staff not found, please login again.', 'error')
        return redirect(url_for('staff_login'))

    remove_booking(booking_id)
    flash('Booking deleted successfully!', 'success')
    return redirect(url_for('manage_bookings', staff_id=staff_id))

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('index')) 

@app.route('/trainer_login', methods=['POST'])
def trainer_login():
    trainer_id = request.form['trainer_id']
    return redirect(url_for('trainer_dashboard', trainer_id=trainer_id))

@app.route('/trainer_dashboard/<int:trainer_id>')
def trainer_dashboard(trainer_id):
    return render_template('trainer_dashboard.html', trainer_id=trainer_id)

@app.route('/update_schedule/<int:trainer_id>', methods=['POST'])
def update_schedule(trainer_id):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    availability = {}
    for day in days:
        availability[day] = request.form.get(day, '') 
        
    formatted_availability = ','.join([f"{day}:{times}" for day, times in availability.items() if times])

    trainer = load_trainer(trainer_id)
    if not trainer:
        flash('Trainer not found!', 'error')
        return redirect(url_for('trainer_dashboard', trainer_id=trainer_id))

    trainer.update_working_hours(formatted_availability)  
    trainer.save() 
    flash('Schedule updated successfully!', 'success')
    
    trainer.save()
    return redirect(url_for('trainer_dashboard', trainer_id=trainer_id))

@app.route('/view_member_profile', methods=['POST'])
def view_member_profile():
    trainer_id = request.form['trainer_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    # Assuming you can get a Trainer object by ID
    trainer = get_trainer_by_id(trainer_id)  # Define this function to fetch the trainer

    if not trainer:
        flash('Trainer not found', 'error')
        return redirect(url_for('trainer_dashboard', trainer_id=trainer_id))

    member_details = trainer.view_member_profile(first_name, last_name)

    if not member_details:
        flash('Member not found', 'error')
        return redirect(url_for('trainer_dashboard', trainer_id=trainer_id))

    return render_template('member_profile_trainer.html', 
                           trainer_id=trainer_id,
                           member_name=f"{first_name} {last_name}",
                           **member_details)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        staff_id = request.form.get('staff_id')  
        if staff_id:
            staff = load_staff(staff_id)
            if staff:
                session['staff_id'] = staff_id
                flash('Login successful. Welcome, {}'.format(staff.first_name), 'success')
                return redirect(url_for('dashboard'))  
            else:
                flash('Invalid staff ID', 'error')
        else:
            flash('Please enter a staff ID', 'error')

    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
    

