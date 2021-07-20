# age = 10 
# sex = 'male'
class man2:
    commonAge = 10
    print('class man 2 has been called')
    def sayMyAge(self,age,sex):
        # print('your age is {age} and you are {sex}'.format(age=age,sex=sex))
        # print('common age value is',self.common
        return 'ee'
class man:
    commonAge = 10
    print('class man has been called')
    def sayMyAge(self,age,sex):
        # print('your age is {age} and you are {sex}'.format(age=age,sex=sex))
        # print('common age value is',self.commonAge)


     print('object has been not initialised')

ismayil = man()
print('object has initialised')
ismayil.commonAge = 20
man.commonAge = 18

# man.sayMyAge('ss',25,'male')
ismayil.sayMyAge(27,'female')
