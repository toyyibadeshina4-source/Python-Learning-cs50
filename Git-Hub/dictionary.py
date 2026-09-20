#Examples for dictionary
#Empty Dictionary
emp_dict= {}
# dictionary with integer keys
emp_dict = {20:'Adeshina', 35:'Yusuf',45:'Adebayo'}
print(emp_dict)
# dictionary with mixed keys
emp_dict= {20:'Adeshina','skills':['Python','Linux Basics']}
print(emp_dict[20])
print(emp_dict['skills'])
print(emp_dict)
#using dict() function
emp_dict = dict(husband='Adeshina', wife='Halimah')
print(emp_dict)
#Let's create emp_dict of this format
'''
{
    'Employee ID':

 {   Name: 'string'
    Joined: 'yyy-mm-dd'
    Title:'string'
    Skills:['list','of','skills'] 
    Project: {'project_name:'project description'}

  }
}
'''
#Intializing Employee
emp_dict = {
    10:
    {
      'name':"Toyyib",
      'joined':"2026-09-16",
      'title':"Data Security Analyst",
      'skills':['Python','Linux Basics','Cyber-Security Concepts'],
      'projects':{
          'Number Guessing Game':'Implement Usage of While, loops, if statements'
      }
    },
15:
{
    'name':"Halimah",
    'joined':"2024-06-13",
    'title':"IT Director",
    'skills':['Excel','Computer Literacy','Javascript'],
    'projects':{
        'Google spreader':'Automate score of users in dashboard'
    }

}
}
print(emp_dict)
# Get the type of emp_dict
print(type(emp_dict))

# get keys of a dictionary using keys()
emp_ids = emp_dict.keys()
print(emp_ids)
# Get values of a dictionary using values()
emp_details = emp_dict.values()
print(emp_details)
# get key and value both using items()
emps = emp_dict.items()
print(emps)
# Length of a dictionary (number of items) using len()
print(len(emp_dict))
# Iterate through a dictionary
for id in emp_dict.keys():
    print(f"Employee ID:{id}")
    print(f"\tEmployee Details: {emp_dict[id]}")
# Acessing elements from dictionary
# get vs [] for retreiving elements
# Toyyib
print(emp_dict[10]['joined'])
# ['Excel','Computer Literacy','Javascript']
print(emp_dict[10].get('skills'))
#Try to Access keys which doesn't exist
#None
#print(emp_dict[24]).get('roles')
# KeyError: 'location' Comment below line to execute other lines
# print(emp_dict'[24]['location'])

# Add one more employee to emp_dict using update()
new_emp = {
  25:
  { 
    'name': "Kauthar",
    'joined': "2014-04-09",
    'title' : "Business Analyst",
    'skills': ['Power BI','MBA','Marketing Expertise'],
    'projects':{
        'Golden Marketing': 'Increase the membership, my targeted audience'
    }
  }  
}
emp_dict.update(new_emp)
print(emp_dict)

# Update the existing value. Update title of emp_id:10 as "Sr . Cloud Security Engineer"
emp_dict[10]['title'] = "Sr. Cloud Security Engineer"
print(emp_dict[10])
# Learn to delete
# pop,clear,del
# Pop employee id 101
emp_dict.pop(101,"not found")
print(len(emp_dict))
# Delete the employee 25
del emp_dict[25]
print(len(emp_dict))
# Clear the dictionary
emp_dict.clear()
print(emp_dict)
# Delete the dictionary itself and printing it would thrrow an error
del emp_dict
#print(emp_dict)