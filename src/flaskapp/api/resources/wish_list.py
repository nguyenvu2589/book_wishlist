import json
import logging
from functools import wraps

from flask import jsonify, request
from flask_restful import Resource
from flaskapp.api.models.books import Book
from flaskapp.extensions import db  # db is sqlalchemy db management
from sqlalchemy.sql import \
    text  # for text queries.  We're not doing much with the ORM for microservices, we use

from .error import validate_error

# from .helper import get_properties_query, validate


class WishListResource(Resource):
    def get(self):
        """
        Add book to wish list
        ---
        parameters:
          - in: path
            name: start_date
            schema:
                type: datetime(year, month, day)
            required: true
            description: start date
          - in: path
            name: num_of_nights
            schema:
                type: int
            required: true
            description: number of nights
        responses:
          200:
            description: Return list of properties and descriptions
          401:
            description: Unauthorized request
          400:
            description: Invalid request param
          404:
            description: No properties available
        """
        result = Book.query.all()
        response = jsonify(json_list=result)
        return response

        # start_date = request.args.get("start_date", None)
        # num_of_nights = request.args.get("num_of_nights", None)
        # errors = validate(start_date, num_of_nights)
        # if errors:
        #     logging.warning(errors)
        #     return validate_error(errors, 400)
        # return get_properties(start_date, num_of_nights)


# def get_properties(request_start_date, request_num_of_nights):
#     query = get_properties_query(request_start_date, request_num_of_nights)
#     logging.info(query)
#     result = db.get_engine().execute(text(query)).fetchall()
#     if not result:
#         return validate_error(
#             f"No property available in giving range {request_start_date} - {request_num_of_nights}",
#             404,
#         )

#     logging.info(f"There are {len(result)} properties")

#     response = jsonify([dict(row) for row in result])
#     response.status_code = 200
#     return response
