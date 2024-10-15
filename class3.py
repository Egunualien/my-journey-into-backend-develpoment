'''
set __ set is unordered collection of unique immutable element and they are defined using {}
'''

set1 = {1,2,3,4,5,4}
print(set1)
empty_set = set()
my_list = [1,2,3,4,5,3,4,5,3,6,7]
con_list = set(my_list)
print(con_list)
'''operations in set'''
#add
set1.add(8)
print(set1)
set1.remove(8)
print(set1)
print(len(set1))
set1.clear()
print(set1)

yoruba_food = {'rice','beans','ewedu','salad','fish','egusi'}
igbo_food = {'egusi','bitter leaf','rice','beans','banga'}
union_set = yoruba_food | igbo_food
print(union_set)
interset_set = yoruba_food & igbo_food
print(interset_set)

user_names = list(input("enter random letters"))
print(user_names)
non_duplicate = set(user_names)
print(non_duplicate)

sign_up_user = {'user1','user2','user3','user4','user5'}
logged_in_user = {'user1','user3','user5'}
active_users = sign_up_user & logged_in_user
print(active_users)

'''dictionary is an unordered collection of items that store datas in key value pair'''
joy_details = {
    'username' : 'joy',
    'password' : 30447737404,
    'email' : 'joy419@gmail.com'
}

joy_name = joy_details['username']
print(joy_name)
joy_details['id number'] = 419
print(joy_details)
joy_details['password'] = 839638363936
print(joy_details)
del joy_details['email']
print(joy_details)