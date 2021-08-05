## Process employee data
The second function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount.

`def process_data(employee_list):`

This function needs to pass the employee_list, received from the previous section, as a parameter to the function.

Now, initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list.

  `department_list = []`
  
  `for employee_data in employee_list:`
   
   `department_list.append(employee_data['Department'])`
    
The department_list should now have a redundant list of all the department names. We now have to remove the redundancy and return a dictionary. We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.

  `department_data = {}
  
   for department_name in set(department_list):
  
    department_data[department_name] = department_list.count(department_name)
    
   return department_data`
   
This uses the set() method, which converts iterable elements to distinct elements.

Now, call this function by passing the employee_list from the previous section. Then, save the output in a variable called dictionary. Print the variable dictionary.

`dictionary = process_data(employee_list)

 print(dictionary)`

This should return a dictionary in the format department: amount, as shown below.
