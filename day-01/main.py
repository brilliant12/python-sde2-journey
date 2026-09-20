developer = {
    "name": "Arjun Gupta",
    "current_stack": "PHP/Laravel",
    "target_stack": "Python/FastAPI",
    "target_role": "Python Backend SDE-2",
    "years_of_experience": 4,
    "learning_topics"  :['Python', 'DSA', 'FastAPI',  'System Design'],
    
}

if developer["learning_topics"] :
    for topic in developer["learning_topics"] :
        print(f"Learning: {topic}")
else:
    print('There is No Learning Topics .')

developer['target_role']="Python Full-Stack Developer"

print(f'Hello, {developer["name"]}!')
print(f'Current stack: {developer["current_stack"]}')
print(f'Target stack: {developer["target_stack"]}')
print(f'Target role: {developer["target_role"]}')