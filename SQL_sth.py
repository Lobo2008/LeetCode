


#183. Customers Who Never Order
select Name as Customers from Customers where id not in(select CustomerId from Orders)

#182. Duplicate Emails
select Email from Person group by Email having count(Email) > 1

#181. Employees Earning More Than Their Managers
select a.Name as Employee from Employee as a,Employee as b where a.ManagerId = b.id and a.Salary > b.Salary

#176. Second Highest Salary
