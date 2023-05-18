# STANDARD IMPORTS
from http import HTTPStatus
from json import dumps

# THIRD PART IMPORTS
from aioflask import Flask
from flask import Response, request
from loguru import logger

# PROJECT IMPORTS
from src.domain.response.response_model import ResponseModel
from src.domain.enums.status_code import InternalCode
from src.domain.validators.validators import UserDataValidator
from src.services.services import UserServices
from src.utils.utils import HelpersFunctions


app = Flask("Harpia API")


@app.route('/')
async def work_on() -> Response:
    response = {"success": True, "message": "Harpia API is working"}
    return Response(dumps(response))


@app.route("/get_list_of_users")
async def get_list_of_users() -> Response:
    try:
        data = UserServices.get_list_user()

        if not data:
            data_response = "Não Existem Dados Na Nossa Base Ainda"
        else:
            data_response = data

        response = ResponseModel(
            success=True,
            message="SUCCESS",
            result=data_response,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="An Unexpected Error Occurred",
            code=InternalCode.VALUE_ERROR,
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="The Body Params Are Not Fitting the API Requirements",
            code=InternalCode.INTERNAL_SERVER_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response


@app.route("/post/register_user", methods=["POST"])
async def post_register_user() -> Response:
    try:
        user_data = request.get_json()
        payload_validated = UserDataValidator(**user_data)
        normalized_data = HelpersFunctions.normalize_request_body(dict(payload_validated))

        data = UserServices.create_user(normalized_data)

        response = ResponseModel(
            success=True,
            message="OK",
            result=data,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="The Body Params Are Not Fitting the API Requirements",
            code=InternalCode.VALUE_ERROR,
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="An Unexpected Error Occurred",
            code=InternalCode.INTERNAL_SERVER_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response
