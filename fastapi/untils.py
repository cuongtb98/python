

def get_items(itm, kwargs):
    itm = f"{kwargs['_id']}"
    kwargs['_id'] = itm
    return kwargs

def get_course(collection):
    """
        output: form data:{
            items:[]
            total_count: 
        }
    """
    length = collection.count_documents({})
    if length == 0:
        return "courses updating ..."
    else:
        cursor = collection.find({})
        courses = [get_items(course['_id'], course) for course in cursor]
        data = {
            "items": courses,
            "total_count": length
        }
        return data

def create_id_auto_increment(collection,data):
    '''
    input: data{*itm, id} -> id any
    output: data id -> id auto icrement
    '''
    length = collection.count_documents({})
    if length != 0:
        course = get_course(collection)
        item_bottom = course['items'][-1]['id']
        data['id'] = int(item_bottom)+1
        return data
    else:
        data['id'] = 0
        return data