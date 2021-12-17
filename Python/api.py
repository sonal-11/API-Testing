from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class Data(Resource):
    def get(self):
        data = pd.read_csv('data.csv')  # read local CSV
        data = data.to_dict()  # convert dataframe to dict
        return {'data': data}, 200  # return data and 200 OK

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add args
        parser.add_argument('name', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('data.csv')

        if args['id'] in list(data['id']):
            return {
                'message': f"'{args['id']}' already exists."
            }, 409
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'id': [args['id']],
                'name': [args['name']],
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('data.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK

   

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id', required=True)  # add userId arg
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('data.csv')
        
        if args['id'] in list(data['id']):
            # remove data entry matching given userId
            data = data[data['id'] != args['id']]
            
            # save back to CSV
            data.to_csv('data.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            # otherwise we return 404 because userId does not exist
            return {
                'message': f"'{args['id']}' user not found."
            }, 404

                    

api.add_resource(Data, '/data')  # add endpoints


if __name__ == '__main__':
    app.run()  # run our Flask app