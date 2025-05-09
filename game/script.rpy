# Define characters
define mc = Character("[player_name]", color="#3b83bd")
define mccuen = Character("Mr. McCuen", color="#2ca02c")
define cisco = Character("Mr. Cisco", color="#d62728")
define mim = Character("Mim Jatlock", color="#9467bd")
define ut1 = Character("Unnamed Teacher #1", color="#8c564b")
define ut2 = Character("Unnamed Teacher #2", color="#e377c2")
define vince = Character("Vince McMahon", color="#7f7f7f")
define taylor = Character("Taylor Swift", color="#bcbd22")
define von = Character("King Von", color="#17becf")
define shannon = Character("Shannon Sharpe (Unc)", color="#ff7f0e")
define us1 = Character("Unnamed Student #1", color="#aec7e8")
define us2 = Character("Unnamed Student #2", color="#ffbb78")
define us3 = Character("Unnamed Student #3", color="#98df8a")
define filipino = Character("Filipino", color="#ff9896")

# Define images (placeholders)
image classroom = "images/classroom.jpg"
image classroom_hot = "images/classroom_hot.jpg"
image classroom_cold = "images/classroom_cold.jpg"
image hallway = "images/hallway.jpg"
image computer_lab = "images/computer_lab.jpg"
image ceiling_incident = "images/ceiling_incident.jpg"
image von_reveal = "images/von_reveal.jpg"

# Define character sprites
image mccuen = "images/characters/mccuen.png"
image cisco = "images/characters/cisco.png"
image mim = "images/characters/mim.png"
image ut1 = "images/characters/unnamed_teacher1.png"
image ut2 = "images/characters/unnamed_teacher2.png"
image vince = "images/characters/vince_mcmahon.png"
image taylor = "images/characters/taylor_swift.png"
image von = "images/characters/king_von.png"
image shannon = "images/characters/shannon_sharpe.png"
image us1 = "images/characters/unnamed_student1.png"
image us2 = "images/characters/unnamed_student2.png"
image us3 = "images/characters/unnamed_student3.png"
image filipino = "images/characters/filipino.png"

# Initialize variables
default respect_points = 0
default coding_skill = 0
default has_evidence = False
default survived_falling_bar = False

