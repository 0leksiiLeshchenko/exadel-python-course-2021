def create_user(name: str, surname: str, age: int = 42, **kwargs) -> dict:
    result = {'name': name, 'surname': surname, 'age': age, 'extra': {}}
    for k, v in kwargs.items():
        result['extra'][k] = v
    return result


print(create_user("Marie", "Curie", age=66, occupation="physicist",
            won_nobel=True) == \
   {
       "name": "Marie",
       "surname": "Curie",
       "age": 66,
       "extra": {
           "occupation": "physicist",
           "won_nobel": True
       }
   })
