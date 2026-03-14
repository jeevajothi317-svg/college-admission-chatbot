user_name = ""
def get_response(message):
    message = message.lower()
    global user_name 
    if "my name is" in message:
        user_name=message.replace("my name is","").strip()
        return f"Nice to meet you {user_name}.How can I help with admission?"   

    if "hi" in message or "hello" in message or "hey" in message:
        if user_name:
            return f"Welcome back {user_name}.How can I help you?"
        else:
            return "Welcome to our College Admission Assistant \nWhat is your name?"

    words = message.split()
    for w in words:
        if w.isdigit():
            mark = int(w)

            if mark >= 180:
                return "Your mark is good. You can try BSc Computer Science or BCA." 
            elif mark >= 150:
                return "You can try Bcom,BCA or BSc Maths." 
            elif mark >= 120:
                return "You can try BA or BCom Courses." 
            else:
                return "Please contact the admission office for course guidance." 
   
    if "i want admmission" in message or "need admission" in message or "join" in message:
        return "Great Please tell your 12th mark so I can suggest a suitable course."       

    elif "admission" in message or "apply" in message or "join" in message:
        return "Admission starts in June. Visit the admission office or apply online."
     
    elif "computer" in message:
        return "If you like computer field you can choose:\n1.BSc Computer Science\n2.BCA"

    elif"commerce" in message:
        return "If you like commerce field you can choose:\n1.BCom\n2.BBA"

    elif "science" in message:
        return "If you like science field you can choose:\n1.BSc Maths\n2.BSc Physics" 

    elif "course" in message or "courses" in message or "courses available" in message or "department" in message:
        return "Our college offers  the following courses:\n1. BSc Computer Science,\n2. BCA,\n3. BCom, \n4. BBA , \n5.BA English,and\n6. MSc"

    elif "fees" in message or "fee" in message or "cost" in message:
        return "The average annual fee is around ₹40,000 depending on the course."

    elif "hostel" in message or "stay" in message or "accommodation" in message:
        return "Yes, hostel facilities are available for both boys and girls with food and accommodation."
    
    elif "where" in message or "location" in message or "college location" in message:
        return "Our Arts and Science college campus is located in Tamil Nadu.You can visit the admission office for details."

    elif "contact" in message or "phone" in message or "number" in message: 
        return "You can contact the admission office at 9876543210."
    
    elif "thanks" in message or "thank you" in message:
        return "You're welcome .If you need admission details,feel free to ask."
    
    elif "bye" in message or "goodbye" in message:
        return "Thank you for visiting our College Admission Assistant."
    
    elif "placement" in message:
        return "Placement support available for final year students."
    
    elif "last date" in message or "deadline" in message:
        return "The last date to apply for admission is 30 June.Please submit your application before the deadline."
    
    elif "When to apply" in message:
        return "You should apply before 30 June to secure your seat."
    
    elif "bca" in message:
        return "Yes BCA course is available."
    
    elif "mba" in message:
        return "Yes MBA course is available."
    
    elif "companies" in message:
        return "Many IT companies visit for campus placement."
    
    elif "library" in message:
        return "The college has a large library."
    
    elif "wifi" in message:
        return "Campus WiFi is available."
    
    elif "canteen" in message:
        return "The college has a canteen facility."
    
    elif "sports" in message:
        return "Sports facilities are available."
    
    elif "scholarship" in message:
        return "Scholarships are available for eligible students."
    
    elif "government scholarship" in message:
        return "Government scholarship are available."
    
    elif "location" in message:
        return "The college is located in the city campus."
    
    elif "office hours" in message:
        return "Office hours are 9AM to 2PM."
    
    elif "attendance" in message:
        return "Attendance is compulsory."
    
    elif "id card" in message:
        return "Students receive ID cards."
    
    elif "ragging" in message:
        return "Ragging is strictly prohibited in the campus."
    
    elif "event" in message:
        return "Cultural events and college fest are conducted."
    
    elif "clubs" in message:
        return "Various student clubs are available."
    
    elif "workshops" in message:
        return "Workshops and seminars are conducted regularly."
    
    elif "thank" in message or "thanks" in message:
        return "You're welcome.If you need admission details,feel free to ask."
    
    elif "ok" in message or "okay" in message:
        return "Alright.Let me know if you need any other college information."
     
    elif "good" in message:
        return "glad you found it helpful" 

    else:
        return "Sorry, I didn't understand. Please ask about admission, courses, fees, or hostel."