# Start the game
label start:
    
    # Introduction
    scene black
    "Two Years of Code: A CS Class Story"
    "A game about surviving Mr. McCuen's computer science class..."
    
    python:
        player_name = renpy.input("What is your name?", length=20)
        if player_name == "":
            player_name = "Student"
    
    scene classroom
    "Day 1 - First Year"
    "Your journey in Mr. McCuen's computer science class begins..."
    
    show mccuen at center with dissolve
    mccuen "Welcome to Computer Science. I'm Mr. McCuen, and for the next two years, you'll be learning how to code and solve problems."
    
    show mccuen at left with move
    show cisco at right with dissolve
    cisco "And I'm Mr. Cisco. I'll be popping in from time to time to check on your progress."
    
    hide cisco with dissolve
    
    mccuen "Let's start with the basics. Who here has coding experience?"
    
    menu:
        "Raise your hand confidently":
            $ respect_points += 1
            $ coding_skill += 2
            mccuen "Good to see some experience. That might help you, but don't get cocky."
        
        "Raise your hand hesitantly":
            $ respect_points += 0
            $ coding_skill += 1
            mccuen "Some familiarity will help, but you have a lot to learn."
        
        "Keep your hand down":
            $ coding_skill += 0
            mccuen "That's alright. We all start somewhere."
    
    hide mccuen
    
    "As class continues, you notice something strange about the room..."
    
    # Temperature incident #1
    scene classroom_hot
    "The classroom suddenly becomes unbearably hot."
    
    show us1 at left
    us1 "Is it just me or is it like a sauna in here?"
    
    show filipino at right
    filipino "I'm melting, bro. It wasn't this hot back home."
    
    show mccuen at center
    mccuen "The temperature controls in this building have always been... temperamental. Let me see what I can do."
    
    hide mccuen
    hide us1
    hide filipino
    
    "Ten minutes later..."
    
    scene classroom_cold
    "Now the room is freezing cold."
    
    show us2 at left
    us2 "I can't feel my fingers to type!"
    
    show mccuen at center
    mccuen "Welcome to the joys of this classroom. You'll get used to it... or you won't."
    
    "This would be the first of many temperature adventures in Mr. McCuen's class."
    
    # First year montage
    scene classroom
    "The first year passes with many coding challenges and temperature fluctuations."
    
    "You learn about variables, loops, conditionals, and how to bring an extra sweater AND a fan to class."
    
    $ coding_skill += 5
    
    # Start of second year
    scene classroom
    "Day 1 - Second Year"
    
    show mccuen at center
    mccuen "Welcome back! I hope you remember something from last year because we're diving straight into advanced topics."
    
    # Celebrity cameo #1
    show mccuen at left
    show taylor at right
    
    taylor "Surprise guest lecture! Today I'll be teaching you about how I use programming concepts in my music production."
    
    menu:
        "Ask a thoughtful question":
            $ respect_points += 2
            taylor "That's a really good question! I appreciate your interest."
        
        "Ask for an autograph":
            $ respect_points -= 1
            taylor "Let's stay focused on coding today, okay?"
        
        "Stay quiet and take notes":
            $ respect_points += 1
            "You diligently take notes on Taylor's coding insights."
    
    hide taylor
    hide mccuen
    
    # The ceiling incident
    scene ceiling_incident
    "One day during a particularly intense debugging session..."
    
    "CRASH!"
    
    show us3 at center
    us3 "AHHH!"
    
    show mccuen at left
    mccuen "Everyone stay calm!"
    
    "A metal bar has fallen from the ceiling, narrowly missing Unnamed Student #3."
    
    menu:
        "Rush to help move the bar":
            $ respect_points += 2
            $ survived_falling_bar = True
            "You and other students carefully move the fallen bar to the side."
            mccuen "Quick thinking there. Safety first in coding and in life."
        
        "Take photos as evidence":
            $ has_evidence = True
            $ survived_falling_bar = True
            "You document the incident. This might come in handy later."
            mccuen "I appreciate the documentation, but maybe help your classmate first next time?"
        
        "Freeze in shock":
            $ survived_falling_bar = True
            "You're too shocked to move, but fortunately no one was hurt."
            mccuen "These things happen... though they probably shouldn't."
    
    hide us3
    hide mccuen
    
    # Mystery begins
    scene classroom
    "As the second year progresses, strange things start happening in the classroom."
    
    "Code mysteriously deletes itself. The temperature swings become more extreme."
    
    show mim at center
    mim "I've been analyzing the classroom data. Something's not right with the system."
    
    hide mim
    
    show shannon at center
    shannon "Listen here, skip. I been watching this classroom, and something ain't right. That's on God."
    
    hide shannon
    
    # Investigation phase
    scene computer_lab
    "You decide to investigate what's happening."
    
    menu:
        "Check the HVAC system logs":
            "You discover unusual patterns in the temperature changes. They seem... deliberate."
            $ has_evidence = True
        
        "Review the security camera footage":
            "The footage shows a shadowy figure accessing the computer systems late at night."
            $ has_evidence = True
        
        "Ask other teachers about the history of the room":
            show ut1 at left
            ut1 "This room? Oh, there have always been strange stories about this place."
            
            show ut2 at right
            ut2 "I wouldn't worry about it. Probably just old wiring."
            
            "Something about their dismissive attitude seems suspicious."
            hide ut1
            hide ut2
    
    # Confrontation
    scene classroom
    "After gathering evidence, you confront Mr. McCuen with your findings."
    
    show mccuen at center
    mccuen "I've suspected something was wrong for a while, but I couldn't prove it."
    
    if has_evidence:
        mccuen "With what you've discovered, we might finally get to the bottom of this."
        $ respect_points += 3
    else:
        mccuen "We need more concrete evidence before we can act."
    
    hide mccuen
    
    # The twist villain reveal
    scene von_reveal
    "Later that week, you stay late to work on a project when you hear voices from the server room."
    
    "You quietly approach and peek inside..."
    
    show vince at left
    vince "The plan is working perfectly. Soon we'll have control of all the school's systems."
    
    show von at right
    von "And no one suspects a thing. These coding students are too busy dealing with the temperature to notice what we're really doing."
    
    "You gasp involuntarily."
    
    show von at center
    hide vince
    von "Well, well, well. Looks like we have a curious student."
    
    # Final confrontation
    menu:
        "Confront King Von directly":
            mc "I know what you're doing! The temperature changes, the falling ceiling parts - it was all a distraction!"
            
            von "Smart kid. Too bad no one will believe you."
            
            if coding_skill >= 7:
                "Using your coding knowledge, you quickly send a message to Mr. McCuen with your location."
                $ respect_points += 2
            else:
                "You wish you had paid more attention in class now."
        
        "Pretend you didn't hear anything":
            mc "Oh! I was just looking for my flash drive. I'll be going now..."
            
            von "Not so fast. I think you heard too much."
            
            if has_evidence:
                mc "I've already backed up evidence about what's happening here. People know."
                von "That complicates things."
            else:
                "You realize you have no leverage in this situation."
        
        "Try to hack into the system on the spot":
            if coding_skill >= 8:
                "You quickly execute the code you've been working on all semester."
                "The system responds to your commands, locking Von out."
                von "What? What are you doing to my system?"
                $ respect_points += 3
            else:
                "You try to remember what Mr. McCuen taught about security protocols, but your mind goes blank."
                von "Nice try, amateur."
    
    # Climax
    "Just as the situation seems dire..."
    
    show mccuen at left
    show cisco at right
    
    mccuen "Step away from my student, Von!"
    
    cisco "We've been tracking your activities for months."
    
    show shannon at center
    shannon "That's what I'm talkin' about! Game over for you, Von. That's on God!"
    
    # Resolution
    scene classroom
    "With King Von's scheme exposed, the classroom returns to normal... well, as normal as Mr. McCuen's class ever was."
    
    show mccuen at center
    
    if respect_points >= 8:
        mccuen "Your problem-solving skills and determination throughout these two years have been exceptional. You have a bright future in computer science."
    elif respect_points >= 4:
        mccuen "You've shown real growth over these two years. Keep developing those skills."
    else:
        mccuen "Well, you made it through two years. That's something, I suppose."
    
    hide mccuen
    
    # Epilogue
    "As you finish your final project for Mr. McCuen's class, you reflect on everything you've learned."
    
    "Not just about coding, but about perseverance, problem-solving, and surviving extreme temperature fluctuations."
    
    "Whatever challenges await you after this class, you know you're prepared to face them."
    
    "THE END"
    
    # Credits
    scene black
    "Two Years of Code: A CS Class Story"
    "Based on real experiences in Mr. McCuen's Computer Science Class"
    "Special thanks to the real Mr. McCuen for two unforgettable years"
    
    return