huy = {
    'Name' : 'Huy',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary per hour ($)' : '0,8'
}
tung = {
    'Name' : 'Tung',
    'Role' : 'Cook',
    'Hours' : 24,
    'Salary per hour' : '1,5'
}
mduc = {
    'Name' : 'M.Duc',
    'Role' : 'Manager',
    'Hours' : '20',
    'Salary per hour' : '2'
}
don = {
    'Name' : 'Don',
    'Role' : 'Waiter',
    'Hour' : 12,
    'Salary per hour' : '0,9'
}
hduc = {
    'Name' : 'H.Duc',
    'Role' : 'Waiter',
    'Hour' : 14,
    'Salary per hour' : '0,7'
}
danhsach_list = [huy, tung, mduc, don, hduc]
count = 0
for i in danhsach_list:
    count += 1
    print (i)