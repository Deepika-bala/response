import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "good morning", "hey"):
        return "hey!WELCOME to Madurai startups.Are you looking for office / co working / events / free lancers/ jobs / showcase"
    if user_message in ("yes, i am looking for office", "office"):
        return "we have offices from 4 people and above.?How many people do you have on a team"
    if user_message in ("4", "5", "6"):
        return "okay will update you the details.Do you want to book(yes/no)"
    if user_message in ("yes", "yes,i want to book"):
        return "okay,please do specify your mail id. we will update you via mail soon.have a nice day"
    if user_message in "no":
        return "okay,Thankyou.let us know if you need any help."
    if user_message in "co working":
        return "We offer a Floating work place from 400 rs per day,Do you want to book(yes/no)?"
    if user_message in ("events"):
        return "here are our events.please do check https://maduraistartups.in/events/. Do you want to book or" , "organise any events?"
    if user_message in ("freelancers", "free lancers", "free lancer"):
        return "what Domain you are looking for? and  also specify your mail id to  get notified "
    if user_message in ("Showcases", "product Showcase","showcase"):
        return "do check here. https://maduraistartups.in/showcase/"
    if user_message in ("job" , "jobs"):
        return "do check here.https://maduraistartups.in/job-openings/  and specify your mail id"


    if user_message in "Thankyou":
        return "we are here to assist you anytime.Thanks"
    if user_message in ("time", "time?"):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    #return "okay.will contact you soon.Have a nice day"

