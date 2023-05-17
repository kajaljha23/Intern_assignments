class APis:
    # create_api = '/create'
    view_all_items_api = '/viewing_data'
    create_api = '/items/creating_new_item'
    update_api = '/items/{items_id}'
    delete_api = '/delete/{items_id}'
    send_api = '/sending_email'
    get_api = '/total_billing'


class DBConstants:
    DB_URI = 'mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23'
    DB_DATABASE = 'interns_b2_23'
    DB_COllECTION = 'kajalk_billing'
