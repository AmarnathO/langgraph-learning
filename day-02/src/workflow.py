from node import add_skill, add_salary, add_roadmap

state = {
    "name" : "Amar"
}
skill_state = add_skill(state)
print(f"Skill State:{skill_state}")
roadmap_update = add_roadmap(state)
print(f"Roadmap_Update : {roadmap_update}")
salary_update = add_salary(state)
print(f"Salary_update : {salary_update}")

print(f"Skill State:{skill_state} \n\n Roadmap_Update : {roadmap_update} \n\n Salary_update {salary_update}")
