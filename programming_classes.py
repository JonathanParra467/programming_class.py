"""
Now, let's practice using tuples. Imagine you're planning the classes for a programming certificate.
You need to list out six classes. Here's what you need to do:
"""
def main():
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")
    for item in programming_classes:
        print(item)
    print("The tuple has", len(programming_classes), "items.")

main()