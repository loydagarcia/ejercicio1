import sender_stand_request
import data

#funcion get_user_body  #first_name argumento
def get_user_body(first_name):
    #currebt_body es una variable  #dat es el otro aechivo de donde se copiara el namen
    current_body = data.user_body.copy()
    #current_body  #firstName es el diccionario  que queremos probar
    current_body["firstName"] = first_name
    return current_body

#pruebas postivas
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    message_response = 'Has introducido un nombre de usuario no válido. El nombre solo puede '\
                        'contener letras del alfabeto latino, la longitud debe ser de 2 a 15 '\
                         'caracteres.'

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == message_response

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Assssssscccssss")

def test_create_user_1_letter_in_first_name_get_success_response():
    negative_assert_symbol("A")

def test_create_user_16_letters_in_first_name_get_success_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

def test_create_user_blank_space_between_letters_in_first_name_get_success_response():
        negative_assert_symbol("Ram ses")

def test_create_user_special_characters_letters_in_first_name_get_success_response():
    negative_assert_symbol("$%$%#$")

def test_create_user_numeros_in_first_name_get_success_response():
    negative_assert_symbol("123")

def test_create_user_space_empty_in_first_name_get_success_response():
    negative_assert_symbol(" ")

def test_create_user_numero_in_first_name_get_success_response():
    negative_assert_symbol("numero")