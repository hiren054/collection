# from sqlalchemy.inspection import inspect

# # @views.route('/users')
# def get_users():
#     users = Users.query.all()
#     # print(users)
#     # data = list(map(lambda x: {c: getattr(x, c) for c in inspect(x).attrs.keys()}, users))
#     # print(data[0])
    
#     user_schema = UserSchema(many=True)
#     output = user_schema.dump(users).data
#     return jsonify(output)

