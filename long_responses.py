import random

R_EATING = "I dont like eating anything because I'm a bot obviously."
def unknown():
    response = ['could you please re-phrase that?',
                 "...",
                 "sounds about right",
                 "What does that mean?"][random.randrange(44)]
    return response