"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів 
    (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись 
    валідатором, перевірить ці дані і надрукує для кожної пари значень 
    відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""


import s2
dataBase = [["vasya", "12345678qQ"], ["asya", "1234"],
            ["sya", "1sfgsgdsgdsgds"], ["ya", "1"], ["vasya1", "dfgdfgdfgqQ"]]


def printResult(login, password, status):
    print(f"Name: {login}")
    print(f"Password: {password}")
    print(f"Status: {status}")
    print("-----")


for log, pas in dataBase:
    try:
        if s2.isValid(log, pas):
            printResult(log, pas, "Ok")
    except s2.LoginNotValid as err:
        printResult(err.username, err.password, err.status)
