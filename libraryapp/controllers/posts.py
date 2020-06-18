from flask import Blueprint, jsonify, request


from libraryapp.repositories.posts import DataBaseService


posts_controller = Blueprint(name='posts_controller', import_name=__name__)

db = []
DataBaseService.full(db)

@posts_controller.route("/")
def index():
    return jsonify(
        {
            "msg": "Zdravstvuy chitatel",
        }
    ), 200

#добавить книгу
@posts_controller.route("/posts/add_book", methods=['POST'])
def add_book():
    author = request.json.get("author")
    book_name = request.json.get("book_name")
    publishing_house = request.json.get("publishing_house")
    year = request.json.get("year")
    annotation = request.json.get("annotation")
    rubricator = request.json.get("rubricator")
    db.append(
        {
            "author": author,
            "book_name": book_name,
            "publishing_house" : publishing_house,
            "year": year,
            "annotation": annotation,
            "rubricator": rubricator
        }
    )
    return jsonify({
        "msg": "Kniga Dobavlena",
        "bookid":(len(db)-1)
    }), 201

#Список всех книг
@posts_controller.route("/posts/get_all_books", methods=['GET'])
def get_all_books():
    return jsonify({
        "all_books": db
    }), 200


#Поиск книги(category_found,what_found)
@posts_controller.route("/posts/book_found", methods=['POST'])
def book_found():
    category_found = request.json.get("category_found")
    what_found = request.json.get("what_found")
    otvet = []
    for i in db:
      if i[category_found] == what_found:
        return jsonify({
            "book": i,
            "bookid": (db.index(i))
        }), 200
      else:
        return jsonify({
              "msg": "Knigi ne naydeny"
        }), 200


#Получение книги по её ID в списке(id)
@posts_controller.route("/posts/book_id", methods=['POST'])
def get_book_id():
    id = request.json.get("id")
    return jsonify({
        "book": db[int(id)]
    }), 200

#Редактирование книги(id,)
@posts_controller.route("/posts/book_redact", methods=['POST'])
def book_redact():
    id = int(request.json.get("id"))
    i = id
    author2 = request.json.get("author")
    book_name2 = request.json.get("book_name")
    publishing_house2 = request.json.get("publishing_house")
    year2 = request.json.get("year")
    annotation2 = request.json.get("annotation")
    rubricator2 = request.json.get("rubricator")
    if id < len(db):
      for i in db:
        if author2 != None: 
          db[id]['author'] = author2
        if book_name2 != None: 
          db[id]['book_name'] = book_name2
        if publishing_house2 != None: 
          db[id]['publishing_house'] = publishing_house2
        if year2 != None: 
          db[id]['year'] = year2
        if annotation2 != None: 
          db[id]['annotation'] = annotation2
        if rubricator2 != None: 
          db[id]['rubricator'] = rubricator2
        return jsonify({
              "Change complete": i
          }), 200
    else:
          return jsonify({
                "msg": "Kniga ne naydena"
          }), 200

