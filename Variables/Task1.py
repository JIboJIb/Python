name="Vlad"
day="Friday"
print("Good day "+name+"! "+day+" is a perfect day to learn some python.")

# 1 old style %
print("Good day %(name)s ! %(day)s is a perfect day to learn some python." 
      % {"name":"Vlad","day":"Friday"})

# 2. str.format
print("Good day {name}! {day} is a perfect day to learn some python."
      .format(name="Vlad",day="Friday"))

#3 f-strings
name="Vlad"
day="Friday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")

#4 template strings

from string import Template #імпорт з темплей який не заданий?
print("Good day $name! $day is a perfect day to learn some python.")
t.substitute(name="Vlad",day="Friday") # t.substitute?! 

#  ^ не зрозумів як працює

