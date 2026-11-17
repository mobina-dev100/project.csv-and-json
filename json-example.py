import json

student = {
    "name": "Ali",
    "age": 20,
    "score": 18
}

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)

# نوشتن اطلاعات در فایل


with open("student.json", "r") as file:

    student = json.load(file)

    print(student)
    print(student["name"])

# خواندن اطلاعات از فایل


student = {
    "name": "Ali",
    "age": 20
}

result = json.dumps(student)

print(result)

# تبدیل اطلاعات پایتون به متن JSON



data = '{"name": "Ali", "age": 20}'

student = json.loads(data)

print(student["name"])

# تبدیل متن JSON به اطلاعات پایتون