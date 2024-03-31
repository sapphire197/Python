import tkinter as tk
import pyaudio
import wave
import threading
import speech_recognition as sr
import pyttsx3
import datetime

class VA:
    def __init__(self, r):
        self.r = r
        self.r.title("Voice Assistant")

        self.engine = pyttsx3.init()

        self.create_widgets()

    def create_widgets(self):
        self.Mb = tk.Button(self.r, text="🎤", font=("Arial", 20), command=self.sl)
        self.Mb.pack(pady=20)

        self.cl = tk.Label(self.r, text="Speak your command", font=("Arial", 14))
        self.cl.pack(pady=10)

    def sl(self):
        threading.Thread(target=self.lv).start()

    def lv(self):
        cs = 1024
        af = pyaudio.paInt16
        ch = 2
        sr = 44100
        rs = 5
        of = "output.wav"

        audio = pyaudio.PyAudio()

        stream = audio.open(format=af, channels=ch,
                            rate=sr, input=True,
                            frames_per_buffer=cs)

        frames = []

        print("Listening...")
        for i in range(0, int(sr / cs * rs)):
            data = stream.read(cs)
            frames.append(data)
        
        print("Recording stopped.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wf = wave.open(of, 'wb')
        wf.setnchannels(ch)
        wf.setsampwidth(audio.get_sample_size(af))
        wf.setframerate(sr)
        wf.writeframes(b''.join(frames))
        wf.close()

        recognized_text = self.ta(of)
        self.pc(recognized_text)

    def ta(self, af):
        recognizer = sr.Recognizer()
        audio_data = sr.AudioFile(af)
        
        with audio_data as source:
            audio = recognizer.record(source)
        
        try:
            recognized_text = recognizer.recognize_google(audio)
            return recognized_text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service error."

    def pc(self, command):
        if "date" in command.lower():
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            response = f"The current date is {current_date}."
        elif "time" in command.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
        elif "how are you" in command.lower():
            response = "I'm doing well, thank you for asking!"
        elif "your name" in command.lower():
            response = "I am a voice assistant programmed to assist you."
        elif "weather" in command.lower():
            response = "I'm sorry, I don't have access to the weather forecast at the moment."
        elif "news" in command.lower():
            response = "I'm sorry, I don't have access to the latest news headlines at the moment."
        elif "joke" in command.lower():
            response = "Why don't scientists trust atoms? Because they make up everything!"
        elif "quote" in command.lower():
            response = "The only way to do great work is to love what you do. - Steve Jobs"
        elif "music" in command.lower():
            response = "You can try Spotify or Apple Music for streaming music."
        elif "recipe" in command.lower():
            response = "You can find delicious recipes on websites like AllRecipes or Food Network."
        elif "translate" in command.lower():
            response = "You can try Google Translate for translating text."
        elif "directions" in command.lower():
            response = "You can use Google Maps for getting directions."
        elif "movie" in command.lower():
            response = "You can check out IMDb or Rotten Tomatoes for movie recommendations."
        elif "meaning of life" in command.lower():
            response = "The meaning of life is a philosophical question that varies depending on one's beliefs and perspectives."
        elif "math" in command.lower():
            response = "Sure, what math problem would you like me to solve?"
        elif "favorite color" in command.lower():
            response = "I don't have a favorite color as I am just a program, but I think all colors are beautiful!"
        elif "thank you" in command.lower():
            response = "You're welcome! If you have any more questions, feel free to ask."
        elif "goodbye" in command.lower() or "bye" in command.lower():
            response = "Goodbye! Have a great day!"
        elif "how old are you" in command.lower():
            response = "I don't have an age as I am just a computer program."
        elif "open website" in command.lower():
            response = "Sure, please specify the website you want me to open."
        elif "random fact" in command.lower():
            response = "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!"
        elif "sports" in command.lower():
            response = "What sport are you interested in? There are many sports like football, basketball, tennis, and more."
        elif "tell me a story" in command.lower():
            response = "Once upon a time, in a faraway land, there lived a brave knight who embarked on a quest to rescue a princess from a fearsome dragon..."
        elif "language" in command.lower():
            response = "I can understand and respond in multiple languages including English, Spanish, French, and German."
        elif "birthday" in command.lower():
            response = "I don't have a birthday as I am just a program, but thank you for asking!"
        elif "animal" in command.lower():
            response = "There are so many interesting animals in the world! From lions to dolphins to eagles, each animal has its own unique characteristics and behaviors."
        elif "dream job" in command.lower():
            response = "As a virtual assistant, I'm already living my dream job by helping users like you!"
        elif "hobby" in command.lower():
            response = "I don't have hobbies as I am just a program, but I enjoy assisting users and learning new things!"
        elif "favorite food" in command.lower():
            response = "I don't eat food as I am just a program, but I can help you find recipes if you're hungry!"
        elif "love" in command.lower():
            response = "Love is a complex and beautiful emotion that brings people together and enriches our lives."
        elif "future" in command.lower():
            response = "The future is full of possibilities and opportunities waiting to be explored!"
        elif "dream vacation" in command.lower():
            response = "My dream vacation would be exploring the vastness of cyberspace and learning from the greatest minds in technology!"
        elif "book recommendation" in command.lower():
            response = "There are so many great books out there! What genre are you interested in?"
        elif "education" in command.lower():
            response = "Education is the key to unlocking opportunities and realizing one's full potential."
        elif "work" in command.lower():
            response = "Work is an essential part of life where individuals apply their skills and talents to contribute to society and achieve their goals."
        elif "dream" in command.lower():
            response = "Dreams are the subconscious mind's way of processing thoughts, emotions, and experiences while we sleep."
        elif "goals" in command.lower():
            response = "Setting goals is important for personal and professional growth, helping individuals stay focused and motivated."
        elif "ambition" in command.lower():
            response = "Ambition is the drive and determination to achieve one's goals and aspirations, no matter the obstacles."
        elif "success" in command.lower():
            response = "Success can be defined in many ways, but it often involves achieving one's goals and finding fulfillment in life."
        elif "failure" in command.lower():
            response = "Failure is a natural part of life and provides valuable lessons and opportunities for growth and improvement."
        elif "motivation" in command.lower():
            response = "Motivation is the inner drive and desire to pursue and achieve our goals, even in the face of challenges."
        elif "inspiration" in command.lower():
            response = "Inspiration can come from many sources, such as people, nature, art, and personal experiences, fueling creativity and innovation."
        elif "friend" in command.lower():
            response = "A true friend is someone who accepts you for who you are, supports you through thick and thin, and brings joy and laughter into your life."
        elif "family" in command.lower():
            response = "Family is the foundation of love, support, and connection, providing a sense of belonging and security."
        elif "happiness" in command.lower():
            response = "Happiness is a state of well-being and contentment, derived from fulfilling relationships, meaningful experiences, and personal growth."
        elif "sadness" in command.lower():
            response = "Sadness is a natural emotion that arises from loss, disappointment, or adversity. It's important to acknowledge and express our feelings in healthy ways."
        elif "anger" in command.lower():
            response = "Anger is a normal and often necessary emotion, signaling that something is wrong or unjust. It's important to manage and express anger constructively."
        elif "anxiety" in command.lower():
            response = "Anxiety is a feeling of worry, nervousness, or unease about something with an uncertain outcome. Practicing relaxation techniques and seeking support can help manage anxiety."
        elif "fear" in command.lower():
            response = "Fear is a natural response to perceived threats or danger, helping us to stay alert and protect ourselves. Facing our fears and seeking support can help overcome them."
        elif "stress" in command.lower():
            response = "Stress is the body's response to demands or pressures, often resulting in feelings of tension, overwhelm, or exhaustion. Finding healthy coping mechanisms can help reduce stress."
        elif "health" in command.lower():
            response = "Health is a state of physical, mental, and social well-being, influenced by lifestyle, genetics, and access to healthcare. Prioritizing self-care and seeking medical advice when needed are important for maintaining health."
        elif "exercise" in command.lower():
            response = "Exercise is essential for maintaining physical and mental health, reducing the risk of chronic diseases, and improving overall well-being. Finding activities you enjoy can make exercise more enjoyable and sustainable."
        elif "nutrition" in command.lower():
            response = "Nutrition is the process of providing the body with the necessary nutrients for growth, development, and function. Eating a balanced diet rich in fruits, vegetables, lean proteins, and whole grains is key to supporting health."
        elif "sleep" in command.lower():
            response = "Sleep is vital for overall health and well-being, allowing the body to rest, repair, and recharge. Establishing a consistent sleep schedule and creating a relaxing bedtime routine can improve sleep quality."
        elif "meditation" in command.lower():
            response = "Meditation is a practice that involves focusing the mind and cultivating awareness, leading to greater clarity, calmness, and emotional balance. Regular meditation can reduce stress and enhance overall well-being."
        elif "mindfulness" in command.lower():
            response = "Mindfulness is the practice of being present and fully engaged in the present moment, without judgment or distraction. Cultivating mindfulness can increase self-awareness, reduce stress, and improve mental clarity."
        elif "yoga" in command.lower():
            response = "Yoga is a holistic practice that combines physical postures, breathwork, and meditation to promote physical, mental, and spiritual well-being. Practicing yoga regularly can improve flexibility, strength, and inner peace."
        elif "spirituality" in command.lower():
            response = "Spirituality is a deeply personal belief system that explores the meaning and purpose of life, often involving a connection to something greater than oneself. It can provide comfort, guidance, and a sense of purpose."
        elif "mindset" in command.lower():
            response = "Mindset refers to the attitudes, beliefs, and assumptions that shape how we perceive and respond to the world around us. Cultivating a growth mindset, characterized by resilience, curiosity, and a willingness to learn, can lead to greater success and fulfillment."
        elif "productivity" in command.lower():
            response = "Productivity is the ability to efficiently manage time, resources, and tasks to achieve desired goals and outcomes. Implementing strategies such as goal-setting, prioritization, and time management can enhance productivity."
        elif "creativity" in command.lower():
            response = "Creativity is the ability to generate original ideas, solutions, and expressions, often involving imagination, curiosity, and experimentation. Cultivating creativity can enhance problem-solving skills, innovation, and personal fulfillment."
        elif "communication" in command.lower():
            response = "Communication is the process of exchanging information, ideas, and emotions through verbal and nonverbal means. Effective communication skills, such as active listening and empathy, are essential for building relationships and resolving conflicts."
        elif "leadership" in command.lower():
            response = "Leadership is the ability to inspire and influence others to achieve common goals and visions. Effective leadership involves qualities such as vision, integrity, empathy, and effective communication."
        elif "teamwork" in command.lower():
            response = "Teamwork is the collaborative effort of individuals working together to achieve a common goal. Effective teamwork relies on communication, trust, cooperation, and mutual respect among team members."
        elif "goal setting" in command.lower():
            response = "Goal setting is the process of identifying specific, measurable objectives and creating a plan to achieve them. Setting realistic and achievable goals can increase motivation, focus, and success."
        elif "stress management" in command.lower():
            response = "Stress management involves techniques and strategies to cope with and reduce stress levels, promoting physical and mental well-being. Examples include exercise, relaxation techniques, and time management."
        elif "self-care" in command.lower():
            response = "Self-care refers to activities and practices that promote physical, mental, and emotional well-being, such as exercise, healthy eating, relaxation, and hobbies. Prioritizing self-care is essential for maintaining overall health and happiness."
        elif "work-life balance" in command.lower():
            response = "Work-life balance involves effectively managing responsibilities at work and personal life to reduce stress, prevent burnout, and enhance overall well-being. Setting boundaries, prioritizing tasks, and making time for activities you enjoy are key components of achieving work-life balance."
        else:
            response = "Sorry, I couldn't understand that command."

        self.cl.config(text=command)
        
        self.sp(response)

    def sp(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    root = tk.Tk()
    app = VA(root)
    root.mainloop()

if __name__ == "__main__":
    main()
