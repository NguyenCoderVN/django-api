from datetime import datetime
import json


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# main function
if __name__ == "__main__":
    ''' A. Convert Object to Json '''
    comment_obj = Comment(email='leila@example.com', content='foo bar')
    print("Comment object Object", comment_obj)

    comment_dict = vars(comment_obj)
    print("comment_dict", comment_dict)

    comment_json = json.dumps(comment_dict, indent=4)
    print("comment_json", comment_json)

    ''' B. Convert Json to Object '''
    comment_dict_back = json.loads(comment_json)
    print("comment_dict_back", comment_dict_back)

    comment_obj_back = Comment(**comment_dict_back)
    print("comment_obj_back", comment_obj_back)
