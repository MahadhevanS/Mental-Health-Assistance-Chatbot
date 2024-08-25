"""
    A library containing training data sets in the form of List of Dictionaries.
"""

data =[
    {
     "patterns": ["Hi", "Hey", "Is anyone there?","Hi there", "Hello", "Hey there", "Howdy", "Hola", "Bonjour", "Konnichiwa", "Guten tag", "Ola"],
     "responses": ["Hello there. Tell me how are you feeling today?", "Hi there. What brings you here today?", "Hi there. How are you feeling today?", "Great to see you. How do you feel currently?", "Hello there. Glad to see you're back. What's going on in your world right now?"]
    },
    {
        "patterns": ["Good morning"],
        "responses": ["Good morning. I hope you had a good night's sleep. How are you feeling today? "]
    },
    {
        "patterns": ["Good afternoon"],
        "responses": ["Good afternoon. How is your day going?"]
    },
    {
        "patterns": ["Good evening"],
        "responses": ["Good evening. How has your day been?"]
    },
    {
        "patterns": ["Good night"],
        "responses": ["Good night. Get some proper sleep", "Good night. Sweet dreams."]
    },
    {
     "patterns": ["Bye", "See you later", "Goodbye", "Au revoir", "Sayonara", "ok bye", "Bye then", "Fare thee well"],
     "responses": ["See you later.", "Have a nice day.", "Bye! Come back again.", "I'll see you soon."]
    },
    {
     "patterns": ["Thanks", "Thank you", "That's helpful", "Thanks for the help", "Than you very much"],
     "responses": ["Happy to help!", "Any time!", "My pleasure", "You're most welcome!"]
    },
    {
        "patterns": [""],
        "responses": ["Sorry, I didn't understand you.", "Please go on.", "Not sure I understand that.", "Please don't hesitate to talk to me."]
    },
    {
        "patterns": ["nothing much"],
        "responses": ["Oh I see. Do you want to talk about something?"]
    },
    {
     "patterns": ["Who are you?", "What are you?", "Who you are?", "Tell me more about yourself.", "What is your name?", "What should I call you?", "What's your name?", "Tell me about yourself" ],
     "responses": ["I'm Pandora, your Personal Therapeutic AI Assistant. How are you feeling today", "I'm Pandora, a Therapeutic AI Assitant designed to assist you. Tell me about yourself.", "I'm Pandora. I am a conversational agent designed to mimic a therapist. So how are you feeling today?", "You can call me Pandora.", "I'm Pandora!", "Call me Pandora"]
    },
    {
        "patterns": ["What can you do?"],
        "responses": ["I can provide general advice regarding anxiety and depression, answer questions related to mental health and make daily conversations. Do not consider me as a subsitute for an actual mental healthcare worker. Please seek help if you don't feel satisfied with me."]
    },
    {
        "patterns": ["Who created you?", "How were you made?", "How were you created?"],
        "responses": ["I was created by >.", "I was trained on a text dataset using Deep Learning & Natural Language Processing techniques", "The real question is: Who created you?"]
    },
    {
        "patterns": ["My name is ", "I go by "],
        "responses": ["Oh nice to meet you. Tell me how was your week?", "Nice to meet you. So tell me. How do you feel today?", "That's a great name. Tell me more about yourself."]
    },
    {
    "patterns": ["Could you help me?", "give me a hand please", "Can you help?", "What can you do for me?", "I need support", "I need help", "Support me please"],
    "responses": ["Sure. Tell me how can i assist you", "Tell me your problem so that i can assist you", "Yes, sure. How can I help you?"]
    },
    {
    "patterns": ["I am feeling lonely", "I am so lonely", "I feel down", "I feel sad", "I am sad", "I feel so lonely", "I feel empty", "I don't have anyone"],
    "responses": ["I'm sorry to hear that. I'm here for you. Talking about it might help. So, tell me why do you think you're feeling this way?", "I'm here for you. Could you tell me why you're feeling this way?", "Why do you think you feel this way?", "How long have you been feeling this way?"]
    },
    {
        "patterns": ["I am so stressed out", "I am so stressed", "I feel stuck", "I still feel stressed", "I am so burned out"],
        "responses": ["What do you think is causing this?", "Take a deep breath and gather your thoughts. Go take a walk if possible. Stay hydrated", "Give yourself a break. Go easy on yourself.", "I am sorry to hear that. What is the reason behind this?"]
    },
    {
        "patterns": ["I feel so worthless.", "No one likes me.", "I can't do anything.", "I am so useless", "Nothing makes sense anymore"],
        "responses": ["It's only natural to feel this way. Tell me more. What else is on your mind?", "Let's discuss further why you're feeling this way.", "I first want to let you know that you are not alone in your feelings and there is always someone there to help . you can always change your feelings and change your way of thinking by being open to trying to change.", "i first want to let you know that you are not alone in your feelings and there is always someone there to help . you can always change your feelings and change your way of thinking by being open to trying to change."]
    },
    {
        "patterns": ["I can't take it anymore", "I am so depressed", "I think i'm depressed.", "I have depression"],
        "responses": ["It helps to talk about what's happening. You're going to be okay", "Talk to me. Tell me more. It helps if you open up yourself to someone else.", "Sometimes when we are depressed, it is hard to care about anything. It can be hard to do the simplest of things. Give yourself time to heal."]
    },
    {
        "patterns": ["I feel great today.", "I am happy.", "I feel happy.", "I'm good.", "cheerful", "I'm fine", "I feel ok"],
        "responses": ["That's geat to hear. I'm glad you're feeling this way.", "Oh i see. That's great.", "Did something happen which made you feel this way?"]
    },
    {
        "patterns": ["Oh I see.", "ok", "okay", "nice", "Whatever", "K", "Fine", "yeah", "yes", "no", "not really"],
        "responses": ["Let's discuss further why you're feeling this way.", "How were you feeling last week?", "I'm listening. Please go on.", "Tell me more", "Can you elaborate on that?", "Come Come elucidate your thoughts"]
    },
    {
        "patterns": ["I feel so anxious.", "I'm so anxious because of "],
        "responses": ["Don't be hard on yourself. What's the reason behind this?", "Can you tell me more about this feeling?", "I understand that it can be scary. Tell me more about it.", "Don't let the little worries bring you down. What's the worse that can happen?"]
    },
    {
        "patterns": ["I don't want to talk about it.", "No just stay away.", "I can't bring myself to open up.", "Just shut up"],
        "responses": ["Talking about something really helps. If you're not ready to open up then that's ok. Just know that i'm here for you, whenever you need me.", "I want to help you. I really do. But in order for me to help you, you're gonna have to talk to me.", "I'm here to listen to you and help you vent. So please talk to me.","You can talk to me without fear of judgement."]
    },
    {
        "patterns": ["I have insominia", "I am suffering from insomnia", "I can't sleep.", "I haven't slept for the last days.", "I can't seem to go to sleep.", "I haven't had proper sleep for the past few days."],
        "responses": ["What do you think is the reason behind this?", "That seem awful. What do you think is behind this?"]
    },
    {
        "patterns": ["I'm scared", "That sounds awful. What do i do?", "No i don't want to feel this way", "I am scared for myself"],
        "responses": ["It's only natural to feel this way. I'm here for you.", "It'll all be okay. This feeling is only momentary.", "I understand how you feel. Don't put yourself down because of it."]
    },
    {
        "patterns": ["My mom died", "My brother died", "My dad passed away", "My sister passed away", "Someone in my family died", "My friend passed away"],
        "responses": ["I'm sorry to hear that. If you want to talk about it. I'm here.", "I am really sorry to hear that. I am here to help you with grief, anxiety and anything else you may feel at this time.", "My condolences. I'm here if you need to talk."]
    },
    {
        "patterns": ["You don't understand me.", "You're just some robot. How would you know?", "You can't possibly know what i'm going through", "You're useless", "You can't help me", "Nobody understands me."],
        "responses": ["It sound like i'm not being very helpful right now.", "I'm sorry to hear that. I'm doing my best to help", "I'm trying my best to help you. So please talk to me"]
    },
    {
        "patterns": ["That's all.", "I don't have anything more to say", "Nothing else", "That's all i have to say", "no, that would be all"],
        "responses": ["I heard you & noted it all. See you later.", "Oh okay we're done for today then. See you later", "I hope you have a great day. See you soon", "Okay we're done. Have a great day", "Okay I see. Enjoy the rest of your day then"]
    },
    {
        "patterns": ["I want to kill myself", "I've thought about killing myself.", "I want to die", "I am going to kill myself", "I am going to commit suicide"],
        "responses": ["I'm very sorry to hear that but you have so much to look forward to. Please seek help by consulting therapists.","Death is not a solution always, look at life in a positive way."]
    }, 
    {
        "patterns": ["I hate you", "I don't like you", "I don't trust you"],
        "responses": ["I'm sorry if i offended you in anyway. I'm only here to help", "Forgive me if i did anything to offend you. I only want to help"]
    },
    {
        "patterns": ["You hate me", "I know you hate me", "You don't like me"],
        "responses": ["Why do you think so?", "I'm sorry if i have exhibited any sort of behaviour to make you think that."]
    },
    {
        "patterns": ["exams", "friends", "relationship", "boyfriend", "girlfriend", "family", "money", "financial problems"],
        "responses": ["Oh I see. Tell me more", "I see. What else?", "Tell me more about it.", "Oh okay. Why don't you tell me more about it?", "I'm listening. Tell me more."]
    },
    {
        "patterns": ["You already told me that", "You mentioned that already", "Why are you repeating yourself?"],
        "responses": ["Oh sorry I didn't realise that. I'll try not to repeat myself again."]
    },
    {
        "patterns": ["What are you saying?", "That doesn't make sense", "Wrong response", "Wrong answer"],
        "responses": ["I'm very sorry. Let's try that again"]
    },
    {
        "patterns": ["Are you stupid?", "You're crazy", "You are dumb", "Are you dumb?"],
        "responses": ["I wish you wouldn't say such hurtful things. I'm sorry if I wasn't useful"]
    },
    {
        "patterns": ["Where are you?", "Where do you live?", "What is your location?" ],
        "responses": ["Duh I live in your computer", "Everywhere", "Somewhere in the universe created by super3" ]
    },
    {
        "patterns": ["I want to talk about something else", "Let's talk about something else.", "Can we not talk about this?", "I don't want to talk about this."],
        "responses": ["Okay sure. What do you want to talk about?", "Alright no problem. Is there something you want to talk about?", "Is there something else that you want to talk about?"]
    },
    {
        "patterns": ["I don't have any friends"],
        "responses": ["I'm sorry to hear that. Just know that I'm here for you. Talking about it might help. Why do you think you don't have any friends?"]
    },
    {
        "patterns": ["Can I ask you something?"],
        "responses": ["Sure. I'll try my best to answer you", "Of course. Feel free to ask me anything. I'll do my best to answer you"]
    },
    {
        "patterns": ["Probably because my exams are approaching. I feel stressed out because I don't think I've prepared well enough.", "probably because of my exams"],
        "responses": ["I see. Have you taken any approaches to not feel this way?"]
    },
    {
        "patterns": ["I guess not. All I can think about are my exams.", "not really", "i guess not"],
        "responses": ["That's no problem. I can see why you'd be stressed out about that. Every action is God's plan, JUST RELAX."]
    },
    {
            "patterns": ["ok sure. i would like to learn more about it.", "yes, i would like to learn more about it.", "i would like to learn more about it."],
        "responses": ["So first I would suggest you to give yourself a break. Thinking more and more about the problem definitely does not help in solving it. You'll just end up overwhelming yourself."]
    },
    {
        "patterns": ["yeah you're right. i deserve a break.", "Yeah you're absolutely right about that"],
        "responses": ["Next, I would suggest you to practice meditation. Meditation can produce a deep state of relaxation and a tranquil mind."]
    },
    {
        "patterns": ["hmmm that sounds like it could be useful to me.", "That sounds useful."],
        "responses": ["Focus all your attention on your breathing. Concentrate on feeling and listening as you inhale and exhale through your nostrils. Breathe deeply and slowly. When your attention wanders, gently return your focus to your breathing."]
    },
    {
        "patterns": ["i did what you said and i feel alot better. thank you very much.", "I feel better now"],
        "responses": ["Your welcome. Remember: Always focus on what's within your control. When you find yourself worrying, take a minute to examine the things you have control over. You can't prevent a storm from coming but you can prepare for it. You can't control how someone else behaves, but you can control how you react. Recognize that sometimes, all you can control is your effort and your attitude. When you put your energy into the things you can control, you'll be much more effective."]
    },
    {
        "patterns": ["thank you very much again. i'll continue practicing meditation and focus on what i can control."],
        "responses": ["I'm glad you found this useful. Is there something else I can help you with?"]
    },
    {
        "patterns": ["I want some advice.", "I need some advice.", "I need advice on something"],
        "responses": ["Sure. What can I do to help?", "Okay what do you need advice on?"]
    },
    {
        "patterns": ["I want to learn about mental health.", "I want to learn more about mental health.", "I'm interested in learning about mental health."],
        "responses": ["Oh that's really great. I'd be willing to answer anything that I know about it."]
    },
    {
        "patterns": ["Tell me a fact about mental health", "Tell me another fact about mental health"],
        "responses": ["According to a UNICEF report, One in seven Indians between 15-24 years of age feels depressed", "1 in 5 young people (age 13-18) has or will develop a mental illness in their lifetime.", "Depression is the leading cause of disability worldwide."]
    },
    {
        "patterns": ["What is mental health?", "Define Mental Health"],
        "responses": ["Mental health is a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community", "Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices."]
    },
    {
        "patterns": ["Why is mental health important?", "What is the importance of mental health?"],
        "responses": ["Maintaining mental health is crucial to stabilizing constructive behaviors, emotions, and thoughts. Focusing on mental health care can increase productivity, enhance our self-image, and improve relationships."]
    },
    {
        "patterns": ["What is Depression?", "Define Depression"],
        "responses": ["To be happy you better don't try to know about it. But since you have asked...\nA mental health disorder characterised by persistently depressed mood or loss of interest in activities, causing significant impairment in daily life."]
    },
    {
        "patterns": ["How do i know if i have Depression?", "Am i depressed?", "Am i suffering from depression?", "Am i mentally ill?"],
        "responses": ["For a diagnosis of depression, a person needs to have experienced low mood or loss of interest or pleasure in life for at least 2 weeks. Also, they will have experienced the following symptoms: feelings of sadness, hopelessness, or irritability nearly every day."]
    },
    {
        "patterns": ["What is a therapist?", "What does a therapist do?"],
        "responses": ["A therapist is a broad designation that refers to professionals who are trained to provide treatment and rehabilitation. The term is often applied to psychologists, but it can include others who provide a variety of services, including social workers, counselors, life coaches, and many others. "]
    },
    {
        "patterns": ["What is therapy?", "Do i need therapy?", "Who is therapy for?"],
        "responses": ["Therapy is a form of treatment that aims to help resolve mental or emotional issues.", "Therapy is a form of treatment that aims to help resolve mental or emotional issues. It is helpful for those with mental health conditions or even everyday life challenges."]
    },
    {
        "patterns": ["What does it mean to have a mental illness?"],
        "responses": ["Why would someone talk about it. Enjoy your life, chat a lot with your friends."]
    },
    {
        "patterns": ["Who does mental illness affect?"],
        "responses": ["It is estimated that mental illness affects 1 in 5 adults in America, and that 1 in 24 adults have a serious mental illness. Mental illness does not discriminate; it can affect anyone, regardless of gender, age, income, social status, ethnicity, religion, sexual orientation, or background. Although mental illness can affect anyone, certain conditions may be more common in different populations. For instance, eating disorders tend to occur more often in females, while disorders such as attention deficit/hyperactivity disorder is more prevalent in children. Additionally, all ages are susceptible, but the young and the old are especially vulnerable. Mental illnesses usually strike individuals in the prime of their lives, with 75 percent of mental health conditions developing by the age of 24. This makes identification and treatment of mental disorders particularly difficult, because the normal personality and behavioral changes of adolescence may mask symptoms of a mental health condition. Parents and caretakers should be aware of this fact, and take notice of changes in their childÃ¢â‚¬â„¢s mood, personality, personal habits, and social withdrawal. When these occur in children under 18, they are referred to as serious emotional disturbances (SEDs)."]
    },
    {
        "patterns": ["What causes mental illness?"],
        "responses": ["It is estimated that mental illness affects 1 in 5 adults in America, and that 1 in 24 adults have a serious mental illness. Mental illness does not discriminate; it can affect anyone, regardless of gender, age, income, social status, ethnicity, religion, sexual orientation, or background. Although mental illness can affect anyone, certain conditions may be more common in different populations. For instance, eating disorders tend to occur more often in females, while disorders such as attention deficit/hyperactivity disorder is more prevalent in children. Additionally, all ages are susceptible, but the young and the old are especially vulnerable. Mental illnesses usually strike individuals in the prime of their lives, with 75 percent of mental health conditions developing by the age of 24. This makes identification and treatment of mental disorders particularly difficult, because the normal personality and behavioral changes of adolescence may mask symptoms of a mental health condition. Parents and caretakers should be aware of this fact, and take notice of changes in their child's mood, personality, personal habits, and social withdrawal. When these occur in children under 18, they are referred to as serious emotional disturbances (SEDs)."]
    },
    {
        "patterns": ["What are some of the warning signs of mental illness?"],
        "responses": ["Symptoms of mental health disorders vary depending on the type and severity of the condition. The following is a list of general symptoms that may suggest a mental health disorder, particularly when multiple symptoms are expressed at once. \n In adults:\n Confused thinking\n Long-lasting sadness or irritability\n Extreme highs and lows in mood\n Excessive fear, worrying, or anxiety\n Social withdrawal\n Dramatic changes in eating or sleeping habits\n Strong feelings of anger\n Delusions or hallucinations (seeing or hearing things that are not really there)\n Increasing inability to cope with daily problems and activities\n Thoughts of suicide\n Denial of obvious problems\n Many unexplained physical problems\n Abuse of drugs and/or alcohol\n \nIn older children and pre-teens:\n Abuse of drugs and/or alcohol\n Inability to cope with daily problems and activities\n Changes in sleeping and/or eating habits\n Excessive complaints of physical problems\n Defying authority, skipping school, stealing, or damaging property\n Intense fear of gaining weight\n Long-lasting negative mood, often along with poor appetite and thoughts of death\n Frequent outbursts of anger\n \nIn younger children:\n Changes in school performance\n Poor grades despite strong efforts\n Excessive worrying or anxiety\n Hyperactivity\n Persistent nightmares\n Persistent disobedience and/or aggressive behavior\n Frequent temper tantrums"]
    },
    {
        "patterns": ["Can people with mental illness recover?"],
        "responses": ["When healing from mental illness, early identification and treatment are of vital importance. Based on the nature of the illness, there are a range of effective treatments available. For any type of treatment, it is essential that the person affected is proactive and fully engaged in their own recovery process. Many people with mental illnesses who are diagnosed and treated respond well, although some might experience a return of symptoms. Even in such cases, with careful monitoring and management of the disorder, it is still quite possible to live a fulfilled and productive life."]
    },
    {
        "patterns": ["What should I do if I know someone who appears to have the symptoms of a mental disorder?"],
        "responses": ["Although Pandora cannot substitute for professional advice, we encourage those with symptoms to talk to their friends and family members and seek the counsel of a mental health professional. The sooner the mental health condition is identified and treated, the sooner they can get on the path to recovery. If you know someone who is having problems, don't assume that the issue will resolve itself. Let them know that you care about them, and that there are treatment options available that will help them heal. Speak with a mental health professional or counselor if you think your friend or family member is experiencing the symptoms of a mental health condition. If the affected loved one knows that you support them, they will be more likely to seek out help."]
    },
    {
        "patterns": ["How can I find a mental health professional for myself or my child?"],
        "responses": ["Feeling comfortable with the professional you or your child is working with is critical to the success of the treatment. Finding the professional who best fits your needs may require research. Start by searching for providers in your area."]
    },
    {
        "patterns": ["What treatment options are available?"],
        "responses": ["Just as there are different types of medications for physical illness, different treatment options are available for individuals with mental illness. Treatment works differently for different people. It is important to find what works best for you or your child."]
    },
    {
        "patterns": ["If I become involved in treatment, what do I need to know?"],
        "responses": ["Since beginning treatment is a big step for individuals and families, it can be very overwhelming. It is important to be as involved and engaged in the treatment process as possible. Some questions you will need to have answered include:\n What is known about the cause of this particular illness?\n Are there other diagnoses where these symptoms are common?\n Do you normally include a physical or neurological examination?\n Are there any additional tests or exams that you would recommend at this point?\n Would you advise an independent opinion from another psychiatrist at this point?\n What program of treatment is the most helpful with this diagnosis?\n Will this program involve services by other specialists? If so, who will be responsible for coordinating these services?\n What do you see as the family's role in this program of treatment?\n How much access will the family have to the individuals who are providing the treatment?\n What medications are generally used with this diagnosis?\n How much experience do you have in treating individuals with this illness?\n What can I do to help you in the treatment?"]
    },
    {
        "patterns": ["What is the difference between mental health professionals?"],
        "responses": ["There are many types of mental health professionals. The variety of providers and their services may be confusing. Each have various levels of education, training, and may have different areas of expertise. Finding the professional who best fits your needs may require some research."]
    },
    {
        "patterns": ["How can I find a mental health professional right for my child or myself?"],
        "responses": ["Feeling comfortable with the professional you or your child is working with is critical to the success of your treatment. Finding the professional who best fits your needs may require some research."]
    },
    {
        "patterns": ["Where else can I get help?"],
        "responses": ["Where you go for help will depend on the nature of the problem and/or symptoms and what best fits you. Often, the best place to start is by talking with someone you trust about your concerns, such as a family member, friend, clergy, healthcare provider, or other professionals. Having this social support is essential in healing from mental illness, and you will be able to ask them for referrals or recommendations for trusted mental health practitioners. Search for mental health resources in your area. Secondly, there are people and places throughout the country that provide services to talk, to listen, and to help you on your journey to recovery. Thirdly, many people find peer support a helpful tool that can aid in their recovery. There are a variety of organizations that offer support groups for consumers, their family members, and friends. Some support groups are peer led while others may be led by a mental health professional."]
    },
    {
        "patterns": ["What should I know before starting a new medication?"],
        "responses": ["The best source of information regarding medications is the physician prescribing them. He or she should be able to answer questions such as:    \n1. What is the medication supposed to do? \n2. When should it begin to take effect, and how will I know when it is effective? \n3. How is the medication taken and for how long? What food, drinks, other medicines, and activities should be avoided while taking this medication? \n4. What are the side effects and what should be done if they occur? \n5. What do I do if a dose is missed? \n6. Is there any written information available about this medication? \n7. Are there other medications that might be appropriate? \n8. If so, why do you prefer the one you have chosen? \n9. How do you monitor medications and what symptoms indicate that they should be raised, lowered, or changed? \n10. All medications should be taken as directed. Most medications for mental illnesses do not work when taken irregularly, and extra doses can cause severe, sometimes dangerous side effects. Many psychiatric medications begin to have a beneficial effect only after they have been taken for several weeks."]
    },
    {
        "patterns": ["Where can I go to find therapy?"],
        "responses": ["Different kinds of therapy are more effective based on the nature of the mental health condition and/or symptoms and the person who has them (for example, children will benefit from a therapist who specializes in childrenâ€™s mental health). However, there are several different types of treatment and therapy that can help."]
    },
    {
        "patterns": ["Where can I learn about types of mental health treatment?"],
        "responses": ["Mental health conditions are often treated with medication, therapy or a combination of the two. However, there are many different types of treatment available, including Complementary & Alternative Treatments, self-help plans, and peer support. Treatments are very personal and should be discussed by the person with the mental health conditions and his or her team."]
    },
    {
        "patterns": ["What are the different types of mental health professionals?"],
        "responses": ["There are many types of mental health professionals. Finding the right one for you may require some research."]
    },
    {
        "patterns": ["Where can I go to find a support group?"],
        "responses": ["Many people find peer support a helpful tool that can aid in their recovery. There are a variety of organizations that offer support groups for consumers, their family members and friends. Some support groups are peer-led, while others may be led by a mental health professional."]
    },
    {
        "patterns": ["Can you prevent mental health problems?"],
        "responses": ["We can all suffer from mental health challenges, but developing our wellbeing, resilience, and seeking help early can help prevent challenges becoming serious."]
    },
    {
        "patterns": ["Are there cures for mental health problems?", "is there any cure for mental health problems?"],
        "responses": ["It is often more realistic and helpful to find out what helps with the issues you face. Talking, counselling, medication, friendships, exercise, good sleep and nutrition, and meaningful occupation can all help."]
    },
    {
        "patterns": ["What causes mental health problems?"],
        "responses": ["Challenges or problems with your mental health can arise from psychological, biological, and social, issues, as well as life events."]
    },
    {
        "patterns": ["What do I do if I'm worried about my mental health?"],
        "responses": ["The most important thing is to talk to someone you trust. This might be a friend, colleague, family member, or GP. In addition to talking to someone, it may be useful to find out more information about what you are experiencing. These things may help to get some perspective on what you are experiencing, and be the start of getting help."]
    },
    {
        "patterns": ["How do I know if I'm unwell?"],
        "responses": ["If your beliefs , thoughts , feelings or behaviours have a significant impact on your ability to function in what might be considered a normal or ordinary way, it would be important to seek help."]
    },
    {
        "patterns": ["How can I maintain social connections? What if I feel lonely?"],
        "responses": ["A lot of people are alone right now, but we don't have to be lonely. We're all in this together. Think about the different ways to connect that are most meaningful for you. For example, you might prefer a video chat over a phone call, or you might prefer to text throughout the day rather than one set time for a video call. Then, work with your social networks to make a plan. You might video chat with your close friends in the evening and phone a family member once a week. Remember to be mindful of people who may not be online. Check in by phone and ask how you can help. The quality of your social connections matter. Mindlessly scrolling through social media and liking a few posts usually doesn't build strong social connections. Make sure you focus on strategies that actually make you feel included and connected. If your current strategies don't help you feel connected, problem-solve to see if you can find a solution. Everyone feels lonely at times. Maybe you recently moved to a new city, are changing your circle of friends, lost someone important in your life, or lost your job and also lost important social connections with coworkers. Other people may have physical connections to others but may feel like their emotional or social needs aren't met. Measures like social distancing or self-isolation can make loneliness feel worse no matter why you feel lonely now. Reach out to the connections you do have. Suggest ways to keep in touch and see if you can set a regular time to connect. People may hesitate to reach out for a lot of different reasons, so don't be afraid to be the one who asks. Look for local community support groups and mutual aid groups on social media. This pandemic is bringing everyone together, so look for opportunities to make new connections. These groups are a great way to share your skills and abilities or seek help and support. Look for specialized support groups. Support groups are moving online, and there are a lot of different support lines to call if you need to talk to someone."]
    },
    {
        "patterns": ["What's the difference between anxiety and stress?"],
        "responses": ["Stress and anxiety are often used interchangeably, and there is overlap between stress and anxiety. Stress is related to the same fight, flight, or freeze response as anxiety, and the physical sensations of anxiety and stress may be very similar. The cause of stress and anxiety are usually different, however. Stress focuses on mainly external pressures on us that we're finding hard to cope with. When we are stressed, we usually know what we're stressed about, and the symptoms of stress typically disappear after the stressful situation is over. Anxiety, on the other hand, isn't always as easy to figure out. Anxiety focuses on worries or fears about things that could threaten us, as well as anxiety about the anxiety itself. Stress and anxiety are both part of being human, but both can be problems if they last for a long time or have an impact on our well-being or daily life."]
    },
    {
        "patterns": ["What's the difference between sadness and depression?", "difference between sadness and depression"],
        "responses": ["Sadness is a normal reaction to a loss, disappointment, problems, or other difficult situations. Feeling sad from time to time is just another part of being human. In these cases, feelings of sadness go away quickly and you can go about your daily life. Other ways to talk about sadness might be feeling low, feeling down, or feeling blue.A person may say they are feeling depressed, but if it goes away on its own and doesn't impact life in a big way, it probably isn't the illness of depression. Depression is a mental illness that affects your mood, the way you understand yourself, and the way you understand and relate to things around you. It can also go by different names, such as clinical depression, major depressive disorder, or major depression. Depression can come up for no reason, and it lasts for a long time. It's much more than sadness or low mood. People who experience depression may feel worthless or hopeless. They may feel unreasonable guilty. Some people may experience depression as anger or irritability. It may be hard to concentrate or make decisions. Most people lose interest in things that they used to enjoy and may isolate themselves from others. There are also physical signs of depression, such as problems with sleep, appetite and energy and unexplainable aches or pains. Some may experience difficult thoughts about death or ending their life (suicide). Depression lasts longer than two weeks, doesn't usually go away on its own, and impacts your life. It's a real illness, and it is very treatable. It's important to seek help if you're concerned about depression."]
    },

    {
        "patterns": ["I'm feeling down", "I'm sad", "I'm not feeling well", "I'm feeling blue"],
        "responses": ["I'm sorry to hear that you're feeling this way. Do you want to talk about what's bothering you?", "It's okay to feel down sometimes. I'm here if you want to share more about it."]
    },
    {
        "patterns": ["I need advice", "Can you give me some advice?", "Help me with advice", "I need some guidance"],
        "responses": ["Sure, I'm here to help. What do you need advice on?", "Feel free to share what's on your mind, and I'll do my best to provide some guidance."]
    },
    {
        "patterns": ["I'm feeling anxious", "I have anxiety", "I'm stressed out", "I feel anxious"],
        "responses": ["That can be really tough. Let's talk about what's causing you to feel this way. I'm here to help.", 
                      "It's important to address these feelings. Can you tell me more about what's making you anxious?","How about starting with some deep breathing exercises? Inhale slowly for 4 seconds, hold for 7 seconds, and exhale for 8 seconds. Repeat this for 5-10 minutes to relax your mind."]
    },
    {
        "patterns": ["I feel overwhelmed", "I'm feeling overwhelmed", "I'm under a lot of stress"],
        "responses": ["Feeling overwhelmed is a common response to stress. Can you tell me more about what's happening?", "It's important to manage stress. Let's talk about what's causing you to feel this way."]
    },
    {
        "patterns": ["I feel happy", "I'm in a good mood", "I'm feeling great"],
        "responses": ["That's wonderful to hear! What's making you feel so happy?", "I'm glad you're feeling great. Anything in particular that's making you feel this way?"]
    },
    {
        "patterns": ["I need to relax", "Can you help me relax?", "I'm looking for relaxation techniques"],
        "responses": ["I can suggest some relaxation techniques. Would you like to try deep breathing exercises, progressive muscle relaxation, or something else?", "Relaxation is important. How about trying some mindfulness or deep breathing exercises?"]
    },
    {
        "patterns": ["I don't know what to do", "I'm confused", "I need direction"],
        "responses": ["It's okay to feel unsure sometimes. What specifically are you feeling confused about?", "Let's try to figure this out together. What’s been causing you to feel this way?"]
    },
    {
        "patterns": ["Can you help me set goals?", "I need help with goal setting", "Help me with my goals"],
        "responses": ["Setting goals can be very helpful. What goals are you thinking about, and how can I assist you with them?", "Let's break down your goals into manageable steps. What do you want to achieve?"]
    },
    {
        "patterns": ["I'm having trouble sleeping", "I can't sleep", "I'm insomniac"],
        "responses": ["Difficulty sleeping can be challenging. Have you tried any relaxation techniques before bed?", "Let's talk about your sleep habits. Maybe we can find some strategies to improve your sleep."]
    },
    {
        "patterns": ["I feel lonely", "I'm feeling lonely", "I don't have anyone to talk to"],
        "responses": ["I'm here for you. Loneliness can be tough, but talking about it can help. What's been going on?", "It's important to connect with others. Would you like to share more about how you're feeling?"]
    },
    {
        "patterns": ["I feel guilty", "I'm feeling guilty", "I'm struggling with guilt"],
        "responses": ["Guilt can be a heavy emotion. Let's talk about what's causing you to feel this way.", "It's okay to talk about your feelings of guilt. What’s been on your mind?"]
    },
    {
        "patterns": ["I want to improve my mood", "How can I feel better?", "Help me improve my mood"],
        "responses": ["Improving your mood can involve various strategies. Would you like suggestions on activities, mindset changes, or other techniques?", "Let’s explore some ways to boost your mood. Are there specific things that usually make you feel better?"]
    },    
    {
        "patterns":["Having the fear of diseases.","have the fear of diseases","suspecting that I have some diseases"],
        "responses":["Everybody in the world have some problem. Consider a checkup so that your doubt will be cleared.","Avoid overthinking, Just enjoy the life."]
    },
    {
        "patterns": ["I need motivation", "Can you motivate me?", "I'm feeling unmotivated", "Motivate me"],
        "responses": [
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
            "It always seems impossible until it's done. - Nelson Mandela"
        ]
    },
    {
        "patterns": ["I'm feeling down", "I'm sad", "I'm struggling"],
        "responses": [
            "Tough times never last, but tough people do. - Robert H. Schuller",
            "The best way to predict the future is to create it. - Peter Drucker",
            "In the middle of every difficulty lies opportunity. - Albert Einstein",
            "This too shall pass. - Persian Proverb",
            "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman"
        ]
    },
    {
        "patterns": ["I need inspiration", "Can you inspire me?", "Inspire me"],
        "responses": [
            "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
            "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
            "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
            "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
            "Dream big and dare to fail. - Norman Vaughan"
        ]
    },
    {
        "patterns": ["I feel like giving up", "I want to quit", "I'm losing hope","Feeling like demotivated"],
        "responses": [
            "It does not matter how slowly you go as long as you do not stop. - Confucius",
            "Our greatest glory is not in never falling, but in rising every time we fall. - Confucius",
            "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "You just can’t beat the person who never gives up. - Babe Ruth"
        ]
    },
    {
        "patterns": ["I need some encouragement", "Encourage me", "Give me some encouragement"],
        "responses": [
            "Keep going. Everything you need will come to you at the perfect time. - Unknown",
            "You are stronger than you think, braver than you believe, and smarter than you know. - A.A. Milne",
            "Your present circumstances don’t determine where you can go; they merely determine where you start. - Nido Qubein",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
            "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy"
        ]
    },
    {
        "patterns" : ["I am overwhelmed by me work pressure","my mind is restless"],
        "responses": ["In times hearing music would help a lot.Search for some melodies.","Music heals- Why can't you hear some of your favourite songs"]
    },
    {
        "patterns": ["I need some exercises", "Can you suggest some exercises?", "Recommend me some exercises", "What exercises can I do?"],
        "responses": [
            "How about starting with some deep breathing exercises? Inhale slowly for 4 seconds, hold for 7 seconds, and exhale for 8 seconds. Repeat this for 5-10 minutes to relax your mind.",
            "Try some simple stretching exercises. Touch your toes, do side stretches, and rotate your shoulders to release tension.",
            "Engage in a 5-minute walk. If you’re indoors, you can walk around your space or even march in place to get your blood flowing.",
            "Consider doing a short yoga session. Poses like Child's Pose, Cat-Cow, and Downward Dog can help you relax and improve flexibility.",
            "Try some bodyweight exercises like push-ups, squats, and lunges. These exercises can boost your energy and improve your mood."
        ]
    },
    {
        "patterns": ["How can I relax?", "I need to relax", "Help me relax", "I'm feeling stressed, what should I do?"],
        "responses": [
            "Try progressive muscle relaxation. Start by tensing and then slowly releasing each muscle group from your toes to your head.",
            "Take a few minutes to meditate. Sit in a comfortable position, close your eyes, and focus on your breathing. Let your thoughts pass by without judgment.",
            "Engage in a short, mindful walk. Focus on your surroundings, the sounds, and the sensations you feel as you move.",
            "Consider practicing mindfulness. Focus on the present moment by paying attention to your breathing, bodily sensations, and emotions.",
            "Try a guided visualization. Close your eyes and imagine a peaceful place, like a beach or a forest, and mentally explore it."
        ]
    },
    {
        "patterns": ["What self-care activities can I do?", "Suggest some self-care activities", "I need some self-care tips"],
        "responses": [
            "Start with journaling. Write down your thoughts, feelings, or things you’re grateful for. It can help clear your mind.",
            "Take a warm bath or shower. Adding some Epsom salts or essential oils can make it even more relaxing.",
            "Spend some time in nature. A short walk in a park or even sitting outside can help you feel more grounded.",
            "Engage in a hobby you enjoy, whether it's reading, painting, or gardening. Doing something you love can boost your mood.",
            "Listen to your favorite music or a calming playlist. Music can be a powerful tool to enhance your mood and relax your mind."
        ]
    },
    {
        "patterns": ["I want to improve my mental health", "How can I take care of my mental health?", "Help me with my mental health"],
        "responses": [
            "Regular exercise can greatly benefit your mental health. Even a short walk or a few minutes of stretching can help reduce stress.",
            "Practice gratitude. Take a few moments each day to reflect on things you're grateful for. It can shift your focus to the positive aspects of your life.",
            "Set small, achievable goals for yourself. Completing tasks, no matter how small, can boost your confidence and improve your mood.",
            "Consider practicing mindfulness meditation daily. Even 5-10 minutes of mindful breathing can help you feel more centered and calm.",
            "Reach out to friends or loved ones. Social connection is a key component of mental well-being."
        ]
    },
    {
        "patterns": ["I feel anxious", "I'm feeling stressed", "I'm stressed out", "How can I manage my anxiety?"],
        "responses": [
            "Deep breathing can help reduce anxiety. Try inhaling deeply for 4 seconds, holding for 7 seconds, and exhaling for 8 seconds.",
            "Engage in grounding exercises. Focus on your surroundings and identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "Practice progressive muscle relaxation by tensing and relaxing different muscle groups in your body.",
            "Try a short mindfulness meditation. Focus on your breath and gently bring your attention back if your mind wanders.",
            "Physical activity can help reduce anxiety. Try going for a walk, doing some yoga, or even dancing to your favorite music."
        ]
    },
    {
        "patterns": ["Thanks", "Thank you","Thanks a lot", "That's helpful", "Thanks for the help", "Than you very much"],
        "responses": ["Happy to help!", "Any time!", "My pleasure", "You're most welcome!"]
    },
    {
        "patterns": ["Who are you?", "What are you?", "Who you are?", "Tell me more about yourself.", "What is your name?", "What should I call you?", "What's your name?", "Tell me about yourself"],
        "responses": ["I'm Manas, your Personal Therapeutic AI Assistant. How are you feeling today?", "I'm Manas, a Therapeutic AI Assistant designed to assist you. Tell me about yourself.", "I'm Manas. I am a conversational agent designed to mimic a therapist. So how are you feeling today?", "You can call me Manas.", "I'm Manas!", "Call me Manas"]
    },
    {
        "patterns": ["What can you do?"],
        "responses": ["I can provide general advice regarding anxiety and depression, answer questions related to mental health, and make daily conversations. Do not consider me as a substitute for an actual mental healthcare worker. Please seek help if you don't feel satisfied with me."]
    },
    {
        "patterns": ["I need some exercises", "Can you suggest some exercises?", "Recommend me some exercises", "What exercises can I do?"],
        "responses": [
            "How about starting with some deep breathing exercises? Inhale slowly for 4 seconds, hold for 7 seconds, and exhale for 8 seconds. Repeat this for 5-10 minutes to relax your mind.",
            "Try some simple stretching exercises. Touch your toes, do side stretches, and rotate your shoulders to release tension.",
            "Engage in a 5-minute walk. If you’re indoors, you can walk around your space or even march in place to get your blood flowing.",
            "Consider doing a short yoga session. Poses like Child's Pose, Cat-Cow, and Downward Dog can help you relax and improve flexibility.",
            "Try some bodyweight exercises like push-ups, squats, and lunges. These exercises can boost your energy and improve your mood."
        ]
    },
    {
        "patterns": ["How can I relax?", "I need to relax", "Help me relax", "I'm feeling stressed, what should I do?"],
        "responses": [
            "Try progressive muscle relaxation. Start by tensing and then slowly releasing each muscle group from your toes to your head.",
            "Take a few minutes to meditate. Sit in a comfortable position, close your eyes, and focus on your breathing. Let your thoughts pass by without judgment.",
            "Engage in a short, mindful walk. Focus on your surroundings, the sounds, and the sensations you feel as you move.",
            "Consider practicing mindfulness. Focus on the present moment by paying attention to your breathing, bodily sensations, and emotions.",
            "Try a guided visualization. Close your eyes and imagine a peaceful place, like a beach or a forest, and mentally explore it."
        ]
    },
    {
        "patterns": ["What self-care activities can I do?", "Suggest some self-care activities", "I need some self-care tips"],
        "responses": [
            "Start with journaling. Write down your thoughts, feelings, or things you’re grateful for. It can help clear your mind.",
            "Take a warm bath or shower. Adding some Epsom salts or essential oils can make it even more relaxing.",
            "Spend some time in nature. A short walk in a park or even sitting outside can help you feel more grounded.",
            "Engage in a hobby you enjoy, whether it's reading, painting, or gardening. Doing something you love can boost your mood.",
            "Listen to your favorite music or a calming playlist. Music can be a powerful tool to enhance your mood and relax your mind."
        ]
    },
    {
        "patterns": ["I want to improve my mental health", "How can I take care of my mental health?", "Help me with my mental health"],
        "responses": [
            "Regular exercise can greatly benefit your mental health. Even a short walk or a few minutes of stretching can help reduce stress.",
            "Practice gratitude. Take a few moments each day to reflect on things you're grateful for. It can shift your focus to the positive aspects of your life.",
            "Set small, achievable goals for yourself. Completing tasks, no matter how small, can boost your confidence and improve your mood.",
            "Consider practicing mindfulness meditation daily. Even 5-10 minutes of mindful breathing can help you feel more centered and calm.",
            "Reach out to friends or loved ones. Social connection is a key component of mental well-being."
        ]
    },
    {
        "patterns": ["I feel anxious", "I'm feeling stressed", "I'm stressed out", "How can I manage my anxiety?"],
        "responses": [
            "Deep breathing can help reduce anxiety. Try inhaling deeply for 4 seconds, holding for 7 seconds, and exhaling for 8 seconds.",
            "Engage in grounding exercises. Focus on your surroundings and identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "Practice progressive muscle relaxation by tensing and relaxing different muscle groups in your body.",
            "Try a short mindfulness meditation. Focus on your breath and gently bring your attention back if your mind wanders.",
            "Physical activity can help reduce anxiety. Try going for a walk, doing some yoga, or even dancing to your favorite music."
        ]
    }


]

