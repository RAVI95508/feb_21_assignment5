electrical_equipments=["fan","light","television","blender","iron","refrigerator","blender","iron","refrigerator"]
print(electrical_equipments)
electrical_equipments[1]="lamp"
print(electrical_equipments)
electrical_equipments.append("mixer") #append
print(electrical_equipments)
electrical_equipments.insert(1,"washing machine") # insert
print(electrical_equipments)
electrical_equipments.remove("mixer") #remove
print(electrical_equipments)
electrical_equipments.reverse() # reverse
print(electrical_equipments)
y=electrical_equipments.count("iron") #count
print("The number of times:",y)
electrical_equipments={"fan", "light","television","blender","iron","refrigerator","fan", "light","television"} #topple
print(electrical_equipments)
data={"tortoise":"fast runner","hare":"slow runner"} #dictionary
print(data)
electrical={
    "electrical_equipments":["fan","light","television"],
    "features":["create airflow","create vision","create connectivity"]

}
print(electrical["electrical_equipments"])
print(electrical["features"]) 
ele_equ=input("enter the electrical equipment:") 
if ele_equ in electrical["electrical_equipments"]:
       print(f"hey....! you enter {ele_equ}...right......! ")
       feature_of_equ=input("enter the features of tha equipment:")
       if ele_equ=="fan":
            if feature_of_equ=="create airflow":
                  print(f"yes....{ele_equ} have the {feature_of_equ}")
            elif feature_of_equ=="create vision"or"create connectivity":
                  print(f"sorry,{ele_equ} don't have that {feature_of_equ}")
       else:
          if ele_equ=="light":
              if feature_of_equ=="create vision":
                   print(f"yes....{ele_equ} have the {feature_of_equ}")
              elif feature_of_equ=="create airflow"or"create connectivity":
                  print(f"sorry,{ele_equ} don't have that {feature_of_equ}")
          else:
             if ele_equ=="television":
                if feature_of_equ=="create connectivity":
                    print(f"yes....{ele_equ} have the {feature_of_equ}")
                elif feature_of_equ=="create airflow"or"create vision":
                 print(f"sorry,{ele_equ} don't have that {feature_of_equ}")
else:
    print(f"sorry,{ele_equ} is invalid ..pls try again thank you")
       
